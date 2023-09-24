# 2.10 
# nadim barakat
# exercices for Python Crash Course 2-1, 2-2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-10

# 2.1 
name = "nadim"
print(name)

# 2.2 
animal = "cat"
print(animal)
animal = "dog"
print(animal)

# 2.3
person = "John"
print("Hello " + person + "! How are you?")

# 2.4 
new_name = "Eric"
print(new_name.lower(), " ", new_name.upper(), " ", new_name.title())

# 2.5 
print("""JFK once said "ask not what your country can do for you — ask what you can do for your country" """)

# 2.6 
famous_person = "JFK"
quote = "'ask not what your country can do for you — ask what you can do for your country'"
print(famous_person, "once said", quote)

# 2.7 
human = "\tbob\n"
print(human)
print(human.lstrip())
print(human.rstrip())
print(human.strip())

# 2.10 
# see file header 


# 3-1, 3-2, 3-3, 3-4, 3-5, 3-6, 3-7, 3-8
print()

# 3.1 
names = ["john", "emily", "steve"]
for name in names: 
    print(name)

# 3.2
for name in names: 
    print("hello ", name)

# 3.3 
items = ["chicken", "soup", "banana"]
for item in items: 
    print("I would like to eat", item)

# 3.4 
guests = ["mom", "dad", "siblings"]
for guest in guests: 
    print("You are invited to dinner", guest)

# 3.5 
guests = ["bob", "joe", "siblings"]
for guest in guests: 
    print("You are invited to dinner", guest)

print(guests[2], "can't make it")
for guest in guests[:-1]:
    print("you are invited to dinner, ", guest)

# 3.6 
print("we found a bigger table")
guests.insert(0, "john")
guests.insert(1, "emily")
guests.append("george")
for guest in guests: 
    print("You are invited to dinner", guest)

# 3.7 
print()

print("I can only invite two people")
for guest in guests[2:]:
    print(guests[-1], "you can't come")
    guests.pop()

for guest in guests: 
    print(guest, "you are still invited")

del guests[0]
del guests[0]
print(guests)

print()
print()

# 3.8 
places = ["maine", "japan", "australia", "indonesia", "brazil"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 4-1, 4-2, 4-3, 4-6, 4-10, 4-11
print()
print()
# 4-1 
pizzas = ["cheese", "chicken", "pineapple"]
for pizza in pizzas: 
    print("I like", pizza, "pizza")
print("I like all pizzas")

print()
# 4-2
animals = ["bird", "dog", "cat"]
for animal in animals:
    print(animal, "would make a great pet")
print("all these would make great pets")

# 4-3
for num in range(20): 
    print(num + 1)

print()
# 4-6
for num in range(1, 20, 2):
    print(num)

# 4-10 
stuff = ["car", "chair", "math", "notebook", "phone", "computer", "board"]
print("the first three are ", stuff[:3])
print("the middle three are ", stuff[3:6])
print("the last three are ", stuff[4:])


# 4-11
pizzas = ["cheese", "chicken", "pineapple"]
friends_pizzas = []
for pizza in pizzas: 
    friends_pizzas.append(pizza)

pizzas.append("pepperoni")
friends_pizzas.append("alfredo")
print("my favorite pizzas are")
for pizza in pizzas: 
    print(pizza, end = ", ")

print()

print("my friend favorite pizzas are ")
for friend_pizza in friends_pizzas: 
    print(friend_pizza, end = ", ")