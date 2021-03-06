
def bishops_can_attack(bishops, size):
    """
    On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
    You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
    For example: M=5 and points: (0, 0), (1, 2) ,(2, 2) ,(4, 0). You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
    """

    # matches = dict()
    matches = [ [] for i in range(len(bishops))]

    cont = 0
    while cont < len(bishops):
        pos = 0
        current = bishops[cont]
        while pos < len(bishops):
            compare = bishops[pos]
            if cont != pos:
                if abs(current[0] - compare[0]) == abs(current[1] - compare[1]):
                    if cont not in matches[pos]:
                        matches[pos].append(cont)
                        matches[cont].append(pos)
            pos += 1
        cont += 1
    sum = 0
    for item in matches:
        sum += len(item)
    

    return int(sum/2)

def largest_three_product(array):
    """
    Given a list of integers, return the largest product that can be made by multiplying any three integers.
    """

    if len(array) < 3:
        return None
    
    array.sort()
    less = 0
    up = len(array) - 1
    cont = 0
    values = []
    acumulado = 1
    while cont < 3:
        if abs(array[less] * acumulado) > abs(array[up] * acumulado):
            values.append(array[less])
            acumulado *= array[less]
            less += 1
        else:
            values.append(array[up])
            acumulado *= array[up]
            up -= 1
        cont += 1

    return values


def main():
    # print(bishops_can_attack([(0, 0), (1, 2) ,(2, 2) ,(4, 0)], 5))
    print(largest_three_product([-10, -10, 5, 2]))

if __name__ == "__main__":
    main()
