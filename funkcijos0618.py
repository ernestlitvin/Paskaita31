# Medziaga

import random
""""
def say_hi(): #nieko nepriima, nieko negrazina
    print("sveikuciai")
say_hi()

def lala():
    print("hala")
lala()


def say_hi_to(name):#priima kintamaji, nieko negrazina
    print("hi", name)
say_hi_to("Jonas")
say_hi_to("Petras")

def lala(vardas):
    print("hala", vardas)
lala("ernestas")

vardas = "Klemensas"
lala(vardas)



def sim_pi():#nieko nepriima, grazina reiksme
    return 3.14
print(sim_pi())
# sp = sim_pi()
# print(sp)



def sumavimas(a,b):#priima du kintamuosius, grazina reiksme
    return a + b

res = sumavimas(123,5)
print(res)


def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

print( make_initials("Naglis","Mockevicius") )

print( make_initials("naglis","mockevicius") )

def make_initials_v2(txt):
    parts = txt.split()
    init = ""
    for pt in parts:
        init += pt[0]
    return init.upper()
print(make_initials_v2("Naglis Mockevicius"))
print(make_initials_v2("Naglis Jonas Mockevicius"))


def calc_age(birth_year=2025):
    return 2025 - birth_year

age = calc_age()
print(age)
age = calc_age(1914)
print(age)

def print_info(name = "", surname = "", birth_year = 0):
    print("mano vardas",name,"pavarde",surname,"gimimo metai",birth_year)


print_info()
print_info("Naglis")
print_info(35)
print_info(surname="Mockevicius",birth_year = 1999)



def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

txt = generate_rnd_str(10)
print(txt)
for i in txt:
    print(i)
"""
print()
print("---------UZD 1-----------")
# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def sumavimas(a,b):
    print (a+b)
sumavimas(3,7)

print()
print("---------UZD 2-----------")
# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

def PISq():
    return 9.8596

print(PISq())

print()
print("---------UZD 3-----------")
# Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

def sandauga(a,b):
    return a*b
print(sandauga(3,7))

print()
print("---------UZD 4-----------")
# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.

numbers = [1,2,3,4,5,6,7,8,9]

def my_list(lst):
    for skaiciai in lst:
        print(skaiciai, end = " ")

my_list(numbers)

print()
print("---------UZD 5-----------")
# Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.


def skaiciai(min, max):
    nam = random.randint(min, max)
    return nam

print(skaiciai(10,100))

print()
print("---------UZD 6-----------")

# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.


import random
def skaiciai(min,max,length):
    nums = []
    for sk in range(length):
        nam = random.randint(min,max)
        nums.append(nam)
    return nums

print(skaiciai(1,10, 5))

print()
print("---------UZD 7-----------")

# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį),
# susumuotų ir gražintų reikšmę.


masyvas = skaiciai(1,10,5)

def suma(masyvas):
    return sum(masyvas)

print(masyvas)
print(suma(masyvas))

print()
print("---------UZD 8-----------")
# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.

masyvas = skaiciai(1,10,5)

def vid(masyvas):
    return sum(masyvas) / len(masyvas)

print(masyvas)
print(vid(masyvas))

print()
print("---------UZD 9-----------")
# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.

def square(aukstis, plotis):
    for x in range(aukstis):
        for y in range(plotis):
            print("*", end=" ")
        print()

square(3,8)

print()
print("---------UZD 10-----------")

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)




