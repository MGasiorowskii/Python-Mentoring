class Manager:

    def __init__(self):
        self.orders = {}

    def __str__(self):
        for order in self.orders:
            print(order)
            print(f"- quantity: {self.orders[order]}")
        return "This is list of product in Stock\n"        #twrozyć jakas tablice do wyswietlania czy tak jest ok ?

    def add_product(self, id: int, name: str, price: float):

        create_flag = 1
        for order in self.orders:
            if id == order.id:
                self.orders[order] += 1
                create_flag = 0

        if create_flag:
            self.orders[Order(id, name, price)] = 1

    def sell_product(self, id_to_sell):
        for order in self.orders:
            if order.id == id_to_sell:
                self.orders[order] -=1


class Order:
    def __init__(self, id_: int, name_: str, price_: float):
        self.id = id_
        self.name = name_
        self.price = price_

    def __str__(self):
        return f"Product:\n- id: {self.id}\n- name: {self.name}\n- price: {self.price}"


def main():

    ziomek = Manager()
    ziomek.add_product(1, "toster", 12.33)
    ziomek.add_product(2, "patelnia", 5.33)
    ziomek.add_product(2, "patelnia", 5.33)
    print(ziomek)

    ziomek.sell_product(2)
    print(ziomek)


if __name__ == "__main__":
    main()
