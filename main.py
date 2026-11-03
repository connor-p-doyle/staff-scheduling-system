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

for employee in employees:
    print(employee.name)

    for shift in employee.assigned_shifts:
        print(shift.day ,shift.start_time, shift.end_time, employee.assigned_roles[shift])
