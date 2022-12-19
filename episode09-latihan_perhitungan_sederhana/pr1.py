# fahrenheit to kelvin
print("\nPR KONVERSI FAHRENHEIT ke KELVIN\n")

# Fahrenheit to Kelvin

Fahrenheit = float(input('Masukkan suhu dalam Fahrenheit : '))

Kelvin = (Fahrenheit - 32) * (5/9) + 273

print('Kelvin : ', Kelvin, 'K')



# Kelvin to Fahrenheit

Kelvin = float(input('Masukkan suhu dalam Kelvin : '))

Fahrenheit = (Kelvin - 273) * (9/5) + 32

print('Fahrenheit : ', Fahrenheit, 'F')