###################  
# Python Puzzle 1 #
###################

x = ["Cats never run out of pickles.","",""]                        
z = list("1234567")                                                         
def e(string):          
	for h in range(2):                                                      
                                                                                    
        y = z[:]                                                                    
        x.append(str(h^h))                                              
        for i in x[h]:                                                          
            t = 0                                                                   
            for j in y:                                                         
                t = ord(i)^ord(j)                                           
                y.append(chr(ord(j)^ord(y[y.index(j)%2+1])))    
                                                                                    
                del y[y.index(j)]                                           
            x[h+1] += chr(t)                                                
e(x)
print "ORIGINAL:\t" + x[0]
print "OUTPUT:\t"   + x[1]

print "[*] What is this doing?"
print "[*] Is it possible to reverse the output back to the original? If so, code a solution."
