def clac_fines(days_overdue):
   fine = .5 + (days_overdue * .8)
   if fine > 30:
       fine = 30
   return fine

days_overdue_ = int(input("enter days overdue: "))
print(f"for {days_overdue_} the fine is ${clac_fines()}")






