# Trabajo Final Primer Bimestre

## Uso de SqlAlchemy

Dada la información de la carpeta ***data***. Realizar las siguientes tareas:

* Analizar el contenido

* Identificar las posibles entidades que se puedan generar

* La base de datos que se debe usar es mysql; el nombre de la base de datos es **final1bimaa22**

* Las entidades deben satisfacer lo siguiente:
	* Un establecimiento tiene características propias.
	* Un establecimiento pertenece a una parroquia.
	* Una parroquia pertenece a un cantón.
	* Un cantón pertenece a un provincia.

* Generar un proceso de generación de entidades a través de SqlAlchemy.
	* genera_tablas.py

* Ingresar la información en cada entidad creada.
	* ingresa_provincias.py
	* ingresa_cantones.py
	* ingresa_parroquias.py
	* ingresa_establecimientos.py

* Generar las siguientes consultas:
	* datos1.py
		* Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 110553
		* Todos los establecimientos de la provincia del Oro.
		* Todos los establecimientos del cantón de Portovelo.
		* Todos los establecimientos del cantón de Zamora.
	* datos2.py
    	* Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
	* datos3.py
		* Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
		* Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
	* datos4.py
			* Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.

	* datos5.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
