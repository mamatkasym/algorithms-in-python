class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def cross_product(a: Point2D, b: Point2D):
    return a.x * b.y - a.y * b.x


def cross(a: Point3D, b: Point3D) -> Point3D:
    return Point3D(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
