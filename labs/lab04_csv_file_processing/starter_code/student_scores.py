# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.

#This
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


def calculate_average(scores):
    """
    Calculate the average of a list of numeric scores.

    If the list is empty, return None.
    """
    avg = 0
    valid = 0
    for score in scores:
        if score is None:
            pass
        else:
            avg += score
            valid += 1
    if valid > 0:
        return avg / valid
    else:
        return None


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
    records = []
    with open(filename, "r") as f:
        # Reads a line of open file
        for line in f:
            list1 = line.strip().split(",")
            if list1[0] == "name":
                continue
            score1 = (clean_score(list1[1]), clean_score(list1[2]), clean_score(list1[3]))
            dict1 = {"name": list1[0], "scores": score1, "average": calculate_average(score1)}
            records.append(dict1)
    return records


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
    if average >= 87:
        return "A"
    elif average >= 77:
        return "B"
    elif average >= 67:
        return "C"
    elif average >= 57:
        return "D"
    elif average is None:
        return "N/A"
    else:
        return "F"


def print_student_report(records):
    """
    Print one line of output for each student.
    """
    for record in records:
        name = record["name"]
        avg = record["average"]
        grade = letter_grade(avg)
        print(f"{name}: Average = {avg:.2f} Grade = {grade}")

def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        class average
        highest average
        lowest average
    """
    students = 0
    highest = 0
    lowest = 200
    avg = 0
    for record in records:
        students += 1
        if record["average"] > highest:
            highest = record["average"]
        if record["average"] < lowest:
            lowest = record["average"]
        avg += record["average"]
    print(f"Number of students: {students}")
    print(f"Class average: {avg/students:.2f}")
    print(f"Highest average: {highest:.2f}")
    print(f"Lowest average: {lowest:.2f}")
    pass


def main():
    filename = "../data/quiz_scores.csv"

    records = read_scores(filename)

    print_student_report(records)
    print()
    print_class_summary(records)

main()
