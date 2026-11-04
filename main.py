from src.employee import Employee
from src.shift import Shift
from src.optimizer import generate_schedule


connor_availability = {
    "monday": [(9, 17)],
    "tuesday": [(13, 21)],
    "wednesday": [],
    "thursday": [(9, 17)],
    "friday": [(9, 13)],
    "saturday": [],
    "sunday": []
}
alex_availability = {
    "monday": [(9, 17)],
        "tuesday": [(10, 21)],
        "wednesday": [(2, 14)],
        "thursday": [(9, 17)],
        "friday": [(9, 13)],
        "saturday": [(2, 23)],
        "sunday": []
}
employees = [
    Employee(
        "Connor",
        ["lifeguard"],
        20,
        connor_availability,
        []
    ),
    Employee(
        "Alex",
        ["lifeguard", "supervisor"],
        20,
        alex_availability,
        []
    )
]

shifts = [
    Shift(
        "Monday",
        9,
        13,
        2,
        {
            "lifeguard": 1,
            "supervisor": 1
        }
    )
]

success = generate_schedule(employees, shifts)

print(success)

def display_schedule(employees, shifts):
    print("WEEKLY SCHEDULE\n")
    for shift in shifts:
        print(f"{shift.day} | {shift.start_time} - {shift.end_time}")
        for employee in employees:
            for x in employee.assigned_shifts:
                if x.day.lower() == shift.day.lower():
                    print(f"{employee.name} - {employee.assigned_roles[shift]}")
display_schedule(employees, shifts)
