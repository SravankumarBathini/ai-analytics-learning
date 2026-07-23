# ==========================================
# Lesson 6: Loops
# Repository: AI Analytics Learning
# ==========================================

employees = ["Alice", "Bob", "Charlie", "Shravan"]

for employee in employees:
    print(employee)

# ==========================================
# Example
# ==========================================

salaries = [50000, 80000, 120000, 95000]
for salary in salaries:
    if salary >= 100000:
        print("High salary")
    elif salary >= 80000:
        print("Medium salary")
    else:
        print("Low salary")



##########Range function
for i in range(2,5):
    print(i)

# ==========================================
# Exercise
# ==========================================
sales = [25000, 48000, 12000, 95000, 67000]

for sale in sales:
    if sale >= 50000:
        print(f"{sale} -> target Achieved")
    else:
        print(f"{sale} -> target Not Achieved")