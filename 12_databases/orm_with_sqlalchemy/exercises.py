"""
EXERCISES: The ORM Architect

EXERCISE 1: The Product Model
1. Define a 'Product' model using SQLAlchemy.
2. Columns: 'id' (Integer, primary_key), 'name' (String), 'price' (Integer).
3. Create the engine (use SQLite) and the tables.

EXERCISE 2: Bulk Operations
1. Create a session.
2. Add 5 different products to the database using 'session.add_all()'.
3. Commit the changes.

EXERCISE 3: Smart Querying
1. Write a query to find all products that cost more than $50.
2. Print their names.
3. Update the price of one product and verify the change.
"""

# TODO: Implement the exercises below


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# --- Setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"sqlite:///{os.path.join(BASE_DIR, 'ecommerce.db')}"

engine = create_engine(DB_PATH, echo=False)
Base = declarative_base()

# --- Model ---
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"


# --- Create Tables ---
Base.metadata.create_all(engine)

# --- Session ---
Session = sessionmaker(bind=engine)


# =========================
# FUNCTIONS
# =========================

def add_products(session):
    products = [
        Product(name="Laptop", price=1000),
        Product(name="Mouse", price=20),
        Product(name="Keyboard", price=50),
        Product(name="Monitor", price=200),
        Product(name="Webcam", price=50)
    ]

    session.add_all(products)
    session.commit()

    print("Products added successfully.")


def get_expensive_products(session, minimum_price):
    print(f"\nProducts that cost more than ${minimum_price}:")

    products = session.query(Product).filter(
        Product.price > minimum_price
    ).all()

    for product in products:
        print(product.name)

    return products


def update_product_price(session, product_name, new_price):
    product = session.query(Product).filter_by(
        name=product_name
    ).first()

    if product:
        product.price = new_price
        session.commit()

        print(f"\nUpdated {product.name} price to ${new_price}")
    else:
        print(f"\nProduct '{product_name}' not found.")


def show_product(session, product_name):
    product = session.query(Product).filter_by(
        name=product_name
    ).first()

    if product:
        print(product)
    else:
        print("Product not found.")


# =========================
# MAIN PROGRAM
# =========================

def main():
    session = Session()

    try:
        add_products(session)

        get_expensive_products(session, 50)

        update_product_price(session, "Mouse", 25)

        print("\nVerifying update:")
        show_product(session, "Mouse")

    finally:
        session.close()


if __name__ == "__main__":
    main()