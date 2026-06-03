def read_temperatures(filename):
    temperatures = []
    with open(filename, "r") as f:
        for line in f:
            if line != "\n":
                number = float(line.strip())
                temperatures.append(number)
    return temperatures

def calculate_average(values):
    return sum(values) / len(values)

def find_maximum(values):
    pass

def find_minimum(values):
    pass

def count_above_threshold(values, threshold):
    pass

def print_report(values):
    print("Temperature Report")
    print(f"Average: {calculate_average(values):.2f}")
    pass

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
