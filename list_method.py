#List is a container to contain different types of objects and is used to iterate objects.
#1.List is mutable
#2.List iteration is slower and is time consuming.
#3.List is useful for insertion and deletion operations.
#4.List consumes more memory

list1=[4,5,3,1,2]
list2=['banana','apples','mango','oranges']
#combined 2list together-extend()
#list1.extend(list2)
#print(list1)

#append-use to add a element at the end of the list.
print(len(list2))#length of the list is 4
list2.append('cherry')
print(list2)
print(len(list2))#after appending one element length of the list will be 5

#insert function-
list2.insert(1,'pineapple')#insert an elemnt at index 1..
#print(list2)

#remove function--
list2.remove('banana')
#del list2[0]
#print(list2)

#clear function-
#list2.clear()#now the list should be null..
#print(list2)

#check the index number--
print(list2.index('mango'))

#count the list elements
print(list2.count('mango'))#in our list mango is one time

#sorted order-
list1.sort()
print(list1)
#reverse order-
list2.reverse()
print(list2)
#copy-
#list3=list2.copy()
#print(list3)

#delete the last value--
list2.pop(1)
print(list2)
