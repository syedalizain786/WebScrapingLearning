#Generators in Python

#Iterator is use to iterate the integers vales in python
#for loop use iterator behind the scene

data=[1,2,3,4]

# for d in data:
#     print(d)

it=iter(data)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Stops iteration because of no value

#print(next(it))

while True:
    try:
        print(next(it))
    except Exception as e:
         break


#Generator in Python (for effiecient memory occupancy)
#Memory Efficent for large datasets and large data
def creator():
    i=1
    while i<=200:
        yield i
        i+=1

x=creator()
print(next(x))

def generator():
    for i in range(1000):
        yield i


g=generator()
# print(next(g))
# print(next(g))

#It occupy memeory on the fly. Don't occup memory like list beforehand. Whenever whatever space is required
#It will occupy

# for j in g:
#     print(j)

print(list(g))

#A usecase can be, when creating a image visualization tool that takes entire directory as the input,
# you may not want to load all the images. At that time, generators can be used.