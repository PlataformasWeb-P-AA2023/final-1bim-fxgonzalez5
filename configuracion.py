from sqlalchemy import create_engine

# MySQL
engine = create_engine("mysql+mysqlconnector://root:07102002@localhost:3306/final1bimaa22", echo=True)