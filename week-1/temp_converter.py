def cel_to_fahr(celsius_temp: float) -> float:
    return celsius_temp * 1.8 + 32


def main():
    celsius_temp_string: str = input("Enter celsius value: ")
    celsius_temp: float = float(celsius_temp_string)
    fahrenheit_temp: float = cel_to_fahr(celsius_temp)
    print(f"{fahrenheit_temp:.1f}°F")
