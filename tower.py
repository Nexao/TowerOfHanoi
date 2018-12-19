
#-------
#Simple version of tower of hanoi
#-------

def hanoi(n, P1, P2, P3):
    """ Move n discs from pole P1 to pole P3. """
    if n == 0:
        # No more discs to move in this step
        return

    global moves
    moves += 1

    # move n-1 discs from P1 to P2
    hanoi(n-1, P1, P3, P2)

    if P1:
        # move disc from P1 to P3
        P3.append(P1.pop())
        print(A, B, C)

    # move n-1 discs from P2 to P3
    hanoi(n-1, P2, P1, P3)

# Creates the poles and sets all the disks on pole A

# Changing the variable of N, will increase / decrease the amount of disks
n = 3
A = list(range(n,0,-1))
B, C = [], []

print(A, B, C)
moves = 0
hanoi(n, A, B, C)
# Prints the moves made to finish the tower
print(moves)