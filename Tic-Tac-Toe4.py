a="7"; b="8"; c="9"; d="4"; e="5"; f="6"; g="1"; h="2"; i="3"; count=0
while count<9:
    print(a+"|"+b+"|"+c); print(d+"|"+e+"|"+f) ;print(g+"|"+h+"|"+i); X="X" if count%2==0 else "O"; inputin=input(str(count%2+1)+" :")
    while True:
        if inputin=="7":a=X
        elif inputin=="8":b=X
        elif inputin=="9":c=X
        elif inputin=="4":d=X
        elif inputin=="5":e=X
        elif inputin=="6":f=X
        elif inputin=="1":g=X
        elif inputin=="2":h=X
        elif inputin=="3":i=X
        break
    count+=1