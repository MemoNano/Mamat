from math import pi


class CriticalExam:
    """Common base class for critical tests."""

    def test_circle_area(r):
        return pi * (r ** 2)

    # Test function
    radii = [3, 0, -3, 2 + 5j, True, "radius"]
    message = "Area of circle with radius = {radius} is {area}."
