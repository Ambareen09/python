def SieveOfEratosthenes(n): 
    p = 2
    while (p * p <= n):
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]: 
            print p, #Use print(p) for python 3 
 
if __name__=='__main__': 
    n = 30
    print "Following are the prime numbers smaller",  
    print "than or equal to", n 
    SieveOfEratosthenes(n) 
