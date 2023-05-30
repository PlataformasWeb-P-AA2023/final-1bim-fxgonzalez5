from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
parroquias = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == 'Matutina y Vespertina').all()

print('Consulta 1: Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"')
print("""\
+------------------------------------------+
| Parroquia                                | 
+------------------------------------------+\
""")
for parroquia in parroquias:
    print('{1}{0:42s}{1}'.format(parroquia.nombre,'|'))
print('+------------------------------------------+\n')


#* Consulta 2: Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
cantones = session.query(Canton).join(Parroquia).join(Establecimiento).filter(Establecimiento.nro_estudiantes.in_([448, 450, 451, 454, 458, 459])).all()

print('Consulta 2: Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459')
print("""\
+--------------------+
| Cantones           | 
+--------------------+\
""")
for canton in cantones:
    print('{1}{0:20s}{1}'.format(canton.nombre,'|'))
print('+--------------------+')
