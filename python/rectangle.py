class Rectangle:
    def __init__(self,height,width):
        print(height)
        print(width)
        self.height=height
        self.width=width
        print('__init__')

rect1=Rectangle(20,30)
rect2=Rectangle(40,10)


print(rect1.height * rect1.width)
print(rect2.height * rect2.width)