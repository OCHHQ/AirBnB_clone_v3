#!/usr/bin/env python3
from models import storage
from models.state import State

print("All objects:", storage.all())
print("States:", storage.all(State))

# Try to access the list directly to see if it's empty
all_states = list(storage.all(State).values())
print("All states list:", all_states)

if all_states:
    first_state_id = all_states[0].id
    print("First state ID:", first_state_id)
else:
    print("No states found.")
