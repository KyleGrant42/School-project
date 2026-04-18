# Authors: Grant, Kyle
# Date Created: April 17, 2026
# Course: ITT103 - Programming Techniques
# GitHub URL: https://github.com/KyleGrant42/School-project/tree/main
# Purpose: This program is a point of sale system for a store called QuickMart
#          it lets the cashier add items to a cart, remove them, checkout and print a receipt


# this is the list of products in the store
# each product has a price and how many are in stock
products = {
    "Apple":        {"price": 50.00,  "stock": 100},
    "Banana":       {"price": 30.00,  "stock": 80},
    "Bread":        {"price": 250.00, "stock": 40},
    "Butter":       {"price": 350.00, "stock": 25},
    "Chicken":      {"price": 800.00, "stock": 20},
    "Eggs":         {"price": 450.00, "stock": 15},
    "Milk":         {"price": 200.00, "stock": 50},
    "Rice":         {"price": 180.00, "stock": 60},
    "Sugar":        {"price": 220.00, "stock": 45},
    "Cooking Oil":  {"price": 600.00, "stock": 30},
    "Cheese":       {"price": 500.00, "stock": 10},
    "Orange Juice": {"price": 350.00, "stock": 8},
}

# tax is 10 percent
TAX = 0.10

# discount is 5 percent if the bill is over 5000
DISCOUNT = 0.05
DISCOUNT_MIN = 5000

# low stock warning if item goes below 5
LOW_STOCK = 5


# this function shows all the products
def show_products():
    print("==================================================")
    print("              PRODUCT LIST                        ")
    print("==================================================")
    print(f"  {'Product':<20} {'Price':>10} {'Stock':>8}")
    print("--------------------------------------------------")
    for name in products:
        p = products[name]["price"]
        s = products[name]["stock"]
        # if stock is low show a warning next to it
        if s < LOW_STOCK:
            print(f"  {name:<20} ${p:>9.2f} {s:>6}  ** LOW STOCK **")
        else:
            print(f"  {name:<20} ${p:>9.2f} {s:>6}")
    print("==================================================")


# this function shows whats in the cart right now
def show_cart(cart):
    print("==================================================")
    print("               YOUR CART                         ")
    print("==================================================")

    if len(cart) == 0:
        print("  Cart is empty")
        print("==================================================")
        return

    print(f"  {'Item':<20} {'Qty':>5} {'Price':>10} {'Total':>10}")
    print("--------------------------------------------------")

    subtotal = 0
    for item in cart:
        qty = cart[item]["quantity"]
        price = cart[item]["unit_price"]
        total = qty * price
        subtotal = subtotal + total
        print(f"  {item:<20} {qty:>5} ${price:>9.2f} ${total:>9.2f}")

    print("--------------------------------------------------")
    print(f"  {'Subtotal':<36} ${subtotal:>9.2f}")
    print("==================================================")


# this function adds an item to the cart
def add_item(cart):
    print("==================================================")
    print("              ADD ITEM                           ")
    print("==================================================")

    name = input("  Enter product name: ").strip().title()

    # check if the product exists
    if name not in products:
        print("  Sorry that product was not found. Check the spelling.")
        return

    stock = products[name]["stock"]
    price = products[name]["price"]
    print(f"  {name} costs ${price:.2f} and there are {stock} in stock")

    # get quantity and make sure its a valid number
    while True:
        qty_input = input("  How many do you want to add? ").strip()
        if qty_input.isdigit() and int(qty_input) >= 1:
            qty = int(qty_input)
            break
        else:
            print("  Please enter a valid whole number")

    # check if there is enough stock
    if qty > stock:
        print(f"  Not enough stock. Only {stock} available.")
        return

    # if item already in cart just add the quantity
    if name in cart:
        new_qty = cart[name]["quantity"] + qty
        if new_qty > stock:
            print(f"  Cannot add that many. Only {stock} total in stock.")
            return
        cart[name]["quantity"] = new_qty
    else:
        cart[name] = {"quantity": qty, "unit_price": price}

    # take away from stock
    products[name]["stock"] = products[name]["stock"] - qty

    print(f"  Added {qty} x {name} to cart!")

    # check if any items are running low
    for p in products:
        if products[p]["stock"] < LOW_STOCK:
            print(f"  ** WARNING: {p} is low on stock ({products[p]['stock']} left) **")


# this function removes an item from the cart
def remove_item(cart):
    print("==================================================")
    print("             REMOVE ITEM                         ")
    print("==================================================")

    if len(cart) == 0:
        print("  Cart is empty, nothing to remove")
        return

    show_cart(cart)

    name = input("  Enter the name of the item to remove: ").strip().title()

    if name not in cart:
        print("  That item is not in the cart")
        return

    # put the stock back
    qty = cart[name]["quantity"]
    products[name]["stock"] = products[name]["stock"] + qty

    # remove from cart
    del cart[name]
    print(f"  {name} was removed from the cart")


# this function does the checkout
def checkout(cart):
    print("==================================================")
    print("               CHECKOUT                          ")
    print("==================================================")

    if len(cart) == 0:
        print("  Cart is empty. Add items before checking out.")
        return None

    # calculate subtotal
    subtotal = 0
    for item in cart:
        qty = cart[item]["quantity"]
        price = cart[item]["unit_price"]
        subtotal = subtotal + (qty * price)

    # check if discount applies
    discount_amount = 0
    if subtotal > DISCOUNT_MIN:
        discount_amount = subtotal * DISCOUNT
        print(f"  Subtotal:              ${subtotal:.2f}")
        print(f"  Discount (5%):        -${discount_amount:.2f}")
    else:
        print(f"  Subtotal:              ${subtotal:.2f}")

    # calculate tax after discount
    after_discount = subtotal - discount_amount
    tax_amount = after_discount * TAX
    total = after_discount + tax_amount

    print(f"  Tax (10%):             ${tax_amount:.2f}")
    print("--------------------------------------------------")
    print(f"  TOTAL:                 ${total:.2f}")
    print("==================================================")

    # get payment from cashier
    while True:
        pay_input = input("  Enter amount paid by customer: $").strip()
        try:
            amount_paid = float(pay_input)
            if amount_paid < total:
                print(f"  Not enough. Customer needs to pay at least ${total:.2f}")
            else:
                break
        except:
            print("  Please enter a valid amount")

    change = amount_paid - total
    print(f"  Change to give back:   ${change:.2f}")

    return subtotal, discount_amount, tax_amount, total, amount_paid, change


# this function prints the receipt
def print_receipt(cart, subtotal, discount_amount, tax_amount, total, amount_paid, change):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print()
    print("**************************************************")
    print("*              QUICKMART STORE                   *")
    print("*           Kingston, Jamaica                    *")
    print("*           Tel: (876) 555-0199                  *")
    print("**************************************************")
    print(f"  Date: {now}")
    print("--------------------------------------------------")
    print(f"  {'Item':<20} {'Qty':>4} {'Price':>9} {'Total':>9}")
    print("--------------------------------------------------")

    for item in cart:
        qty = cart[item]["quantity"]
        price = cart[item]["unit_price"]
        line = qty * price
        print(f"  {item:<20} {qty:>4} ${price:>8.2f} ${line:>8.2f}")

    print("--------------------------------------------------")
    print(f"  Subtotal:                        ${subtotal:>8.2f}")

    if discount_amount > 0:
        print(f"  Discount (5%):                  -${discount_amount:>8.2f}")

    print(f"  Tax (10%):                        ${tax_amount:>8.2f}")
    print("--------------------------------------------------")
    print(f"  TOTAL:                            ${total:>8.2f}")
    print(f"  Amount Paid:                      ${amount_paid:>8.2f}")
    print(f"  Change:                           ${change:>8.2f}")
    print("**************************************************")
    print("*        Thank you for shopping with us!         *")
    print("*                 Come again!                    *")
    print("**************************************************")
    print()


# this is the main menu function
def show_menu():
    print("==================================================")
    print("          QUICKMART - POS SYSTEM                 ")
    print("==================================================")
    print("  1. View Products")
    print("  2. Add Item to Cart")
    print("  3. Remove Item from Cart")
    print("  4. View Cart")
    print("  5. Checkout")
    print("  6. New Transaction")
    print("  7. Exit")
    print("==================================================")


# this is where the program starts running
def main():
    print()
    print("**************************************************")
    print("*       Welcome to QuickMart POS System         *")
    print("**************************************************")
    print()

    # create an empty cart to start
    cart = {}

    # keep showing the menu until the user exits
    while True:
        show_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            add_item(cart)

        elif choice == "3":
            remove_item(cart)

        elif choice == "4":
            show_cart(cart)

        elif choice == "5":
            result = checkout(cart)
            if result != None:
                subtotal, discount_amount, tax_amount, total, amount_paid, change = result
                print_receipt(cart, subtotal, discount_amount, tax_amount, total, amount_paid, change)
                # clear the cart after checkout
                cart = {}
                print("  Transaction done! Cart has been cleared.")

        elif choice == "6":
            # start a new transaction
            if len(cart) > 0:
                confirm = input("  Cart is not empty. Start new transaction anyway? (y/n): ").strip().lower()
                if confirm == "y":
                    # put stock back before clearing
                    for item in cart:
                        products[item]["stock"] = products[item]["stock"] + cart[item]["quantity"]
                    cart = {}
                    print("  New transaction started!")
                else:
                    print("  Cancelled.")
            else:
                cart = {}
                print("  New transaction started!")

        elif choice == "7":
            if len(cart) > 0:
                confirm = input("  You still have items in the cart. Exit anyway? (y/n): ").strip().lower()
                if confirm != "y":
                    continue
                # put stock back
                for item in cart:
                    products[item]["stock"] = products[item]["stock"] + cart[item]["quantity"]
            print()
            print("**************************************************")
            print("*        Thanks for using QuickMart POS!        *")
            print("*                 Goodbye!                       *")
            print("**************************************************")
            break

        else:
            print("  Invalid choice. Please enter a number from 1 to 7.")

        input("\n  Press ENTER to continue...")
        print()


# run the program
main()
