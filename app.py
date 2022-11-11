from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'Data': 'Testing'}


@app.get('/products')
def products():
    return {'Data': 'Products'}


@app.get('/categories')
def products():
    return {'Data': 'Categories'}


@app.get('/products-categories')
def products():
    return {'Data': 'Products-Categories'}


if __name__ == '__main__':

    print()

