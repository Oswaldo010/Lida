import os.path
import numpy as np


class Usuario:
  """
  Clase de usuario:
  @attrs:
    id:int
    nombre:str
    fecha_nac:str
    ciudad_nac:str
    direccion:str
    telefono:int
    email:str
  """

  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre

  # Métodos ID
  def set_id(self, id):
    self.id = id
    return f'id:{self.id}'

  def get_id(self):
    return f'{self.id}'

  # Métodos Nombre
  def set_nombre(self, nombre):
    self.nombre = nombre
    return f'nombre:{self.nombre}'

  def get_nombre(self):
    return f'{self.nombre}'

  # Métodos Fecha de Nacimiento
  def set_fecha_nacimiento(self, fecha_nac):
    fecha = Fecha(fecha_nac)
    fecha.definir_fecha()
    self.fecha_nac = fecha.__str__()
    return f'fecha nacimiento:{self.fecha_nac}'

  def get_fecha_nacimiento(self):
    return f'{self.fecha_nac}'

  # Métodos Ciudad de nacimiento
  def set_ciudad_nacimiento(self, ciudad_nac):
    self.ciudad_nac = ciudad_nac
    return f'ciudad nacimiento:{self.ciudad_nac}'

  def get_ciudad_nacimiento(self):
    return f'{self.ciudad_nac}'

  # Métodos Dirección
  def set_direccion(self, direccion):
    dir = Direccion(direccion)
    dir.definir_direccion()
    self.direccion = direccion.__str__()
    return f'direccion:{self.direccion}'

  def get_direccion(self):
    return f'{self.direccion}'

  # Métodos Teléfono
  def set_telefono(self, telefono:int):
    self.telefono = telefono
    return f'telefono:{self.telefono}'

  def get_telefono(self):
    return f'{self.telefono}'

  # Métodos Email
  def set_email(self, email:str):
    self.email = email
    return f'email:{self.email}'

  def get_email(self):
    return f'{self.email}'

  # Método String (toString)
  def __str__(self):
    info = 'USUARIO'
    for att, val in vars(self).items():
      info += '\n' + f'    {att}: {val}'
    return info


class Registro:
  """Arreglo de Usuarios, inicialmente un arreglo de None's."""

  num_registros = 0
  registro = []

  def __init__(self, capacidad):
    self.capacidad = capacidad

    # Llenar el arreglo de None's
    for i in range(capacidad):
      self.registro.append(None)

  def agregar(self, usuario, *args):
    # Verificar que hay espacio en el arreglo y el usuario no está registrado aún
    if (self.num_registros < self.capacidad) and (self.buscar_usuario(usuario.id) == None):
      # Añadir el usuario al arreglo
      self.registro[self.num_registros] = usuario
      self.num_registros += 1

      # Ordenar el arreglo por ID (menor a mayor)
      if self.num_registros > 1:
        i = self.num_registros - 1
        while (i > 0 and self.registro[i].id < self.registro[i-1].id):
          self.registro[i] = self.registro[i-1]
          self.registro[i-1] = usuario
          i -= 1
      return True
    else:
      return False

  def eliminar(self, id):
    indice = self.buscar_posicion(id)
    temporal = self.registro[indice]

    # Reacomodar los usuarios restantes
    for i in range(indice, self.num_registros - 1):
      self.registro[i] = self.registro[i+1]

    self.registro[self.num_registros-1] = None
    self.num_registros -= 1
    return temporal

  def buscar_posicion(self, id):
    if self.num_registros > 0:
      i = 0
      while (i < self.num_registros) and (self.registro[i].id != id):
        i += 1
      if i == self.num_registros:
        return -1
      else:
        return i
    else:
      return -1

  def buscar_usuario(self, id):
    if self.num_registros > 0:
      i = 0
      while i < self.num_registros and self.registro[i].id != id:
        i += 1
      if i == self.num_registros:
        return None
      else:
        return self.registro[i]
    else:
      return None

  def importar(self):
    registros_importados = np.array([])

    # Lectura del archivo .txt
    with open('Registros.txt', 'r') as file:
      lines = file.readlines()

      # Agregamos cada registro del archivo al array
      for line in lines:
        registros_importados = np.concatenate((registros_importados, np.array([line])))

      # Limpiamos el salto de linea luego de cada registro
      for i in range(len(registros_importados)-1):
        registros_importados[i] = registros_importados[i][:-1]
    file.close()

    # Separamos cada atributo de cada registro
    registros = np.array([])
    for i in range(len(registros_importados)):
      actual = np.array([])
      suma = 0
      for j in range(7):
        if j == 6:
          actual = np.concatenate((actual, np.array([registros_importados[i][suma+j:]])))
        else:
          actual = np.concatenate((actual, np.array([registros_importados[i][suma+j:registros_importados[i].find(";", suma+j)]])))
        suma += len(actual[-1])
      registros = np.concatenate((registros, actual))

    # Creamos instancias para los Usuarios importados
    # El arreglo registro se llena desde cero
    self.registro = []
    self.num_registros = 0
    self.__init__(self.capacidad)

    for i in range(len(registros_importados)):
      id = registros[i*7]
      id = int(id)

      # Completar la información del Usuario
      usuario = Usuario(id, registros[i*7+1])
      usuario.set_fecha_nacimiento(registros[i*7+2])
      usuario.set_ciudad_nacimiento(registros[i*7+3])
      usuario.set_direccion(registros[i*7+4])
      usuario.set_telefono(registros[i*7+5])
      usuario.set_email(registros[i*7+6])
      self.agregar(usuario)

  def exportar(self):
    # Verificar si el archivo ya existe
    if os.path.isfile("Registros.txt"):
      borrar_vacio = False
    else:
      borrar_vacio = True

    # Agrupamos los atributos del Usuario y lo guardamos en el .txt
    with open('Registros.txt', 'a+') as file:
      for i in range(self.num_registros):
        line = "\n"
        line += f'{self.registro[i].get_id()};'
        line += f'{self.registro[i].get_nombre()};'
        line += f'{self.registro[i].get_fecha_nacimiento()};'
        line += f'{self.registro[i].get_ciudad_nacimiento()};'
        line += f'{self.registro[i].get_direccion()};'
        line += f'{self.registro[i].get_telefono()};'
        line += f'{self.registro[i].get_email()}'
        file.write(line)
      file.close()

    if borrar_vacio:
      f = open("Registros.txt", "r")
      lineas = f.readlines()
      f.close()

      f = open("Registros.txt", "w")

      linea = lineas[0]
      lineas.remove(linea)
      for linea in lineas:
          f.write(linea)
      f.close()


class Fecha:
  """Ejemplo de salida: '20/08/03'."""

  def __init__(self, fecha:str):
    self.fecha = fecha
    self.fecha_array = np.array([])

  def definir_fecha(self):
    self.fecha_array = np.array([self.fecha[:self.fecha.find("/")],  #dia
                            self.fecha[self.fecha.find("/")+1:self.fecha.find("/", 4)],  #mes
                            self.fecha[self.fecha.find("/", 4)+1:]  #año
                            ])

  def get_dia(self):
    return self.fecha_array[0]

  def get_mes(self):
    return self.fecha_array[1]

  def get_anio(self):
    return self.fecha_array[2]

  def set_dia(self, dia):
    self.fecha_array[0] = dia

  def set_mes(self, mes):
    self.fecha_array[1] = mes

  def set_anio(self, anio):
    self.fecha_array[2] = anio

  def __str__(self):
    return f'{self.get_dia()}/{self.get_mes()}/{self.get_anio()}'


class Direccion:
  """Ejemplo de salida: 'Av.80 #65-223, Robledo, Medellin'."""

  def __init__(self, direccion:str):
    self.direccion = direccion
    self.direccion_array = ([])
    self.definir_direccion()

  def definir_direccion(self):
    self.direccion_array = np.array([self.direccion[:self.direccion.find(".")],  #calle
                                self.direccion[self.direccion.find(".")+1:self.direccion.find(" ")],  #numero_calle
                                self.direccion[self.direccion.find(" ")+1:self.direccion.find(",")],  #nomenclatura
                                self.direccion[self.direccion.find(",")+1:self.direccion.find(",", self.direccion.find(",")+1)],  #barrio
                                self.direccion[self.direccion.find(",", self.direccion.find(",")+1)+1:]  #ciudad
                                ])

  def get_calle(self):
    return self.direccion_array[0]

  def get_numero_calle(self):
    return self.direccion_array[1]

  def get_nomenclatura(self):
    return self.direccion_array[2]

  def get_barrio(self):
    return self.direccion_array[3]

  def get_ciudad(self):
    return self.direccion_array[4]

  def set_calle(self, calle):
    self.direccion_array[0] = calle

  def set_numero_calle(self, numero_calle):
    self.direccion_array[1] = numero_calle

  def set_nomenclatura(self, nomenclatura):
    self.direccion_array[2] = nomenclatura

  def set_barrio(self, barrio):
    self.direccion_array[3] = barrio

  def set_ciudad(self, ciudad):
    self.direccion_array[4] = ciudad

  def __str__(self):
    return f'{self.get_calle()} {self.get_numero_calle()} {self.get_nomenclatura()},{self.get_barrio()},{self.get_ciudad()}'
