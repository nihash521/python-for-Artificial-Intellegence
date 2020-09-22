#code snippet for assiging elements for different lists
langs = []

langs.append("Python")
langs.append("Perl")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))
print(langs)

numbers=[1,2,3,4,5,6,7]
numbers.append(25)
print(numbers)

#code snippet for Accessing elements from a tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#code snippet for deleting elemnts in the list
state_capitals={"andhra pradesh":"Hyderbad","maharasta":"mubai","Tamil nadu":"chennai"}
print(state_capitals)
del state_capitals["andhra pradesh"] #deleting element by particular key value
print(state_capitals)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
squares.pop(3)
print(squares)
squares.popitem() #by defult it removes last item 
print(squares)
squares.clear()
print(squares) #clears all elemnts of the dictionary






