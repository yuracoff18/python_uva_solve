"""

    28/03/2024
    Yura Hernandez
    Uva - 10409

"""

#   North, South, East, West
#   Cara = [0][2]
#   [0][x] = Acceso vertical
#   [1][y] = Acceso horizontal


#          0         1
#      Vertical  Horizontal

def comando_cambio(die: list, comando):
    if comando == 'North':
        current = die[0][3]
        die[0].pop(3)
        die[0].insert(0,current)
        die[1][0] = die[0][0]
        die[1][2] = die[0][2]
    elif comando == 'South':
        current = die[0][0]
        die[0].pop(0)
        die[0].append(current)
        die[1][0] = die[0][0]
        die[1][2] = die[0][2]
    elif comando == 'East':
        current = die[1][0]
        die[1].pop(0)
        die[1].append(current)
        die[0][0] = die[1][0]
        die[0][2] = die[1][2]
    elif comando == 'West':
        current = die[1][3]
        die[1].pop(3)
        die[1].insert(0,current)
        die[0][0] = die[1][0]
        die[0][2] = die[1][2]
    else:
        print("Command not found.")
        
continuar = True

while continuar:
    die = [[6,5,1,2],[6,4,1,3]]
    n = int(input())
    n = abs(n)
    
    if n == 0:
        continuar = False
        break
    else:
        for i in range(n):
            com = input()
            comando_cambio(die, com)
        print(die[0][2])