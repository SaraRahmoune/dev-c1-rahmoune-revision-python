def calculatrice(chaine_oper):
    
    chaine_oper = chaine_oper.replace('x', '*')

  
    try:
        resultat = eval(chaine_oper)
        return resultat
    except:
        return "Erreur d'évaluation"


chaine_oper = input("Entrez une chaîne d'opérations : ")


resultat = calculatrice(chaine_oper)


print("Résultat :", resultat)