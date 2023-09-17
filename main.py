# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
Age_90_months = 12*90

Age_90_weeks = 52*90

Age_90_days = 365*90

current_months = 12*age_int

current_weeks = 52*age_int

current_days = 365*age_int

left_months= Age_90_months - current_months

left_weeks = Age_90_weeks - current_weeks

left_days = Age_90_days - current_days

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left")



