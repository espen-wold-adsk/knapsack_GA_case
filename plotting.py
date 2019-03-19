import matplotlib
import matplotlib.patches
import matplotlib.pyplot as plt


def plot_polygons_lines_and_points(
    blue_polygons=None, red_polygons=None, yellow_polygon=None, additional_polygons=None
):
    patches = [] if additional_polygons is None else additional_polygons
    if red_polygons is not None:
        patches += [_get_patch(polygon, "red") for polygon in red_polygons]

    if blue_polygons is not None:
        patches += [_get_patch(polygon, "blue") for polygon in blue_polygons]

    if yellow_polygon is not None:
        polygon = matplotlib.patches.Polygon(yellow_polygon, True, alpha=0.4, color="yellow")
        patches.append(polygon)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axis("auto")

    for patch in patches:
        ax.add_patch(patch)

    plt.axis("equal")

    plt.show()


def _get_patch(p, color):
    return matplotlib.patches.Polygon(p, True, alpha=0.4, color=color)
