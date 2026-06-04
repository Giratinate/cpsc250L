# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.


def clean_score(score_text):
    """
    Convert a score string into an integer.

    If the score is missing or invalid, return None.
    """
    e = score_text.strip()
    if e.isdigit():
        return int(e)
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
    che = []
    with open(filename, "r") as f:
        # Reads a line of open file
        for line in f:
            list1 = line.strip().split(",")
            if list1[0] == "name":
                continue
            score1 = (clean_score(list1[1]), clean_score(list1[2]), clean_score(list1[3]))
            dict1 = {"name": list1[0], "scores": score1, "average": calculate_average(score1)}
            print(dict1)
            che.append(dict1)
    return che


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
    pass


def print_student_report(records):
    """
    Print one line of output for each student.
    """
    pass


def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        class average
        highest average
        lowest average
    """
    pass


def main():
    filename = "../data/quiz_scores.csv"

    records = read_scores(filename)

    print_student_report(records)
    print()
    print_class_summary(records)

main()
