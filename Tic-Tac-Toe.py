import random
def board(a,b,c,d,e,f,g,h,i):
    print(a+"|"+b+"|"+c)
    print(d+"|"+e+"|"+f)
    print(g+"|"+h+"|"+i)
def end():
    global cdd
    print("Merci d'avoir joué.")
    cdd=False
def check_win():
    global Case1
    global Case2
    global Case3
    global Case4
    global Case5
    global Case6
    global Case7
    global Case8
    global Case9
    if Case7+Case8+Case9==3:
        print("Gagner")
        end()
    elif Case4+Case5+Case6==3:
        print("Gagner")
        end()
    elif Case1+Case2+Case3==3:
        print("Gagner")
        end()
    elif Case7+Case4+Case1==3:
        print("Gagner")
        end()
    elif Case8+Case5+Case2==3:
        print("Gagner")
        end()
    elif Case9+Case6+Case3==3:
        print("Gagner")
        end()
    elif Case7+Case5+Case3==3:
        print("Gagner")
        end()
    elif Case9+Case5+Case1==3:
        print("Gagner")
        end()
    elif Case7+Case8+Case9==15:
        print("Perdu")
        end()
    elif Case4+Case5+Case6==15:
        print("Perdu")
        end()
    elif Case1+Case2+Case3==15:
        print("Perdu")
        end()
    elif Case7+Case4+Case1==15:
        print("Perdu")
        end()
    elif Case8+Case5+Case2==15:
        print("Perdu")
        end()
    elif Case9+Case6+Case3==15:
        print("Perdu")
        end()
    elif Case7+Case5+Case3==15:
        print("Perdu")
        end()
    elif Case9+Case5+Case1==15:
        print("Perdu")
        end()
    elif Case1+Case2+Case3+Case4+Case5+Case6+Case7+Case8+Case9==25:
        print("Egalité")
        end()
    elif Case1+Case2+Case3+Case4+Case5+Case6+Case7+Case8+Case9==29:
        print("Egalité")
        end()
def AI():
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
    global X
    global O
    if Case7+Case8+Case9==10:
        Case7=5
        Case8=5
        Case9=5
        aa=O
        bb=O
        cc=O
    elif Case4+Case5+Case6==10:
        Case4=5
        Case5=5
        Case6=5
        dd=O
        ee=O
        ff=O
    elif Case1+Case2+Case3==10:
        Case1=5
        Case2=5
        Case3=5
        gg=O
        hh=O
        ii=O
    elif Case7+Case4+Case1==10:
        Case7=5
        Case4=5
        Case1=5
        aa=O
        dd=O
        gg=O
    elif Case8+Case5+Case2==10:
        Case8=5
        Case5=5
        Case2=5
        bb=O
        ee=O
        hh=O
    elif Case9+Case6+Case3==10:
        Case9=5
        Case6=5
        Case3=5
        cc=O
        ff=O
        ii=O
    elif Case7+Case5+Case3==10:
        Case7=5
        Case5=5
        Case3=5
        aa=O
        ee=O
        ii=O
    elif Case9+Case5+Case1==10:
        Case9=5
        Case5=5
        Case1=5
        cc=O
        ee=O
        gg=O
    elif Case7+Case8+Case9==2:
        if Case7==0:
            Case7=5
            aa=O
        elif Case8==0:
            Case8=5
            bb=O
        else:
            Case9=5
            cc=O
    elif Case4+Case5+Case6==2:
        if Case4==0:
            Case4=5
            dd=O
        elif Case5==0:
            Case5=5
            ee=O
        else:
            Case6=5
            ff=O
    elif Case1+Case2+Case3==2:
        if Case1==0:
            Case1=5
            gg=O
        elif Case2==0:
            Case2=5
            hh=O
        else:
            Case3=5
            ii=O
    elif Case7+Case4+Case1==2:
        if Case7==0:
            Case7=5
            aa=O
        elif Case4==0:
            Case4=5
            dd=O
        else:
            Case1=5
            gg=O
    elif Case8+Case5+Case2==2:
        if Case8==0:
            Case8=5
            bb=O
        elif Case5==0:
            Case5=5
            ee=O
        else:
            Case2=5
            hh=O
    elif Case9+Case6+Case3==2:
        if Case9==0:
            Case9=5
            cc=O
        elif Case6==0:
            Case6=5
            ff=O
        else:
            Case3=5
            ii=O
    elif Case7+Case5+Case3==2:
        if Case7==0:
            Case7=5
            aa=O
        elif Case5==0:
            Case5=5
            ee=O
        else:
            Case3=5
            ii=O
    elif Case9+Case5+Case1==2:
        if Case9==0:
            Case9=5
            cc=O
        elif Case5==0:
            Case5=5
            ee=O
        else:
            Case1=5
            gg=O
    elif Case7+Case9+Case1+Case3<12:
        while True:
            loul1=random.randint(0,3)
            if loul1==0 and Case7==0:
                Case7=5
                aa=O
                break
            elif loul1==1 and Case9==0:
                Case9=5
                cc=O
                break
            elif loul1==2 and Case1==0:
                Case1=5
                gg=O
                break
            elif loul1==3 and Case3==0:
                Case3=5
                ii=O
                break
            elif loul1==0 and Case7>0:
                continue
            elif loul1==1 and Case9>0:
                continue
            elif loul1==2 and Case1>0:
                continue
            elif loul1==3 and Case3>0:
                continue
            break
    elif Case5==0:
        Case5=5
        ee=O
    elif Case8+Case4+Case2+Case6<12:
        while True:
            loul2=random.randint(0,3)
            if loul2==0 and Case8==0:
                Case8=5
                bb=O
                break
            elif loul2==1 and Case4==0:
                Case4=5
                dd=O
                break
            elif loul2==2 and Case2==0:
                Case2=5
                hh=O
                break
            elif loul2==3 and Case6==0:
                Case6=5
                ff=O
                break
            elif loul2==0 and Case8>0:
                continue
            elif loul2==1 and Case4>0:
                continue
            elif loul2==2 and Case2>0:
                continue
            elif loul2==3 and Case6>0:
                continue
            break
def user():
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
    global X
    global O
    inputin=input("Quelle case veux tu choisir ?:")
    while True:
        if inputin=="7" and Case7==0:
            Case7=1
            aa=X
            break
        elif inputin=="8" and Case8==0:
            Case8=1
            bb=X
            break
        elif inputin=="9" and Case9==0:
            Case9=1
            cc=X
            break
        elif inputin=="4" and Case4==0:
            Case4=1
            dd=X
            break
        elif inputin=="5" and Case5==0:
            Case5=1
            ee=X
            break
        elif inputin=="6" and Case6==0:
            Case6=1
            ff=X
            break
        elif inputin=="1" and Case1==0:
            Case1=1
            gg=X
            break
        elif inputin=="2" and Case2==0:
            Case2=1
            hh=X
            break
        elif inputin=="3" and Case3==0:
            Case3=1
            ii=X
            break
        else:
            inputin=input("Ce numéro est déjà pris ou n'existe pas .:")
            continue
def main():
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
    global cdd
    global X
    global O
    cdd=True
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
    X="X"
    O="O"
    inputin3=input("Quel signe veux tu choisir (o/x) ?:")
    if inputin3=="o":
        X="O"
        O="X"
    board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
    while cdd:
        user()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        check_win()
        if cdd==False:
            break
        print("ORDI:")
        AI()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        check_win()
def main2():
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
    global cdd
    global X
    global O
    cdd=True
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
    X="X"
    O="O"
    inputin3=input("Quel signe veux tu choisir (o/x) ?:")
    if inputin3=="o":
        X="O"
        O="X"
    while cdd:
        print("ORDI:")
        AI()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        check_win()
        if cdd==False:
            break
        user()
        board(aa,bb,cc,dd,ee,ff,gg,hh,ii)
        check_win()
cdd=True
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
X="X"
O="O"
while True:
    inputin4=input("Veux tu commencer (y/n) ?:")
    if inputin4=="y":
        main()
        inputin2=input("Veux tu rejouer (y/n) ?:")
        if inputin2=="y":
            continue
        else:
            break
    else:
        main2()
        inputin2=input("Veux tu rejouer (y/n) ?:")
        if inputin2=="y":
            continue
        else:
            break