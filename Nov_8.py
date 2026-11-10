#learning from code with harry
#learning set

"""s1={1,2,3,4,5}
s2={3,8,10,12}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1,s2)
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s2.issuperset(s1))
s1.update(s2)
print(s1)

cities ={"hetauda" , "chitwan" ,"kathmandu","Newyork"}
#del cities
print (cities) 
#we get an error here because we have deleted entire set of cities. These kind of eror is called name error.

if "hetauda" in cities:
    print("hetauda is present")
else:
    print("hetauda is absent")

cities.clear()
print (cities)


#let's see something  in dictionaries

di = {'name' : 'shyam', 'age' : 467 , 'home' : ' not to be declared yet'}

#print(di(class)) , here it displays error because there is no such key called class
#if you want to check if some key exists or not then you can write like this:

print(di.get('class'))

# for accessing all the keys

print(di.keys())
print(di.values())
print(di.items())


for key in di.keys():
    print(di[key])



#dictionaries method is same as that of set methods

# Creating multiplication table in python using exception handling.


try:
    
    num = int(input("enter the number "))
    for i in range(1,11):
        print(f"{num} * {i} ={num*i}")


except ValueError:
    print("the number input is not an integer")  # we canwrite here except: only ad the Exception we used here is an built in class which stores error
    print("this is invalid input")"""
    

#using finin eror handling
def myfunc():
    yu = [ 1,2,3,4,5,6,7,8] 

    try:
        num = int(input("enter the index"))

        for i in yu:
            print(yu[i])
            return 1
    
    
    except IndexError:
        print("The index doesn't exist here")
        return 0

    finally:
        print("you are at the end!")


myfunc()


        