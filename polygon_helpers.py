import numpy as np


def polygon_area(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def rotate(polygon, angle):
    centroid = get_centroid(polygon)
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)

    org_from_centroid_vectors = [(p[0] - centroid[0], p[1] - centroid[1]) for p in polygon]
    new_points = [
        (
            centroid[0] + v[0] * cos_angle - v[1] * sin_angle,
            centroid[1] + v[0] * sin_angle + v[1] * cos_angle,
        )
        for v in org_from_centroid_vectors
    ]
    return new_points


def get_centroid(polygon):
    avg = lambda x: sum(x) / float(len(x))
    centroid = map(avg, zip(*polygon))
    return centroid


def translate(polygon, translation_vector):
    return [(p[0] + translation_vector[0], p[1] + translation_vector[1]) for p in polygon]
