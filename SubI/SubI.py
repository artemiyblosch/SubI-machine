from collections import*
import curses
import config

def m(a):
    if(a.real!=0):
        return -1
    return a.imag

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

lenOfW = config.length_of_word
assert lenOfW >= 13

def rep(s,t):
    res = ""
    for i in range(0,t):
        res = res + s
    return res

def dget(i):
    if i not in data:
        data[i] = rep("0",lenOfW)
    return data[i]
 
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

def And(str1, str2):
    res = ""
    for i,v in enumerate(str1):
        res += {"00":"0","01":"0","10":"0","11":"1"}[f"${v}${str2[i]}"]
    return res

def Or(str1, str2):
    res = ""
    for i,v in enumerate(str1):
        res += {"00":"0","01":"1","10":"1","11":"1"}[f"${v}${str2[i]}"]
    return res
data = {}
if(config.path_to_file == ""):
    code = config.script
else:
    with open(config.path_to_file,"r") as file:
        code = file.read()
code = code.replace(" ","")

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

#raster = convert(rep("0100001101000011",lenOfW//13+1)[-lenOfW:]).imag
i = 0
c = 0
while i<len(code):
    if code[i] == "\n":
        c = complex(0, c.imag + 1)
        i += 1
    data[c] = code[i:i+lenOfW]
    i += lenOfW
    c += 1

ip = 0
while True:
    curC = dget( ip )
    arg = dget( ip+1 )
    arg2 = dget( ip+2 )
    if curC == rep("0",lenOfW-13)+"1111111111111": break #end
    elif curC == rep("0",lenOfW-13)+"0000001110111": #print
        stdscr.addch( int(convert(arg).imag), int(convert(arg).real),\
                      chr( int(convert(arg2).real) ), int(convert(arg2).imag))
        stdscr.refresh()
        ip += 2
    elif curC == rep("0",lenOfW-13)+"0110111001100": #goto
        ip = convert( arg ) - 1
    elif curC == rep("0",lenOfW-13)+"0000110011110": #if0
        if convert( dget( convert(arg) ) ) == 0: ip += 1j-1
        else: ip += 1
    elif curC == rep("0",lenOfW-13)+"0001100001111": #add
        data[ convert(arg) ] = add( dget(convert(arg)), arg2 ).zfill(lenOfW)
        ip += 2
    elif curC == rep("0",lenOfW-13)+"0000100011111": #copy
        data[ convert(arg) ] = dget( convert( arg2 ) )
        ip+=2
    elif curC == rep("0",lenOfW-13)+"0001101110111": #shift
        shifting = int(convert(arg2).real)
        if(shifting<0):
            data[ convert(arg) ] = dget( convert(arg) )[:-shifting].zfill(lenOfW)
        else:
            Q = dget( convert(arg) )[shifting:]
            data[ convert(arg) ] = Q + rep("0", lenOfW - len(Q))
        ip+=1
    elif curC == rep("0",lenOfW-13)+"0110110110110": #input
        a=stdscr.getch()
        Q = rconvert(a).zfill(lenOfW)[-lenOfW:]
        data[ convert(arg) ] = Q
        ip += 1
    elif curC == rep("0",lenOfW-13)+"0000000011101": #neg
        data[ convert(arg) ] = rconvert(-dget(convert(arg)))
    elif curC == rep("0",lenOfW-13)+"0000001100000": #and
        data[ convert(arg) ] = And( dget(convert(arg)), arg2 ).zfill(lenOfW)
        ip+=1
    elif curC == rep("0",lenOfW-13)+"1111110011111": #or
        data[ convert(arg) ] = Or( dget(convert(arg)), arg2 ).zfill(lenOfW)
        ip+=1
    ip += 1

curses.nocbreak()
stdscr.keypad(False)
curses.echo()