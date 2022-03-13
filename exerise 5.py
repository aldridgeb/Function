def check_factor(big_num, small_num):
    return big_num % small_num == 0


# main routine
big = int(input("enter the bigger number: "))
small = int(input("enter the smaller number: "))
if check_factor(big, small):
    print(f"{small} is a factor {big}")
else:
    print(f"{small} is NOT a factor if {big}")

