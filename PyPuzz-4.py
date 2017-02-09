###################  
# Python Puzzle 4 #
###################
# HINT: This file is CONFIRMED working. If it errors, there's a reason.

z=[[109,105,120,104,100,123,113,117,125,127],[114,111],
   [125,116,127,123,125,75,125,101,122,124,127,124],
   [65,67,115,117,102,123,96,100,81,83],[51,112],
   [65,67,120,109,127,120,102,121,96,127,85,87]]
y=list("\x5f\x5f\x62\x75")
c=chr
def d(t,x):
  a=[[],[],[],""]
  for i in t:
    a[2].append(i)
  for i in range(30,1,-2):
    a[0].append(i)
  for i,k in enumerate(a[2]):
    if (x==1):
      a[1].append(o(k) ^ a[0][i])
    else:
      a[3]+=(chr(k^a[0][i]))
  return a[3]

o=ord
b=eval(dir()[dir().index(d(z[5],2))])
r=getattr(b,dir(b)[dir(b).index(d(z[3],2))])
s=r(d(z[0],2))
for i,k in enumerate(y):
  y[i] = o(k)
l=getattr(s,dir(s)[dir(s).index(d(z[2],2))])
u=l([d(z[1],2),d(z[4],2)])
print "\nDONE!\n\nThe Result is: " + d(y,2)
print u

print "[*] What is in Z?"
print "[*] What significance does the final result have?"
print "[*] What is the goal of this program?"
print "[*] Is it possible to reverse any encryption encountered in this program? If so, code a solution."
      
