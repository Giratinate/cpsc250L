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
    return max(values)

def find_minimum(values):
    return min(values)

def count_above_threshold(values, threshold):
    cnt = 0
    for value in values:
        if value > threshold:
            cnt = cnt + 1
    return cnt

def print_report(values):
    print("Temperature Report")
    print(f"Average: {calculate_average(values):.2f}")
    print(f"Maximum: {find_maximum(values):.2f}")
    print(f"Minimum: {find_minimum(values):.2f}")
    print(f"Count: {count_above_threshold(values, 75):.2f}")
    pass

def main():
    temperatures = read_temperatures("../data/june_temperatures.txt")
    print_report(temperatures)

main()
