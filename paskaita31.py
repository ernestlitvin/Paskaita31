for i in range(5): # [0,1,2,3,4]
    print("labas")
    print("rytas")
    print(i)

print("zemiau ciklo")

num = 24
    #   0 1 2  3 4
nums = [1,2,15,8,10]  #masyvas
print(nums)
print(nums[0])
print(nums[2])

nums.append(14) # prideti nauja nari
print(nums)
nums[1] = 16 # pakeisti viena skaiciu kitu
print(nums)
nums.remove(16) # pasalinti nurodyta reiksme
print(nums)
#           0           1           2       3       4       - indexai visada yra vienu skaiciu mazesni ne masyvo
games = ["zelda", "final fantasy", "gta", "nfs", "top heroes"]
print(games)
print(games[3])

for number in nums:
    print(number)
print("----------------")
print(len(games)) # pasako kiek yra elementu masyve
for zaidimas in games:
    print("My favorite game is " + zaidimas)





count = 0
for i in range(50):
    print(i)
    count += 1

print("prasisuko", count)

print("___________________")
for i in range(10):
    if i % 2 == 0:
        continue # zodis "continue" sustabdo cikla  ir soka i sekancia iteracija
    print(i)

print("___________________")
for i in range(1,10):
    if i % 4 == 0:
        break # zodis "break" sulauzo cikla
    print(i)

print("___________________")
# while - ciklas, kuris sukasi, kol salyga nebus patenkinta
# "while True" - begalybe iteraciju

counter = 0
while True:
    counter += 1
    if counter >= 5:
        break
    print(counter)

print("___________________")
import random
while True:
    rnd_num = random.randint(1,10)
    print(rnd_num)
    if rnd_num == 1:
        break

print("___________________")

is_even = False
while not is_even:
    rnd_num = random.randint(1,10)
    if rnd_num % 2 == 0:
        is_even = True
    print(rnd_num)

print("___________________")

is_not_even = True
while not is_not_even:
    rnd_num = random.randint(1,10)
    if rnd_num % 2 == 0:
        is_not_even = False
    print(rnd_num)


print("test msg")

print("___________________")

for y in range(1,11):
    for x in range(1,11):
        print(y*x, end=" ") # end=" " - suraso i viena eilute rezultata
    print()  # "print()" - kai interacija baigiasi, meta nauja iteracija i nauja eilute
print("paslepta zinute")

print("_______uzd 1___---------------_____")
print(" ")
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
    print("labas")

print(" ")
print("___________________")

print("_______uzd 2___---------------_____")
print(" ")
# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9..

for i in range(0,9):
    print(i)

print(" ")
print("___________________")


print("_______uzd 3_____---------------___")
print(" ")
# Sukurkite masyvą iš dešimties augalų pavadinimų.

augalai = ["roze", "saulegraza", "lelija", "azuolas", "berzas", "meta", "dilgele", "tulpe", "kaktusas", "ramune"]

print(" ")
print("___________________")


print("_______uzd 4_____---------------___")
print(" ")
# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

augalai = ["roze", "saulegraza", "lelija", "azuolas", "berzas", "meta", "dilgele", "tulpe", "kaktusas", "ramune"]
for aug in augalai:
    print(aug)

print(" ")
print("___________________")


print("_______uzd 5_____---------------___")
print(" ")
# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

augalai = ["roze", "saulegraza", "lelija", "azuolas", "berzas", "meta", "dilgele", "tulpe", "kaktusas", "ramune"]
for aug in reversed(augalai):
    print(aug, end=" ")


print(" ")
print("___________________")


print("_______uzd 6_____---------------___")
print(" ")
# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

# 6 uzdavinis
# i % 2 == 0 - porinis (mano skaicius dalintas is 2, jeigu yra lygus 0 - skaicius porinis
# i % 2 != 0  (jeigu nelygus 0 - neporinis)

for i in range(10,51,2):
    print ((i), end=" ")
print()

print(" ")
print("___________________")

print("_______uzd 7_____---------------___")
print(" ")
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10,51,2):
    if i % 10 == 0:
        continue
    print ((i), end=" ")
print()



print("_______uzd 8_____---------------___")
print(" ")

# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;


count = 0
for i in range(21):
    if i % 2 == 0:
        count += 1
        print((i), end=" ")
print()
print("Kiekis poriniu reiksmiu ", count)


print(" ")
print("___________________")

print("_______uzd 9_____---------------___")
print(" ")

# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)

augalai = ["roze", "saulegraza", "lelija", "azuolas", "berzas", "meta", "dilgele", "tulpe", "kaktusas", "ramune"]

trumpi = 0
ilgi = 0

for augalas in augalai:
    if len(augalas) < 5:
        trumpi += 1
    if len(augalas) > 7:
        ilgi += 1

print("Zodziai trumpesni nei 5 simboliai - ", ilgi)
print("Zodziai ilgesni nei 7 simboliai - ", ilgi)

print("_______uzd 10_____---------------___")
print(" ")
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai.
# (tarp 5 ir 10 simbolių ilgio)

augalai = ["roze", "saulegraza", "lelija", "azuolas", "berzas", "meta", "dilgele", "tulpe", "kaktusas", "ramune"]
count = 0

for aug in augalai:
    if len(aug) > 5 and len(aug) < 10:
        count += 1
print(count)

print("_______uzd 11_____---------------___")
print(" ")
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais
# ir suskaičiuokite kiek tarp jų yra didesnių už 150.
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

skaiciai = []
count = 0
for _ in range(300):
    skaicius = random.randint(1,300)
    skaiciai.append(skaicius)
    if skaicius > 150:
        count += 1

for skaicius in skaiciai:
    if skaicius > 275:
        print(f"[{skaicius}]", end=" ")
    else:
        print(skaicius, end=" ")
print()
print("Number of values greater than 150:", count)

print("___________________")

print("_______uzd 12_____---------------___")
print(" ")
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.


results = []

for numbers in range(1,3001):
    if numbers % 77 == 0:
        results.append(numbers)
print(", ".join(str(x) for x in results))


print()
print("_______uzd 13_____---------------___")
# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.









print(" ")






#
# print(" ")
# print("___________________")
#
#
# grades = [
#     [1,2,3,4,4,5] #math
#     [4,5,6] # lt
#     [5,8,10] # tikyba
#     [4,8,8,10] #anglu
#     [7,5,3,4] #fizika
#     [10,4,10] #PE
#
# sum = 0
# count = 0
#
# for lesson in grades:
#
#
# ]







