# Proxy
class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        else:
            return "Проски: доступ отказан."

    def check_access(self):
        print("Прокси: Checking access prior to forwarding the request.")
        return True

    def log_access(self):
        print("Прокси: Logging the time of request.")

# пример
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())

# Bridge
class Implementation:
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on platform B."

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return f"Abstraction: Base operation with:{self._implementation.operation_implementation()}"

class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"ExtendedAbstraction: Extended operation with:{self._implementation.operation_implementation()}"

# пример
implementation_a = ConcreteImplementationA()
abstraction = Abstraction(implementation_a)
print(abstraction.operation())

implementation_b = ConcreteImplementationB()
extended_abstraction = ExtendedAbstraction(implementation_b)
print(extended_abstraction.operation())

# Adapter
class Target:
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"

# пример
adaptee = Adaptee()
print(f"Adaptee: {adaptee.specific_request()}")

adapter = Adapter(adaptee)
print(f"Adapter: {adapter.request()}")
