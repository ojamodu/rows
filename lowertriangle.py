row = int(input('enter the number of rows'))
if row%2==0:
    half=int(row/2)
else:
    half= int(row/2)+1
space= half-1
for c in range(1,half+1):
    for d in range(1, space+1):
        print(end=" ")
    space= space-1
    num= 1
    for d in range(2*c-1):
        print(end=str(num))
        num = num+1
    print()
space=1
for c in range(1,half):
    for d in range(1, space+1):
        print(end=" ")
    space= space+1
    num= 1
    for d in range(1,2*(half-c)):
        print(end=str(num))
        num = num+1
    print()
