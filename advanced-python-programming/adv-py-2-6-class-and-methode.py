## Class and Methode
# exp (1): Person class
class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    def get_name(self):
        print(f"name is {self.name}")

    def get_age(self):
        print(f"age is {self.age}")

    def get_info(self):
        print(f"name is {self.name} and age is {self.age}")
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}")
    
    def return_count(self):
        return (Person.count)


mohsen = Person("Mohsen", 27)
mohsen.get_name()
mohsen.get_info()
mohsen.birthday()
mohsen.get_age()
jadi = Person("Jadi Mirmirani", 12)
jadi.get_info()

count = mohsen.return_count() 
print(f"at the moment I have {count} person")