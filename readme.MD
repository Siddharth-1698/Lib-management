# Library Management System

A web-based application to manage authors, books, and borrowers. This system is built using Django for the backend and utilizes HTMX for dynamic and interactive UI components. It also features Bootstrap for styling and responsiveness.

---

## Features

- **Manage Authors**: Create, update, delete, and view a list of authors.
- **Manage Books**: Add, edit, delete, and list books, linking them to authors.
- **Manage Borrowers**: Record borrowers and their borrowed books with return dates.
- **Dynamic UI**: HTMX enables seamless updates to the interface without full-page reloads.
- **Responsive Design**: Bootstrap ensures the application is mobile-friendly.

---

## Requirements

- **Python**: `>= 3.8`
- **Django**: `>= 4.0`
- **Bootstrap**: `v5.3.0` (via CDN)
- **HTMX**: Latest version (via CDN)

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Siddharth-1698/Lib-management.git
   cd Lib-management

   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Dependencies

Ensure the following are included in your `requirements.txt` file:

```
Django>=4.0
```

Other dependencies like Bootstrap and HTMX are included via CDN.

## License

This project is licensed under the **MIT License**. Feel free to use and modify it as needed.
