# FastAPI Learning - Todo App

Dự án mẫu học **FastAPI** với xác thực JWT, quản lý Todo theo người dùng và giao diện HTML cơ bản.

## Tính năng chính

- Đăng ký, đăng nhập bằng JWT (OAuth2 password flow).
- Quản lý Todo theo từng user.
- Quyền admin để xem/xóa todo của mọi user.
- Lưu dữ liệu với SQLite + SQLAlchemy ORM.
- Có sẵn bộ test với `pytest`.

## Cấu trúc dự án

```text
FastAPI-Learning/
├── README.md
├── todosapp.db
└── TodoApp/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── routers/
    │   ├── auth.py
    │   ├── todos.py
    │   ├── admin.py
    │   └── users.py
    ├── templates/
    ├── static/
    └── test/
```

## Công nghệ sử dụng

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib (bcrypt)
- python-jose (JWT)
- Pytest

## Cài đặt nhanh

> Khuyến nghị dùng virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell

pip install -r requirements.txt
```

Nếu chưa có `requirements.txt`, bạn có thể cài nhanh:

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart pytest
```

## Chạy ứng dụng

Từ thư mục gốc dự án:

```bash
uvicorn TodoApp.main:app --reload
```

Sau khi chạy:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Luồng sử dụng cơ bản

### 1) Đăng ký người dùng

`POST /auth/`

Ví dụ body JSON:

```json
{
  "username": "john",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "123456",
  "role": "user"
}
```

### 2) Đăng nhập lấy token

`POST /auth/token` (form-data theo chuẩn OAuth2 password)

- `username`: john
- `password`: 123456

Phản hồi:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

### 3) Gọi API cần xác thực

Thêm header:

```text
Authorization: Bearer <jwt_token>
```

## Danh sách endpoint chính

### Auth

- `POST /auth/` — Tạo user mới.
- `POST /auth/token` — Đăng nhập và lấy access token.

### Todo (user)

- `GET /todos/` — Lấy danh sách todo của user hiện tại.
- `GET /todos/todo/{todo_id}` — Lấy chi tiết todo.
- `POST /todos/todo` — Tạo todo mới.
- `PUT /todos/todo/{todo_id}` — Cập nhật todo.
- `DELETE /todos/todo/{todo_id}` — Xóa todo.

### Admin

- `GET /admin/todo` — Lấy toàn bộ todo (chỉ role `admin`).
- `DELETE /admin/todo/{todo_id}` — Xóa todo bất kỳ (chỉ role `admin`).

## Chạy test

```bash
cd TodoApp
pytest
```

## Ghi chú

- SQLite file mặc định: `todosapp.db`.
- Token hiện được cấu hình hết hạn khoảng 20–30 phút (tùy cấu hình trong mã nguồn).
- Kiểm tra role admin hiện thực trực tiếp trong router.

---

Nếu bạn muốn, mình có thể bổ sung thêm:

- hướng dẫn chạy bằng Docker,
- biến môi trường `.env`,
- tài liệu API tiếng Anh.
