l1, t =[], 1
s=int(input("Size:  "))
for i in range(0,(s*(s-1))+s):
    l1.append(str(i))
def print1(b,lt):
    a, c = 0, 0
    c=c+b
    while b<(c**2)+1:
        for i in range(a,b):
            if i!=(b-1):
                if len(lt[i])<2:
                    print(" "+lt[i],end=" ")
                else:
                    print(lt[i],end=" ")
            else:
                if len(lt[i])<2:
                    print(" "+lt[i])
                else:
                    print(lt[i])
        a, b = a+c, b+c
print1(s,l1)
def checkrow(b,lt):
    a, c, ls =0, 0, []
    c=c+b
    while b<(c**2)+1:
        for i in range(a,b):
            ls.append(lt[i])
        if ls.count(ls[0])==c:
            return("win")
            break
        ls=[]
        a, b = a+c, b+c
def checkcolumn(b,lt):
    a, ls = 0, []
    while a<b:
        for i in range(a,(b*(b-1))+a+1,b):
            ls.append(lt[i])
        if ls.count(ls[0])==b:
            return("win")
            break
        ls=[]
        a=a+1
def checkdiag1(b,lt):
    ls=[]
    for i in range(0,b**2,b+1):
        ls.append(lt[i])
    if ls.count(ls[0])==b:
        return("win")
def checkdiag2(b,lt):
    ls=[]
    for i in range(b-1,(b*(b-1))+1,b-1):
        ls.append(lt[i])
    if ls.count(ls[0])==b:
        return("win")
while t<(s**2)+1:
    if t%2!=0:
        p1=int(input("X--> "))
        l1[p1]="X"
        print1(s,l1)
        if checkrow(s,l1)=="win" or checkcolumn(s,l1)=="win" or checkdiag1(s,l1)=="win" or checkdiag2(s,l1)=="win" :
            print("Winner: X")
            break
    else:
        p2=int(input("O--> "))
        l1[p2]= "O"
        print1(s,l1)
        if checkrow(s,l1)=="win" or checkcolumn(s,l1)=="win" or checkdiag1(s,l1)=="win" or checkdiag2(s,l1)=="win" :
            print("Winner: O")
            break
    t=t+1
