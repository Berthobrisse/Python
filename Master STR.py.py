# Mettez tous les caractères en minuscules

print("1 :"+"Mettez tous les caractères en minuscules")

string_lowercase = "Bonjour Tout Le Monde"
lowercase_result = string_lowercase.lower()
print(lowercase_result)

# Coupez la chaîne partout où il y a des espaces
print("2 :"+"Coupez la chaîne partout où il y a des espaces")

string_split = "Ayibobo Haïti"
split_result = string_split.split()
print(split_result)

# Mettez en majuscule la première lettre de chaque mot
print("3 :"+"Mettez en majuscule la première lettre de chaque mot")
string_title = "mettez en majuscule la première lettre"
title_result = string_title.title()
print(title_result)

# Récupérez la première lettre de chaque mot

print("4 :"+"Récupérez la première lettre")
string_initials = "Récupérez la première lettre"
initials_result = ''.join(word[0] for word in string_initials.split())
print(initials_result)

# Remplacez tous les caractères "a" par "@"


print("5 :"+"Remplacez tous les caractères a")
string_replace = "Remplacez tous les caractères a"
replace_result = string_replace.replace('a', '@')
print(replace_result)


# Mettez une chaîne en majuscule
print("6 :"+"Mettez une chaîne en majuscule")
string_upper = "haïti"
upper_result = string_upper.upper()
print(upper_result)

# Index du premier caractère "a" dans une chaîne
print("7 :"+"Index du premier caractère a dans une chaîne")
string_first_a = "Haïti peut avancer"
first_a_index = string_first_a.find('a')
print(first_a_index)

# Index total de tous les caractères "a" dans une chaîne

print("8 :"+" Index total de tous les caractères a dans une chaîne")
string_total_a = "Haïti peut avancer"
total_a_index = string_total_a.lower().count('a')
print(total_a_index)

# Liste des index de tous les caractères "a" dans une chaîne (minuscules uniquement)

print("9 :"+"  Liste des index de tous les caractères a dans une chaîne (minuscules uniquement)")
string_all_a = "Haïti peut avancer"
all_a_indexes = [i for i, letter in enumerate(string_all_a) if letter == 'a']
print(all_a_indexes)



#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo) en python

print("10 :  Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo) en python")
chenn = "Sa se yon chenn ak espas ki gen karaktè"


chenn_san_espas = chenn.replace(" ", "")
kantite_karakte = len(chenn_san_espas)



print("Chenn san espas:", chenn_san_espas)
print("Kantite karaktè san espas:", kantite_karakte)
