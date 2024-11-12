print(
"""Projekt_1.py: první projekt do Engeto Online Python Akademie (Datový analytik s Pythonem)
Author: Monika Matějková
Email: moncinas@centrum.cz\n""")

# Zadaný text
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

print("Projekt 1 - Textový analyzátor\n")

# Registrovaní uživatelé
USERS = {"bob": "123", "ann": "pass123", "mike": "password123"}

# Zadání jména a hesla uživatele
USERNAME = input("username: ")
PASSWORD = input("password: ")

# Ověření uživatele
if USERNAME in USERS and USERS[USERNAME] == PASSWORD:
    print("-" * 42)
    print(f"Welcome to the app, {USERNAME}") 
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu
print("We have 3 texts to be analyzed.") 
print("-" * 42)

# Přiřazení textu
USER_INPUT = input("Enter a number btw. 1 and 3 to select: ")

if USER_INPUT.isdigit():  
    NUMBER = int(USER_INPUT)
    if 1 <= NUMBER <= 3: 
        TEXTS_DICT = {
            "text1": TEXTS[0].strip(),
            "text2": TEXTS[1].strip(),
            "text3": TEXTS[2].strip()
        }
        SELECTED_TEXT = TEXTS_DICT[f"text{NUMBER}"] 
    else:
        print("ERROR: Number must be between 1 and 3.")
        exit()
else:
    print("ERROR: Number must be between 1 and 3.")
    exit()

# Začátek analýzy pro vybraný text
NUMBER_TITLECASE = 0
NUMBER_UPPERCASE = 0
NUMBER_LOWERCASE = 0
NUMBER_NUMBERS = 0
SUM_NUMBERS = 0
WORD_LENGTHS = {}

# Rozdělení textu na slova
SLOVA = SELECTED_TEXT.split()

for slovo in SLOVA:
    # Vyčištění slova od interpunkce
    slovo = slovo.strip(",.?!:-_<>")
    
    # Počet slov začínajících velkým písmenem
    if slovo.istitle():
        NUMBER_TITLECASE += 1
    
    # Počet psaných velkými písmeny
    elif slovo.isupper():
        NUMBER_UPPERCASE  += 1
    
    # Počet slov psaných malými písmeny 
    elif slovo.islower():
         NUMBER_LOWERCASE += 1
    
    # Počet čísel (ne cifer) a jejich součet
    if slovo.isdigit():
        NUMBER_NUMBERS  += 1
        SUM_NUMBERS += int(slovo)

    # Délky slov pro sloupcový graf
    delka = len(slovo)
    if delka not in WORD_LENGTHS:
        WORD_LENGTHS [delka] = 1
    else:
        WORD_LENGTHS [delka] += 1

# Výsledek bádání
print(f"There are {len(SELECTED_TEXT.split())} words in the selected text.")
print(f"There are {NUMBER_TITLECASE} titlecase words.")
print(f"There are {NUMBER_UPPERCASE} uppercase words.")
print(f"There are {NUMBER_LOWERCASE} lowercase words.")
print(f"There are {NUMBER_NUMBERS} numeric strings.")
print(f"The sum of all the numbers {SUM_NUMBERS}")

# Sloupcový graf četnosti délek slov
print("\nLEN|     OCCURENCES     |NR.")
print("-" * 42)
for delka in sorted(WORD_LENGTHS):
    print(f" {delka:2}|{'*' * WORD_LENGTHS[delka]:<20}|{WORD_LENGTHS[delka]}")