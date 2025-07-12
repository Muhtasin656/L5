rows=int(input("enter how many rows you want:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()