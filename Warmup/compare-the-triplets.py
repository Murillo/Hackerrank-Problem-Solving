# Compare the Triplets
# Developer: Murillo Grubler

def solve(a0, a1, a2, b0, b1, b2):
    player_a = 0
    player_b = 0

    if a0 > b0:
        player_a += 1
    elif a0 < b0:
        player_b += 1

    if a1 > b1:
        player_a += 1
    elif a1 < b1:
        player_b += 1

    if a2 > b2:
        player_a += 1
    elif a2 < b2:
        player_b += 1

    return [player_a, player_b]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))