import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from configuracion import engine
from genera_tablas import Canton, Parroquia

# Extracción de la data del csv y conversión a un diccionario de python
data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", sep='|', dtype={'Código División Política Administrativa  Cantón': str, 'Código División Política Administrativa  Parroquia': str})

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# Extracción de las parroquias únicos
unique_values = data[['Código División Política Administrativa  Parroquia', 'Parroquia', 'Código División Política Administrativa  Cantón']].drop_duplicates()
unique_values.reset_index(inplace=True, drop=True)

# Inserción de los registro en MySQL
for i in range(len(unique_values)):
    cod_canton = unique_values['Código División Política Administrativa  Cantón'][i]

    try:
        obj_canton = session.query(Canton).filter_by(codigo = cod_canton).one()
        obj_parroquia = Parroquia(
            codigo = unique_values['Código División Política Administrativa  Parroquia'][i],
            nombre = unique_values['Parroquia'][i],
            canton = obj_canton
        )

        session.add(obj_parroquia)
    except NoResultFound:
        print('No existe el cantón con código %s' % (cod_canton))

# Confirmación de las transacciones
session.commit()