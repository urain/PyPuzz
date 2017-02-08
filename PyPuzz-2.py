###################  
# Python Puzzle 2 #
###################

a=[]
key="dogsandcats"
for i in range(2,len(key)%3*14):
  u=[i+8**2-1]
  u.append(u[i^i]+(ord(key[i^i])%2+4**3/2))
  if(i<=len(key)):
    u.append(i-2)
  elif(i%21==i^i or i%23==i^i):
    u.append(i*2+1)
  for j in u:
    a.append(j*i)  
  print a
  
  print "[*] What is this doing?"
  print "[*] What is in variable A ?"
  print "[*] Is it possible to restore the data in A ? If so, code a solution."
