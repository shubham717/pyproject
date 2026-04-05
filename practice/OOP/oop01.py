#print("hello")

class Calculator:
    num = 100

    def __init__(self):
        print("I'm called automatically when object is created")

    def getdata(self):
        print("I'm now executing as method in class")

obj = Calculator()
