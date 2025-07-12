rows=int(input("enter how many rows you want"))
number=1
print("floyd triangle")
for i in range(rows):
    for j in range(i+1):
        print(number,end=" ")
        number=number+1
    print()