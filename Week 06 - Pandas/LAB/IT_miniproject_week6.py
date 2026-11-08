"""
RECORD CHECK  -  my version
===========================

Name  :  Fareeha M01144857
Lane  :  IT
Date  :  7 October 2026

"""
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD

#my csv is a list of servers with how much storage each one has used
df=pd.read_csv("Week 06 - Pandas/LAB/servers_data.csv")

# ================================================================= PROCESS

df["percent"]=(df["used_gb"]/df["total_gb"])*100
df["status"]=df["percent"].apply(
    lambda p: "OVER LIMIT" if p>=100 
    else "WARNING" 
    if p>=90 
    else "OK"
)
# ================================================================== OUTPUT

line=("="*50)
 
#the full table, so I can check the percent and status columns
print(line)
print("\t\tServer Storage Report")
print(line)
print(df)
print(line)
print()
print()
 
#only the servers that need attention
#this is a boolean filter
print(line)
print("\t\tServers Needing Attention")
print(line)
print(df[df["status"]!="OK"])
print(line)
print()
print()
 
#how many servers fall into each status
counts=df.groupby("status")["percent"].agg(["count"])
print(line)
print("\t\tCount per Status")
print(line)
print(counts)
print(line)
print("Total servers:", len(df))
print(line)
 
#saving the full table to a new file so the og csv file is kept
#index=False so pandas doesnt add extra column of row numbers
df.to_csv("servers_report.csv", index=False)
 
#bar chart of counts
counts["count"].plot(kind="bar", title="Servers by status")
plt.tight_layout()
 
#saved before show() because show() clears the chart
plt.savefig("status_counts.png")
plt.show()