# Django Job Scraper

This is a Django web application that scrapes job postings from various websites and displays them in a user-friendly format.

## Features

- Display a list of all scraped jobs
- Search for jobs based on skills

## Installation

1. Clone this repository:
   git clone https://github.com/mayuresh1301/scraping.git
2. Navigate to the project directory:
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the migrations:
   python manage.py migrate
5. Start the development server:
   python manage.py runserver

## Usage

1. Visit `http://127.0.0.1:8000/scraper/skills_form/` in your browser to see the job list and the form.
2. Enter unfamiliar skills in the form and submit it to filter the job list.
