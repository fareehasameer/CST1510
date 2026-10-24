"""
RECORD CHECK  -  my version
===========================
Name  :  Fareeha M01144857
Lane  :  IT 
Date  :  10 October 2026
===========================
"""

def status_of(percent): 
    '''Returns the status for a percentage, it can be OVER LIMIT, WARNING or OK'''
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    '''Returns the amount of GB free and the percentage used as two separate values'''
    difference=limit-value #this gives the amount of free space left
    percent=(value/limit)*100
    return difference,percent

def print_report(label,value,limit,difference,percent,status): 
    """Prints the report"""
    print()
    print("="*34)
    print(f"  RECORD CHECK  -  {label}")
    print("="*34)
    print(f"  {'Used':<10} : {value:>10.2f}")
    print(f"  {'Total':<10} : {limit:>10.2f}")
    print(f"  {'Free':<10} : {difference:>10.2f}")
    print(f"  {'Percent':<10} : {percent:>10.2f}%")
    print(f"  {'Status':<10} : {status:>10}")
    print("="*34)

over_count = 0 #stores how many records are over the limit

while True: #loop goes on until we break
    label = input("Hostname (or quit): ")
    if label=="quit":
        break
    value=float(input("GB used: "))
    limit=float(input("GB total: "))

    difference, percent = check(value, limit) #puts the returned values into separate variables
    status = status_of(percent)

    if status=="OVER LIMIT":
        over_count+=1

    print_report(label,value,limit,difference,percent,status)

print("Records over limit:",over_count) #this line has to be outside the loop orelse it will print for each and every value
