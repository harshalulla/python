class Car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed=speed
        self.color=color
        print('the__init__is called')

#init servs as the constructor and is called thrice so three times its printed 
ford=Car(20,'blue')
honda=Car(200,'white')
audi=Car(220,'black')

# ford.speed=200
# honda.speed=220
# audi.speed=250

# ford.color='red'
# honda.color='blue'
# audi.color='black'

print(ford.speed)
print(ford.color)


