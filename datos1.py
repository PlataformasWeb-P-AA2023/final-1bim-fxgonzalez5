from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import *

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# ----------- Consultas a la Base de Datos -----------
#* Consulta 1: Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553
establecimientos = session.query(Establecimiento).filter(Establecimiento.parroquia_id == '110553').all()

print('Consulta 1: Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553')
print("""\
+----------------------------------------------------------------------------------------------------------+
| Establecimiento                                      | Código División Política Administrativa Parroquia |
+----------------------------------------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:54s}{2}{1:>51s}{2}'.format(establecimiento.nombre, establecimiento.parroquia_id, '|'))
print('+----------------------------------------------------------------------------------------------------------+\n')

#* Consulta 2: Todos los establecimientos de la provincia del Oro
datos = session.query(Establecimiento).join(Parroquia).join(Canton).join(Provincia).filter(Provincia.nombre == 'EL ORO').all()
establecimientos = [[d, d.parroquia.canton.provincia] for d in datos]

print('Consulta 2: Todos los establecimientos de la provincia del Oro')
print("""\
+--------------------------------------------------------------+
| Establecimiento                                  | Provincia |
+--------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:50s}{2}{1:11s}{2}'.format(establecimiento[0].nombre, establecimiento[1].nombre, '|'))
print('+--------------------------------------------------------------+\n')

#* Consulta 3: Todos los establecimientos del cantón de Portovelo
establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre == 'PORTOVELO').all()

print('Consulta 3: Todos los establecimientos del cantón de Portovelo') 
print("""\
+--------------------------------------------------------+
| Establecimiento                              | Cantón  |
+--------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:46s}{2}{1:8s}{2}'.format(establecimiento.nombre, establecimiento.parroquia.canton.nombre, '|'))
print('+---------------------------parroquia-----------------------------+')

#* Consulta 4: Todos los establecimientos del cantón de Zamora
datos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(Canton.nombre == 'ZAMORA').all()
establecimientos = [[d, d.parroquia.canton] for d in datos]

print('Consulta 4: Todos los establecimientos del cantón de Zamora')
print("""\
+-----------------------------------------------------------------------------+
| Establecimiento                                                    | Cantón |
+-----------------------------------------------------------------------------+\
""")
for establecimiento in establecimientos:
    print('{2}{0:68s}{2}{1:8s}{2}'.format(establecimiento[0].nombre, establecimiento[1].nombre, '|'))
print('+-----------------------------------------------------------------------------+')