age = int(input('Passenger age '))
passport = str.lower(input('Do you have passport? y/n '))
if passport == 'n':
    print("You can't embark")
elif age >= 18 and passport == 'y':
    print('Boarding successfully ')
if age < 18 and passport == 'y':
    accomp_mother = str(input('Accompanied by mother? y/n '))
    accomp_father = str(input('Accompanied by father? y/n '))
    if accomp_mother == 'y' and accomp_father == 'y':
        print('Boarding successfully ')
    elif accomp_mother == 'n' and accomp_father == 'n':
        print('goodbye')
    else:
        if accomp_father == 'y':
            mother_deed = str(input("Mother's deed y/n "))
            if mother_deed == 'y':
                print('Boarding successfully ')
        elif accomp_mother == "y":
            father_deed = str(input("Father's deed y/n "))
            if father_deed == 'y':
                print('Boarding successfully ')
            else:
                print("You can't embark")