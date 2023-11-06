def retounen_envès(mot):
    return mot[::-1]

import random
import string

def kòd_aleyatwa(n):
    return ''.join(random.choices(string.ascii_letters, k=n))
 
def kòd_aleyatwa_san_repetisyon(n):
    return ''.join(random.sample(string.ascii_letters, k=n))


 
def kòd_alfanimerik(n):
    karaktè = string.ascii_letters + string.digits
    return ''.join(random.sample(karaktè, k=n))


 
def kreye_slug(chenn):
    slug = ''.join(e if e.isalnum() else '-' for e in chenn)
    return slug

 
def separe_avek_vigil(mot):
    return '-'.join(mot)

 
def kripte_avek_endèks(mot):
    kripte = '-'.join(str(ord(c.lower()) - 97) for c in mot if c.isalpha())
    return kripte

 
def dekripte_avek_endèks(mot):
    dekripte = ''.join(chr(int(c) + 97) for c in mot.split('-'))
    return dekripte


 
def retounen_tuple(valè1, valè2):
    return valè1, valè2


 
def retounen_inisyal(non):
    inisyal = ''.join(word[0].upper() for word in non.split('-'))
    return inisyal