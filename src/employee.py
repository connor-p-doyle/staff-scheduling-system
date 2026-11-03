class Employee:
    def __init__(self,name, qualifications, max_hours, availability, assigned_shifts):
        self.name = name
        self.qualifications = qualifications
        self.max_hours = max_hours
        self.availability = availability
        self.assigned_shifts = assigned_shifts
        self.assigned_roles = {}
    def hours_worked(self):
        total = 0
        for shift in self.assigned_shifts:
            total += shift.duration()
        return total
def organize_employees(employee_info):
    employees_organized = {}
    for i, employee_instance,  in enumerate(employee_info):
        employees_organized[f"Employee {i + 1}"] = {"name": employee_instance.name,
                                                "qualifications": employee_instance.qualifications,
                                                "max hours": employee_instance.max_hours,
                                                "availability": employee_instance.availability,
                                                "assigned shifts": [
    {
        "day": shift.day,
        "start_time": shift.start_time,
        "end_time": shift.end_time
    }
    for shift in employee_instance.assigned_shifts
]}
    return employees_organized
