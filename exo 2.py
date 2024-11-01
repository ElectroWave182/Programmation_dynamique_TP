def parenthesage (n):

    sol = [0, 1]

    for longueur in range (2, n + 1):
        maxi = 1 + sol[-1]
        
        for coupe in range (2, longueur // 2 + 1):
            somme = sol[coupe] + sol[longueur - coupe]
            produit = sol[coupe] * sol[longueur - coupe]

            if somme > maxi:
                maxi = somme

            if produit > maxi:
                maxi = produit

        sol.append (maxi)

    return sol[-1]


for nb in range (5, 16):
    print (parenthesage (nb))