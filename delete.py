#That list----------------------------------------------------------------------------------
"""
thislist = ["Apple","Banana","Mango","Oranges","Cherry","Blueberry","Guava"]
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[0])
if "Apple" in thislist:
    print("Yes Apple is there")
else:
    print("No it is not there")

thislist[1] = "Kiwi"
print(thislist)


thislist[1:3] = ["Kiwi","Watermelon"]
print(thislist)
thislist.insert(2,"watermelon")
print(thislist)


thislist.append("Orange")
print(thislist)


thislist.insert(1,"Peru")
print(thislist)
#That lsit-------------------------------------------------------------------------------------------
#New list------------------------------------------------------
thatlist = ["Grapes","Dragonfruit","Strawberry"]
#----------------------------------------------------------------

thislist.extend(thatlist)
print(thislist)
thislist.remove("Watermelon")
print(thislist)

#------------------------------

thislist.pop(1)
print(thislist)

for x in thislist:
    print(x)
    for i in range(len(thislist)):
        print(thislist[i])



i=0
while i<len(thislist):
    print(thislist[1])
    i=i+1
 """           
#---------------------------------------------------------------------------------------------
b= "   Hello world   "
print(b[:5])
print(b.upper())
print(b.strip())
print(b.find("Hello"))
x= 100<9
print(bool(x))


class myclass():
    def __len__(self):
        return 0
    
myjob = myclass()
print(bool(myjob))

def myFunction() :
    return True

print(bool(myFunction()))

#----------------------------------------TUPLE-------------------------------------------------

fruits=("apple","mango","banana","cherry")
print(type(fruits))
print(fruits[2:5])
print(fruits[:2])
print(fruits[2:])

if "apple" in fruits:
    print("Yes,'apple' is in the fruits list")
else:
    print("No,'apple'is not in the fruits list")
#Converting tuple to list
y= list(fruits)
#Adding the remaining item 
y[1]="kiwi"
#Converting list to tuple
fruits=tuple(y)

print(fruits)

#other way to add items to tuple
#diffrence between the methods is that in append() the adding is done in the last 
#but in in first option it is done after the first value so it is added at 1 
""" Yay """


y= list(fruits)
y.append("orange")
fruits=tuple(y)

print(fruits)

#Removing items from a tuple
y=list(fruits)
y.remove("apple")
fruits=tuple(y)

print(fruits)

""""Unpacking a tuple-----------------------------------------------------------------------------
(a,b,c,d) = fruits
print(a)
print(b)
print(c)
print(d)
"""

#looping a tuple-----------------------------------------------------------------------------
for x in fruits:
    print(x)

#--------------------------------------------------------------------------------------------
for i in range(len(fruits)):
    print(fruits[i])

#While loop for tuple

i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1

x=fruits.count("apple")
print(x)
y= fruits.count("orange")
print(y)
z= fruits.count("kiwi")
print(z)


x=fruits.index("kiwi")
print(x)
# print(95/2)

thisset= set(("apple","mango","banana"))

for x in thisset:
    print(x)

print("banana" in thisset)
#Adding item to the set
thisset.add("orange")
print(thisset)
#Removing item from the set
thisset.discard("orange")
print(thisset)
#removing a random item from the set 
x=thisset.pop()
print(x)


thatset=(("carrot","potato","onion","brinjal"))

bothsets=thisset.union(thatset)
print(bothsets)

#do the same thing writing less code.Here you did not create a new list called as bothlists
#but added the items from one list to the other

thisset.update(thatset)
print(thisset)

#keep items that are same from both the sets

set1={"microsoft","google","apple","samsung"}
set2={"microsoft","nokia","samsung","lenovo"}

set1.intersection_update(set2)
print(set1)

#only keep items which are not present in both the sets

set1.symmetric_difference_update(set2)
print(set1)
#the same tast that is done in the above code 
set1.difference(set2)
print(set1)


this1= {
    "brand": "ford",
    "model": "mustang",
    "year": "1964"
}


print(this1)
print(this1["brand"])

print(len(this1))

x=this1.get("model")
print(x)

x=this1.keys()
print(x)

x=this1.values()
print(x)

#adding an item in the dictionary 

this1["color"] = "red"

print(this1)


if "color" in this1:
    print("Yes,'color' is one of the keys in this1 dictionary ")
else:
    print("No, it is not in this1 dictionary")

this1["color"] = "white"
print(this1)

this1.update({"engine":"V12"})
print(this1)

for x in this1:
    print(this1)

for x in this1.values():
    print(this1)

for x in this1.keys():
    print(this1)

mydict=this1.copy()
print(mydict)

child1={
    "name": "Harry",
    "class":"10",
    "section": "D"
}

child2={
    "name":"Garry",
    "class": "11",
    "section": "A"
}

child3={
    "name":"Larry",
    "class": "9",
    "section": "B"
}


students= {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(students["child2"]["name"])
print(students["child1"]["class"])
print(students["child3"]["section"])

import random

a= random.randrange(1,500)
b=200
c= random.randrange(1,600)
d= random.randrange(1,700)

if a>b:
    print("a is greater than b")
    
elif a==b:
    print("a is equals to b")
else:
    print("No b is greater than a")

#Write short hand Python command 

print("a is greater than b") if a > b else print("b is greater than a")

if a>b and c>d:
    print("Great")
else:
    print("Oh no")

if a>b or c>d:
    print("Atleast one is greater")
else:
    print("it is of no use ") 

#using if statement-----------------------------------------------------------------
if not a>b:
    print("yay")
else:
    print("No!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

x= 12

if x>10:
    print("above 10")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#while loop

i=1
while i < 6:
    print(i)
    i += 1
#Ending the loop on 3
i=1
while i < 6:
    print(i)
    if i==3:
        break
    i+=1

