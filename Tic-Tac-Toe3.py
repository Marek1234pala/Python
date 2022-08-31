def board(a,b,c,d,e,f,g,h,i):
    print(a+"|"+b+"|"+c)
    print(d+"|"+e+"|"+f)
    print(g+"|"+h+"|"+i)
def user(count):
    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh
    global ii
    if (int(count) % 2) == 0:
        inputin=input("user1 ")
        X="X"
    else:
        inputin=input("user2 ")
        X="O"
    while True:
        if inputin=="7":
            aa=X
        elif inputin=="8":
            bb=X
        elif inputin=="9":
            cc=X
        elif inputin=="4":
            dd=X
        elif inputin=="5":
            ee=X
        elif inputin=="6":
            ff=X
        elif inputin=="1":
            gg=X
        elif inputin=="2":
            hh=X
        elif inputin=="3":
            ii=X
        break
aa="7"
bb="8"
cc="9"
dd="4"
ee="5"
ff="6"
gg="1"
hh="2"
ii="3"
count=0
board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
while count<9:
    user(count)
    board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
    count+=1