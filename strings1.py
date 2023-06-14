def upper1(s):
    n=""
    for x in s:
        y=ord(x)
        if y>=97 and y<=122:
            n+=chr(y-32)
        else:
            n+=x
    return n

def lower1(s):
    n=""
    for x in s:
        y=ord(x)
        if y>=65 and y<=90:
            n+=chr(y+32)
        else:
            n+=x
    return n

def capitalize1(s):
    n=""
    for x in range(len(s)):
        y=ord(s[x])
        if x==0 and y>=65 and y<=90:
            n+=s[x]
        elif x==0 and y>=97 and y<=122:
            n+=chr(y-32)
        else:
            if y>=65 and y<=90:
                n+=chr(y+32)
            else:
                n+=s[x]
    return n

def title1(a):
    n=""
    for x in range(len(a)):
        y=ord(a[x])
        if not(y==32) and not(a[x-1]==" ") and not(y>=33 and y<=64):
            if x==0 and y>=65 and y<=90:
                n+=a[x]
            elif x==0 and y>=97 and y<=122:
                n+=chr(y-32)
            else:
                if y>=65 and y<=90 and not(ord(a[x-1])>=33 and ord(a[x-1])<=64):
                    n+=chr(y+32)
                else:
                    if y>=65 and y<=90 and ord(a[x-1])>=33 and ord(a[x-1])<=64 and not(ord(a[x-2])>=65 and ord(a[x-2])<=122):
                        n+=a[x]
                    elif y>=65 and y<=90 and ord(a[x-1])>=33 and ord(a[x-1])<=64:
                        n+=chr(y+32)
                    elif ord(a[x-1])>=33 and ord(a[x-1])<=64 and not(ord(a[x-2])>=65 and ord(a[x-2])<=122):
                        n+=chr(y-32)
                    elif x==1 and y>=97 and y<=122:
                        n+=chr(y-32)
                    else:
                        n+=a[x]
        elif y==32:
            if ord(a[x+1])>=65 and ord(a[x+1])<=90:
                n+=" "+a[x+1]
            elif ord(a[x+1])>=97 and ord(a[x+1])<=122:
                n+=" "+chr(ord(a[x+1])-32)
            else:
                if ord(a[x+1])>=65 and ord(a[x+1])<=90:
                    n+=chr(ord(a[x+1])+32)
                else:
                    n+=a[x] 
        elif y>=33 and y<=64:
            if ord(a[x+1])>=65 and ord(a[x+1])<=90:
                n+=chr(y)
            elif ord(a[x+1])>=97 and ord(a[x+1])<=122:
                n+=chr(y)
            else:
                n+=a[x]
        else:
            continue
    return n

def isalpha1(a):
    n=0
    for x in a:
        if ord(x)>=65 and ord(x)<=122:
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

def isdigit1(a):
    n=0
    for x in a:
        if ord(x)>=33 and ord(x)<=64:
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

def islower1(a):
    n=0
    for x in a:
        if ord(x)>=97 and ord(x)<=122 or (ord(x)>=32 and ord(x)<=64) or (ord(x)>=91 and ord(x)<=96):
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

def isupper1(a):
    n=0
    for x in a:
        if ord(x)>=65 and ord(x)<=90 or (ord(x)>=32 and ord(x)<=64) or (ord(x)>=91 and ord(x)<=96):
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False

def isalnum1(a):
    n=0
    for x in a:
        if ord(x)>=65 and ord(x)<=90 or (ord(x)>=97 and ord(x)<=122) or (ord(x)>=48 and ord(x)<=57):
            n+=1
        else:
            continue
    if n==len(a):
        return True
    else:
        return False
    
def swapcase1(s):
    n=""
    for x in s:
        if ord(x)>=65 and ord(x)<=90:
            n+=chr(ord(x)+32)
        elif ord(x)>=97 and ord(x)<=122:
            n+=chr(ord(x)-32)
        else:
            n+=x
    return n