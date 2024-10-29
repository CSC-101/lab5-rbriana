import math
from typing import Optional

import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:data.Time, time2:data.Time) -> data.Time:
    total_seconds = time1.second + time2.second
    minutes, second = divmod(total_seconds, 60)
    total_minutes = time1.minute + time2.minute + minutes
    hours_extra, minutes = divmod(total_minutes, 60)
    hours = time1.hour + time2.hour + hours_extra
    return data.Time(hour = hours, minute = minutes, second = second)

# Part 4
def is_descending(lst:list[float]) -> bool:
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False
    return True

# Part 5
def largest_between(lst:list[int], lower:int, upper:int) -> Optional[int]:
    if lower > upper:
        return None
    lower = max(0, lower)
    upper = min(len(lst) - 1, upper)
    max_idx = None
    max_value = float('-inf')
    for i in range(lower, upper + 1):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i
    return max_idx

# Part 6
def furthest_from_origin(points: list[data.Point]) -> Optional[int]:
    if not points:
        return None
    max_idx = 0
    max_dist = points[0].distance_from_origin()

    for i, point in range(1, len(points)):
        distance = points[i].distance_from_origin()
        if distance > max_dist:
            max_dist = distance
            max_idx = i

    return max_idx