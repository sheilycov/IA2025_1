# def computerAreaSquare(side):
#     return side*side

# def computerAreaCircle(radius):
#     pi=3.1415
#     return pi*radius**2

# print (f"The area of an aquare with side 3cm is {computerAreaSquare(3)}")
# print(f"The area of a circle with a radius of 3 is{computerAreaCircle(3):.2f}")


# class Geometry:
#     pi=3.1415
#     def __init__(self,side,radius):
#         self.side=side
#         self.radius=radius
#         print("The object was created succefully!")

# def area(self):
#     squareArea=self.side*self.side
#     circleArea=Geometry.pi*self.radius**2
#     return [squareArea,circleArea]

# areaSquareCircle=Geometry(3,3)
# result=list()
# result=areaSquareCircle.area()
# print(f"The area of the square and circle are:{result[0]},{result[1]:.2f}")

def computeAreaSquare(side):
    return side * side

def computeAreaCircle(radius):
    pi = 3.1415
    return pi * radius ** 2

print(f"The area of a square with side 3cm is {computeAreaSquare(3)}")
print(f"The area of a circle with a radius of 3 is {computeAreaCircle(3):.2f}")


class Geometry:
    pi = 3.1415

    def __init__(self, side, radius):
        self.side = side
        self.radius = radius
        print("The object was created successfully!")

    def area(self):
        squareArea = self.side * self.side
        circleArea = Geometry.pi * self.radius ** 2
        return [squareArea, circleArea]


areaSquareCircle = Geometry(3, 3)
result = areaSquareCircle.area()
print(f"The area of the square and circle are: {result[0]}, {result[1]:.2f}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Ejemplo de uso
rect = Rectangle(5, 10)
print(f"El área es: {rect.area()} cm")


print ("STUDENTS CLASS !!!!!")
import statistics
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def average_grade(self):
        score=statistics.mean(self.grades)
        return score
        # pass 

sheilyStudent= Student('Sheily',[8,8,7,9])
kevinStudent= Student('Kevin',[9,8,9,9])
dayanaStudent= Student('Dayana',[7,9,9,9])

print(f"THE SCORE OF SHEILY IS {sheilyStudent.average_grade():.2f}")
print(f"THE SCORE OF KEVIN IS {kevinStudent.average_grade():.2f}")
print(f"THE SCORE OF DAYANA IS {dayanaStudent.average_grade():.2f}")

print ("OK")
