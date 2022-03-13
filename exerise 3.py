def check_status(number):
    if number < 18.5:
        print("underweight")
    elif number < 25:
        print ("normal")
    elif number < 30:
        print ("overweight")
    else:
        print ("obese")

check_status(19)

