import math


class Vector3D:

    # Modulo
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __len__(self):
        return self.length()

    # Suma de vectores
    def add(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y
        self.z = self.z + v.z

    # Resta de vectores
    def sub(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
        self.z = self.z - v.z

    # Multiplicacion escalar
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    # Normalizar
    def normalize(self):
        l = self.length()
        if l == 0:
            return
        self.x = self.x / l
        self.y = self.y / l
        self.z = self.z / l

    # Producto vectorial
    def cross(self, v):
        u = Vector3D()
        u.x = self.y * v.z - self.z * v.y
        u.y = self.z * v.x - self.x * v.z
        u.z = self.x * v.y - self.y * v.x
        return u

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z)+">"

    def __init__(self, v=None, x=None, y=None, z=None):
        if v is None and not x and not y and not z:
            # New vector
            self.x = self.y = self.z = 0.0
        elif v is not None:
            # From another vector
            self.x = v.x
            self.y = v.y
            self.z = v.z
        elif x or y or z:
            # By coordinates
            if x:
                self.x = x
            else:
                self.x = 0.0
            if y:
                self.y = y
            else:
                self.y = 0.0
            if z:
                self.z = z
            else:
                self.z = 0.0
