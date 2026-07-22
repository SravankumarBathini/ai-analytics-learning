salary = 2000000
bonus_percent = 15

bonus = salary * (bonus_percent / 100)

print(f"bonus: {bonus:.2f}")


a = [1, 2]
b = [1, 2]
c = a

print(a == b)
print(a is b)

print(a == c)
print(a is c)


experience = 11
rating = 4.6
skills = ["Python", "SQL", "Power BI", "Git"]

# Print:
# Eligible for Promotion: True/False
# Knows Python: True/False
# Rating >= 4.5: True/False

if experience >= 5 and rating >= 4.5 and "Python" in skills:
    print("Eligible for Promotion: True")
else:
    print("Eligible for Promotion: False")

