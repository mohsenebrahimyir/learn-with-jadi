## Inheritance
class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
    
    def value(self):
        return self.ram + self.hard + self.cpu

    def __del__(self):
        Computer.count -= 1

class Labtop(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size

pc1 = Computer(12, 2, 4)
print(pc1.value())

labtop1 = Labtop(16, 2, 4)
labtop1.size = 13
print(labtop1.value())