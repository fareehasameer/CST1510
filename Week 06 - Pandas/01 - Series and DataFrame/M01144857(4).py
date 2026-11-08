import pandas as pd
import matplotlib.pyplot as plt


fitness=pd.DataFrame({
    "member_name": ["Fareeha", "Ben", "Chloe", "Tanuri", "Emma", "Farid", "Sarah"],
    "workout_type": ["Cardio", "Strength", "Yoga", "Cardio", "Strength", "Cardio", "Yoga"],
    "calories_burned": [900, 600, 240, 1600, 850, 480, 270],
    "heart_rate": [165, 130, 95, 175, 145, 140, 100],
    "duration_mins": [45, 40, 60, 80, 50, 30, 45],
})

fitness["burn_rate_per_min"]=fitness["calories_burned"]/fitness["duration_mins"]

print("="*30)
print("\nBurn rate per member:")
print(fitness[["member_name","burn_rate_per_min"]])
print()
print("="*30)

print("\nFirst row only:")
print(fitness.iloc[0])
print("\nCalories burned by the member at row label 3 (using loc):")
print(fitness.loc[3, "calories_burned"])
print()
print("="*30)

print("\nWorkouts that are over 45 minutes:")
print(fitness[fitness["duration_mins"]>=45])
print()
print("="*30)

print("\nCardio and Heart rate over 150:")
print(fitness[(fitness["workout_type"]=="Cardio")&(fitness["heart_rate"]>150)])
print()
print("="*30)

print("\nSummary grouped by Workout Type:")
stats=fitness.groupby("workout_type").agg(
    avg_calories=("calories_burned", "mean"),
    max_duration=("duration_mins", "max"),)
print(stats)
print()
print("="*30)

fitness=fitness.sort_values("calories_burned", ascending=False) #sorted by calroeis burnt

fitness["tier"] = fitness["calories_burned"].apply(
    lambda c: "elite" if c >= 1500
    else "advanced" if c >= 800
    else "beginner"
)
print("\nSorted with tiers:")
print(fitness)
print()
print("="*30)

print("\nMembers per tier:")
print(fitness["tier"].value_counts())
print()
print("="*30)

fitness.to_csv("gym_report.csv", index=False)
print("\nData saved to gym_report.csv")
print()
print("="*30)

(fitness["member_name"],fitness["heart_rate"]).plot(kind="bar", title="heart_rate",)
plt.tight_layout()
plt.show()