def board(a,b,c,d,e,f,g,h,i):
    print(a+"|"+b+"|"+c)
    print(d+"|"+e+"|"+f)
    print(g+"|"+h+"|"+i)
def user1():
    global Case1
    global Case2
    global Case3
    global Case4
    global Case5
    global Case6
    global Case7
    global Case8
    global Case9
    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh
    global ii
    print("user1 :")
    inputin=input("Quelle case veux tu choisir? :")
    while True:
        if inputin=="7" and Case7==0:
            Case7=1
            aa="X"
        elif inputin=="8" and Case8==0:
            Case8=1
            bb="X"
        elif inputin=="9" and Case9==0:
            Case9=1
            cc="X"
        elif inputin=="4" and Case4==0:
            Case4=1
            dd="X"
        elif inputin=="5" and Case5==0:
            Case5=1
            ee="X"
        elif inputin=="6" and Case6==0:
            Case6=1
            ff="X"
        elif inputin=="1" and Case1==0:
            Case1=1
            gg="X"
        elif inputin=="2" and Case2==0:
            Case2=1
            hh="X"
        elif inputin=="3" and Case3==0:
            Case3=1
        else:
            inputin=input("Ce numéro est déjà pris ou n'existe pas. :")
            continue
        break
def user2():
    global Case1
    global Case2
    global Case3
    global Case4
    global Case5
    global Case6
    global Case7
    global Case8
    global Case9
    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh
    global ii
    print("user2 :")
    inputin=input("Quelle case veux tu choisir? :")
    while True:
        if inputin=="7" and Case7==0:
            Case7=1
            aa="O"
        elif inputin=="8" and Case8==0:
            Case8=1
            bb="O"
        elif inputin=="9" and Case9==0:
            Case9=1
            cc="O"
        elif inputin=="4" and Case4==0:
            Case4=1
            dd="O"
        elif inputin=="5" and Case5==0:
            Case5=1
            ee="O"
        elif inputin=="6" and Case6==0:
            Case6=1
            ff="O"
        elif inputin=="1" and Case1==0:
            Case1=1
            gg="O"
        elif inputin=="2" and Case2==0:
            Case2=1
            hh="O"
        elif inputin=="3" and Case3==0:
            Case3=1
            ii="O"
        else:
            inputin=input("Ce numéro est déjà pris ou n'existe pas. :")
            continue
        break
while True:
    Case1=0
    Case2=0
    Case3=0
    Case4=0
    Case5=0
    Case6=0
    Case7=0
    Case8=0
    Case9=0
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
    while True:
        user1()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        count+=1
        if count==9:
            break
        user2()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        count+=1
    inputin2=input("Veux tu rejouer (y/n) ?:")
    if inputin2=="y":
        continue
    else:
        break