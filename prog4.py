tickets = int(input("Please enter the number of tickets to sell: "))
remaining_tickets = tickets
total_buyers = 0 
while remaining_tickets > 0:
    tickets_purchase = int(input("Please enter the number of tickets to purchase: "))
    if tickets_purchase < 1 or tickets_purchase == 0 or tickets_purchase > 4 or tickets_purchase > remaining_tickets:
        print('I\'m sorry but I can\'t sell you that many.')
    else:
        remaining_tickets = remaining_tickets - tickets_purchase
        print(remaining_tickets, "tickets remaining.")
        total_buyers = total_buyers + 1
        
print("Total buyers:", total_buyers)






