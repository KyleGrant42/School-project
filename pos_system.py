"""
=============================================================
Point of Sale (POS) System
Course: Programming Techniques (ITT-103)
=============================================================
Description:
    A menu-driven POS system that manages a product catalog,
    shopping cart, checkout, payment, and receipt generation.

Features:
    - Product catalog with stock management
    - Add/remove items from shopping cart
    - Checkout with tax, discount, and change calculation
    - Formatted receipt generation
    - Low-stock alerts
    - Multiple transactions per session
=============================================================
"""

# ─────────────────────────────────────────────────────────────
# PRODUCT CATALOG
# Dictionary structure:
#   product_name: {"price": float, "stock": int}
# ─────────────────────────────────────────────────────────────
product_catalog = {
    "Apple":          {"price": 50.00,   "stock": 100},
    "Banana":         {"price": 30.00,   "stock": 80},
    "Bread":          {"price": 250.00,  "stock": 40},
    "Butter":         {"price": 350.00,  "stock": 25},
    "Chicken":        {"price": 800.00,  "stock": 20},
    "Eggs (dozen)":   {"price": 450.00,  "stock": 15},
    "Milk (1L)":      {"price": 200.00,  "stock": 50},
    "Rice (1kg)":     {"price": 180.00,  "stock": 60},
    "Sugar (1kg)":    {"price": 220.00,  "stock": 45},
    "Cooking Oil":    {"price": 600.00,  "stock": 30},
    "Cheese":         {"price": 500.00,  "stock": 10},
    "Orange Juice":   {"price": 350.00,  "stock": 8},
}

# ─────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────
TAX_RATE            = 0.10   # 10% sales tax
DISCOUNT_RATE       = 0.05   # 5% discount
DISCOUNT_THRESHOLD  = 5000.00  # Discount applies when subtotal > $5000
LOW_STOCK_THRESHOLD = 5      # Alert when stock falls below this value
STORE_NAME          = "QuickMart POS System"
CURRENCY            = "JMD $"


# ─────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def display_separator(char="=", width=55):
    """Print a separator line for formatting."""
    print(char * width)


def display_header(title):
    """Print a formatted section header."""
    display_separator()
    print(f"  {title}")
    display_separator()


def get_integer_input(prompt, min_value=1):
    """
    Prompt the user for a positive integer with input validation.
    Keeps prompting until a valid integer >= min_value is entered.

    Parameters:
        prompt    (str): The message to display to the user.
        min_value (int): The minimum acceptable integer value.

    Returns:
        int: A validated integer from the user.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) >= min_value:
            return int(user_input)
        else:
            print(f"  ⚠  Invalid input. Please enter a whole number "
                  f"of {min_value} or more.")


def get_float_input(prompt, min_value=0.0):
    """
    Prompt the user for a positive float with input validation.

    Parameters:
        prompt    (str):   The message to display.
        min_value (float): The minimum acceptable value.

    Returns:
        float: A validated float from the user.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if value >= min_value:
                return value
            else:
                print(f"  ⚠  Amount must be at least {min_value:.2f}.")
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric amount.")


# ─────────────────────────────────────────────────────────────
# PRODUCT MANAGEMENT FUNCTIONS
# ─────────────────────────────────────────────────────────────

def display_catalog():
    """
    Display the full product catalog with prices and stock levels.
    Highlights items with low stock.
    """
    display_header("PRODUCT CATALOG")
    print(f"  {'#':<4} {'Product':<18} {'Price':>10} {'Stock':>8}")
    display_separator("-")

    for index, (name, details) in enumerate(product_catalog.items(), start=1):
        stock    = details["stock"]
        price    = details["price"]
        low_flag = " ⚠ LOW" if stock < LOW_STOCK_THRESHOLD else ""
        print(f"  {index:<4} {name:<18} {CURRENCY}{price:>8.2f} "
              f"{stock:>6}{low_flag}")

    display_separator()


def check_low_stock():
    """
    Scan the catalog and print an alert for any product
    whose stock is below LOW_STOCK_THRESHOLD.
    """
    low_items = [
        name for name, details in product_catalog.items()
        if details["stock"] < LOW_STOCK_THRESHOLD
    ]

    if low_items:
        display_separator("-")
        print("  ⚠  LOW STOCK ALERT — The following items are running low:")
        for item in low_items:
            qty = product_catalog[item]["stock"]
            print(f"     • {item}: {qty} unit(s) remaining")
        display_separator("-")


# ─────────────────────────────────────────────────────────────
# SHOPPING CART FUNCTIONS
# ─────────────────────────────────────────────────────────────

def create_cart():
    """
    Initialise and return an empty shopping cart dictionary.
    Structure:
        cart = { product_name: {"quantity": int, "unit_price": float} }

    Returns:
        dict: An empty cart.
    """
    return {}


def add_to_cart(cart):
    """
    Prompt the cashier for a product name and quantity,
    validate stock availability, then add the item to the cart.

    Parameters:
        cart (dict): The current shopping cart.
    """
    display_header("ADD ITEM TO CART")
    product_name = input("  Enter product name: ").strip().title()

    # Validate product exists in catalog
    if product_name not in product_catalog:
        print(f"  ✗  '{product_name}' not found in catalog. "
              "Check spelling or view the catalog.")
        return

    available_stock = product_catalog[product_name]["stock"]
    unit_price      = product_catalog[product_name]["price"]

    print(f"  Found: {product_name}  |  Price: {CURRENCY}{unit_price:.2f}"
          f"  |  In Stock: {available_stock}")

    quantity = get_integer_input("  Enter quantity: ", min_value=1)

    # Validate sufficient stock
    if quantity > available_stock:
        print(f"  ✗  Insufficient stock. Only {available_stock} available.")
        return

    # Add to cart or update existing quantity
    if product_name in cart:
        new_qty = cart[product_name]["quantity"] + quantity
        if new_qty > available_stock:
            print(f"  ✗  Cannot add {quantity} more. "
                  f"Total would exceed stock ({available_stock}).")
            return
        cart[product_name]["quantity"] = new_qty
    else:
        cart[product_name] = {"quantity": quantity, "unit_price": unit_price}

    # Deduct from catalog stock
    product_catalog[product_name]["stock"] -= quantity

    print(f"  ✓  Added {quantity} × {product_name} to cart.")
    check_low_stock()


def remove_from_cart(cart):
    """
    Allow the cashier to remove an item (fully) from the cart
    and restore the stock to the catalog.

    Parameters:
        cart (dict): The current shopping cart.
    """
    if not cart:
        print("  Cart is already empty.")
        return

    display_header("REMOVE ITEM FROM CART")
    view_cart(cart)

    product_name = input("  Enter the product name to remove: ").strip().title()

    if product_name not in cart:
        print(f"  ✗  '{product_name}' is not in the cart.")
        return

    # Restore stock
    qty_returned = cart[product_name]["quantity"]
    product_catalog[product_name]["stock"] += qty_returned

    del cart[product_name]
    print(f"  ✓  '{product_name}' removed from cart. "
          f"{qty_returned} unit(s) returned to stock.")


def view_cart(cart):
    """
    Display all items currently in the shopping cart
    along with quantities, unit prices, and line totals.

    Parameters:
        cart (dict): The current shopping cart.
    """
    display_header("SHOPPING CART")

    if not cart:
        print("  Your cart is empty.")
        display_separator()
        return

    print(f"  {'Product':<18} {'Qty':>5} {'Unit Price':>12} {'Total':>12}")
    display_separator("-")

    running_total = 0.0
    for name, details in cart.items():
        qty        = details["quantity"]
        unit_price = details["unit_price"]
        line_total = qty * unit_price
        running_total += line_total
        print(f"  {name:<18} {qty:>5} "
              f"{CURRENCY}{unit_price:>10.2f} {CURRENCY}{line_total:>10.2f}")

    display_separator("-")
    print(f"  {'Subtotal':>38}: {CURRENCY}{running_total:>10.2f}")
    display_separator()


# ─────────────────────────────────────────────────────────────
# CHECKOUT & PAYMENT FUNCTIONS
# ─────────────────────────────────────────────────────────────

def calculate_totals(cart):
    """
    Compute the subtotal, discount (if applicable), tax, and
    final total for the current cart.

    Parameters:
        cart (dict): The current shopping cart.

    Returns:
        tuple: (subtotal, discount_amount, tax_amount, total)
    """
    subtotal = sum(
        d["quantity"] * d["unit_price"] for d in cart.values()
    )

    # Apply 5% discount for bills over the threshold
    discount_amount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0.0

    discounted_subtotal = subtotal - discount_amount
    tax_amount          = discounted_subtotal * TAX_RATE
    total               = discounted_subtotal + tax_amount

    return subtotal, discount_amount, tax_amount, total


def checkout(cart):
    """
    Run the full checkout process:
        - Display order summary with tax / discount
        - Collect payment from cashier
        - Validate payment amount
        - Calculate and display change

    Parameters:
        cart (dict): The current shopping cart.

    Returns:
        tuple or None: (subtotal, discount, tax, total, amount_paid, change)
                       or None if the cart is empty.
    """
    if not cart:
        print("  ✗  Cannot checkout — the cart is empty.")
        return None

    subtotal, discount_amount, tax_amount, total = calculate_totals(cart)

    display_header("CHECKOUT SUMMARY")
    print(f"  {'Subtotal':<30}: {CURRENCY}{subtotal:>10.2f}")

    if discount_amount > 0:
        print(f"  {'Discount (5%)':<30}: -{CURRENCY}{discount_amount:>9.2f}")

    print(f"  {'Sales Tax (10%)':<30}: {CURRENCY}{tax_amount:>10.2f}")
    display_separator("-")
    print(f"  {'TOTAL AMOUNT DUE':<30}: {CURRENCY}{total:>10.2f}")
    display_separator()

    # Collect and validate payment
    while True:
        amount_paid = get_float_input(
            f"  Enter amount received from customer ({CURRENCY}): ",
            min_value=0.0
        )
        if amount_paid >= total:
            break
        print(f"  ✗  Payment of {CURRENCY}{amount_paid:.2f} is less than "
              f"the total due of {CURRENCY}{total:.2f}. Please try again.")

    change = amount_paid - total
    print(f"\n  ✓  Payment accepted.")
    print(f"  Change to return: {CURRENCY}{change:.2f}")

    return subtotal, discount_amount, tax_amount, total, amount_paid, change


# ─────────────────────────────────────────────────────────────
# RECEIPT GENERATION
# ─────────────────────────────────────────────────────────────

def print_receipt(cart, subtotal, discount_amount, tax_amount,
                  total, amount_paid, change):
    """
    Generate and display a formatted receipt for the transaction.

    Parameters:
        cart            (dict):  The purchased items.
        subtotal        (float): Subtotal before tax/discount.
        discount_amount (float): Discount applied.
        tax_amount      (float): Sales tax applied.
        total           (float): Final amount due.
        amount_paid     (float): Amount tendered by customer.
        change          (float): Change returned to customer.
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

    display_separator("*")
    print(f"{'*':>1}{'QuickMart — Point of Sale':^53}{'*':>1}")
    print(f"{'*':>1}{'Kingston, Jamaica':^53}{'*':>1}")
    print(f"{'*':>1}{'Tel: (876) 555-0199':^53}{'*':>1}")
    display_separator("*")
    print(f"  Date & Time : {timestamp}")
    display_separator("-")

    # Itemised list
    print(f"  {'ITEM':<18} {'QTY':>4} {'UNIT PRICE':>11} {'TOTAL':>11}")
    display_separator("-")

    for name, details in cart.items():
        qty        = details["quantity"]
        unit_price = details["unit_price"]
        line_total = qty * unit_price
        print(f"  {name:<18} {qty:>4} "
              f"  {CURRENCY}{unit_price:>8.2f}  {CURRENCY}{line_total:>8.2f}")

    display_separator("-")

    # Totals section
    print(f"  {'Subtotal':<36}: {CURRENCY}{subtotal:>8.2f}")
    if discount_amount > 0:
        print(f"  {'Discount (5% bill over $5000)':<36}: -{CURRENCY}{discount_amount:>7.2f}")
    print(f"  {'Sales Tax (10%)':<36}: {CURRENCY}{tax_amount:>8.2f}")
    display_separator("-")
    print(f"  {'TOTAL DUE':<36}: {CURRENCY}{total:>8.2f}")
    print(f"  {'Amount Paid':<36}: {CURRENCY}{amount_paid:>8.2f}")
    print(f"  {'Change Returned':<36}: {CURRENCY}{change:>8.2f}")
    display_separator("*")
    print(f"{'*':>1}{'Thank you for shopping at QuickMart!':^53}{'*':>1}")
    print(f"{'*':>1}{'Please come again.':^53}{'*':>1}")
    display_separator("*")
    print()


# ─────────────────────────────────────────────────────────────
# MAIN MENU & SESSION LOOP
# ─────────────────────────────────────────────────────────────

def display_menu():
    """Print the main POS menu options."""
    display_header(f"{STORE_NAME} — MAIN MENU")
    print("  1.  View Product Catalog")
    print("  2.  Add Item to Cart")
    print("  3.  Remove Item from Cart")
    print("  4.  View Cart")
    print("  5.  Checkout & Pay")
    print("  6.  New Transaction")
    print("  7.  Exit")
    display_separator()


def run_pos():
    """
    Main entry point — runs the POS session loop.
    Supports multiple transactions until the user exits.
    """
    print()
    display_separator("*")
    print(f"{'*':>1}{STORE_NAME:^53}{'*':>1}")
    print(f"{'*':>1}{'Welcome, Cashier!':^53}{'*':>1}")
    display_separator("*")
    print()

    cart = create_cart()   # Start a fresh cart

    while True:
        display_menu()
        choice = input("  Enter your choice (1-7): ").strip()

        if choice == "1":
            # ── View product catalog ────────────────────────
            display_catalog()

        elif choice == "2":
            # ── Add item to cart ────────────────────────────
            add_to_cart(cart)

        elif choice == "3":
            # ── Remove item from cart ───────────────────────
            remove_from_cart(cart)

        elif choice == "4":
            # ── View cart ───────────────────────────────────
            view_cart(cart)

        elif choice == "5":
            # ── Checkout ────────────────────────────────────
            result = checkout(cart)
            if result:
                subtotal, discount_amount, tax_amount, total, amount_paid, change = result
                view_cart(cart)
                print_receipt(cart, subtotal, discount_amount, tax_amount,
                              total, amount_paid, change)
                # Reset cart for next transaction
                cart = create_cart()
                print("  ✓  Transaction complete. Cart has been cleared.")

        elif choice == "6":
            # ── New transaction ─────────────────────────────
            if cart:
                confirm = input(
                    "  The current cart will be cleared. Continue? (y/n): "
                ).strip().lower()
                if confirm == "y":
                    # Restore stock for all items in cart before clearing
                    for name, details in cart.items():
                        product_catalog[name]["stock"] += details["quantity"]
                    cart = create_cart()
                    print("  ✓  New transaction started. Cart cleared.")
                else:
                    print("  New transaction cancelled.")
            else:
                cart = create_cart()
                print("  ✓  New transaction started.")

        elif choice == "7":
            # ── Exit ────────────────────────────────────────
            if cart:
                confirm = input(
                    "  You have items in the cart. Exit anyway? (y/n): "
                ).strip().lower()
                if confirm != "y":
                    continue
                # Restore stock before exit
                for name, details in cart.items():
                    product_catalog[name]["stock"] += details["quantity"]

            display_separator("*")
            print(f"{'*':>1}{'Thank you for using QuickMart POS.':^53}{'*':>1}")
            print(f"{'*':>1}{'Have a great day!':^53}{'*':>1}")
            display_separator("*")
            break

        else:
            print("  ✗  Invalid choice. Please enter a number between 1 and 7.")

        input("\n  Press ENTER to return to the menu...")
        print()


# ─────────────────────────────────────────────────────────────
# PROGRAM ENTRY POINT
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_pos()
