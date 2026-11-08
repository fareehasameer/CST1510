
import pandas as pd

data = {
    "hostname": ["srv-alpha", "srv-beta", "srv-gamma", "srv-delta", "srv-epsilon"],
    "region": ["east", "west", "east", "north", "west"],
    "failed_logins": ["12", "3", "45", "0", "8"],
    "total_attempts": [50, 100, 200, 50, 80],
}
logs = pd.DataFrame(data)
print("="*30)
print("\nData types BEFORE:")
print(logs.dtypes)
logs["failed_logins"]=logs["failed_logins"].astype(int)
print()
print("="*30)
print("\nData types AFTER:")
print(logs.dtypes)
print()
print("="*30)



logs["failure_rate"]=(logs["failed_logins"]/logs["total_attempts"])*100

print("\nHostname and failure rate:")
print(logs[["hostname", "failure_rate"]])
print()
print("="*30)


high_risk=logs[logs["failure_rate"]>=15]
print("\nHigh-risk servers (>= 15%):")
print(high_risk)
print()
print("="*30)

high_risk.to_csv("high_risk_servers.csv")
print("\nSaved high_risk_servers.csv")
print()
print("="*30)

