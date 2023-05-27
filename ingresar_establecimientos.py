import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from configuracion import engine
from genera_tablas import Parroquia, Establecimiento

# Extracción de la data del csv y conversión a un diccionario de python
data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", sep='|', dtype={'Código AMIE': str, 'Código División Política Administrativa  Parroquia': str, 'Código de Distrito': str})

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# Inserción de los registro en MySQL
for i in range(len(data)):
    cod_parroquia = data['Código División Política Administrativa  Parroquia'][i]

    try:
        obj_parroquia = session.query(Parroquia).filter_by(codigo = cod_parroquia).one()
        obj_establecimiento = Establecimiento(
            codigo = data['Código AMIE'][i],
            nombre = data['Nombre de la Institución Educativa'][i],
            distrito = data['Código de Distrito'][i],
            sostenimiento = data['Sostenimiento'][i],
            tipo_educacion = data['Tipo de Educación'][i],
            modalidad = data['Modalidad'][i],
            jornada = data['Jornada'][i],
            acceso = data['Acceso (terrestre/ aéreo/fluvial)'][i],
            nro_estudiantes = int(data['Número de estudiantes'][i]),
            nro_docentes = int(data['Número de docentes'][i]),
            parroquia = obj_parroquia
        )

        session.add(obj_establecimiento)
    except NoResultFound:
        print('No existe la parroquia con código %s' % (cod_parroquia))

# # Confirmación de las transacciones
session.commit()