GCD = [20, 8,10, 12, 22] #Store GCD in an array or Data Structure

def gcd(a,b):
    while(b!=0):
        t = a
        a = b
        b = t % b

    return a

GCD[1] = 100
print(gcd(60,96)) #should be 12
print(GCD)

class Bike(object):
    def __init__(self, brand):
        self.brand = brand
        self.next = None
    
    def travel(self, travel):
        self.travel = travel   
        return travel

    def color(self, color):
        self.color = color
        return color


Ragley = Bike("Ragley Piglet")
Ragley.travel = "175"
Ragley.color = "Gunmetal"

print(Ragley.travel + " " + Ragley.color)