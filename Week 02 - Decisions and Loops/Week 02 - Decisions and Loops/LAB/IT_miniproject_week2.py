"""
RECORD CHECK  -  my version
===========================
Name  :  Fareeha Sameer
Lane  :  IT
Date  :  2 October 2026


"""
rec_over_limit=0
while True:
    host=input("Enter hostname:")
    if host=="quit":
        break
    gb_used=float(input("enter used gb:"))
    gb_total=float(input("enter total gb:"))
    
    difference=gb_total-gb_used
    percent=(gb_used/gb_total)*100
    status=""

    if percent>=100:
        status="OVER LIMIT"
        rec_over_limit+=1
    elif percent>=90:
        status="WARNING"
    else:
        status="OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {host}")
    print("=" * 34)

    print(f"Used GB:      {gb_used:>10.2f}")
    print(f"Total GB:     {gb_total:>10.2f}")
    print(f"Remaining GB: {difference:>10.2f}")
    print(f"Usage % :     {percent:>10.2f}")
    print(f"Status:       {status:>10}")

    print("=" * 34)

print(f"Records over limit: {rec_over_limit}")
