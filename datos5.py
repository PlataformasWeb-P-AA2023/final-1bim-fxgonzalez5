from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores
establecimientos = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.nro_docentes > 100).order_by(Establecimiento.nro_estudiantes).all()

print('Consulta 1: Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores')
print("""\
+-----------------------------------------------------------------------------------------------------------+
| Establecimiento                                        | Cantidad de Estudiantes | Cantidad de Profesores |
+-----------------------------------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{3}{0:56s}{3}{1:>25d}{3}{2:>24d}{3}'.format(establecimiento.nombre, establecimiento.nro_estudiantes, establecimiento.nro_docentes, '|'))
print('+-----------------------------------------------------------------------------------------------------------+\n')


#* Consulta 2: Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores
establecimientos = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.nro_docentes > 100).order_by(Establecimiento.nro_docentes).all()

print('Consulta 2: Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores')
print("""\
+---------------------------------------------------------------------------------+
| Establecimiento                                        | Cantidad de Profesores |
+---------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:56s}{2}{1:>24d}{2}'.format(establecimiento.nombre, establecimiento.nro_docentes, '|'))
print('+---------------------------------------------------------------------------------+\n')