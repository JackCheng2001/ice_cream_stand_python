"""
STARTER CODE
Homework 3: Ice Cream Stand
Topics Covered:
- Lists (append, pop)
- For and while loops
- Getting user inputs
- Validating user inputs
- Functions and helper functions
- Formatted Strings
"""

# TODO: Students, fill out statement of work header
# Student Name in Canvas: Cheng Erxi
# Penn ID: 62196105
# Did you do this homework on your own (yes / no): Yes
# Resources used outside course materials: None

# import statements
from random import randint, choice


def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    """
    Prints the following:
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """
    # TODO: Write your code here
    print("Welcome to our ice cream stand!\n")
    print("Our current flavors for today are:")
    for value_flavors in list_of_flavors:
        print(value_flavors)
    for size,price in zip(list_of_sizes,list_of_prices):
        print("Our {} size ice cream is {}".format(size,round(price,2)))



def get_order_qty(customer_name):
    """
    Ask the customer how many orders of ice cream they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
    "2.55", "abc", "   ", are a few examples of what should all re-prompt the user.
    Returns: How many orders of ice cream the customer wants.
    """
    order_qty = 0
    # TODO: Write your code here
    while True:
        try:
            order_qty_str = input("Welcome {}! How many ice creams will you be ordering (1 to 5)?: ".format(customer_name))
            if(order_qty_str==''):
                print("Please enter a valid integer.") 
            order_qty = int(order_qty_str)  # Try casting the input to an integer
            if 1 <= order_qty <= 5:  # Check if the integer is within the desired range
                break  # If valid, exit the loop
            else:
                continue
        except ValueError:  # Handle the exception when the input can't be casted to an integer
            continue

    return order_qty


def get_ice_cream_flavor(ice_cream_flavors):
    """
    Ask the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.
    Hint:   Use the indices set in the main function for the flavors.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Cookies and Cream'
            will be considered as 'c' which corresponds to 'Chocolate'.
            Ask again if it is not a valid flavor.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """
    flavor_picked = ""
    # TODO: Write your code here
    # This code prompts the user to select a flavor by entering its corresponding initial.
    # It keeps looping until the user enters a valid choice.
    # The valid choices are:
    # 'v' for Vanilla
    # 'c' for Chocolate
    # 's' for Strawberry
    # The function will return the initial of the chosen flavor.
    temp=ice_cream_flavors
    while True:
        
        if(get_first_letter_of_user_input(temp)=='v'):
            flavor_picked='v'
            break
        elif(get_first_letter_of_user_input(temp)=='c'):
            flavor_picked='c'
            break
        elif(get_first_letter_of_user_input(temp)=='s'):
            flavor_picked='s'
            break
        else:
            temp=input("Which flavor would you like (v/c/s)?")
            continue
    return flavor_picked


def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Hint:   Use the indices set in the main function for the sizes.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Super Large'
            will be considered as 's' which corresponds to 'Small'.
            Ask again if it is not a valid size.
    Returns: String of Size picked (e.g "Small")
    """
    size_picked = ""
    # TODO: Write your code here
    # This code prompts the user to select a size by entering its corresponding initial.
    # It keeps looping until the user enters a valid choice.
    # The valid choices are:
    # 's' for Small
    # 'm' for Medium
    # 'l' for Large
    # The function will return the initial of the chosen size.
    temp=ice_cream_sizes
    while True:
        if(get_first_letter_of_user_input(temp)=='s'):
            size_picked='s'
            break
        elif(get_first_letter_of_user_input(temp)=='m'):
            size_picked='m'
            break
        elif(get_first_letter_of_user_input(temp)=='l'):
            size_picked='l'
            break
        else:
            temp=input("Which size would you like (s/m/l)?")
            continue
    return size_picked


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Hint:   Use the indices set in the main function for the prices of Small, Medium and Large.
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    """
    # TODO: Write your code here
    # This code looks for the price of the chosen ice cream size from the `ice_cream_sizes` and `ice_cream_prices` lists.
    # The user's choice of size is stored in the `ice_cream_size` variable.
    # The code iterates over the two lists in tandem using the `zip` function.
    # When it finds a match between the user's choice and an item in the `ice_cream_sizes` list, 
    # it assigns the corresponding price from the `ice_cream_prices` list to the `price` variable and rounds it to 2 decimal places.
    # After finding a match, the loop is broken using the `breaker` flag.
    # The function then returns the `price` of the selected ice cream size.
    breaker=0
    while True:
        for i,j in zip(ice_cream_sizes,ice_cream_prices):
            if ice_cream_size == 'Small' and i=='Small':
                price = round(float(j),2)
                ice_cream_size=i
                breaker=1
                break
            if ice_cream_size == 'Medium' and i=='Medium':
                price = round(float(j),2)
                ice_cream_size=i
                breaker=1
                break
            if ice_cream_size == 'Large' and i=='Large':
                price = round(float(j),2)
                ice_cream_size=i
                breaker=1
                break
        if(breaker==1):
            break
    return price


def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Hint: Use other helper functions we required you to write whenever needed here.
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0
    price=0
    # TODO: Print a message "Now serving customer: X" where X is the current customer's name
    print("\nNow serving customer: {}".format(customer_name))
    # TODO: Call the get_order_qty and save the value to order_qty
    order_qty = 0
    order_qty = get_order_qty(customer_name)
    # TODO: For Each order you need to get a flavor, and size
    for order in range(order_qty):
        price=0
        print("Order No.:", order + 1)
        # TODO: Write code to get the ice cream flavor for this order
        flavor=input("Which flavor would you like (v/c/s)?")
    # This code block prompts the user to select an ice cream flavor by its initial letter.
    # It repeatedly asks for the user's input until a valid flavor initial is provided.
    # The valid initials and their corresponding flavors are:
    # 'v' for Vanilla
    # 'c' for Chocolate
    # 's' for Strawberry
    # Once a valid initial is chosen, the full name of the flavor is assigned to the variable `flavor`.
    # If the user enters an invalid choice, or if there's a ValueError (likely due to invalid input handling in the `get_first_letter_of_user_input` function),
    # the loop will prompt the user again.
        while True:
            try:
                res_flavor=get_first_letter_of_user_input(flavor)
                if(res_flavor=='v'):
                    flavor='Vanilla'
                    break
                elif(res_flavor=='c'):
                    flavor='Chocolate'
                    break
                elif(res_flavor=='s'):
                    flavor='Strawberry'
                    break
                flavor=input("Which flavor would you like (v/c/s)?")
            except ValueError:
                continue


                
        # TODO: Write code to get the ice cream size for this order
        # The user is initially prompted to select an ice cream size by entering its corresponding initial (s/m/l).
        # Inside a loop, the user's input is processed using the `get_first_letter_of_user_input` function which likely returns the first letter of the input or raises a ValueError if the input is invalid.
        # If the returned value matches:
        # 's' -> the ice cream size is set to 'Small'
        # 'm' -> the ice cream size is set to 'Medium'
        # 'l' -> the ice cream size is set to 'Large'
        # If a valid size is chosen, the loop exits. 
        # If the size doesn't match any of the provided options or if a ValueError occurs (indicative of an invalid input), 
        # the user is prompted again to enter their choice.
        size=input("Which size would you like (s/m/l)?")
        while True:
            try:
                res_size=get_first_letter_of_user_input(size)
                if(res_size=='s'):
                    size='Small'
                    break
                elif(res_size=='m'):
                    size='Medium'
                    break
                elif(res_size=='l'):
                    size='Large'
                    break
                size=input("Which size would you like (s/m/l)?")
            except ValueError:
                continue

        # TODO: Write code to get the price for this order
        price=get_ice_cream_order_price(size, ice_cream_prices, ice_cream_sizes)
        # TODO: Update the total_bill
        total_bill+=price
        # TODO: Print the details for this order
        #   Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
        print("You ordered a {} {} for ${}".format(size,flavor,price))
        # TODO: Remove the pass statement once you have your code written

    # TODO: Print the customer's total_bill
    print("Your total bill is: ${}".format(total_bill))
    # TODO: Once orders are all taken, the customer should be asked if they still want to Pay or Cancel
    #  "Would you like to pay or cancel the order (p/c)? "
    #   Hint: Use the get_first_letter_of_user_input() Re-prompt if answer does not start with 'p' or 'c'
    # The user is initially prompted to decide whether they want to proceed with payment or cancel the order by entering 'p' for pay or 'c' for cancel.
    # Inside the loop, the `get_first_letter_of_user_input` function is used to extract the first letter of the user's response.
    # If the extracted letter is:
    # 'p' -> the loop breaks, and the function will return the current `total_bill`.
    # 'c' -> the order is considered canceled, setting the `total_bill` to 0, then the loop breaks.
    # If the user's input doesn't match 'p' or 'c', they are prompted again to enter their decision.
    str_temp=input("Would you like to pay or cancel the order (p/c)?")
    while True:
        
        res=get_first_letter_of_user_input(str_temp)
        if(res=='p'):
            break
        elif(res=='c'):
            total_bill=0
            break
        else:
            str_temp=input("Would you like to pay or cancel the order (p/c)?")
            continue
    return total_bill



def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """

    first_letter = ""
    # TODO: Write your code here
    # This function takes a string input `question`.
    # If the input is an empty string, it returns an empty string.
    # Otherwise, the function processes the string by:
    # - Removing any leading and trailing whitespaces using `strip()`.
    # - Converting the entire string to lowercase using `lower()`.
    # Then, it extracts the first character of the processed string.
    # Finally, it returns the first character.
    if(question==''):
        return ''
    else:
        processed_input=question.strip().lower()
        first_letter=processed_input[0]
        return first_letter

    


def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Returns: True or False
    """
    # TODO: Write your code here
    if(customer_queue_length==0):
        return True
    else:
        return False



def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here
    print("\nWe have now served {} customer(s), and received ${} in revenue.\n".format(customers_served,round(tracking_revenue,2)))



def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here
    print("\nTotal customers served: {}\nTotal revenue: $ {}".format(customers_served,round(tracking_revenue,2)))


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Hint: See https://www.w3schools.com/python/ref_random_randint.asp
    Returns: The resulting random integer.
    """
    return randint(2, 5)


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    #List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press any key to open the shop! ')
        queue_is_open = True

        # TODO: Call the print_welcome_and_menu function with the parameters in the following order -
        #  ice_cream_flavors, ice_cream_sizes, ice_cream_prices
        print_welcome_and_menu(ice_cream_flavors, ice_cream_sizes, ice_cream_prices)

        # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        # TODO: Call the random_queue_length function and save the result to num_of_customers_in_queue
        num_of_customers_in_queue = 0
        num_of_customers_in_queue = random_queue_length()
        print(num_of_customers_in_queue)
        # TODO: Print how many customers are in the queue
        print("\nNum of customers in queue: ",num_of_customers_in_queue)

        # TODO: Call the imported choice function to generate a random name from customer_names.
        #   Then, append each name to the end of the customers_in_queue list.
        #   The total number of customer names added should be equal to num_of_customers_in_queue
        #   Hint: See https://www.w3schools.com/python/ref_random_choice.asp
        #   Note: It is OK to have duplicate names in the queue.
        for i in range(num_of_customers_in_queue):
            random_name = choice(customer_names)
            customers_in_queue.append(random_name)
        print(customers_in_queue)
        while queue_is_open:
            # TODO: Extract the first customer (index 0) from the customers_in_queue and save it to
            #  the current_customer_name variable.
            #  After extraction, the customer should now be removed from the customers_in_queue list.
            #  Hint: Use the pop function with an index argument
            current_customer_name = ""
            current_customer_name=customers_in_queue[0]
            customers_in_queue.pop(0)


            # TODO: Take a customer at the window and update the revenue by calling the take_customer_order function
            tracking_revenue+=take_customer_order(current_customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices)
            # TODO: Update the customers_served variable
            customers_served+=1
            num_of_customers_in_queue-=1
            # TODO: Call the print_current_status
            print_current_status(customers_served,tracking_revenue)

            # TODO: Call the are_all_customers_served(customer_queue_length) function to check if there are any more
            #  customers in the queue.
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
            if(are_all_customers_served(num_of_customers_in_queue)==False):
                continue
            else:
                print_sales_summary(customers_served, tracking_revenue)
                break

        
        # TODO: Ask if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        #  Hint: Use the get_first_letter_of_user_input function
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given
        
        while True:
            temp=input("Do you want to open again (y/n)? ")
            result=get_first_letter_of_user_input(temp)
            if(result=='y'):
                program_running=True
                break
            elif(result=='n'):
                program_running=False
                break
            else:
                continue




if __name__ == '__main__':
    main()