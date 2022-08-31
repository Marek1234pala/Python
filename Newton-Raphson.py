x0=1
x2=x0
i=0
while True:
    try:
        x1 = x0-(((x0**4)-2)/((x0**3)*4))
    except:
        ZeroDivisionError
        x0=x2/2
        x2=x0
        x1=x0
        #print("changed")
        #print(x2)
    x0 = x1
    print(x1)
    if ((x0**4)-2)==0:
        break
    if i>=500:
        x0=x2/2
        x2=x0
        #print("changed")
        #print(x2)
    i+=1
print("Found")
if x1==1.1113793747425387e-162:
    x1=0
print(x1)