print("Irjon be egy numbert: #1 ")
num1 =(input)()

print("Irjon be egy numbert: #2")
num2 = (input)()

print("Irjon be egy numbert: #3 ")
num3 = (input)()

#1

legkisebb = min(num1, num2, num3)
print("legkisebb szam:", legkisebb)

#2

legnagyobb = max(num1, num2, num3)
print("legnagyobb szam:", legnagyobb)

#3

print("irjon be gy pontszamot")
x = input()

if x < 50:
    print(1)

if x >= 50 and x < 60:
    print(2)
    
if x >= 60 and x < 70:
    print(3)
    
if x >= 70 and x < 85:
    print(4)

if x >= 85:
    print(5)
