class Plant:
    def __init__(self, name, height_cm=20):
        self.name = name
        self.height_cm = height_cm

    def care_instructions(self):
        return "Water regularly and provide adequate sunlight."

    def __str__(self):
        return f"Name: {self.name}; Height {self.height_cm}cm"


class Flower(Plant):
    def __init__(self, name, height_cm=30, color="Green"):
        self.name = name
        self.height_cm = height_cm
        self.color = color

    def care_instructions(self):
        return "Water regularly, provide full sun, and deadhead spent blooms."

    def __str__(self):
        return f"Name: {self.name}; Height: {self.height_cm}cm; Color: {self.color}"


class Vegetable(Plant):
    def __init__(self, name, height_cm=10, harvest_days=90):
        self.name = name
        self.height_cm = height_cm
        self.harvest_days = harvest_days

    def care_instructions(self):
        return "Water regularly, provide full sun, and fertilize every two weeks."

    def __str__(self):
        return f"Name: {self.name}; Height: {self.height_cm}cm; Growing time: {self.harvest_days} days"
