from fastapi import FastAPI, Request
import models
from database import engine, Base
from routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


@app.get("/")
@app.get("/")
def test(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"title": "Todo App"}
    )
@app.get("/healthy")
def health_check():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)