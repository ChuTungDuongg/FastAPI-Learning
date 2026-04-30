from test.utils import *
from routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() ['username'] == 'testuser'
    assert response.json() ['email'] == 'testuser@example.com'
    assert response.json() ['first_name'] == 'Test'
    assert response.json() ['last_name'] == 'User'
    assert response.json() ['phone_number'] == '1234567890'
    assert response.json() ['role'] == 'admin'


def test_change_password_success(test_user):
    response = client.put('/user/password', json={
        'password' : 'testpassword',
        'new_password' : 'newtestpassword'
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={
        'password' : 'wrongpassword',
        'new_password' : 'newtestpassword'
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect password'}
    
def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/0987654321')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert model.phone_number == '0987654321'