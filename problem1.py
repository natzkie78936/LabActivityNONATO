import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage
x = int(input("Enter number for y: "))
y = int(input("Enter number for x: "))
print("the LCM of ",x,"and",y,"is : ", lcm(x, y))
