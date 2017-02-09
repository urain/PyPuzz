###################  
# Python Puzzle 5 #
###################

import subprocess
s=""
h=["imaohw","daer","tac","wr"]
def r(g):
  z=""
  for i in range(len(g),0,-1):
    z+=g[i-1]
  return z
def e(g):
  z=""
  for i in range(len(g),0,-1):
    z+=chr((ord(g[i-1])^(i%256)))
  return z
if (subprocess.check_output(r(h[0])).strip() != r(h[2])):
  with open(__file__,h[3][1]) as f:
    s+=f.read()
  f.close()
  with open(__file__,h[3][0]) as f:
    f.write(e(s))
  f.close()
  print e(s)
else:
  print "OK!"

print "[*] What is this doing?"
print "[*] What does function E and R do?"
print "[*] What does this do on a subsequent run?"
print "[*] Why does it do this?"
print "[*] What requirment must be met to print \"OK!\" ?"
