# The Time in Words
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/the-time-in-words
# Time Complexity = O(1)

desc_hour = {
    1:"one", 
    2:"two", 
    3:"three", 
    4:"four", 
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
}

desc_minute = {
    1:"one minute", 
    2:"two minutes", 
    3:"three minutes", 
    4:"four minutes", 
    5:"five minutes",
    6:"six minutes",
    7:"seven minutes",
    8:"eight minutes",
    9:"nine minutes",
    10:"ten minutes",
    11:"eleven minutes",
    12:"twelve minutes",
    13:"thirteen minutes",
    14:"fourteen minutes",
    15:"fifteen minutes",
    16:"sixteen minutes",
    17:"seventeen minutes",
    18:"eighteen minutes",
    19:"nineteen minutes",
    20:"twenty minutes",
    21:"twenty one minutes",
    22:"twenty two minutes",
    23:"twenty three minutes",
    24:"twenty four minutes",
    25:"twenty five minutes",
    26:"twenty six minutes",
    27:"twenty seven minutes",
    28:"twenty eight minutes",
    29:"twenty nine minutes",
}

quarters = {
    0:"o' clock",
    15:"quarter",
    30:"half",
    45:"quarter"
}

def time_in_words(h, m):
    hour_in_min = 60
    if m == 0:
        desc = "{} {}".format(desc_hour[h], quarters[m])
    elif (m > 0 and m < 15) or (m > 15 and m < 30):
        desc = "{} past {}".format(desc_minute[m], desc_hour[h])
    elif m == 15:
        desc = "{} past {}".format(quarters[m], desc_hour[h])
    elif m == 30:
        desc = "{} past {}".format(quarters[m], desc_hour[h])
    elif (m > 30 and m < 45) or (m > 45 and m < 60):
        desc = "{} to {}".format(desc_minute[hour_in_min - m], desc_hour[h + 1])
    elif m == 45:
        desc = "{} to {}".format(quarters[m], desc_hour[h + 1])
    return desc

h = int(input().strip())
m = int(input().strip())
print (time_in_words(h, m))