class Empleados:

  def __init__(self, nombre, apellido, edad, idiomas, nacionalidad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.idiomas = idiomas
    self.nacionalidad = nacionalidad

print("Datos del empleado:")

Taeil = Empleados("Taeil", "Moon", 28, "coreano", "coreano")
print(Taeil.nombre, Taeil.apellido)
print("-Edad:", Taeil.edad)
print("-Idiomas dominados:", Taeil.idiomas)
print("-Nacionalidad:", Taeil.nacionalidad, "\n")