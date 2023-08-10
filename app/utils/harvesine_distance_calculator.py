from cmath import cos, sin, sqrt
from math import atan2, radians

"""
    Haversine distance calculator.
    Used to determine distance between two points in x/y space.
"""


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    R = 6371.0  # Earth's radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    # c = 2 * atan2(sqrt(a), sqrt(1 - a))
    c = 2 * atan2(sqrt(a), sqrt(max(0, 1 - a)))
    distance = R * c
    return distance
