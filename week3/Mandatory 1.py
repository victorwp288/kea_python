bod = ['Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren']
mgt = ['Tine', 'Trunte', 'Rane']
emp = ['Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars']


#who in the board of directors is not an employee?
s = set(emp)
lst = [x for x in bod if x not in s]
print(lst)

#who in the board of directors is also an employee?
kset = set(emp) & set(bod)
print(kset)

#how many of the management is also member of the board?
vset = set(bod) & set(mgt)
print(vset)

#All members of the managent also an employee
dset = set(emp) & set(mgt)
print(dset)

#All members of the management also in the board?
bset = set(mgt) & set(bod)
print(bset)

#Who is an employee, member of the management, and a member of the board?
tset = set(emp) & set(mgt) & set(bod)
print(tset)

#Who of the employee is neither a memeber or the board or management?


#Using a list comprehension create a list of tuples from the folowing datastructure
t = tuple (['a' 'Alpha','b' 'Beta','g' 'Gamma'])


#Of the 2 sets create a:
s1 = {'a', 'e', 'i', 'o', 'u', 'y'}
s2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

#Union
print(s1 | s2)

#Symmetric Difference
print(s1 ^ s2)

#Difference
print(s1 - s2)

#Disjoint
print(s1 & s2)