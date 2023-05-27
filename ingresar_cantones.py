import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from configuracion import engine
from genera_tablas import Provincia, Canton

# Extracción de la data del csv y conversión a un diccionario de python
data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", sep='|', dtype={'Código División Política Administrativa Provincia': str, 'Código División Política Administrativa  Cantón': str})

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# Extracción de los cantones únicos
unique_values = data[['Código División Política Administrativa  Cantón', 'Cantón', 'Código División Política Administrativa Provincia']].drop_duplicates()
unique_values.reset_index(inplace=True, drop=True)

# Inserción de los registro en MySQL
for i in range(len(unique_values)):
    cod_provincia = unique_values['Código División Política Administrativa Provincia'][i]
    
    try:
        obj_provincia = session.query(Provincia).filter_by(codigo = cod_provincia).one()
        obj_canton = Canton(
            codigo = unique_values['Código División Política Administrativa  Cantón'][i],
            nombre = unique_values['Cantón'][i],
            provincia = obj_provincia
        )

        session.add(obj_canton)
    except NoResultFound:
        print('No existe la provincia con código %s' % (cod_provincia))

# Confirmación de las transacciones
session.commit()