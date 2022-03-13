def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_tickets = 0
    tickets_sold = 0

    tickets_wanted = input("do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()

        num_tickets= int(input("how any of these tickets do you want: "))
        confirm = input(f"confirm purchace of {num_tickets} type {ticket} "
                        f)"tickets(s)? ("Y") "),upper()
        if confirm == "Y":
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
    
