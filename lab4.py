# Strategy Pattern
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid {amount} using Credit Card: {self.card_number}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal: {self.email}"

# пример
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        return self.strategy.pay(amount)

# Chain of Responsibility Pattern
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "HandlerA handled request A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "HandlerB handled request B"
        return super().handle(request)

# пример
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.set_next(handler_b)

# Iterator Pattern
class SimpleIterator:
    def __init__(self, numbers):
        self.contents = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.contents):
            result = self.contents[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

#пример
numbers = [30, '40', False, 30, 'hello']
iterator = SimpleIterator(numbers)

print(iterator)

for number in iterator:
    print(number)

# Example execution
if __name__ == "__main__":
    # Strategy pattern
    payment = PaymentContext(CreditCardPayment("1234-5678-9012-3456"))
    print(payment.execute_payment(100))

    payment = PaymentContext(PayPalPayment("user@example.com"))
    print(payment.execute_payment(200))

    # Chain of Responsibility
    print(handler_a.handle("A"))
    print(handler_a.handle("B"))
    print(handler_a.handle("C"))

