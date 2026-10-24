"""
RECORD CHECK  -  my version
===========================

Name  :  Fareeha M01144857
Lane  :  IT
Date  :  18 October 2026
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    '''returns the status for a percentage it can be OVER LIMIT, WARNING or OK'''
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"

def check_record(value,limit):
    '''returns the GB free, the percentage used and the status for one record'''
    difference=limit-value #this gives the amount of free space left
    percent=(value/limit)*100
    status=status_of(percent)
    return difference, percent, status

def print_report(label,value,limit,difference,percent,status):
    """prints the report for one record"""
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


# ====================================================================== STORE

def load_records(path): #parameter for file name
    """reads hostname, gb_used, gb_total lines from a file and returns a list of dicts"""
    records=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            label,value,limit=line.split(",")
            records.append({"label":label,"value":float(value),"limit":float(limit)})
    return records

def write_results(path,results):
    """writes one label n status line per record to a new file"""
    with open(path,"w") as f: #"w" makes the file or overwrites if its already there
        for label,status in results:
            f.write(f"{label},{status}\n")

#for a missing file to give a message and an empty list instead of a crash
try:
    records = load_records("Week 04 - Lists, Dictionaries and Files/LAB/servers.txt") 
    # i had to use the full path here as python wldnt find the file and show "servers.txt was not found"
except FileNotFoundError:                                                                
    print("servers.txt was not found")
    records=[]

# =============================================================== PROCESS + OUTPUT

results=[]
over_count=0 #stores how many records are over the limit

for rec in records:
    difference, percent, status=check_record(rec["value"], rec["limit"])
    print_report(rec["label"], rec["value"], rec["limit"], difference, percent, status)
    results.append((rec["label"], status))

    if status=="OVER LIMIT":
        over_count+=1


print("Records over limit:",over_count)
write_results("Week 04 - Lists, Dictionaries and Files/LAB/results.txt", results)
#i used the entire path again so that result is saved within the week4 folder
