"""
RECORD CHECK  -  my version
===========================

Name  :  Fareeha M01144857
Lane  :  IT
Date  :  14 November 2026
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """cleans one messy raw line and returns a dict with hostname, used and total"""
    #strip and lower the whole line first so spacing and case dont matter after this
    line=raw_line.strip().lower()
    hostname_part, rest=line.split(",", 1)
    #maxsplit of 1 so only the first comma is split, the hostname comes off and the rest stays together
    fields={}
    for piece in rest.split(","):
        key, value=piece.split("=")
        fields[key.strip()]=float(value.strip())
    return {"hostname":hostname_part.strip(), "used":fields["used"], "total":fields["total"]}

def status_of(used, total, warning_at=90):
    """returns OVER LIMIT, WARNING or OK for a used and total pair"""
    percent=(used/total)*100
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=warning_at:
        return "WARNING"
    else:
        return "OK"

def load_raw_lines(path):
    """reads a file and returns its non-empty lines exactly as they are, still messy"""
    raw_lines=[]
    with open(path) as f:
        for line in f:
            #skipping blank lines so random blanks at the end dont cause a crahs
            if line.strip():
                raw_lines.append(line)
    return raw_lines


# ====================================================================== INPUT

#forward slashes so python doesnt read \L as an escape sequence
#the try/except gives a message and empty list instead of a crash if file is missing
try:
    raw_records=load_raw_lines("Week 07 - Strings and Text Manipulation/LAB/messy_lines.txt")
except FileNotFoundError:
    print("messy_lines.txt was not found")
    raw_records=[]


# ==================================================================== PROCESS
#records holds the lines that parsed and failed_lines holds the ones that didnt
records=[]
failed_lines=[]
flagged_count=0

for raw_record in raw_records:
    try:
        record=parse_line(raw_record)
    except (ValueError, KeyError):
        #ValueError = a value that isnt a number or an extra =, KeyError = a missing field
        failed_lines.append(raw_record.strip())
        continue

    record["percent"]=record["used"]/record["total"]*100
    record["status"]=status_of(record["used"], record["total"])
    records.append(record)

    #anything that isnt OK counts as flagged
    if record["status"]!="OK":
        flagged_count+=1


# ===================================================================== OUTPUT

line=("="*50)

print(line)
print("Server Storage Report")
print(line)
print(f"{'Hostname':<10}{'Used':>8}{'Total':>8}{'Percent':>10}  Status")

for record in records:
    print(f"{record['hostname']:<10}{record['used']:>8.1f}{record['total']:>8.1f}{record['percent']:>9.1f}%  {record['status']}")

print(line)
print()

#only shows if some lines failed to parse
if failed_lines:
    print(line)
    print("Could not parse")
    print(line)
    for bad_line in failed_lines:
        print(bad_line)
    print(line)
    print()

print(line)
print("Summary")
print(line)
print("Records:", len(records))
print("Flagged:", flagged_count)
print("Could not parse:", len(failed_lines))
print(line)


# ==========================================================================
