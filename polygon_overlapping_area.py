NUMERICAL_PRECISION_DISTANCE = 1e-13


class PolyLine:
    def __init__(self, start_point, end_point, x_diff, facing):
        self.slope = (end_point[1] - start_point[1]) / x_diff
        self.y_at_x_zero = start_point[1] - start_point[0] * self.slope
        self.start_x = start_point[0]
        self.end_x = end_point[0]
        self.facing = facing

    def get_y_at_x(self, x):
        return self.y_at_x_zero + self.slope * x


def _get_area_on_interval(start_x, end_x, active_lines):
    x_diff = end_x - start_x
    x_center = (end_x + start_x) / 2.0
    y_at_x_center = [[line.get_y_at_x(x_center), line.facing] for line in active_lines]
    y_at_x_center.sort()

    y_prev = None
    inside = 0
    area = 0
    for y, facing in y_at_x_center:
        if inside == 2:
            area += y - y_prev
        inside += facing
        y_prev = y
    return area * x_diff


def _get_active_lines_on_intervals(interest_points, sorted_lines):
    n = len(interest_points) - 1
    active_lines = [[] for _ in range(n)]
    interest_point_index = 0
    for line in sorted_lines:
        while interest_point_index < n and line.start_x > interest_points[interest_point_index]:
            interest_point_index += 1
        if interest_point_index >= n:
            break
        active_region_index = interest_point_index
        while active_region_index < n and line.end_x >= interest_points[active_region_index + 1]:
            active_lines[active_region_index].append(line)
            active_region_index += 1
    return active_lines


def _get_line_crossings(lines):
    n = len(lines)
    crossing_points = []
    for i in range(n - 1):
        line_1 = lines[i]
        for j in range(i + 1, n):
            line_2 = lines[j]

            if line_2.start_x > line_1.end_x - NUMERICAL_PRECISION_DISTANCE:
                break

            slope_diff = line_1.slope - line_2.slope
            if abs(slope_diff) < NUMERICAL_PRECISION_DISTANCE:
                continue

            x = (line_2.y_at_x_zero - line_1.y_at_x_zero) / slope_diff
            if (
                max(line_1.start_x, line_2.start_x) + NUMERICAL_PRECISION_DISTANCE
                < x
                < min(line_1.end_x, line_2.end_x) - NUMERICAL_PRECISION_DISTANCE
            ):
                crossing_points.append(x)
    crossing_points.sort()
    return crossing_points


def polygon_intersection_area(poly_1, poly_2):
    lines = _get_line_objects_from_polygon(poly_1)
    lines += _get_line_objects_from_polygon(poly_2)
    lines.sort(key=lambda line: line.start_x)

    interest_points = _get_interest_points(poly_1, poly_2)

    active_lines_on_intervals = _get_active_lines_on_intervals(interest_points, lines)
    crossing_points = _get_line_crossings(lines)
    number_of_line_crossings = len(crossing_points)

    area = 0
    crossing_index = 0

    for i in range(len(interest_points) - 1):
        start_x = interest_points[i]
        end_x = interest_points[i + 1]
        if end_x - start_x > NUMERICAL_PRECISION_DISTANCE:
            while (
                crossing_index < number_of_line_crossings
                and crossing_points[crossing_index] < end_x - NUMERICAL_PRECISION_DISTANCE
            ):
                crossing_point = crossing_points[crossing_index]
                crossing_index += 1
                if crossing_point - start_x > NUMERICAL_PRECISION_DISTANCE:
                    area += _get_area_on_interval(
                        start_x, crossing_point, active_lines_on_intervals[i]
                    )
                    start_x = crossing_point

            area += _get_area_on_interval(start_x, end_x, active_lines_on_intervals[i])
    return area


def _get_interest_points(poly_1, poly_2):
    interest_points_1 = [point[0] for point in poly_1]
    interest_points_2 = [point[0] for point in poly_2]
    min_x = max(min(interest_points_1), min(interest_points_2))
    max_x = min(max(interest_points_1), max(interest_points_2))
    interest_points = [
        point for point in interest_points_1 + interest_points_2 if min_x <= point <= max_x
    ]
    interest_points.sort()
    return interest_points


def _get_line_objects_from_polygon(poly):
    n = len(poly)

    lines = []
    start_corner = poly[-1]
    for i in range(n):
        end_corner = poly[i]

        x_diff = end_corner[0] - start_corner[0]
        if x_diff > NUMERICAL_PRECISION_DISTANCE:
            lines.append(PolyLine(start_corner, end_corner, x_diff, facing=1))
        elif x_diff < -NUMERICAL_PRECISION_DISTANCE:
            lines.append(PolyLine(end_corner, start_corner, -x_diff, facing=-1))
        start_corner = end_corner
    return lines
