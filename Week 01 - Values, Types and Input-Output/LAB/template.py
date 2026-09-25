"""
RECORD CHECK  -  my version
===========================

Name  :  Fareeha
Lane  :  IT   
Date  :  25 September 2026

"""

hostname=input("enter hostname:")
gb_used=float(input("enter used gb: "))
gb_total=float(input("enter total gb:"))

difference=gb_total-gb_used
percent=(gb_used/gb_total)*100



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"used gb    : {gb_used:>10.2f}")
print(f"total gb   : {gb_total:>10.2f}")
print(f"difference : {difference:>+10.2f}")
print(f"percent    : {percent:>10.2f} %")
print(f"Each 1%    : {gb_total/100:>10.2f} GB") #this will show how much 1% of storage equates to. it can make the percentage value more understandable.


print("=" * 34)




