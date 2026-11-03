from src.employee import Employee
from src.shift import Shift
from src.optimizer import generate_schedule


def make_availability(monday=None):
    return {
        "monday": monday or [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }


def test_generate_schedule_assigns_required_roles():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    alex = Employee(
        "Alex",
        ["lifeguard", "supervisor"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        2,
        {
            "lifeguard": 1,
            "supervisor": 1
        }
    )

    result = generate_schedule(
        [connor, alex],
        [shift]
    )

    assert result is True
    assert shift in connor.assigned_shifts
    assert shift in alex.assigned_shifts

    assert connor.assigned_roles[shift] == "lifeguard"
    assert alex.assigned_roles[shift] == "supervisor"
