countries=['united kingdom','ghana','india','nigeria']
string='Pramit'
#print(countries[2][1])
print(countries[1:3])
#print(type(countries))
#print(type(string))
countries[0]='australia'
countries[2]='pakistan'
print(countries)

print(countries[-1])#nigeria(last element)
print(countries[-2])#2nd last

print (len(countries))
#list constructor-list()-using this we can put all string int and bool value ...
l1=list(("pramit",19,True))
l2=["pramit",19,True]
print(l1)
print(l2)