# Staff Scheduling System
Workplace scheduling system that generates optimized weekly schedules based on employee availability, qualifications, shift requirements, and maximum hours.

The scheduler uses Google OR-Tools CP-SAT to find valid employee assignments while also satisfying all constraints and minimizing the maximum number of hours assigned to any employee.

## Features

- Generates employee-to-shift assignments.

- Adheres to employee availability.

- Prevents shift overlap.

- Follows employee maximum working hours.

- Matches employees to required qualifications.

- Assigns an exact role count for each shift.

- Enforces worker count.

- Detects when no valid schedule exists.

- Balances workloads to ensure fairness using an optimization objective.

- Includes automated tests.

## Project Structure

```text
staff-scheduling-system/
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── employee.py
│   ├── shift.py
│   ├── scheduler.py
│   └── optimizer.py
└── test/
    ├── test_scheduler.py
    └── test_optimizer.py
```

employee.py contains a class that represents each employee including information such as qualifications, availability, maximum hours, and assigned shifts.

shift.py defines all shift requirements including working times, required workers and required qualifications.

scheduler.py contains reusable schedule rules and constraints.

optimizer.py builds and solves a scheduling model using Google OR-Tools CP-SAT.

main.py provides example employee and shift data and displays a generated schedule.

## Installation 

Clone the repository and install required dependencies:

```bash
py -m pip install -r requirements.txt
```

## Running the Program

From project root:

```bash
py main.py
```

Example output:

```text
WEEKLY SCHEDULE

Monday | 9 - 13
Connor - lifeguard
Alex - supervisor
```

## Running Tests

Run full test suite with:

```bash
py -m pytest -v
```

The tests cover scheduling rules including availability, qualifications, maximum hours, overlap, role requirements, impossible schedules, and workload fairness.

## Technologies

 - Python
 
 - Google OR-Tools CP-SAT

 - pytest
