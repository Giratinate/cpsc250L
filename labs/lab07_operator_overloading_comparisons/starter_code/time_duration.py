# Lab 7: Operator Overloading and Object Comparisons


class TimeDuration:
    def __init__(self, hours, minutes, seconds):
        """
        Store a time duration.

        You may assume the input values are non-negative integers.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self):
        """
        Return the total number of seconds represented by this duration.
        """
        total_seconds = 0
        total_seconds += self.hours * 3600 + self.minutes * 60 + self.seconds
        return total_seconds

    def __str__(self):
        """
        Return a readable string such as:
            1h 05m 09s
        """
        return f"{self.hours}h {self.minutes:02d}m {self.seconds:02d}s"

    def __eq__(self, other):
        """
        Return True if two TimeDuration objects represent the same duration.
        """
        if other.total_seconds() == self.total_seconds():
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Return True if this duration is shorter than the other duration.
        """
        if other > self.total_seconds():
            return True
        else:
            return False

    def __add__(self, other):
        """
        Return a new TimeDuration object that is the sum of this duration and the other duration.
        """
        return TimeDuration(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
