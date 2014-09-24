class Person:
    def __init__(self, first_name, last_name='', age=18): # self is always first argument in all instance method
        # __init__ is initializer
        self.first_name = first_name
        # `self` is used for accessing instance attribute and method.
        self.last_name = last_name
        self.__age = age # Private like attribute

    def full_name(self):
        # Instance method
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        # Since __age is private like variable we need to have getters and setters. Getter
        return self.__age

    def set_age(self, age):
        # Setter
        self.__age = age

    def is_major(self):
        return self.__age >= 18


guido = Person("Guido", "van rossum", 58) # __init__ of Person is called
krace = Person("Kracekumar", "Ramaraju", 24)
# Access instance first_name, last_name
print(guido.first_name)
print(guido.last_name)
print(krace.first_name)
print(krace.last_name)
# Access instance methods
print(guido.full_name()) # self is passed implicitly in the background.
print(krace.is_major())

# Modif the age, first_name
krace.set_age(12)
krace.first_name = 'kracekumar'
print(krace.get_age(), krace.first_name)
print(krace.is_major())
