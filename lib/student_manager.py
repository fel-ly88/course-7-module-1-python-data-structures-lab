class StudentManager:
    """
    A system to manage student records efficiently.
    Demonstrates lists, tuples, sets, comprehensions, and generator expressions.
    """
    
    def __init__(self):
        self.students = []
        
    def add_student(self,student_id, name, age, major, courses):
        """
        Returns(id, name) as a tuple for the given student_id.
        """
        for student in self.students:
            if student["id"] == student_id:
                return (student["id"], student["name"])
        return None
    
    def filter_by_major(self,major):
        return[s for s in self.students if s["age"] >= major]
    
    def filter_by_min_age(self,min_age):
        return[s for s in self.students if s["age"] >= min_age]
    
    def  get_unique_majors(self):
        return{s["major"] for s in self.students}
    

    def get_all_unique_courses(self):
        unique_courses = set()
        for s in self.students:
            unique_courses.update(s["courses"])
        return unique_courses


    def name_age_mapping(self):
        return {s["name"]: s["age"] for s in self.students}


    def average_age(self):
        if not self.students:
            return 0
        ages = (s["age"] for s in self.students)
        return sum(ages) / len(self.students)


if __name__ == "__main__":
    manager = StudentManager()

    manager.add_student(1, "Felister", 21, "Computer Science", ["Python", "Databases"])
    manager.add_student(2, "John", 23, "Data Science", ["Python", "Statistics"])
    manager.add_student(3, "Mary", 20, "Computer Science", ["Algorithms", "Python"])

    print("Unique Majors:", manager.get_unique_majors())
    print("Students 21+:", manager.filter_by_min_age(21))
    print("All Unique Courses:", manager.get_all_unique_courses())
    print("Name-Age Map:", manager.name_age_mapping())
    print("Average Age:", manager.average_age())