# Jim and the Orders
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/jim-and-the-orders/problem

# Time complexity: O(n log n)
def jimOrders(orders):
    total = {}
    for i in range(len(orders)):
        total[i + 1] = sum(orders[i])
    return [item[0] for item in sorted(total.items(), key=lambda x: x[1])]

orders = []
for orders_i in range(int(input().strip())):
    orders.append([int(orders_temp) for orders_temp in input().strip().split(' ')])
print (" ".join(map(str, jimOrders(orders))))