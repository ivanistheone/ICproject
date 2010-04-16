# IPython log file

txt = open("lotsof.txt").read()
len(txt)
#[Out]# 2439197
import re
import collections
word = re.compile("\w[^\w]+\w")
word.search("alskj laksj alsjk ")
#[Out]# <_sre.SRE_Match object at 0x1021b4d30>
word.findall("as aslkj alkj a")
#[Out]# ['s a', 'j a', 'j a']
word = re.compile("\s[^\S]+\s")
word.findall("as aslkj alkj a")
#[Out]# []
word = re.compile("\s[^\s]+\s")
word.findall("as aslkj alkj a")
#[Out]# [' aslkj ']
word.findall("as aslkj alkj a asd sd ")
#[Out]# [' aslkj ', ' a ', ' sd ']
word.findall("as aslkj alkj a asd sd  laksdj sldkj ")
#[Out]# [' aslkj ', ' a ', ' sd ', ' laksdj ']
word = re.compile("\s+[^\s]+\s+")
word.findall("as aslkj alkj a asd sd  laksdj sldkj ")
#[Out]# [' aslkj ', ' a ', ' sd  ', ' sldkj ']
word = re.compile(r"\s+[^\s]+\s+")
word.findall("as aslkj alkj a asd sd  laksdj sldkj ")
#[Out]# [' aslkj ', ' a ', ' sd  ', ' sldkj ']
word.findall("as aslkj alkj a asd sd  laksdj sldkj ")
#[Out]# [' aslkj ', ' a ', ' sd  ', ' sldkj ']
word = re.compile(r"\s+?[^\s]+?\s+?")
word = re.compile("\s+?[^\s]+?\s+?")
word.findall("as aslkj alkj a asd sd  laksdj sldkj ")
#[Out]# [' aslkj ', ' a ', ' sd ', ' laksdj ']
words = txt.split()
len(words)
#[Out]# 437452
words
#?d = collections.defaultdict
#?collections.defaultdict
d = collections.defaultdict(int)
d["asf"]
#[Out]# 0
for w in words:
    d[w]+=1
    
len(d)
#[Out]# 30283
totalNwords = 0
for w,count in d.iteritems():
    totalNwords+=count
    
len(words)
#[Out]# 437452
totalNwords
#[Out]# 437452
#pw is the prob of w for each w
d["the"}
d["the"]
#[Out]# 25916
d["the"]/totalNwords
#[Out]# 0
float(d["the"])/totalNwords
#[Out]# 0.059243071239816023
pw = []
for w,cnt in words:
    pw.append( float(cnt)/totalNwords )
    
for w,cnt in words.iteritems():
    pw.append( float(cnt)/totalNwords )
    
for w,cnt in d.iteritems():
    pw.append( float(cnt)/totalNwords )
    
len(pw)
#[Out]# 30283
pw[1:30]
#[Out]# [2.2859650887411649e-05, 1.1429825443705824e-05, 2.2859650887411646e-06, 2.2859650887411646e-06, 1.8287720709929317e-05, 2.2859650887411646e-06, 4.5719301774823293e-06, 2.2859650887411646e-06, 2.0573685798670481e-05, 2.2859650887411646e-06, 2.2859650887411646e-06, 4.5719301774823293e-06, 2.2859650887411646e-06, 6.8578952662234943e-06, 5.257719704104679e-05, 2.2859650887411646e-06, 2.2859650887411646e-06, 4.5719301774823293e-06, 2.2859650887411646e-06, 2.2859650887411646e-06, 6.8578952662234943e-06, 2.2859650887411646e-06, 2.0573685798670481e-05, 1.3715790532446989e-05, 5.7149127218529119e-05, 2.2859650887411646e-06, 4.5719301774823293e-06, 1.6001755621188153e-05, 9.1438603549646585e-06]
from numpy import *
sum(log(pw)*pw)
#[Out]# nan
log(pw)
#[Out]# array([-11.89010998, -10.68613717, -11.37928435, ..., -12.29557508,
#[Out]#        -12.29557508, -11.37928435])
any( pw == nan )
#[Out]# False
any( log(pw) == nan )
#[Out]# False
any( log(pw)*pw == nan )
#[Out]# False
log(pw)*pw
#[Out]# array([ -8.15411289e-05,  -2.44281365e-04,  -1.30063234e-04, ...,
#[Out]#         -5.62145108e-05,  -5.62145108e-05,  -1.30063234e-04])
sum(log(pw)*pw)
#[Out]# nan
sum(log(pw)*pw[0:1000])
sum( (log(pw)*pw)[0:1000] )
#[Out]# -0.27533823932135648
sum( (log(pw)*pw)[0:4000] )
#[Out]# -0.89336200368813223
sum( (log(pw)*pw)[0:5000] )
#[Out]# -1.0974379419220495
sum( (log(pw)*pw)[0:10000] )
#[Out]# -2.5208894393676067
sum( (log(pw)*pw)[0:100000] )
#[Out]# nan
sum( (log(pw)*pw)[0:10000] )
#[Out]# -2.5208894393676067
sum( (log(pw)*pw)[0:20000] )
#[Out]# nan
sum( (log(pw)*pw)[0:10000] )
#[Out]# -2.5208894393676067
sum( (log(pw)*pw)[0:15000] )
#[Out]# nan
sum( (log(pw)*pw)[0:14000] )
#[Out]# nan
sum( (log(pw)*pw)[0:13000] )
#[Out]# nan
len(d)
#[Out]# 30283
pwMAX = float(1)/30283*ones([30283,1])
len(pwMAX)
#[Out]# 30283
sum(pwMAX*log( pwMAX))
#[Out]# -10.318341777945065
#?any
pw=ones(py/core/fromnumeric.py
Definition:       any(a, axis=None, out=None)
Docstring:
    Test whether an
any( pw == ones([30283,1]) )
#[Out]# False
any( pw*log(pw) == nan*ones([30283,1]) )
#[Out]# False
non*ones([3,1])
nan
#[Out]# nan
sum(pw*log(pw))
#[Out]# nan
nan
#[Out]# nan
nan*1
#[Out]# nan
#?nansum
nansum(pw*log(pw))
#[Out]# -7.4451406072083923
nansum(pw*log(pw))/sum(pwMAX*log(pwMAX))
#[Out]# 0.72154429145989374
nansum(pw*log(pw))
#[Out]# -7.4451406072083923
sum(pwMAX*log( pwMAX))
#[Out]# -10.318341777945065
len(d)
#[Out]# 30283
log(len(d))
#[Out]# 10.318341777940978
7.44514*30283
#[Out]# 225461.17462000001
7.44514*30283/1024
#[Out]# 220.17692833984376
get_ipython().system("ls -F ")