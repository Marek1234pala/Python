import random
def nul():
    global aa
    global r
    global c
    for r in range(9):
        for c in range(9):
            if aa[r][c]==0:
                return r,c 
def test():
    global aa
    global r
    global c
    global c0
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global r0
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7
    global r8
    global cc0
    global cc1
    global rr0
    global rr1
    if r<3 and c<3:
        if r==0:
            rr0=1
            rr1=2
        if r==1:
            rr0=0
            rr0=2
        if r==2:
            rr0=0
            rr1=1
        if c==0:
            cc0=1
            cc1=2
        if c==1:
            cc0=0
            cc0=2
        if c==2:
            cc0=0
            cc1=1
    elif r<3 and c<6:
        if r==0:
            rr0=1
            rr1=2
        if r==1:
            rr0=0
            rr0=2
        if r==2:
            rr0=0
            rr1=1
        if c==3:
            cc0=4
            cc1=5
        if c==4:
            cc0=3
            cc0=5
        if c==5:
            cc0=3
            cc1=4
    elif r<3 and c<9:
        if r==0:
            rr0=1
            rr1=2
        if r==1:
            rr0=0
            rr0=2
        if r==2:
            rr0=0
            rr1=1
        if c==6:
            cc0=7
            cc1=8
        if c==7:
            cc0=6
            cc0=8
        if c==8:
            cc0=6
            cc1=7
    elif r<6 and c<3:
        if r==3:
            rr0=4
            rr1=5
        if r==4:
            rr0=3
            rr0=5
        if r==5:
            rr0=3
            rr1=4
        if c==0:
            cc0=1
            cc1=2
        if c==1:
            cc0=0
            cc0=2
        if c==2:
            cc0=0
            cc1=1
    elif r<6 and c<6:
        if r==3:
            rr0=4
            rr1=5
        if r==4:
            rr0=3
            rr0=5
        if r==5:
            rr0=3
            rr1=4
        if c==3:
            cc0=4
            cc1=5
        if c==4:
            cc0=3
            cc0=5
        if c==5:
            cc0=3
            cc1=4
    elif r<6 and c<9:
        if r==3:
            rr0=4
            rr1=5
        if r==4:
            rr0=3
            rr0=5
        if r==5:
            rr0=3
            rr1=4
        if c==6:
            cc0=7
            cc1=8
        if c==7:
            cc0=6
            cc0=8
        if c==8:
            cc0=6
            cc1=7
    elif r<9 and c<3:
        if r==6:
            rr0=7
            rr1=8
        if r==7:
            rr0=6
            rr0=8
        if r==8:
            rr0=6
            rr1=7
        if c==0:
            cc0=1
            cc1=2
        if c==1:
            cc0=0
            cc0=2
        if c==2:
            cc0=0
            cc1=1
    elif r<9 and c<6:
        if r==6:
            rr0=7
            rr1=8
        if r==7:
            rr0=6
            rr0=8
        if r==8:
            rr0=6
            rr1=7
        if c==3:
            cc0=4
            cc1=5
        if c==4:
            cc0=3
            cc0=5
        if c==5:
            cc0=3
            cc1=4
    elif r<9 and c<9:
        if r==6:
            rr0=7
            rr1=8
        if r==7:
            rr0=6
            rr0=8
        if r==8:
            rr0=6
            rr1=7
        if c==6:
            cc0=7
            cc1=8
        if c==7:
            cc0=6
            cc0=8
        if c==8:
            cc0=6
            cc1=7
    if c==0:
        c0=-8
        c1=-8
        c2=-7
        c3=-6
        c4=-5
        c5=-4
        c6=-3
        c7=-2
        c8=-1
    if c==1:
        c0=-9
        c1=-7
        c2=-7
        c3=-6
        c4=-5
        c5=-4
        c6=-3
        c7=-2
        c8=-1
    if c==2:
        c0=-9
        c1=-8
        c2=-6
        c3=-6
        c4=-5
        c5=-4
        c6=-3
        c7=-2
        c8=-1
    if c==3:
        c0=-9
        c1=-8
        c2=-7
        c3=-5
        c4=-5
        c5=-4
        c6=-3
        c7=-2
        c8=-1
    if c==4:
        c0=-9
        c1=-8
        c2=-7
        c3=-6
        c4=-4
        c5=-4
        c6=-3
        c7=-2
        c8=-1
    if c==5:
        c0=-9
        c1=-8
        c2=-7
        c3=-6
        c4=-5
        c5=-3
        c6=-3
        c7=-2
        c8=-1
    if c==6:
        c0=-9
        c1=-8
        c2=-7
        c3=-6
        c4=-5
        c5=-4
        c6=-2
        c7=-2
        c8=-1
    if c==7:
        c0=-9
        c1=-8
        c2=-7
        c3=-6
        c4=-5
        c5=-4
        c6=-3
        c7=-1
        c8=-1
    if c==8:
        c0=-9
        c1=-8
        c2=-7
        c3=-6
        c4=-5
        c5=-4
        c6=-3
        c7=-2
        c8=-9
    if r==0:
        r0=-8
        r1=-8
        r2=-7
        r3=-6
        r4=-5
        r5=-4
        r6=-3
        r7=-2
        r8=-1
    if r==1:
        r0=-9
        r1=-7
        r2=-7
        r3=-6
        r4=-5
        r5=-4
        r6=-3
        r7=-2
        r8=-1
    if r==2:
        r0=-9
        r1=-8
        r2=-6
        r3=-6
        r4=-5
        r5=-4
        r6=-3
        r7=-2
        r8=-1
    if r==3:
        r0=-9
        r1=-8
        r2=-7
        r3=-5
        r4=-5
        r5=-4
        r6=-3
        r7=-2
        r8=-1
    if r==4:
        r0=-9
        r1=-8
        r2=-7
        r3=-6
        r4=-4
        r5=-4
        r6=-3
        r7=-2
        r8=-1
    if r==5:
        r0=-9
        r1=-8
        r2=-7
        r3=-6
        r4=-5
        r5=-3
        r6=-3
        r7=-2
        r8=-1
    if r==6:
        r0=-9
        r1=-8
        r2=-7
        r3=-6
        r4=-5
        r5=-4
        r6=-2
        r7=-2
        r8=-1
    if r==7:
        r0=-9
        r1=-8
        r2=-7
        r3=-6
        r4=-5
        r5=-4
        r6=-3
        r7=-1
        r8=-1
    if r==8:
        r0=-9
        r1=-8
        r2=-7
        r3=-6
        r4=-5
        r5=-4
        r6=-3
        r7=-2
        r8=-9
def logi():
    global aa
    global r
    global c
    global c0
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global r0
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7
    global r8
    global cc0
    global cc1
    global rr0
    global rr1
    global i
    bb=[1,2,3,4,5,6,7,8,9]
    while True:
        if i>300:
            aa[0]=[0,0,0,0,0,0,0,0,0]
            aa[1]=[0,0,0,0,0,0,0,0,0]
            aa[2]=[0,0,0,0,0,0,0,0,0]
            aa[3]=[0,0,0,0,0,0,0,0,0]
            aa[4]=[0,0,0,0,0,0,0,0,0]
            aa[5]=[0,0,0,0,0,0,0,0,0]
            aa[6]=[0,0,0,0,0,0,0,0,0]
            aa[7]=[0,0,0,0,0,0,0,0,0]
            aa[8]=[0,0,0,0,0,0,0,0,0]
            i=0
            break
        aa[r][c]=bb[random.randint(0,8)]
        if aa[r][c]!=aa[r][c0] and aa[r][c]!=aa[r][c1] and aa[r][c]!=aa[r][c2] and aa[r][c]!=aa[r][c3] and aa[r][c]!=aa[r][c4] and aa[r][c]!=aa[r][c5] and aa[r][c]!=aa[r][c6] and aa[r][c]!=aa[r][c7] and aa[r][c]!=aa[r][c8]:
            if aa[r][c]!=aa[r0][c] and aa[r][c]!=aa[r1][c] and aa[r][c]!=aa[r2][c] and aa[r][c]!=aa[r3][c] and aa[r][c]!=aa[r4][c] and aa[r][c]!=aa[r5][c] and aa[r][c]!=aa[r6][c] and aa[r][c]!=aa[r7][c] and aa[r][c]!=aa[r8][c]:
                if aa[r][c]!=aa[r][cc0] and aa[r][c]!=aa[r][cc1] and aa[r][c]!=aa[rr0][c] and aa[r][c]!=aa[rr1][c] and aa[r][c]!=aa[rr1][cc0] and aa[r][c]!=aa[rr1][cc1] and aa[r][c]!=aa[rr0][cc0] and aa[r][c]!=aa[rr0][cc1]:
                    break
        else:
            i+=1
            continue
def win():
    global cdd
    global aa
    if aa[0][0]+aa[1][0]+aa[2][0]+aa[3][0]+aa[4][0]+aa[5][0]+aa[6][0]+aa[7][0]+aa[8][0]==45:
        if aa[0][8]+aa[1][8]+aa[2][8]+aa[3][8]+aa[4][8]+aa[5][8]+aa[6][8]+aa[7][8]+aa[8][8]==45:
            if aa[8][0]+aa[8][1]+aa[8][2]+aa[8][3]+aa[8][4]+aa[8][5]+aa[8][6]+aa[8][7]+aa[8][8]==45:
                cdd=False
cdd=True
r=0
c=0
c0=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
r0=0
r1=0
r2=0
r3=0
r4=0
r5=0
r6=0
r7=0
r8=0
cc0=0
cc1=0
rr0=0
rr1=0
aa=[0,1,2,3,4,5,6,7,8]
aa[0]=[0,0,0,0,0,0,0,0,0]
aa[1]=[0,0,0,0,0,0,0,0,0]
aa[2]=[0,0,0,0,0,0,0,0,0]
aa[3]=[0,0,0,0,0,0,0,0,0]
aa[4]=[0,0,0,0,0,0,0,0,0]
aa[5]=[0,0,0,0,0,0,0,0,0]
aa[6]=[0,0,0,0,0,0,0,0,0]
aa[7]=[0,0,0,0,0,0,0,0,0]
aa[8]=[0,0,0,0,0,0,0,0,0]
i=0
while cdd:
    nul()
    test()
    logi()
    win()
    i=0
    print(aa)
print("finis")
print(aa[0])
print(aa[1])
print(aa[2])
print(aa[3])
print(aa[4])
print(aa[5])
print(aa[6])
print(aa[7])
print(aa[8])