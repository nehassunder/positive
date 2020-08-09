inp=input("Enter the elements of list1: ")
list1=[]
elements=inp.split(" ")
print("list1:",end=" ")
print(elements)
print("The positive numbers in the list are: ",end=" ")
for num in elements:
    if int(num)>=0:
        print(num,end=",")
