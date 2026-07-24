def cel_to_fahr(celsius_temp):
    return celsius_temp * 1.8 + 32


celsius_temp_string = input("Enter celsius value: ")

celsius_temp = float(celsius_temp_string)

fahrenheit_temp = cel_to_fahr(celsius_temp)

print(f"{fahrenheit_temp:.1f}°F")
