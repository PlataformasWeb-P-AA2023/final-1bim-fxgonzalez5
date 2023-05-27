from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores
data = session.query(Establecimiento, Parroquia, Canton).join(Parroquia.canton).filter(Establecimiento.nro_docentes.in_([0, 5, 11]))
cantones = [d[2].nombre for d in data]

print('Consulta 1: Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores')
print("""\
+--------------------+
| Cantones           | 
+--------------------+\
""")
for canton in set(cantones):
    print('{1}{0:20s}{1}'.format(canton,'|'))
print('+--------------------+\n')


#* Consulta 2: Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
datos = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.nro_estudiantes >= 21).filter(Parroquia.nombre == "PINDAL").all()
establecimientos = [[d, d.parroquia] for d in datos]

print('Consulta 2: Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21')
print("""\
+----------------------------------------------------------------------------+
| Establecimiento                                                | Parroquia |
+----------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:64s}{2}{1:11s}{2}'.format(establecimiento[0].nombre, establecimiento[1].nombre, '|'))
print('+----------------------------------------------------------------------------+')
