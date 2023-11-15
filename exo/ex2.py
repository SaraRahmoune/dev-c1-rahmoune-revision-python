phrase_user = input("Entrez une phrase : ")


phrase_majuscules = phrase_user.upper()
print("Phrase en majuscules :", phrase_majuscules)


phrase_minuscules = phrase_user.lower()
print("Phrase en minuscules :", phrase_minuscules)

# Comptez le nombre de mots dans la phrase
nombre_de_mots = len(phrase_user.split())
print("Nombre de mots dans la phrase :", nombre_de_mots)