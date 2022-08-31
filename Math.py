a=int(input('number : '))
ans=0
i=0
while True:
    ans=(i**2)+((i+1)**2)+((i+2)**2)
    if ans==a:
        print("found")
        print(i, i+1, i+2)
        break
    if ans>a:
        print("impossible")
        break
    i+=1