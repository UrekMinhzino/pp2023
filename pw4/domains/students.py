class Students:
    def __init__(self, id: str, name: str, dob: int):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.credits = {}
        self.gpa = None

    def __repr__(self):
        return f"Student(id='{self.id}', name='{self.name}', dob={self.dob}, marks={self.marks}, credits={self.credits}, gpa={self.gpa})"
