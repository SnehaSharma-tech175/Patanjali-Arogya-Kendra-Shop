from datetime import datetime

# Menu using short codes
menu = {
    'A001': 120,
    'D050': 15,
    'D100': 35,
    'D150': 80,
    'DRSE': 10,
    'DLBN': 20,
    'H250': 60,
    'H500': 110,
    'BCAM': 80,
    'CAMR': 60,
}

# Mapping short code to full item name
full_names = {
    'A001': 'Aastha Aitar',
    'D050': 'Aastha Dhoop 50gm',
    'D100': 'Aastha Dhoop 100gm',
    'D150': 'Aastha Dhoop 150gm',
    'DRSE': 'Aastha Dhoop Rose',
    'DLBN': 'Aastha Dry Dhoop Loban',
    'H250': 'Aastha Hawan Samagri 250gm',
    'H500': 'Aastha Hawan Samagri 500gm',
    'BCAM': 'Aastha Premium Bhasmi Camphor',
    'CAMR': 'Aastha Premium Camphor',
}

# Dictionary to store all orders per date
sales_by_date = {}

while True:
    print("\nWelcome to PATANJALI AROGYA KENDRA\n")
    print(f"{'Code':6} | {'Item Name':40} | {'Price (Rs)':>10}")
    print("-" * 65)
    for code, price in menu.items():
        print(f"{code:6} | {full_names[code]:40} | {price:10}")

    order_total = 0
    ordered_items = []

    while True:
        item_code = input("\nEnter the item code you want to order: ").strip().upper()
        if item_code in menu:
            try:
                quantity = int(input(f"Enter quantity for '{full_names[item_code]}': "))
                if quantity <= 0:
                    print("Please enter a positive quantity.")
                    continue
                total_price = menu[item_code] * quantity
                order_total += total_price
                ordered_items.append((item_code, menu[item_code], quantity, total_price))
                print(f"{quantity} x '{full_names[item_code]}' added to your order.")
            except ValueError:
                print("Invalid input! Quantity should be a number.")
        else:
            print(f"Sorry, the item code '{item_code}' is not valid!")

        another = input("Do you want to add another item? (Yes/No): ").strip().lower()
        if another != 'yes':
            break

    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%I:%M %p")

    # Save order to date-wise sales record
    if date_str not in sales_by_date:
        sales_by_date[date_str] = []

    sales_by_date[date_str].append(order_total)

    # Show order summary
    if ordered_items:
        print("\nOrder Summary:\n")
        print(f"Date: {date_str}    Time: {time_str}")
        print(f"{'Item Name':40} | {'Qty':>3} | {'Unit Price':>10} | {'Total (Rs)':>12}")
        print("-" * 75)
        for code, unit_price, qty, total in ordered_items:
            print(f"{full_names[code]:40} | {qty:>3} | {unit_price:10} | {total:12}")
        print("-" * 75)
        print(f"{'Total Amount':58} | {order_total:12}")
        print(f"\nTotal Sales on {date_str}: ₹{sum(sales_by_date[date_str])}")
    else:
        print("\nNo valid items were ordered.")

    # Ask to take next order or exit
    again = input("\nDo you want to take another order? (Yes/No): ").strip().lower()
    if again != 'yes':
        print("\nFinal Sales Summary:")
        for date, sales_list in sales_by_date.items():
            print(f"Date: {date} | Total Sales: ₹{sum(sales_list)} from {len(sales_list)} orders")
        break