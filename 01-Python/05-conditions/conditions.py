# ==========================================
# Lesson 5: Conditions
# Repository: AI Analytics Learning
# ==========================================

credit_score = 780
annual_income = 1200000

if credit_score >= 750:
    print("Good credit score")

    monthly_spend = 18000

if monthly_spend >= 50000:
    segment = "Platinum"

elif monthly_spend >= 20000:
    segment = "Gold"

elif monthly_spend >= 10000:
    segment = "Silver"

else:
    segment = "Regular"

print(segment)


#############Exercise
experience = 11
rating = 4.6
certified = True

if experience >= 5 and rating >= 4.5 and certified:
    print("Promotion eligible")
else :
    print("Promotion not eligible")