class Empleados:

  def __init__(self, nombre, apellido, edad, idiomas, nacionalidad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.idiomas = idiomas
    self.nacionalidad = nacionalidad

print("Datos del empleado:")

Taeil = Empleados("Taeil", "Moon", 25, "coreano", "coreano")
print(Taeil.nombre, Taeil.apellido)
print("-Edad:", Taeil.edad)
print("-Idiomas dominados:", Taeil.idiomas)
print("-Nacionalidad:", Taeil.nacionalidad, "\n")

Johnny = Empleados("Johnny", "Sunh", 28, "coreano, ingles, japones y español",
                   "americano")
print(Johnny.nombre, Johnny.apellido)
print("-Edad:", Johnny.edad)
print("-Idiomas dominados:", Johnny.idiomas)
print("-Nacionalidad:", Johnny.nacionalidad, "\n")

Taeyong = Empleados("Taeyong", "Lee", 27, "coreano, japones e ingles",
                    "coreano")
print(Taeyong.nombre, Taeyong.apellido)
print("-Edad:", Taeyong.edad)
print("-Idiomas dominados:", Taeyong.idiomas)
print("-Nacionalidad:", Taeyong.nacionalidad, "\n")