from student_record import StudentRecord

def clean_score(score_text):
    """
    Convert score text to an integer.

    Return None if the score is missing or invalid.
    """
    score = score_text.strip()
    # If the score is a digit, then it is returned as an integer
    if score.isdigit():
        return int(score)
    # If the score is not an integer, then None is returned
    else:
        return None


def read_student_records(filename):
    """
    Read the CSV file and return a list of StudentRecord objects.
    """
    records = []
    # Opens file
    with open(filename, "r") as f:
        # Reads a line of open file
        for line in f:
            # Strips whitespace and splits the lines before turning them into a list
            list1 = line.strip().split(",")
            # Skips first line since it will start with "name"
            if list1[1] == "name":
                continue
            # Makes a list of scores, using the clean_score function to turn them into ints and Nones
            score1 = (clean_score(list1[2]), clean_score(list1[3]), clean_score(list1[4]))
            # Turns the list into a dictionary
            record = StudentRecord(list1[1], list1[0])
            for score in score1:
                record.add_score(score)
            # Adds list to scores
            records.append(record)
    # returns the list
    return records

    pass


def class_average(students):
    """
    Return the average of all student averages.

    Ignore students with no valid scores.
    """
    class_sum = 0
    for student in students:
        class_sum += student.calculate_average()
    class_avg = class_sum / len(students)
    return class_avg


def find_highest_average_student(students):
    """
    Return the StudentRecord object with the highest average.
    """
    pass


def find_lowest_average_student(students):
    """
    Return the StudentRecord object with the lowest average.
    """
    pass


def print_class_report(students):
    """
    Print all student records and a class summary.
    """
    for student in students:
        print(student)
    print(f"Class average: {class_average(students):.2f}")
    pass


def main():
    students = read_student_records("../data/student_scores.csv")
    print_class_report(students)


main()
