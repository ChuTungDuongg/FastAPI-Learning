# FastAPI Learning - Todo App

Dự án mẫu học **FastAPI** với các tính năng:
- Đăng ký tài khoản và đăng nhập bằng JWT.
- Quản lý Todo theo từng người dùng.
- Endpoint admin để xem/xóa toàn bộ todo.
- Lưu dữ liệu bằng **SQLite** + **SQLAlchemy ORM**.

## 1) Cấu trúc dự án

```text
FastAPI-Learning/
├── README.md
├── todosapp.db
└── TodoApp/
    ├── main.py
    ├── database.py
    ├── models.py
    └── routers/
        ├── auth.py
        ├── todos.py
        └── admin.py
```

## 2) Công nghệ sử dụng

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib (bcrypt)
- python-jose (JWT)

## 3) Cài đặt nhanh

> Khuyến nghị dùng virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell

pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart
```

## 4) Chạy ứng dụng

Trong thư mục `TodoApp`:

```bash
uvicorn main:app --reload
```

Sau khi chạy:
- API docs (Swagger): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 5) Luồng sử dụng cơ bản

### Bước 1: Đăng ký người dùng
`POST /auth/auth`

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

### Bước 2: Đăng nhập lấy token
`POST /auth/token` (form-data theo chuẩn OAuth2 password)

- `username`: john
- `password`: 123456

Kết quả trả về:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

### Bước 3: Gọi API có xác thực
Thêm header:

```text
Authorization: Bearer <jwt_token>
```

## 6) Danh sách endpoint

### Auth
- `POST /auth/auth` — Tạo user mới.
- `POST /auth/token` — Đăng nhập và lấy access token.

### Todo (user thường)
- `GET /` — Lấy tất cả todo của user hiện tại.
- `GET /todo/{todo_id}` — Lấy chi tiết một todo của chính user đó.
- `POST /todo/` — Tạo todo mới.
- `PUT /todo/{todo_id}` — Cập nhật todo.
- `DELETE /todo/{todo_id}` — Xóa todo.

### Admin
- `GET /admin/todo` — Lấy toàn bộ todo (chỉ role `admin`).
- `DELETE /admin/todo/{todo_id}` — Xóa todo bất kỳ (chỉ role `admin`).

## 7) Lưu ý

- CSDL đang dùng SQLite file (`todosapp.db`).
- Token hết hạn sau khoảng 30 phút.
- Role được kiểm tra thủ công tại router admin (`user_role == 'admin'`).

## 8) Hướng mở rộng

- Tách cấu hình ra file `.env` (secret key, thời gian hết hạn token, DB URL).
- Thêm Alembic để quản lý migration.
- Viết test bằng `pytest` + `httpx`.
- Tổ chức project theo package rõ ràng hơn (absolute imports).

---

Nếu bạn muốn, mình có thể tạo luôn phiên bản README tiếng Anh hoặc thêm phần chạy bằng Docker.
