def area(a,b):
    ra = a%4
    a-=ra 
    rb = b%2
    b-=rb 
    
    res = a*b
    if(rb):
        res += a
    if(ra>=1):
        res += b*3//2
        if(rb):
            res += 2
    if(ra>=2):
        res += b*3//2
        if(rb):
            res +=1
    if(ra>=3):
        res += b //2
    return res

a,b,c,d = map(int, input().split())
#下駄をはかす

#if(a<0):
a+=10**9
c+=10**9
#if(b<0):
b+=10**9
d+=10**9

#方針：原点と(c,d)の長方形から、原点と(a,b)、
#                        原点と(c,d)を引いて原点と(a,b)をたす

ans = area(c,d) + area(a,b)- area(a,d) - area(c,b)

print(int(ans))

