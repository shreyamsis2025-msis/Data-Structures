"""
Design a python application which keeps track of the shares in hand,
It is assumed that it does not allow more than 5 companies of share at any time. 
The rule says that if we want to purchase a new t allow or company share, if already 5 companies are present,
oldest company shares should be sold before purchasing new company shares. Selling should be always the oldest share. 
Partial selling share. 
Partial selling is also allowed (If 100 shares of 'A' company is in hand, 50 shares can be sold). 
Provide the following functionalities: 
a. Method to purchase shares specifving company name, qty and share price 
b. Method to sell share with current price present shares 
C. Display all currenty shares with numbers. Store and display all transactions (purchase and sell)
"""

from collections import deque
from datetime import datetime

class SharePortfolio:
    def __init__(self, max_companies=5):
        self.max_companies = max_companies
        # deque of {name, qty, avg_price}
        self.companies = deque()
        self.transactions = []  # history strings/dicts

    def _find_company(self, name):
        for idx, comp in enumerate(self.companies):
            if comp["name"] == name:
                return idx, comp
        return None, None

    def buy(self, name, qty, price):
        qty = int(qty); price = float(price)
        idx, comp = self._find_company(name)
        if comp:
            # simple average price update (weighted)
            total_value = comp["qty"] * comp["avg_price"] + qty * price
            comp["qty"] += qty
            comp["avg_price"] = total_value / comp["qty"]
            self.transactions.append({
                "type": "BUY", "name": name, "qty": qty, "price": price,
                "time": datetime.now().isoformat(sep=' ', timespec='seconds')
            })
            print(f"Bought {qty} of existing {name}")
            return

        # new company: enforce max companies
        while len(self.companies) >= self.max_companies:
            oldest = self.companies.popleft()
            self.transactions.append({
                "type": "FORCED_SELL", "name": oldest["name"], "qty": oldest["qty"],
                "price": None, "time": datetime.now().isoformat(sep=' ', timespec='seconds')
            })
            print(f"Forced sell oldest company {oldest['name']} qty {oldest['qty']}")

        # add new company
        self.companies.append({"name": name, "qty": qty, "avg_price": price})
        self.transactions.append({
            "type": "BUY", "name": name, "qty": qty, "price": price,
            "time": datetime.now().isoformat(sep=' ', timespec='seconds')
        })
        print(f"Bought new company {name} qty {qty}")

    def sell(self, qty, current_price):
        qty = int(qty); current_price = float(current_price)
        if not self.companies:
            print("No companies to sell from.")
            return

        # Always sell from the oldest company
        oldest = self.companies[0]
        if qty >= oldest["qty"]:
            sold_qty = oldest["qty"]
            self.companies.popleft()
            print(f"Sold all {sold_qty} of {oldest['name']}")
        else:
            oldest["qty"] -= qty
            sold_qty = qty
            print(f"Sold {sold_qty} of {oldest['name']} (partial)")

        self.transactions.append({
            "type": "SELL", "name": oldest["name"], "qty": sold_qty,
            "price": current_price, "time": datetime.now().isoformat(sep=' ', timespec='seconds')
        })

    def display_holdings(self):
        print("\nCURRENT HOLDINGS (oldest → newest):")
        if not self.companies:
            print("No holdings.")
            return
        for c in self.companies:
            print(f"{c['name']:10} qty:{c['qty']:4} avg_price:₹{c['avg_price']:.2f}")

    def display_transactions(self):
        print("\nTRANSACTIONS:")
        for t in self.transactions:
            t_str = f"{t['time']} | {t['type']} | {t['name']} | qty:{t['qty']}"
            if t.get("price") is not None:
                t_str += f" | price:₹{t['price']:.2f}"
            print(t_str)

# Example usage
if __name__ == "__main__":
    p = SharePortfolio()
    p.buy("A", 100, 50)
    p.buy("B", 200, 60)
    p.buy("C", 150, 40)
    p.buy("D", 80, 70)
    p.buy("E", 90, 35)
    # buying F forces sell of oldest (A)
    p.buy("F", 120, 45)
    p.display_holdings()
    p.sell(50, 55)  # sells from oldest (now B)
    p.display_holdings()
    p.display_transactions()
