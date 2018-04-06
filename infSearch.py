
#inicialização de uma matriz correta, com 0 a ser a posição vazia
correctMatrix = [[],[],[]]

for e in range(3):
    for i in range(3):
        correctMatrix[e] += [3 * e + i + 1]
correctMatrix[2][2] = 0

#matriz de teste
incorrectMatrix = [[1, 2, 3], [4, 5, 6], [7, 200, 8]]



#imprime uma matriz 3x3 (não está muito correcta mas não me lembro muito bem de python)
def printMatrix(matrix):
    for e in range(3):
        print(correctMatrix[e][0], correctMatrix[e][1], correctMatrix[e][2])
    print('\n')

#for debbuging purposes
printMatrix(incorrectMatrix)


#devolve o numero de semlehanças entre as matrizes, sendo 9 o máximo (quando as matrizes são iguais)
def compareMatrix(matrix1, matrix2):
    score = 0

    for e in range(3):
        for i in range(3):
            if matrix1[e][i] == matrix2[e][i]:
                score += 1

    return score


#move o espaço vazio para a direita, se possível
def moveRight(matrix):
    for e in range(3):
        for i in range(3):
            if matrix[e][i] == 0:
                if i < 2:
                    matrix[e][i] = matrix[e][i + 1]
                    matrix[e][i + 1] = 0
                return matrix
    return matrix


#move o espaço vazio para a esquerda, se possível
def moveLeft(matrix):
    for e in range(3):
        for i in range(3):
            if matrix[e][i] == 0:
                if i > 0:
                    matrix[e][i] = matrix[e][i - 1]
                    matrix[e][i - 1] = 0
                return matrix
    return matrix


#move o espaço vazio para cima, se possível
def moveUp(matrix):
    for e in range(3):
        for i in range(3):
            if matrix[e][i] == 0:
                if e > 0:
                    matrix[e][i] = matrix[e - 1][i]
                    matrix[e - 1][i] = 0
                return matrix
    return matrix


#move o espaço vazio para baixo, se possível
def moveDown(matrix):
    for e in range(3):
        for i in range(3):
            if matrix[e][i] == 0:
                if e < 2:
                    matrix[e][i] = matrix[e + 1][i]
                    matrix[e + 1][i] = 0
                return matrix
    return matrix



#devolve o index do elemento maior numa lista de 4 elementos
def max4(list):
    maximum = 0
    index = 1
    for e in range(4):
        if maximum < list[e]:
            maximum = list[e]
            index = e
    return index


#funçao que faz a procura informada
def informedSearch(matrix):

    #caso de paragem
    if compareMatrix(matrix, correctMatrix) == 9:
        return matrix

    #os movimentos sao efetuados
    matrix1 = moveUp(matrix)
    matrix2 = moveDown(matrix)
    matrix3 = moveRight(matrix)
    matrix4 = moveLeft(matrix)

    #a semelhança com a matriz final é calculada (mas só é tida em conta se ocorreu um movimento)
    results = []
    if compareMatrix(matrix1, matrix) != 9:
        results += [compareMatrix(matrix1, correctMatrix)]
    else:
        results += [0]
    if compareMatrix(matrix2, matrix) != 9:
        results += [compareMatrix(matrix2, correctMatrix)]
    else:
        results += [0]
    if compareMatrix(matrix3, matrix) != 9:
        results += [compareMatrix(matrix3, correctMatrix)]
    else:
        results += [0]
    if compareMatrix(matrix4, matrix) != 9:
        results += [compareMatrix(matrix4, correctMatrix)]
    else:
        results += [0]


    #determina-se a matriz mais proxima do final
    best = max4(results) + 1

    if best == 1:
        return informedSearch(matrix1)
    elif best == 2:
        return informedSearch(matrix2)
    elif best == 3:
        return informedSearch(matrix3)
    else:
        return informedSearch(matrix4)

#printMatrix(informedSearch(incorrectMatrix))
printMatrix(incorrectMatrix)
