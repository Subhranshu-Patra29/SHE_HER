# Pickup Lines Generator

A Django web application that generates random romantic and techy pickup lines.

## Features

- **Two Types of Pickup Lines**: Romantic and Techy + Romantic
- **Random Generation**: Each page refresh or button click shows a new pickup line
- **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **API Endpoints**: RESTful API endpoints for both types of pickup lines
- **Database Storage**: 15 romantic and 15 techy pickup lines stored in SQLite database

## Installation

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Populate the database with sample pickup lines**:
   ```bash
   python manage.py populate_pickup_lines
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and go to `http://127.0.0.1:8000/`

## Usage

- Click "Generate Romantic Pickup Line" for classic romantic pickup lines
- Click "Generate Techy + Romantic Pickup Line" for programming-themed pickup lines
- Refresh the page to get a completely new experience
- Each button click generates a random pickup line from the database

## API Endpoints

- `GET /api/romantic/` - Returns a random romantic pickup line
- `GET /api/techy/` - Returns a random techy pickup line

Both endpoints return JSON responses with the pickup line text and category.

## Project Structure

```
pickup_lines_app/
├── pickup_lines_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pickup_lines/
│   ├── models.py          # PickupLine model
│   ├── views.py           # API views
│   ├── urls.py            # URL patterns
│   ├── management/
│   │   └── commands/
│   │       └── populate_pickup_lines.py
│   └── templates/
│       └── pickup_lines/
│           └── home.html  # Main page template
├── manage.py
└── requirements.txt
```

## Adding More Pickup Lines

To add more pickup lines, you can either:

1. **Use the Django admin** (create a superuser first):
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
   ```
   Then go to `http://127.0.0.1:8000/admin/`

2. **Modify the management command** in `pickup_lines/management/commands/populate_pickup_lines.py` and run it again

3. **Add them programmatically** using the Django shell:
   ```bash
   python manage.py shell
   ```
   ```python
   from pickup_lines.models import PickupLine
   PickupLine.objects.create(text="Your new pickup line", category="romantic")
   ```

## Technologies Used

- **Django 5.2.4** - Web framework
- **SQLite** - Database
- **HTML5/CSS3** - Frontend styling
- **JavaScript** - Frontend interactivity
- **Bootstrap-inspired design** - Modern UI components
