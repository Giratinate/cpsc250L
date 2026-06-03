# This function reads the list of temperatures from a file
def read_temperatures(filename):
    # Creation of temperature list
    temperatures = []
    # Opens file
    with open(filename, "r") as f:
        # Reads a line of open file
        for line in f:
            # Checks that line is not empty
            if line != "\n":
                # If line is not empty, it will read the line and add it to the temperatures list
                number = float(line.strip())
                temperatures.append(number)
    # Returns temperatures
    return temperatures

# Calculates the average
def calculate_average(values):
    # Returns the average by dividing the sum of the values with the length of the list
    return sum(values) / len(values)

# This function finds and returns the maximum in the list
def find_maximum(values):
    return max(values)

# This function finds and returns the minimum in the list
def find_minimum(values):
    return min(values)

# This functions counts the number of values above a certain threshold and returns the count
def count_above_threshold(values, threshold):
    # Creation of count
    cnt = 0
    # Goes through each number in list
    for value in values:
        # If a value is above the threshold, the count goes up by 1
        if value > threshold:
            cnt = cnt + 1
    # Returns count
    return cnt

# This function prints out a formatted report for the temperature list provided
def print_report(values):
    print("Temperature Report")
    print("------------------")
    print(f"Average temperature: {calculate_average(values):.2f}")
    print(f"Maximum temperature: {find_maximum(values):.2f}")
    print(f"Minimum temperature: {find_minimum(values):.2f}")
    print(f"Temperatures above 80: {count_above_threshold(values, 80)}")
    # No value returned
    pass

# Main function
def main():
    # Calls both the text file with the temperatures and the function that turns the values into a list
    temperatures = read_temperatures("../data/june_temperatures.txt")
    # Calls the function that prints the temperature report
    print_report(temperatures)

# Calls main function
main()
