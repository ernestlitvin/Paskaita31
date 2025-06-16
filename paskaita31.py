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



# 6 uzdavinis
# i % 2 == 0 - porinis (mano skaicius dalintas is 2, jeigu yra lygus 0 - skaicius porinis
# i % 2 != 0  (jeigu nelygus 0 - neporinis)

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


