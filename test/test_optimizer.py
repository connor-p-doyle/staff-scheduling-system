import pytest
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


def test_generate_schedule_fails_without_required_qualification():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift = Shift(
        "Monday",
        9,
        13,
        1,
        {
            "supervisor": 1
        }
    )

    result = generate_schedule(
        [connor],
        [shift]
    )

    assert result is False
    assert shift not in connor.assigned_shifts

def test_generate_schedule_fails_when_max_hours_exceeded():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        6,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift_one = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    shift_two = Shift(
        "Monday",
        13,
        17,
        1,
        {"lifeguard": 1}
    )

    result = generate_schedule(
        [connor],
        [shift_one, shift_two]
    )

    assert result is False
    assert connor.assigned_shifts == []

def test_generate_schedule_fails_with_overlapping_shifts():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 17)]),
        []
    )

    shift_one = Shift(
        "Monday",
        9,
        13,
        1,
        {"lifeguard": 1}
    )

    shift_two = Shift(
        "Monday",
        12,
        16,
        1,
        {"lifeguard": 1}
    )

    result = generate_schedule(
        [connor],
        [shift_one, shift_two]
    )

    assert result is False
    assert connor.assigned_shifts == []

def test_generate_schedule_fails_when_employee_unavailable():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        20,
        make_availability(monday=[(9, 12)]),
        []
    )

    shift = Shift(
        "Monday",
        12,
        16,
        1,
        {"lifeguard": 1}
    )

    result = generate_schedule(
        [connor],
        [shift]
    )

    assert result is False
    assert connor.assigned_shifts == []

def test_generate_schedule_balances_employee_hours():
    connor = Employee(
        "Connor",
        ["lifeguard"],
        8,
        make_availability(monday=[(9, 17)]),
        []
    )

    alex = Employee(
        "Alex",
        ["lifeguard"],
        8,
        make_availability(monday=[(9, 17)]),
        []
    )

    shifts = [
        Shift("Monday", 9, 11, 1, {"lifeguard": 1}),
        Shift("Monday", 11, 13, 1, {"lifeguard": 1}),
        Shift("Monday", 13, 15, 1, {"lifeguard": 1}),
        Shift("Monday", 15, 17, 1, {"lifeguard": 1})
    ]

    result = generate_schedule(
        [connor, alex],
        shifts
    )

    assert result is True

    assert connor.hours_worked() == 4
    assert alex.hours_worked() == 4

    assert len(connor.assigned_shifts) == 2
    assert len(alex.assigned_shifts) == 2
