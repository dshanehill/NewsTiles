import json,re,glob,os,sys
m=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'master.json')))
K=m['keys']; P=m['patterns']
def tags(s): return sorted(re.findall(r'<[^>]+>',s))
def ph(s): return sorted(re.findall(r'\{\d\}',s))
TR={}; bad=0
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tr','*.txt'))):
    code=os.path.basename(f)[:-4]; arr=[None]*len(K)
    for ln in open(f,encoding='utf8').read().split('\n'):
        if not ln.strip(): continue
        n,t=ln.split('\t',1); n=int(n)
        if arr[n] is not None: print(code,'dup',n); bad+=1
        arr[n]=t.strip()
    for i,(e,t) in enumerate(zip(K,arr)):
        if t is None: print(code,'missing',i); bad+=1; continue
        if tags(e)!=tags(t): print(code,i,'TAGS',tags(e),tags(t)); bad+=1
        if ph(e)!=ph(t): print(code,i,'PH',e,'|',t); bad+=1
    TR[code]=arr
print('langs',len(TR),'problems',bad)
out='// News Tiles in your language: the words, in the order of NG_KEYS (made by build.py)\n'
out+='window.NG_KEYS = '+json.dumps(K,ensure_ascii=False)+';\n'
out+='window.NG_PATTERNS = ['+','.join('[/%s/, %d]'%(r,K.index(t)) for t,r in P)+'];\n'
out+='window.NG_TR = {\n'+',\n'.join('%s: %s'%(json.dumps(c),json.dumps(a,ensure_ascii=False)) for c,a in TR.items())+'\n};\n'
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','extension','i18n-strings.js'),'w',encoding='utf8').write(out)
print('size',len(out.encode()))
