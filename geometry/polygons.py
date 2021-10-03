from basic import Point2D, cross_product
from typing import List
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point


def sign(v: int) -> int:
    return 1 if v > 0 else (0 if v == 0 else -1)


def point_in_convex_polygon(point: Point2D, points: List[Point2D]):
    pass