import pandas

data = pandas.read_csv("insurance.csv")

# All variables before editing

age = data["age"]
region = data["region"]
sex = data["sex"]
Children = data["children"]
bml = data["bmi"]
smoker = data["smoker"]
charges = data["charges"]

total_70 = 0
total_60 = 0
total_50 = 0
total_40 = 0
total_30 = 0
total_20 = 0


# Functions

def get_average(rows, charges):
    return charges / rows
    



for i in age:
    if i <= 20 :
        total_20 += 1
    elif i <= 30:
        total_30 += 1
    elif i <= 40:
        total_40 += 1
    elif i <= 50:
        total_50 += 1
    elif i <= 60:
        total_60 += 1
    elif i <= 64:
        total_70 += 1
        
#print(f'Total under 70: {total_70},Total under 60: {total_60},Total under 50: {total_50},Total under 40: {total_40}, Total under 30: {total_30}, Total under 20: {total_20}')


# 20's and under age group calculations, I know I can do it in the last for loop I just like to keep stuff organized this way
total_charges_under_20 = 0
for i in range(len(age)):
    if age[i] <= 20:
        total_charges_under_20 += charges[i]
    else:
        pass
print(total_charges_under_20)


# 30's and under
total_charges_under_30 = 0
for i in range(len(age)):
    if age[i] <= 30:
        total_charges_under_30 += charges[i]
    else:
        pass
print(total_charges_under_30)


# 40's and under
total_charges_under_40 = 0
for i in range(len(age)):
    if age[i] <= 40:
        total_charges_under_40 += charges[i]
    else:
        pass
print(total_charges_under_40)

# 50's and under
total_charges_under_50 = 0
for i in range(len(age)):
    if age[i] <= 50:
        total_charges_under_50 += charges[i]
    else:
        pass
print(total_charges_under_50)

# 60's and under
total_charges_under_60 = 0
for i in range(len(age)):
    if age[i] <= 20:
        total_charges_under_60 += charges[i]
    else:
        pass
print(total_charges_under_60)

# 70's and under
total_charges_under_70 = 0
for i in range(len(age)):
    if age[i] <= 70:
        total_charges_under_70 += charges[i]
    else:
        pass
print(total_charges_under_70)

under_20_average_charges = get_average(total_20, total_charges_under_20)
print(f"20's {under_20_average_charges}")
under_30_average_charges = get_average(total_30, total_charges_under_30)
print(f"30's {under_30_average_charges}")
under_40_average_charges = get_average(total_40, total_charges_under_40)
print(f"40's {under_40_average_charges}")
under_50_average_charges = get_average(total_50, total_charges_under_50)
print(f"50's {under_50_average_charges}")
under_60_average_charges = get_average(total_60, total_charges_under_60)
print(f"60's {under_60_average_charges}")
under_70_average_charges = get_average(total_70, total_charges_under_70)
print(f"70's {under_70_average_charges}")