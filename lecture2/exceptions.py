
try:
    x = int(input("x: "))
    y = int(input("y: "))
except: 
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot device by 0")
    sys.exit(1)

print(f"{x} / {y} = {result}")