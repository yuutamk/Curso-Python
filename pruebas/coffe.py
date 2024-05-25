class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print('Ingresa un número o decimal')
            exit()
        if budget < 0:
            print('Lo siento, no tienes dinero')
            exit()

    def get_change(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'Puedes comprar el café {self.name}')
            if budget == self.price:
                print('Es exacto')
            else:
                print(f'Aquí tienes tu cambio: {self.get_change(budget)}$')
            exit('Gracias por tu compra')
cafe1 = Coffee("Latte", 3.5)
cafe1.sell(5)