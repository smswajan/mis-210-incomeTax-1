#A python program for Calculating Income Tax

print("Tax Payer categories are:")
print("-------------------------")
print("1: Single")
print("2: Married Filing Jointly")
print("3: Married Filing Separately")
print("4: Head of the household")

category = eval(input("Please specify your category as a tax-payer: "))

income = eval(input("Please enter your income amount: "))

#Tax Calculation for Single
if(category == 1):
    a = 8350
    b = 33950
    c = 82250
    d = 171550
    e = 372950
    if income <=a:
        tax = income * .1
    elif income <= b:
        tax = a * .1 + (income - a) *.15
    elif income <= c:
        tax = a * .1 + (b-a)*.15 + (income-b)*.25
    elif income <= d:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (income - c)*.28
    elif income <= e:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (income -d)*.33
    else:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (e-d)*.33 + (income - e)*.35

#Tax Calculation for Married Filing Jointly       
elif category == 2 :
    a = 16700
    b = 67900
    c = 137050
    d = 208850
    e = 372950
    if income <=a:
        tax = income * .1
    elif income <= b:
        tax = a * .1 + (income - a) *.15
    elif income <= c:
        tax = a * .1 + (b-a)*.15 + (income-b)*.25
    elif income <= d:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (income - c)*.28
    elif income <= e:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (income -d)*.33
    else:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (e-d)*.33 + (income - e)*.35

#Tax Calculation for Married Filing Separately
elif category == 3 :
    a = 8350
    b = 33950
    c = 68525
    d = 104425
    e = 186475
    if income <=a:
        tax = income * .1
    elif income <= b:
        tax = a * .1 + (income - a) *.15
    elif income <= c:
        tax = a * .1 + (b-a)*.15 + (income-b)*.25
    elif income <= d:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (income - c)*.28
    elif income <= e:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (income -d)*.33
    else:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (e-d)*.33 + (income - e)*.35

# Tax Calculation for Head of Household     
elif category == 4 :
    a = 11950
    b = 45500
    c = 117450
    d = 190200
    e = 372950
    if income <=a:
        tax = income * .1
    elif income <= b:
        tax = a * .1 + (income - a) *.15
    elif income <= c:
        tax = a * .1 + (b-a)*.15 + (income-b)*.25
    elif income <= d:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (income - c)*.28
    elif income <= e:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (income -d)*.33
    else:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (e-d)*.33 + (income - e)*.35
        
print("Your tax amount is: ", tax)
