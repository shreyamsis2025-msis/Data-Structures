"""Design and implement billing software for Super Market. 
Here items fall into 0%, 5%, 10% and 20% GST. Essential day to day items like wheat, rice, dals, salt, sugar fall in 0% bracket.
Soaps & detergents, tooth paste, cooking oils, cookies & biscuits are in 5% category. 
Shampoos, cosmetics, ready to eat items are in 10% tax 
TV, washing machines, refrigerator are in 20% bracket. 
Implement the following functionalities:  
a. Method to add items into stock. Data to be stored are item name, tax rate, unit price and quantity. 
b. Provision to change the unit price, tax rate and update quantity. 
c. Customer can choose any listed products and should get bill. In addition to purchased item detail, bill amount should include the total GST applied to selected items.
"""

class SuperMarket:
    def __init__(self):
        # Item format:
        # name: {price, gst, quantity}
        self.stock = {}

    # a. Add item into stock
    def add_item(self, name, price, gst, quantity):
        self.stock[name] = {
            "price": price,
            "gst": gst,
            "quantity": quantity
        }
        print(f"Item '{name}' added successfully.")

    # b. Update item details
    def update_item(self, name, price=None, gst=None, quantity=None):
        if name not in self.stock:
            print("Item not found.")
            return

        if price is not None:
            self.stock[name]["price"] = price
        if gst is not None:
            self.stock[name]["gst"] = gst
        if quantity is not None:
            self.stock[name]["quantity"] = quantity

        print(f"Item '{name}' updated successfully.")

    # Display all items
    def show_stock(self):
        print("\nAvailable Stock:")
        for name, details in self.stock.items():
            print(f"{name} | Price: ₹{details['price']} | GST: {details['gst']}% | Qty: {details['quantity']}")

    # c. Generate bill
    def generate_bill(self, cart):
        print("\n------ CUSTOMER BILL ------")
        total_amount = 0
        total_gst = 0

        for item, qty in cart.items():
            if item not in self.stock:
                print(f"{item} not available.")
                continue

            if qty > self.stock[item]["quantity"]:
                print(f"Insufficient stock for {item}.")
                continue

            price = self.stock[item]["price"]
            gst_rate = self.stock[item]["gst"]

            amount = price * qty
            gst_amount = amount * gst_rate / 100
            total = amount + gst_amount

            self.stock[item]["quantity"] -= qty

            total_amount += amount
            total_gst += gst_amount

            print(f"{item} | Qty: {qty} | Rate: ₹{price} | GST: ₹{gst_amount:.2f} | Total: ₹{total:.2f}")

        print("-----------------------------")
        print(f"Total Amount: ₹{total_amount:.2f}")
        print(f"Total GST: ₹{total_gst:.2f}")
        print(f"Grand Total: ₹{(total_amount + total_gst):.2f}")


market = SuperMarket()

# Adding items
market.add_item("Rice", 50, 0, 100)
market.add_item("Soap", 30, 5, 50)
market.add_item("Shampoo", 120, 10, 40)
market.add_item("TV", 25000, 20, 10)

# Display stock
market.show_stock()

# Update price or quantity
market.update_item("Soap", price=35)

# Customer purchase
cart = {
    "Rice": 2,
    "Soap": 3,
    "TV": 1
}

market.generate_bill(cart)
