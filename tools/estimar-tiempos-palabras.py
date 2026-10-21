# Estimate word timings for known-text TTS clips: speech regions from ffmpeg
# silencedetect, clause boundaries snapped to the longest interior pauses,
# words inside a clause spread by vowel-group (syllable) weight.
import json, re, subprocess, sys
proj = sys.argv[1]
meta_p = f"{proj}/audio_meta.json"
meta = json.load(open(meta_p))
script = open(f"{proj}/SCRIPT.md").read()
lines = {}
cur = None
for l in script.splitlines():
    m = re.match(r"## Line \d+ .*\(Frame (\d+)\)", l)
    if m: cur = int(m.group(1))
    elif l.startswith("    ") and cur: lines[cur] = l.strip()
def sil(path):
    out = subprocess.run(["ffmpeg","-i",path,"-af","silencedetect=noise=-38dB:d=0.09","-f","null","-"],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",out)]
    en=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",out)]
    return list(zip(st,en+[None]*(len(st)-len(en))))
def syl(w):
    return max(1, len(re.findall(r"[aeiouáéíóúü]+", w.lower())))
for v in meta["voices"]:
    dur = v["duration_s"]; text = lines[v["frame"]]
    s = sil(f"{proj}/{v['path']}")
    speech0 = 0.0; speech1 = dur; inner=[]
    for a,b in s:
        b = dur if b is None else b
        if a <= 0.02: speech0 = b
        elif b >= dur-0.02: speech1 = a
        else: inner.append((a,b))
    words = text.split()
    breaks = [i for i,w in enumerate(words[:-1]) if re.search(r"[,.;:]$", w)]
    pauses = sorted(sorted(inner, key=lambda p: p[1]-p[0], reverse=True)[:len(breaks)])
    if len(pauses) < len(breaks):
        breaks = breaks[:0]; pauses = []
    bounds=[]; start=speech0; prev=0
    for bi,(a,b) in zip(breaks,pauses):
        bounds.append((prev, bi+1, start, a)); prev=bi+1; start=b
    bounds.append((prev, len(words), start, speech1))
    out=[]
    for i0,i1,t0,t1 in bounds:
        ws=words[i0:i1]; wt=[syl(w)+0.4 for w in ws]; tot=sum(wt); t=t0
        for w,k in zip(ws,wt):
            d=(t1-t0)*k/tot
            out.append({"id":f"w{len(out)}","text":w,"start":round(t,3),"end":round(t+d-0.02,3)}); t+=d
    v["words"]=out
    print(v["frame"], len(words), "words", len(breaks), "breaks", f"{speech0:.2f}-{speech1:.2f}")
json.dump(meta, open(meta_p,"w"), indent=2, ensure_ascii=False)
