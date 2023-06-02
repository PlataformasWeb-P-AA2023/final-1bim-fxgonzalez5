from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores
cantones = session.query(Canton).join(Parroquia).join(Establecimiento).filter(Establecimiento.nro_docentes.in_([0, 5, 11])).all()

print('Consulta 1: Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores')
print("""\
+--------------------+
| Cantones           | 
+--------------------+\
""")
for canton in set(cantones):
    print('{1}{0:20s}{1}'.format(canton.nombre,'|'))
print('+--------------------+\n')


#* Consulta 2: Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
datos = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.nro_estudiantes >= 21).filter(Parroquia.nombre == "PINDAL").all()
establecimientos = [[d, d.parroquia, d.parroquia.canton, d.parroquia.canton.provincia] for d in datos]

print('Consulta 2: Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21')
print("""\
+-------------------------------------------------------------------------------------------------+
| Establecimiento                                                | Parroquia | Cantón | Provincia |
+-------------------------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{4}{0:64s}{4}{1:11s}{4}{2:8s}{4}{3:11s}{4}'.format(establecimiento[0].nombre, establecimiento[1].nombre, establecimiento[2].nombre, establecimiento[3].nombre, '|'))
print('+-------------------------------------------------------------------------------------------------+')

