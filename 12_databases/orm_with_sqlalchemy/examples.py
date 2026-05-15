# Examples: Managing Data with SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# --- Setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"sqlite:///{os.path.join(BASE_DIR, 'example.db')}"

# 1. Create the Engine and Base
engine = create_engine(DB_PATH, echo=True) # echo=True shows the SQL in the terminal
Base = declarative_base()

# 2. Define a Model
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<Student(name='{self.name}', age={self.age})>"

# 3. Create the tables in the database
Base.metadata.create_all(engine)

# 4. Create a Session
Session = sessionmaker(bind=engine)
session = Session()

def run_demo():
    # --- CREATE ---
    print("\n--- Adding Students ---")
    s1 = Student(name="Hamza", age=25)
    s2 = Student(name="Ali", age=22)
    session.add_all([s1, s2])
    session.commit()

    # --- READ ---
    print("\n--- Querying Students ---")
    all_students = session.query(Student).all()
    for student in all_students:
        print(student)

    # --- UPDATE ---
    print("\n--- Updating Hamza's Age ---")
    hamza = session.query(Student).filter_by(name="Hamza").first()
    if hamza:
        hamza.age = 26
        session.commit()
    print(f"Updated: {hamza}")

    # --- DELETE ---
    print("\n--- Deleting Ali ---")
    ali = session.query(Student).filter_by(name="Ali").first()
    if ali:
        session.delete(ali)
        session.commit()
    
    print("Final List:")
    print(session.query(Student).all())

if __name__ == "__main__":
    # Note: Run 'pip install sqlalchemy' first!
    run_demo()
    session.close()
