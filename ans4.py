list1=[]
n1=int(input("enter the size of list 1:"))
print("enter the elements of list1:")
for i in range (0,n1):
    element=int(input())
    list1.append(element)
print(list1)
def func(a,b):
    del list1[a:b]
    return list1
y=input("Do you want to delete(enter 1) or insert(enter 2) and element:")
if(y=="1"):
    z=input("You want to delete by value(enter 3) or index(enter 4) or slice of elements(enter 5):")
    if(z=="3"):
        a=int(input("Please enter the element to delete:"))
        list1.remove(a)
        print(list1)
    elif(z=="4"):
        a=int(input("Please eneter index to delete:"))
        list1.pop(a)
        print(list1)
#pop is used to remove by index and remove is used to remove by value
    elif(z=="5"):
        p=int(input("index of 1st element to be removed"))
        q=int(input("index of the last element to be removed"))

        cropped_list=func(p,q)
        print("The remaining list is:",cropped_list)
if(y=="2"):
    t=int(input("enter the element to be inserted:"))
    list1.append(t)
    print(list1)

        


 







