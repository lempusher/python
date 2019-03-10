employees = []
while True:
    try:
        fname, lname = input("enter full name: ").split()
        employees.append({"fname": fname, "lname": lname})
    except ValueError:
        print("enter FIRST and LAST name!")
    else: break
print(employees)