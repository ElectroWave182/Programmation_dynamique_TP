def rendu (n):

    sol = [0, 1, 2, 1]
    for longueur in range (4, n + 1):
        mini = 1 + sol[longueur - 1]
        piece_3 = 1 + sol[longueur - 3]
        piece_4 = 1 + sol[longueur - 4]

        if piece_3 < mini:
            mini = piece_3

        if piece_4 < mini:
            mini = piece_4

        sol.append (mini)

    return sol[-1]


print (rendu (5))