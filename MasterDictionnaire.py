

print("1 :Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè:")

def rekipere_valè_ak_kle(diksyonè):
    return list(diksyonè.values()), list(diksyonè.keys())

# Test la
diksyonè_test = {"non": "Jean", "laj": 30, "adres": "Rue 10"}
valè, kle = rekipere_valè_ak_kle(diksyonè_test)
print("Liste Valè:", valè)
print("Liste Kle:", kle)


print("2: Verifye si l gen akolad devan ak dèyè:")

# Verifye si l gen akolad devan ak dèyè
def verifye_akolad(chèn):
    if chèn.startswith("{") and chèn.endswith("}"):
        return True
    else:
        return False

valè_antre = input("Tape yon valè: ")
rezilta = verifye_akolad(valè_antre)
if rezilta:
    print("Valè a gen akolad devan ak dèyè.")
else:
    print("Valè a pa gen akolad devan ak dèyè.")
print("3. Afiche tout kle yo:")

def afiche_tout_kle(diksyonè):
    for kle in diksyonè.keys():
        print(kle)

# Test la
diksyonè_test = {"non": "Jean", "laj": 30, "adres": "Rue 10"}
afiche_tout_kle(diksyonè_test)


print("4. Afiche tout valè yo:")

# Afiche tout valè yo
def afiche_tout_valè(diksyonè):
    for valè in diksyonè.values():
        print(valè)

# Test la
diksyonè_test = {"non": "Jean", "laj": 30, "adres": "Rue 10"}
afiche_tout_valè(diksyonè_test)


print("5. Kreye yon kopi sou yon diksyonè:")

def kreye_kopi_diksyonè(diksyonè):
    kopi_diksyonè = diksyonè.copy()
    return kopi_diksyonè

# Test la
diksyonè_test = {"non": "Jean", "laj": 30, "adres": "Rue 10"}
kopi = kreye_kopi_diksyonè(diksyonè_test)
print("Diksyonè Original:", diksyonè_test)
print("Kopi Diksyonè:", kopi)


print ("6. Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo:")

def ajoute_underscore_chenn(diksyonè):
    for kle, valè in diksyonè.items():
        if isinstance(valè, str):
            diksyonè[kle] = f"_{valè}_"
    return diksyonè

# Test la
diksyonè_test = {"non": "Lub", "laj": 14, "biens": ["òdinatè", "telefon"]}
nouvo_diksyonè = ajoute_underscore_chenn(diksyonè_test)
print("Diksyonè Original:", diksyonè_test)
print("Nouvo Diksyonè:", nouvo_diksyonè)


print("7. Kreye yon nouvo diksyonè ak valè ki se chenn sèlman:")

def nouvo_diksyonè_valè_chenn_sèlman(diksyonè):
    nouvo_diksyonè = {k: v for k, v in diksyonè.items() if isinstance(v, str)}
    return nouvo_diksyonè

# Test la
diksyonè_test = {"a": "12", "b": "abc", "c": "12r", "d": "90"}
nouvo_diksyonè = nouvo_diksyonè_valè_chenn_sèlman(diksyonè_test)
print("Diksyonè Original:", diksyonè_test)
print("Nouvo Diksyonè:", nouvo_diksyonè)


print("8. Mete yon diksyonè sou fòm lis:")

def diksyonè_an_lis(diksyonè):
    return list(diksyonè.items())

# Test la
diksyonè_test = {"a": 1, "b": 2}
lis_rezilta = diksyonè_an_lis(diksyonè_test)
print("Diksyonè an Lis:", lis_rezilta)

print("9:  Mete yon lis sou fòm diksyonè")
# Mete yon lis sou fòm diksyonè
def lis_an_diksyonè(lis):
    return dict(lis)

# Test la
lis_test = [("a", 1), ("b", 2)]
diksyonè_rezilta = lis_an_diksyonè(lis_test)
print("Lis an Diksyonè:", diksyonè_rezilta)

