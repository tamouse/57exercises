from decimal import Decimal

class Cart:

    def __init__(self, tax_rate):
        self.tax_rate = Decimal(tax_rate)
        self.items = []

    def item_count(self):
        return len(self.items)

    def add_item(self, description, quantity, unit_price):
        description = str(description)
        quantity = int(quantity)
        unit_price = Decimal(unit_price)
        self.items.append(
            {
                'item': description,
                'quantity': quantity,
                'unit_price': unit_price,
                'item_cost': unit_price * quantity
            }
        )

    def subtotal(self):
        st = Decimal(sum([x['item_cost'] for x in self.items]))
        return st

    def tax_on_items(self):
        return self.subtotal()*self.tax_rate

    def grand_total(self):
        return self.subtotal()+self.tax_on_items()
