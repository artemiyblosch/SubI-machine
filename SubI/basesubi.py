from collections import*

def add(*s,p=0):
 r=defaultdict(int,{0:0})
 for S in s:
  n=0
  for d in S[::-1]:r[n]+=d=='1';n+=1
 while p<=max(r):
  while r[p]>1:
   r[p]-=2
   if r[p+1]>1<=r[p+2]:r[p+1]-=2;r[p+2]-=1
   else:r[p+2]+=1;r[p+3]+=1
  p+=1
 return str([*map(r.get,sorted(r))])[-2::-3]

def convert(num):
    num = num[::-1]
    res = 0
    for i, v in enumerate(num):
        res += int(v) * ( (1j-1)**i)
    return res
 
def rconvert(num):
    res = "0"
    while num!=0:
        if(num.real > 0):
            res = add(res,"1")
            num -= 1
        elif(num.real < 0):
            res = add(res,"11101")
            num += 1
        if(num.imag > 0):
            res = add(res,"11")
            num -= 1j
        elif(num.imag < 0):
            res = add(res,"110")
            num += 1j
    return res

while 1:
 a = input("Do you want to convert to or from base i-1?(t/f):")
 if a!="t": print( convert(input()) )
 else: print( rconvert( complex(input()) ) )