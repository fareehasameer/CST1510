"""
RECORD CHECK  -  my version
===========================

Name  : Fareeha Sameer M01144857
Lane  : IT  
Date  : 24 October 2026

"""

# ====================================================================== CLASS
class Record:
    def __init__(self, label, value, limit):
        # label is the hostname, value is gb used, limit is gb total
        self.label=label
        self.value=value
        self.limit=limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on how full the disk is"""
        percent=self.value/self.limit*100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Read label, value and limit lines from a file to return a list of records"""
    records=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            # skipping empty lines so random blanks at the end dont mess with the code
            if line:
                label, value, limit=line.split(",")
                # file gives strings, so value and limit need float() before any calculation can happen
                records.append(Record(label, float(value), float(limit)))
    return records

records=load_records(r"C:\Users\creep\Documents\CST1510\Week 05 - Classes and Objects\LAB\servers.txt")


# ==================================================================== OUTPUT

over_limit_count=0

for record in records:
    status=record.status()
    if status=="OVER LIMIT":
        over_limit_count+=1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Hostname : {record.label}")
    print(f"  GB used  : {record.value}")
    print(f"  GB total : {record.limit}")
    print(f"  Status   : {status}")
    print("=" * 34)

print()
print(f"{over_limit_count} of {len(records)} servers are OVER LIMIT")

# ==========================================================================
