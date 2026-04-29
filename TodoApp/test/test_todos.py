from sqlalchemy import StaticPool, create_engine, text
from database import Base
from sqlalchemy.orm import sessionmaker
from main import app
from routers.todos import get_db, get_current_user
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from models import Todos
SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'


engine = create_engine(SQLALCHEMY_DATABASE_URI, 
                       connect_args={"check_same_thread": False},
                       poolclass = StaticPool,
                       )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username' : 'testuser', 'id' : 1, 'role' : 'admin'}
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title = "Test Todo",
        description = "This is a test todo",
        priority = 3,
        completed = False,
        owner_id = 1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos"))
        connection.commit()

def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'completed': False, 'description': 'This is a test todo', 'id': 1, 'owner_id': 1, 'priority': 3, 'title': 'Test Todo'}]
    
    
def test_read_one_authenticated():
    response = client.get('/todo/999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}