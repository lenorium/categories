from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

product_category = Table(
    'product_category',
    Base.metadata,
    Column('product_id', ForeignKey('products.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True),
)


class Product(Base):
    __tablename__ = 'products'

    id_ = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)

    categories = relationship('Category', secondary=product_category, back_populates='products')

    def __init__(self, title: str, categories=None):
        super().__init__()
        self.title = title
        self.categories = [] if categories is None else categories


class Category(Base):
    __tablename__ = 'categories'

    id_ = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)

    products = relationship('Product', secondary=product_category, back_populates='categories')

    def __init__(self, title: str):
        super().__init__()
        self.title = title

