import math
import os
import random
import re
import sys
from datetime import datetime 
from datetime import timedelta  

# Complete the lagDuration function below.
def lagDuration(h1, m1, h2, m2, k):
    start = datetime.strptime("{}:{}".format(h1, m1), "%H:%M")
    lag_end = datetime.strptime("{}:{}".format(h2, m2), "%H:%M")
    real_end = start + timedelta(hours=k)
    return int(abs((real_end - lag_end).seconds / 60))

if __name__ == '__main__':
    fptr = open(os.environ'OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        h1M1H2M2 = input().split()
        h1 = int(h1M1H2M2[0])
        m1 = int(h1M1H2M2[1])
        h2 = int(h1M1H2M2[2])
        m2 = int(h1M1H2M2[3])
        k = int(input())
        result = lagDuration(h1, m1, h2, m2, k)
        print (str(result) + '\n')
        fptr.write(str(result) + '\n')

    fptr.close()