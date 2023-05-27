from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
data = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Establecimiento.jornada == 'Matutina y Vespertina').all()
parroquias = [d[1].nombre for d in data]

print('Consulta 1: Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"')
print("""\
+------------------------------------------+
| Parroquia                                | 
+------------------------------------------+\
""")
for parroquia in set(parroquias):
    print('{1}{0:42s}{1}'.format(parroquia,'|'))
print('+------------------------------------------+\n')


#* Consulta 2: Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
data = session.query(Establecimiento, Parroquia, Canton).join(Parroquia.canton).filter(Establecimiento.nro_estudiantes.in_([448, 450, 451, 454, 458, 459]))
cantones = [d[2].nombre for d in data]

print('Consulta 2: Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459')
print("""\
+--------------------+
| Cantones           | 
+--------------------+\
""")
for canton in set(cantones):
    print('{1}{0:20s}{1}'.format(canton,'|'))
print('+--------------------+')
