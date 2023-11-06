print("# 1 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif")
     
  
n = 20
divisible_by_2 = [i for i in range(n + 1) if i % 2 == 0]
print(divisible_by_2)


print("# 2 Ou gen yon lis antye, konvèti l an yon lis chenn ")
     
  
liste_antye = [1, 2, 3, 4, 5]
liste_chenn = list(map(str, liste_antye))
print(liste_chenn)



print("# 3 Ou gen yon lis chenn ki an miniskil, konvèti l an yon lis chenn majiskil ")
     
  
liste_chenn_miniskil = ['bonjou', 'kijan ou ye', 'sa kap fèt']
liste_chenn_majiskil = [mot.upper() for mot in liste_chenn_miniskil]
print(liste_chenn_majiskil)



print("# 4 Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman ")
     
  
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nouvo_liste = [liste[i] for i in range(len(liste)) if i % 3 == 0]
print(nouvo_liste)


print("# 5 Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl ")
     
  
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_liste = [tuple(liste[i:i+3]) for i in range(0, len(liste), 3)]
print(nouvo_liste)


print("# 6 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon ")
     
  
liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
nouvo_liste = list(set(liste))
print(nouvo_liste)


print("# 7 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo ")
     
  
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]
nouvo_liste = list(set(liste1).intersection(liste2))
print(nouvo_liste)


print("# 8 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo ")
     
  
liste1 = [1, 2, 3, 4]
liste2 = [3, 4, 5, 6]
nouvo_liste = list(set(liste1).symmetric_difference(liste2))
print(nouvo_liste)



print("# 9 Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman ")
     
  
diksyone = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
liste_kle = list(diksyone.keys())
liste_valè = list(diksyone.values())
print(liste_kle)
print(liste_valè)



print("#  10 Reyini 3 lis ansanm, san okenn doublon ")
     
  
liste1 = [1, 2, 3]
liste2 = [3, 4, 5]
liste3 = [5, 6, 7]

liste_kombinez = list(set(liste1 + liste2 + liste3))
print(liste_kombinez)




