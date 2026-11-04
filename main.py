from src.employee import Employee
from src.shift import Shift
from src.optimizer import generate_schedule

def display_schedule(employees, shifts):
    print("WEEKLY SCHEDULE\n")
    for shift in shifts:
        print(f"{shift.day} | {shift.start_time} - {shift.end_time}")
        for employee in employees:
            if shift in employee.assigned_shifts:
                print(f"{employee.name} - {employee.assigned_roles[shift]}")

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

if success:
    display_schedule(employees, shifts)
else:
    print("No valid schedule could be generated")



