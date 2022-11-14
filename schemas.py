from pydantic import BaseModel


class Product(BaseModel):
    id_: int
    title: str

    categories: list = []

    class Config:
        orm_mode = True


class Category(BaseModel):
    id_: int
    title: str

    products: list = []

    class Config:
        orm_mode = True


class ProductCategory(BaseModel):
    product: str
    category: str
