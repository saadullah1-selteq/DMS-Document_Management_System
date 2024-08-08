
# Document Management System (DMS)

## Overview

This project is a Django-based Document Management System (DMS) that provides comprehensive file and folder management functionalities for businesses and customers. The system is designed to manage files, directories, and business entities, offering APIs for CRUD operations on these resources. 

## Features

- **Business Management**: Create, retrieve, update, and delete businesses.
- **Sub-Business Management**: Manage child businesses under main businesses.
- **Folder Management**: Create and manage folders for businesses and sub-businesses.
- **File Management**: Upload and manage files within specific folders.

## Implemented APIs

### Business APIs

- **`/api/businesses/`**: CRUD operations for business entities.
- **`/api/sub-businesses/`**: CRUD operations for sub-businesses.
- **`/api/businesses/<id>/folders/`**: Create folders within a business.
- **`/api/sub-businesses/<id>/folders/`**: Create folders within a sub-business.

### File APIs

- **`/api/folders/<id>/files/`**: Upload files to a specific folder.
- **`/api/files/<id>/`**: Retrieve details of a single file.
- **`/api/folders/<id>/`**: Retrieve the contents of a folder.

### Customer APIs

- **`/api/customers/<id>/folders/`**: Manage customer directories.
- **`/api/customers/<id>/files/`**: Manage customer files.
- **`/api/customers/<id>/recycle-bin/`**: Manage the recycle bin for a customer.

## Project Structure

```
DMS/
│
├── documents/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── DMS/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/saadullah1-selteq/DMS-Document_Management_System/tree/master/media/files
   cd dms
   ```

2. **Create and activate a virtual environment**:
   ```
   python -m venv .venv
   source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Apply the migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

6. **Access the API documentation**:
   Visit `http://127.0.0.1:8000/api/` to explore the API endpoints.

## Requirements

- Python 3.x
- Django 4.x
- djangorestframework 3.x


### requirements.txt

```plaintext
Django>=4.0,<5.0
djangorestframework>=3.12,<4.0
```

