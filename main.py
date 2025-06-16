import re
import random


print("-------------------------- 06-12 paskaita --------------------------")

vardas = "pEtRaS_pOnaAas"

print(vardas.lower())
print(vardas.upper())
print(vardas.capitalize())
print(len(vardas))

print(vardas)
print(vardas[0])
print(vardas[1:4].lower()) ## 1 inclusive (ieina), 4 exclusive (neiina)

print(vardas)

# 0 1 2 3 4 5
# p e t r a s

print(vardas[-3])
print(vardas[-2:])

print(vardas.replace("a", "+"))

print("kazkoks sprendimas")
print()

all = "0123abc456def789ghijklmnoprtsuvzwgyABCDEFGHIJK"
print(re.sub("[a]", "+", all))
print(re.sub("[A-D]", "+", all))

print(" ")
print("-------uzd 1-----")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus
# (Jonas Jonaitis). Atspausdinti trumpesnį stringą.

vardas = "Daniel"
pavarde = "Radcliffe"

print(vardas + " " + pavarde)

print(len(vardas))
print(len(pavarde))

if len(vardas) < len(pavarde):
    print(pavarde)
elif len(vardas) > len(pavarde):
    print(vardas)
else:
    print("Vienodi")

print(" ")
print("-------uzd 2-----")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)

vardas = "Daniel"
pavarde = "Radcliffe"

print(vardas.upper() + " " + pavarde.lower())

print(" ")
print("-------uzd 3-----")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.

vardas = "Daniel"
pavarde = "Radcliffe"
mix = vardas[0:3] + " " + pavarde[0:3]
print(vardas + " " + pavarde)
print(mix)

print(" ")
print("-------uzd 4-----")
# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių.
# Jį atspausdinti.

vardas = "Daniel"
pavarde = "Radcliffe"
mix = vardas[-3:] + " " + pavarde[-3:]

print(vardas + " " + pavarde)
print(mix)

print(" ")
print("-------uzd 5-----")

# Sukurti kintamąjį su stringu: "An American in Paris".
# Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.

name = "An American in Paris"

print(re.sub("[Aa]", "*", name))

print(" ")
print("-------uzd 6-----")
# Sukurti kintamąjį su stringu: "An American in Paris". Jame ištrinti visas balses.
# Rezultatą atspausdinti. Kodą pakartoti su stringais:
# "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".


# print(re.sub("[aeiouAEIOU]", "", name))

name = "An American in Paris"
name1 = "Breakfast at Tiffany's"
name2 = "2001: A Space Odyssey"
name3 = "It's a Wonderful Life"

print((re.sub("[aeiouAEIOU]", "", name)) + (re.sub("[aeiouAEIOU]", "", name1)) + (re.sub("[aeiouAEIOU]", "", name2) + (re.sub("[aeiouAEIOU]", "", name3))))

print(re.sub("[aeiouAEIOU]", "", name))
print(re.sub("[aeiouAEIOU]", "", name1))
print(re.sub("[aeiouAEIOU]", "", name2))
print(re.sub("[aeiouAEIOU]", "", name3))

print(" ")
print("-------uzd 7-----")
# Stringe, kurį generuoja toks kodas: starWars = "Star Wars: Episode " + (" " * random.randint(1, 9))
# + str(random.randint(1, 7)) + " - A New Hope"
# Surasti ir atspausdinti epizodo numerį.



starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"

print(starWars)
print(starWars[-14])
print(re.sub(r"[^\d]","",starWars))

print(" ")
print("-------uzd 9-----")
# Parašyti kodą, kuris generuotų atsitiktinį stringą iš lotyniškų mažųjų raidžių. Stringo ilgis 3 simboliai.

import random
import string

length = 3
random_letters = ''.join(random.choices(string.ascii_lowercase, k = length))
print(random_letters)

print(" ")
print("-------uzd 8-----")
# Suskaičiuoti kiek stringe “Don't Be a Menace to South Central While Drinking Your Juice in the Hood” yra žodžių trumpesnių arba lygių nei 5 raidės.
# Pakartokite kodą su stringu “Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale”.

name = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
print(name)
print(len(name))


git config --global user.name "ernestlitvin"
git config --global user.email "erik.litvin@gmail.com"

