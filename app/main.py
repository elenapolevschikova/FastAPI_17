from fastapi import FastAPI
from app.routers import category, products

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}


app.include_router(category.router)
app.include_router(products.router)

######################################################
# Запуск :

# 1.Для запуска и автоматической перезагрузки сервера:
# uvicorn main:app --reload   (только при тестировании--reload )

# pip install fastapi
# pip install sqlalchemy
# pip install slugify
# pip install pydantic
# pip install alembic

# alembic init migrations
# alembic revision --autogenerate -m "Initial migration"

######################################################
# Попробуйте новую кроссплатформленную оболочку Powershell(https://aka.ms//pscore6)
# pip install fastapi[all]

# python.exe -m pip install upgrade pip
