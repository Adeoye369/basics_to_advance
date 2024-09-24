
h = float(input("height(m): "))
w = float(input("weight(kg): "))


if h > 4.0:
    raise ValueError("Human height should not exceed 4 meters")
elif w > 1000:
    raise ValueError("Human weight should not excceed 1000 kg")
else:
    bmi = w / h **2
    print(f"Your bmi is {bmi}")
