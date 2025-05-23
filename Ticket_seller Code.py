#Function to ask user how many tickets they want to get
def ask_for_tickets(remaining):
    while True:
        try:
            tickets = int(input("How many tickets do you want to buy? (1 to 4): "))
            if tickets < 1 or tickets > 4:
                print("You can only buy between 1 and 4 tickets.")
            elif tickets > remaining:
                print("Not enough tickets left. Please choose fewer.")
            else:
                return tickets
        except ValueError:
            print("That’s not a number. Please enter a number between 1 and 4.")

#sell tickets
def sell_tickets():
    total_tickets = 20          #Maximum tickets
    tickets_sold = 0            #tickets sold
    total_buyers = 0            #number of buyers

    while tickets_sold < total_tickets:  #Loop until all tickets are gone
        print(f"\nTickets left: {total_tickets - tickets_sold}")
        tickets = ask_for_tickets(total_tickets - tickets_sold)  #usr input
        tickets_sold += tickets    #Update total
        total_buyers += 1          #Count buyer
        print(f"You bought {tickets} ticket(s).")

    print("\nAll tickets are sold out!")
    print(f"Total number of buyers: {total_buyers}")

#display
sell_tickets()
