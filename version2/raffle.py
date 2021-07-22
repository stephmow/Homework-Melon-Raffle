"""Randomly pick customer and print customer info"""

import random

# the initial creator of this file created a separate file to get customers info - import this function
from customers import get_customers_from_file

# new function to pick the winner from customer info file  
def pick_winner(customers): 
    """ Choose a random winner from list of customers. """

    # need to use random.choice since we used 'import random' 
    chosen_customer = random.choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won!")

def run_raffle():
    """ Run the weekly raffle. """

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

# runs as a script.  *double check what this means...*
if __name__ == "__main__": 
    run_raffle()
