###################  
# Python Puzzle 3 #
###################

s=list("stuff and things")
t=[" "]
for i in dir(dict) + dir(str):
  for x in i:
    if x not in t:
      t.append(x)
for i in s:
  s[s.index(i)]=chr(t.index(i)+len(t)*2+9)  
print "OUTPUT: " + ''.join(s)

print "[*] What is this doing?"
print "[*] Is it possible to reverse the output? If so, code a solution."
