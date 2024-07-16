print()
print("  ****************  ")
print("** UNIT CONVERTER **")
print("  ****************  ")
print()

conversion_available = [
    (1, "km", "mi"),
    (2, "mi", "km"),
    (3, "kg", "lb"),
    (4, "lb", "kg"),
    (5, "°C", "°F"),
    (6, "°F", "°C"),
]

print("Convertions available:")
print()

for conversion_number, from_unit, to_unit, in conversion_available:
    print(f'{conversion_number} {from_unit} -> {to_unit}')

print()
conversion = input("Enter of number to convertion to use --> ")
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversion_available[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> '))

if conversion_number == 1:
    to_value = from_value * 0.62
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 2:
    to_value = from_value * 1.61
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 3:
    to_value = from_value * 2.205
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 4:
    to_value = from_value * 0.45
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 5:
    to_value = (from_value - 32) / 1.8
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion_number == 6:
    to_value = from_value * 1.8 + 32
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')