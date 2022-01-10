A, B, C=['0','1','2','3','4','5','6','7','8'], ['0','1','2','3','4','5','6','7','8'], ['0','1','2','3','4','5','6','7','8']
l1, l2, a, t, b = [A,B,C], ['A','B','C'], 1, 1, 1
def print1(l1):
    if len(l1)==3:
        A, B, C = l1[0], l1[1], l1[2]
        print("A      B      C")
        print(A[0],A[1],A[2]+"  "+B[0],B[1],B[2]+"  "+C[0],C[1],C[2])
        print(A[3],A[4],A[5]+"  "+B[3],B[4],B[5]+"  "+C[3],C[4],C[5])
        print(A[6],A[7],A[8]+"  "+B[6],B[7],B[8]+"  "+C[6],C[7],C[8])
    elif len(l1)==2:
        a1, b1 = l1[0], l1[1]
        print(l2[0]+"      "+l2[1])
        print(a1[0],a1[1],a1[2]+"  "+b1[0],b1[1],b1[2])
        print(a1[3],a1[4],a1[5]+"  "+b1[3],b1[4],b1[5])
        print(a1[6],a1[7],a1[8]+"  "+b1[6],b1[7],b1[8])
    else:
        a1=l1[0]
        print(l2[0])
        print(a1[0],a1[1],a1[2])
        print(a1[3],a1[4],a1[5])
        print(a1[6],a1[7],a1[8])
def checkrow(lt):
    a, c, ls =0, 0, []
    b=3
    c=c+b
    while b<(c**2)+1:
        for i in range(a,b):
            ls.append(lt[i])
        if ls.count(ls[0])==c:
            return("win")
            break
        ls=[]
        a, b = a+c, b+c
def checkcolumn(lt):
    a, ls = 0, []
    while a<3:
        for i in range(a,(3*(3-1))+a+1,3):
            ls.append(lt[i])
        if ls.count(ls[0])==3:
            return("win")
            break
        ls=[]
        a=a+1
def checkdiag1(lt):
    ls=[]
    for i in range(0,3**2,3+1):
        ls.append(lt[i])
    if ls.count(ls[0])==3:
        return("win")
def checkdiag2(lt):
    ls=[]
    for i in range(3-1,(3*(3-1))+1,3-1):
        ls.append(lt[i])
    if ls.count(ls[0])==3:
        return("win")
print1(l1)
while b==1:
    if t%2!=0:
        p1=input("Player 1: ")
        tc=int(p1[1])
        if (p1[0] not in l2) or len(p1)>2:
            print("Invalid move, please input again")
        elif (p1[0] in l2):
            tt=l2.index(p1[0])
            if (l1[tt][tc] == 'X'):
                print("Invalid move, please input again")
            else:
                l1[tt][tc]='X'
                t+=1
        for i in l1:
            if checkrow(i)=="win" or checkcolumn(i)=="win" or checkdiag1(i)=="win" or checkdiag2(i)=="win" :
                l2.pop(l1.index(i))
                l1.remove(i)
        if len(l1)==0:
            b=b+1
        if len(l1)>0:
            print1(l1)
    else:
        p1=input("Player 2: ")
        tc=int(p1[1])
        if (p1[0] not in l2) or len(p1)>2:
                print("Invalid move, please input again")
        elif (p1[0] in l2):
            tt=l2.index(p1[0])
            if (l1[tt][tc] == 'X'):
                print("Invalid move, please input again")
            else:
                l1[tt][tc]='X'
                t+=1
        for i in l1:
            if checkrow(i)=="win" or checkcolumn(i)=="win" or checkdiag1(i)=="win" or checkdiag2(i)=="win" :
                l2.pop(l1.index(i))
                l1.remove(i)
        if len(l1)==0:
            b=b+1
        if len(l1)>0:
            print1(l1)
if t%2==0:
    print("Player 2 wins game")
else:
    print("Player 1 wins game")
