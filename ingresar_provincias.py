import pandas as pd
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from genera_tablas import Provincia

# Extracción de la data del csv y conversión a un diccionario de python
data = pd.read_csv("data/Listado-Instituciones-Educativas.csv", sep='|', dtype={'Código División Política Administrativa Provincia': str})

# Conexión a MySQL
Session = sessionmaker(bind=engine)
session = Session()

# Extracción de las provincias únicos
unique_values = data[['Código División Política Administrativa Provincia', 'Provincia']].drop_duplicates()
unique_values.reset_index(inplace=True, drop=True)

# Inserción de los registro en MySQL
for i in range(len(unique_values)):
    obj_provincia = Provincia(
        codigo = unique_values['Código División Política Administrativa Provincia'][i],
        nombre = unique_values['Provincia'][i],
    )

    session.add(obj_provincia)

# Confirmación de las transacciones
session.commit()