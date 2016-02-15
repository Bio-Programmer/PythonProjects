def isLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

def nextLeap(year):
    total = year + 1
    while(isLeap(total)==False):
        total = total + 1
    return(total)

print (isLeap(2016))
print (nextLeap(2016))
