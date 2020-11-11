# Write a Python class to convert an integer to a roman numeral
import random


class Converter:
    @staticmethod
    def ConvertToRoman(number):
        romanValues = [
            (1, "I"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (900, "CM"),
            (1000, "M"),
        ]
        result = ""
        for key, value in reversed(romanValues):
            div = number // key
            if div > 0:
                result += div * value
                number -= div * key
        return print(f"Roman Number is: {result}")


result = Converter.ConvertToRoman(1278)


class Human:
    def __init__(self, name, height, age, numKids=0):
        self.name = name
        self.height = height
        self.age = int(age)
        self.numKids = int(numKids)

    def defineself(self):
        print(
            f"My name is: {self.name},my height is: {self.height},my age is: {self.age}, I have {self.numKids} kids"
        )

    def growold(self, year):
        """
        adds years to the age
        """
        self.age += int(year)

    def getyounger(self, year):
        self.age -= int(year)

    def havekid(self):
        self.age += random.randint(1, 5)
        self.numKids += 1


class Student(Human):
    def __init__(self, name, height, age, department, GPA):
        super().__init__(name, height, age)
        self.department = department
        self.GPA = GPA


human1 = Human("Tolga", "180", "36")
human1.defineself()
human1.growold(30)
human1.defineself()
human1.getyounger(40)
human1.defineself()
human1.havekid()
human1.defineself()

# help(random)
# print(random.randint(1,5))
stundent1 = Student("Zekiye", "160", "35", "ECE", "3.00")
