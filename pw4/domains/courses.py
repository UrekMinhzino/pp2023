class Courses:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Course(id='{self.id}', name='{self.name}')"