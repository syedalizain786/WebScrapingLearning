#Python Data Structures

#Collections

#List [ ] ordered and changeable. Duplicates OK


#Index start ffrom zero by default in list

cities = ['Gujrat', 'Lahore', 'Sialkot']
print(cities)

#Throws error because no element at 3rd index
#print(cities[3])

print(cities[::2])

#for printing all
for c in cities:
    print(c)


#Getting to know all list methods
#print(dir(cities))

#Getting detail of all these methods using help
#print(help(cities))

#Length the list
print(len(cities))

#Check if any value in list or not
print("sia" in cities)

#Appending list
cities.append("Pesshawar")

print(cities)

#Remvoving the element
cities.remove("Pesshawar")
print(cities)

#Reversing the list
cities.reverse()
print(cities)

#Returning Index
print(cities.index("Gujrat"))

#Count no of times
print(cities.count("Gujrat"))


########################################################################################
# Set {} unordered and immutable, but Add/Remove OK. NO duplicates

frame={'nodejs','ror','nest','powerbi'}
#Unordered
print(frame)

#Help, Len,dri other functions are same like lists

#Throws error because sets are unordered no indexing
#print(frame[0])

#Add element
frame.add("123")
print(frame)

frame.remove("123")
print(frame)

#Pop method also remove whatever element top of set

print(dir(frame))
#No dulicates allowed

frame.add("nodejs")
print(frame)

##########################################################################################

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits=("apple","orange","mango")
print(fruits)

print(fruits.index("apple"))

print(fruits.count("orange"))



########################################################
# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals={
    "Pakistan":"Islamabad",
    "India":"Delhi",
    "Russia":"Mosscow"
}

#Get values of keys from dictionary
print(capitals.get("Pakistan"))

if capitals.get("India"):
    print("Cappital exists")
else:
    print("Don't exists")

#update can be use to insert new or update previous key
capitals.update({"Germany":"Berlin"})
print(capitals)

capitals.update({"Germany":"Warsac"})
print(capitals)

#"Remove element"
capitals.pop("India")
print(capitals)

#Pop item remove the top element
capitals.popitem()
print(capitals)

#Return keys

print(capitals.keys())

#Items and length
print(capitals.items())
print(len(capitals.items()))

for keys,values in capitals.items():
    print(f"{keys}:{values}")
