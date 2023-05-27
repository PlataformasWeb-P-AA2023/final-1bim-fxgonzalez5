from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación
datos = session.query(Establecimiento).join(Parroquia).filter(Establecimiento.nro_docentes > 40).filter(Establecimiento.tipo_educacion == 'Educación regular').order_by(Parroquia.nombre).all()
establecimientos = [[d, d.parroquia ]for d in datos]

print('Consulta 1: Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación')
print("""\
+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Establecimiento                                         | Parroquia                                | Cantidad de Profesores | Tipo de Educación |
+-------------------------------------------------------------------------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{4}{0:57s}{4}{1:42s}{4}{2:>12d}{4:>13s}{3:19s}{4}'.format(establecimiento[0].nombre, establecimiento[1].nombre, establecimiento[0].nro_docentes, establecimiento[0].tipo_educacion, '|'))
print('+-------------------------------------------------------------------------------------------------------------------------------------------------+\n')


#* Consulta 2: Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04
establecimientos = session.query(Establecimiento).filter(Establecimiento.distrito == '11D04').order_by(Establecimiento.sostenimiento).all()

print('Consulta 2: Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04')
print("""\
+--------------------------------------------------------------------------------------------+
| Establecimiento                                                 | Distrito | Sostenimiento |
+--------------------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{3}{0:65s}{3}{1:>8s}{3:>3s}{2:15s}{3}'.format(establecimiento.nombre, establecimiento.distrito, establecimiento.sostenimiento, '|'))
print('+--------------------------------------------------------------------------------------------+\n')