import statistics


def iSum(list):
    sum = 0
    for x in list:
        sum += x
    return sum


def iAveg(list):
    Sum = iSum(list)
    aveg = Sum / len(list)
    return aveg


mylist = [3, 5, 6]
print(iSum(mylist))
print(iAveg(mylist))

print(statistics.mean(mylist))


class UnivMember:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email


class Student(UnivMember):
    def __init__(self, name, address, email, subjCode, gpaGrade):
        super().__init__(name, address, email)
        self.subjCode = subjCode
        self.gpaGrade = gpaGrade

    def is_diffName(self, student):
        return self.nameStd != student.nameStd


help(len)


"""
ceStudent = Student('Harry', 'CIND-830', 3.9)
print(ceStudent.nameStd)
print(ceStudent.subjCode)
print(ceStudent.gpaGrade)
ceStudent1 = Student('Harry', 'CIND-830', 3.9)
ceStudent2 = Student('Harry', 'CIND-830', 3.9)
ceStudent3 = Student('Sally', 'CIND-830', 3.9)

print(ceStudent1.is_diffName(ceStudent1))
print(ceStudent1.is_diffName(ceStudent2)) #Should Return False
print(ceStudent1.is_diffName(ceStudent3)) #Should Return True
"""
ceStudent1 = Student("Harry", "Montreal", "harry@ryerson.ca", "IND-830", 3.9)
ceStudent2 = Student("Sally", "Toronto", "sally@ryerson.ca", "IND-830", 4.1)
print(ceStudent1.email)  # Should display harry@ryerson.ca
print(ceStudent1.gpaGrade)  # Should display 3.9
print(ceStudent1.address)