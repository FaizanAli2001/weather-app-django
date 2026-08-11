# Weather App

A weather application built with **Python and Django** that allows users to search for a city and view its current weather information using the OpenWeather API.

## Features

* Search weather by city name
* Display current temperature
* Display weather description
* Display weather icon
* Default city: Lahore
* Error message for invalid city names
* Django messages framework for error handling

## Technologies Used

* Python
* Django
* HTML
* CSS
* OpenWeather API
* Requests

## Installation

Clone the repository:

```bash
git clone https://github.com/FaizanAli2001/weather-app-django.git
```

Go to the project directory:

```bash
cd weather-app-django
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenWeather API key:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
weatherproject/
├── manage.py
├── README.md
├── requirements.txt
├── weatherapp/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── ...
└── weatherproject/
    ├── settings.py
    ├── urls.py
    └── ...
```

## Git Workflow

This project uses Git for version control.

Feature development is done using separate branches:

```bash
git checkout -b feature/feature-name
```

After completing a feature:

```bash
git add .
git commit -m "feat: add feature"
git checkout main
git merge feature/feature-name
git push origin main
```

## API

Weather data is provided by the OpenWeather API.

## Author

Faizan Ali
