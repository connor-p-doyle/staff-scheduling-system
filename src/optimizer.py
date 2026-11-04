from ortools.sat.python import cp_model

from .scheduler import is_available, shifts_overlap

def generate_schedule(employees, shifts):
    model = cp_model.CpModel()
    assigned = {}
    for x in range(len(employees)):
        for y in range(len(shifts)):
            assigned[x, y] = model.new_bool_var(f"Assigned_{x}_{y}")

    for y in range(len(shifts)):
        model.add(sum(assigned[x,y] for x in range(len(employees))) == shifts[y].required_workers)

    for x in range(len(employees)):
        for y in range(len(shifts)):
            if not is_available(employees[x], shifts[y]): 
                model.add(assigned[x, y] == 0)

    for x in range(len(employees)):
        model.add(sum(assigned[x, y] * shifts[y].duration() for y in range(len(shifts))) <= employees[x].max_hours)

    for x in range(len(employees)):
        for first_shift in range(len(shifts)):
            for second_shift in range(first_shift + 1, len(shifts)):
                shift_a = shifts[first_shift]
                shift_b = shifts[second_shift]

                if shifts_overlap(shift_a, shift_b):
                    model.add(assigned[x, first_shift] + assigned[x, second_shift] <= 1)
    role_assigned = {}

    for x in range(len(employees)):
        for y in range(len(shifts)):
            for qualification in shifts[y].required_qualifications:
                role_assigned[x,y, qualification] = model.new_bool_var(f"Role_{x}_{y}_{qualification}")

    for x in range(len(employees)):
        for y in range(len(shifts)):
            for qualification in shifts[y].required_qualifications:
                if qualification not in employees[x].qualifications:
                    model.add(role_assigned[x,y, qualification] == 0)
    
    for x in range(len(employees)):
        for y in range(len(shifts)):
            model.add(sum(role_assigned[x,y, qualification] for qualification in shifts[y].required_qualifications) == assigned[x, y])

    for y in range(len(shifts)):
        for qualification, required_count in shifts[y].required_qualifications.items():
            model.add(sum(role_assigned[x, y, qualification] for x in range(len(employees))) == required_count)

    employee_hours = {}

    for x in range(len(employees)):
        employee_hours[x] = model.new_int_var(0, employees[x].max_hours, f"Hours_{x}")
        model.add(employee_hours[x] == sum(assigned[x, y] * shifts[y].duration() for y in range(len(shifts))))
        
    solver = cp_model.CpSolver()

    status = solver.solve(model)

    if status not in(cp_model.FEASIBLE, cp_model.OPTIMAL):
        return False
    for x in range(len(employees)):
        for y in range(len(shifts)):
            if solver.value(assigned[x, y]) == 1:
                employees[x].assigned_shifts.append(shifts[y])
                for qualification in shifts[y].required_qualifications:
                    if solver.value(role_assigned[x, y, qualification]) == 1:
                        employees[x].assigned_roles[shifts[y]] = qualification
    return True
