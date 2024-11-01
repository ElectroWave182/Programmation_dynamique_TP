def decoupage (n):

    sol = [0, 0]
    for longueur in range (2, n + 1):
        sol.append (longueur + sol[-1])

        for coupe in range (2, longueur // 2 + 1):

            valeur = longueur + sol[coupe] + sol[longueur - coupe]
            if valeur < sol[longueur]:
                sol[longueur] = valeur

    return sol[-1]

assert decoupage (100) == 672
assert decoupage (5) == 12
assert decoupage (4) == 8