from .employee import Employee, organize_employees
from .shift import Shift, organize_shifts
# availability check
def is_available(employee, shift):
    day = shift.day.lower()
    for start, end in employee.availability[day]:
        if shift.start_time >= start and shift.end_time <= end:
            return True
    return False
# qualification check
def matching_qualifications(employee, shift):
    shift_qualifications = shift.required_qualifications
    relevant_qualifications = []
    for qual in employee.qualifications:
        if qual in shift_qualifications:
            relevant_qualifications.append(qual)
    return relevant_qualifications
# hours worked
def within_max_hours(employee, shift):
    return employee.hours_worked() + shift.duration() <= employee.max_hours
# shift overlap
def shifts_overlap(shift_a, shift_b):
    if shift_a.day.lower() != shift_b.day.lower():
        return False
    return (shift_a.start_time < shift_b.end_time and shift_a.end_time < shift_b.start_time)
def has_shift_conflict(employee, new_shift):
    for assigned_shift in employee.assigned_shifts:
        if shifts_overlap(assigned_shift, new_shift):
            return True
    return False

# shift qualification check
def can_work_shift(employee, shift):
    return matching_qualifications(employee, shift) != [] and is_available(employee, shift) and within_max_hours(employee, shift) and not has_shift_conflict(employee, shift)

# assign shifts
def assign_shift(employee, shift):
    if can_work_shift(employee, shift):
        employee.assigned_shifts.append(shift)
        return True
    return False
