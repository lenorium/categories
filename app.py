import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from config import settings
from database import session_maker
from models import Category, Product

app = FastAPI()


def get_session():
    with session_maker() as session:
        yield session


@app.get('/')
def home():
    return 'It works!'


@app.get('/products', response_model=list[schemas.Product])
def products(session: Session = Depends(get_session)):
    return crud.get_products(session)


@app.get('/categories', response_model=list[schemas.Category])
def products(session: Session = Depends(get_session)):
    return crud.get_categories(session)


@app.get('/products-categories', response_model=list[schemas.ProductCategory])
def products(session: Session = Depends(get_session)):
    return crud.get_product_category(session)


def init_db():
    with session_maker.begin() as session:
        categories = [Category(f'cat_{i}') for i in range(5)]

        product_0 = Product('prod_0', categories[:2])
        product_1 = Product('prod_1', [categories[0]])
        product_2 = Product('prod_2', [categories[0]])
        product_3 = Product('prod_3', [categories[3]])
        product_4 = Product('prod_4')

        products = (product_0, product_1, product_2, product_3, product_4)

        session.add_all(products)
        session.add(categories[4])


if __name__ == '__main__':
    init_db()
    uvicorn.run("app:app", host='0.0.0.0', port=settings.api_port, log_level=settings.log_level, reload=True)
