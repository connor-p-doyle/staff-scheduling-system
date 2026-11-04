# staff-scheduling-system
Workplace scheduling system that generates optimized weekly schedules based on employee availability, qualifications, shift requirements, and maximum hours.

The scheduler uses Google OR-Tools CP-SAT to find valid employee assignments while also satisfiying all constraints and minimizing the maximum number of hours assigned to each employee.

# Features

Generates employee-to-shift assignments.

Adheres to employee availability.

Prevents shift overlap.

Follows employee maximum working hours.

Matches employees required qualifications.

Assigns an exact role count for each shift
Enforces worker count.

Detects when no valid shifts exist.

Balances workloads to ensure fairness using an optimization objective.

Includes automated tests.

# Structure

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
employee.py contains a class that reperesents each employee including information such as qualifications, availability, maximum hours, and assigned shifts.

shift.py defines all shift requirements includig working times, required workers and required qualifications.

scheduler.py containes reusable shedule rules and constraints.

optimizer.py builds and solves a scheduling model using Google OR-Tools CP-Sat.

main.py provides example employee and shift data and displays a generated schedule.
