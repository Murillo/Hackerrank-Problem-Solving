# Colleen is turning n years old! Therefore, she has n candles 
# of various heights on her cake, and candle i has height height. 
# Because the taller candles tower over the shorter ones, 
# Colleen can only blow out the tallest candles.

# Given the height for each individual candle, find and print the 
# number of candles she can successfully blow out.

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles

# define funcrion
def birthdayCakeCandles(n, ar):
    max_number = max(ar)
    candles = []
    for i in range(n):
        if max_number == ar[i]:
            candles.append(ar[i])

    return len(candles)

# Get initial values
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)