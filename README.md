# Streamlit Login & Authentication Demo

This repository provides a **simple login and authentication system** for Streamlit-based UIs. It's ideal for lightweight use cases such as university projects, prototypes, or internal tools.

## 🚀 Features

- 🔐 Basic user authentication
- 🧭 Streamlit UI with a navigation sidebar
- 📦 Minimal demo app showcasing login functionality

## 👤 Demo Users

The system includes pre-defined user credentials for testing purposes:

- **Users**: `user1`, `user2`
- **Passwords**: `123` (for both users)
- **Register Password**: `register` (used to allow new user registration)

## 🎯 Use Cases

This authentication module is suited for:

- 🎓 Educational projects  
- 🧪 Classroom demos  
- 🛠️ Prototypes or proof-of-concept applications

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/MaxwellMuF/Streamlit_login_system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run streamlit_app.py
```

### 4. Run Tests

To run the unit tests for the authenticator:
```bash
python -m unittest tests/test_authenticator.py
```