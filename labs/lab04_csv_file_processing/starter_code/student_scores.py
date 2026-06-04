# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.

#This function converts the strings of scores into integers
def clean_score(score_text):
    """
    Convert a score string into an integer.

    If the score is missing or invalid, return None.
    """
    #First step is to strip any white space from the score
    score = score_text.strip()
    #If the score is a digit, then it is returned as an integer
    if score.isdigit():
        return int(score)
    #If the score is not an integer, then None is returned
    else:
        return None

#Calculates the average score from a list
def calculate_average(scores):
    """
    Calculate the average of a list of numeric scores.

    If the list is empty, return None.
    """
    sum = 0
    #counts valid scores
    valid = 0
    for score in scores:
        #If score is empty, then the function moves on
        if score is None:
            pass
        #If score is an int, then it is added to avg and the counter of valid scores goes up
        else:
            sum += score
            valid += 1
    #If there are valid scores, then the sum is divided by the number of valid scores and returned
    if valid > 0:
        return sum / valid
    #If there are no valid scores, then None is returned
    else:
        return None

#This function reads the file and returns a list of dictionaries with the students' records in it
def read_scores(filename):
    """
    Read student quiz scores from a CSV file.

    Return a list of dictionaries.

    Each dictionary should contain:
        "name": student name
        "scores": list of valid numeric quiz scores
        "average": student average

    So, the returned list of dictionaries should look like:
    [
        {
            "name": "Alice",
            "scores": [85, 90, 78],
            "average": 84.33
        },
        {
            "name": "Bob",
            "scores": [92, None, 88],
            "average": 90.0
        },
        ...
    ]
    """
    #List that will contain the dictionaries
    records = []
    #Opens file
    with open(filename, "r") as f:
        # Reads a line of open file
        for line in f:
            #Strips whitespace and splits the lines before turning them into a list
            list1 = line.strip().split(",")
            #Skips first line since it will start with "name"
            if list1[0] == "name":
                continue
            #Makes a list of scores, using the clean_score function to turn them into ints and Nones
            score1 = (clean_score(list1[1]), clean_score(list1[2]), clean_score(list1[3]))
            #Turns the list into a dictionary
            dict1 = {"name": list1[0], "scores": score1, "average": calculate_average(score1)}
            #Adds list to scores
            records.append(dict1)
    #returns the list
    return records

#Calculates a letter grade based on the average
def letter_grade(average):
    """
    Return a simple letter grade based on the average.

    Suggested scale:
        A: average >= 87
        B: average >= 77
        C: average >= 67
        D: average >= 57
        F: otherwise

    If the average is None, return "N/A".
    """
    #Goes through each minimum for a grade. If no minimum is met, then the letter returned is F
    if average >= 87:
        return "A"
    elif average >= 77:
        return "B"
    elif average >= 67:
        return "C"
    elif average >= 57:
        return "D"
    #If the Average is None, then the letter is N/A
    elif average is None:
        return "N/A"
    else:
        return "F"

#Prints out an individual report for each student
def print_student_report(records):
    """
    Print one line of output for each student.
    """
    #goes through each dictionary in the list
    for record in records:
        #Name, average, and letter are assigned before printing the report. This was necessary for formatting reasons.
        name = record["name"]
        avg = record["average"]
        grade = letter_grade(avg)
        #Prints out the report
        print(f"{name}: Average = {avg:.2f} Grade = {grade}")

#Prints out a report for the whole class
def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        class average
        highest average
        lowest average
    """
    #Declaration of variables
    #Students counts the number of students in the class
    students = 0
    #Highest counts the highes grade in the class
    highest = 0
    #Lowest counts the lowest grade in the class. There cannot be a lower high than 0 and a higher low than 100.
    lowest = 100
    #sum track of the total score before being divided by the number of students to get the average
    sum = 0
    #Goes through each record, adds a student to the total, checks to see if the average is a new high or low, and adds score to total
    for record in records:
        students += 1
        if record["average"] > highest:
            highest = record["average"]
        if record["average"] < lowest:
            lowest = record["average"]
        sum += record["average"]
    #Prints out the information
    print(f"Number of students: {students}")
    print(f"Class average: {sum/students:.2f}")
    print(f"Highest average: {highest:.2f}")
    print(f"Lowest average: {lowest:.2f}")
    pass

#Main function
def main():
    #Gets file
    filename = "../data/quiz_scores.csv"
    #Gets a list of dictionaries using the read_scores function
    records = read_scores(filename)
    #Calls student reports function
    print_student_report(records)
    print()
    #Calls class summary function
    print_class_summary(records)
#Calls Main function
main()
