from configuracion import engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()    

class Provincia(Base):
    __tablename__ = 'provincia'

    codigo = Column(String(2), primary_key=True, autoincrement=False)
    nombre = Column(String(100))
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigo=%s, nommbre=%s" % (self.codigo, self.nombre)


class Canton(Base):
    __tablename__ = 'canton'

    codigo = Column(String(4), primary_key=True, autoincrement=False)
    nombre = Column(String(100))
    provincia_id = Column(String(2), ForeignKey('provincia.codigo'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigo=%s, nommbre=%s, provincia_id=%s" % (self.codigo, self.nombre, self.provincia.codigo)


class Parroquia(Base):
    __tablename__ = 'parroquia'

    codigo = Column(String(6), primary_key=True, autoincrement=False)
    nombre = Column(String(100))
    canton_id = Column(String(4), ForeignKey('canton.codigo'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return "Parroquia: codigo=%s, nommbre=%s, canton_id=%s" % (self.codigo, self.nombre, self.canton.codigo)


class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    codigo = Column(String(8), primary_key=True, autoincrement=False)
    nombre = Column(String(200))
    distrito = Column(String(10))
    sostenimiento = Column(String(20))
    tipo_educacion = Column(String(35))
    modalidad = Column(String(75))
    jornada = Column(String(75))
    acceso = Column(String(15))
    nro_estudiantes = Column(Integer)
    nro_docentes = Column(Integer)
    parroquia_id = Column(String(6), ForeignKey('parroquia.codigo'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "Establecimiento: codigo=%s, nommbre=%s, distrito=%s, sostenimiento=%s, tipo_educacion=%s, modalidad=%s, jornada=%s, acceso=%s, nro_estudiantes=%d, nro_docentes=%d, parroquia_id=%s" % (
            self.codigo, self.nombre, self.distrito, self.sostenimiento, self.tipo_educacion, self.modalidad, self.jornada, self.acceso, self.nro_estudiantes, self.nro_docentes, self.parroquia.codigo)


Base.metadata.create_all(engine)
