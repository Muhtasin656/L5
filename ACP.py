row=int(input("how many rows do you want:"))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()