import random

def mod (a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def Mypow (a,b):
    cont = 0
    res = 1
    while (cont < b):
        res = res * a
        cont = cont +1
    return res

def getNros(n):
    t = 1
    while (2**t % n-1 != 0):
        if(mod(n-1,2) == 1):
            t = 0
            u = n-1
            return (u,t)
        t = t+1
    t = t//2
    u = (n-1) // (2**t)


    #print(n-1,"= 2^",t,"*",u)
    #print(Mypow(2,t)*u)
    return (int(u),int(t))

def witness (a,n):

    (u,t) = (getNros(n))

    x0 = Mypow(a,u) % n
    if (x0 == 1 or x0 ==n-1):
        return False #n es posiblemente primo

    list = [x0]
    for i in range (1,t):
        xj = list[i-1]
        xi = Mypow(xj,2) % 2
        list.append	(xi)

        if (list[i] == n-1):
                return True #x es posiblemente primo
    return True #n es un nro compuesto

def miller (n,s):
    
    for j in range (1,s):
        a = random.randint(1,n-1)
        if witness(a,n):
            return True
    return False

def prime_candidate (b):
    n = ""
    for i in range (1,b+1):
        val = random.randint(0,1)
        n = n + str(val)

    if (len(n) != b):
        prime_candidate(b)

    n = int(n,2)
    #print("N: ",n)
    #print("N: ",n)
    m = Mypow(2,b-1) + 1
    n = n or m
    return n

def generate_Prime (b):
    s = 15
    n = prime_candidate(b)
    while (miller(n,s) == True):
        n = n+2
    
    return n

def onehPrimes():
    list = []

    for i in range (1,100):
        list.append(generate_Prime(10))
    return list

print(onehPrimes())
