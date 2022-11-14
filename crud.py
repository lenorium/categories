from sqlalchemy.orm import Session

from models import *


def get_products(session: Session) -> list[Product]:
    return session.query(Product) \
        .outerjoin(product_category, Product.id_ == product_category.c.product_id) \
        .outerjoin(Category, Category.id_ == product_category.c.category_id) \
        .all()


def get_categories(session: Session) -> list[Category]:
    return session.query(Category) \
        .outerjoin(product_category, Category.id_ == product_category.c.category_id) \
        .outerjoin(Product, Product.id_ == product_category.c.product_id) \
        .all()


def get_product_category(session: Session):
    products = session.query(Product) \
        .join(product_category, Product.id_ == product_category.c.product_id) \
        .join(Category, Category.id_ == product_category.c.category_id) \
        .order_by(Product.title) \
        .all()
    return [{'product': p.title, 'category': c.title} for p in products for c in p.categories]
