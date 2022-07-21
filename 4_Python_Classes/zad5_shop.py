from __future__ import annotations


class Manager:

    def __init__(self):
        self.orders = {}

    def display_orders(self):
        for order in self.orders:
            print(order)
            print(f"- quantity: {self.orders[order]}")

    def add_product(self, new_order: Order):
        if not self.orders:
            self.orders[new_order] = 1
            return
        for order in self.orders:
            if new_order.id == order.id:
                self.orders[order] += 1
                return
        self.orders[new_order] = 1

    def sell_product(self, id_to_sell):
        for order in self.orders:
            if order.id == id_to_sell:
                self.orders[order] -= 1


class Order:
    def __init__(self, id_: int, name_: str, price_: float):
        self.id = id_
        self.name = name_
        self.price = price_

    def __str__(self):
        return f"Product:\n- id: {self.id}\n- name: {self.name}\n- price: {self.price}"


def main():

    ziomek = Manager()
    p1 = Order(1, "toster", 12.33)
    p2 = Order(1, "toster", 12.33)
    ziomek.add_product(p1)
    ziomek.add_product(p2)
    # ziomek.add_product(2, "patelnia", 5.33)
    # ziomek.add_product(2, "patelnia", 5.33)
    print(ziomek.display_orders())

    # ziomek.sell_product(2)
    # print(ziomek)


if __name__ == "__main__":
    main()
