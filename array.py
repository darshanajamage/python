import array as arr
a=arr.array('i',[1,2,3,4,5,6,7])
print("The new created array is :",end=" ")
for i in range(0,7):
    print(a[i],end=" ")
a.insert(1,2)
print("Array after insertion:",end=" ")
for i in(a):
    print(i,end=" ")
a.append(8)
print("Array after adding the ele:",end=" ")
for i in(a):
    print(i,end=" ")
a.remove(8)
print("Array after removing:",end=" ")
for i in(a):
    print(i,end=" ")
a.pop()
print("Array after poping:",end=" ")
for i in(a):
    print(i,end=" ")
a.reverse()
print("Array after reversing:",end=" ")
for i in(a):
    print(i,end=" ")
a.clear()
print("Array after clearing:",end=" ")
for i in(a):
    print(i,end=" ")