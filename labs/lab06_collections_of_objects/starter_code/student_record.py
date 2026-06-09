# Lab 6: Collections of Objects
#
# Complete this class. You may reuse ideas from Lab 5.


class StudentRecord:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        if score == None:
            self.scores.append(None)
        elif score > 100 or score < 0:
            True
        else:
            self.scores.append(score)
        pass

    def calculate_average(self):
        total = 0
        cnt = 0
        if len(self.scores) == 0:
            return None
        else:
            for score in self.scores:
                if score != None:
                    total += score
                    cnt += 1
        average = total / cnt
        return average

    def highest_score(self):
        high = 0
        if len(self.scores) == 0:
            return None
        else:
            high = self.scores[0]
            for score in self.scores:
                if score > high:
                    high = score
        return high

    def lowest_score(self):
        if len(self.scores) == 0:
            return None
        else:
            low = self.scores[0]
            for score in self.scores:
                if score < low:
                    low = score
        return low

    def letter_grade(self):
        average = self.calculate_average()
        if average >= 87:
            return "A"
        elif average >= 77:
            return "B"
        elif average >= 67:
            return "C"
        elif average >= 57:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"StudentRecord(name={self.name}, student_id={self.student_id}, scores={self.scores}"
