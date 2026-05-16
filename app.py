from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

PROJECTS = {
    'caluclator-app': {
        "title": "Interactive Command Line Calculator",
        "description": "A calculator on the command line that looks for errors and finds finds the solution to acceptable calculations. Does the basic four functions of math.",
        "tech_stack": ["Basic Python", "Control Flow", "Functions, Parameters, Arguments", "Error Handling"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project1Calculator.py"
    },

    'task-list-app': {
        "title": "Interactive Command Line Task List(non persistent)",
        "description": "A task list on the command line that allows you to add to, remove from, view, and exit the list. It looks for errors and preforms its given functions.",
        "tech_stack": ["Basic Python", "Control Flow", "Functions, Parameters, Arguments", "Error Handling", "Lists"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project2TaskList.py"
    },

    'weather-tracker-app': {
        "title": "Interactive Weather Tracker Using Latitude, Longitude, and APIs",
        "description": "A weather tracker that uses an API key to get a latitude and longitude to find a location and find its tempurature and weather conditions.",
        "tech_stack": ["Python With Libraries", "Requests Library", "API Integration", "JSON"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project3WeatherApp.py"
    },

    'csv-expense-file-app': {
        "title": "Interactive CSV File Editor, Tracking Expenses",
        "description": "An expense tracker using CSV files and pandas to make a expense tracker with persistent data.",
        "tech_stack": ["Python With Libraries", "Pandas Library", "File Handling"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project4CSVfileExpenses.py"
    },

    'oop-quiz-app': {
        "title": "Interactive OOP Quiz",
        "description": "A quiz using OOPs to make a quiz that tracks your score.",
        "tech_stack": ["Basic Python", "OOPs"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project5OOPquiz.py"
    },

    'web-scraper': {
        "title": "Web Scraper",
        "description": "An app that uses BeautifulSoup and Requests to look through a website and get information out of it.(uses bookstoscrape.com)",
        "tech_stack": ["Python With Libraries", "BeautifulSoup", "Requests", "Data Parsing", "Web Scraping"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project6WebScraper.py"
    }

    'ai-guessing-game': {
        "title": "AI Guessing Game",
        "description": "A game that uses ai to make an interactive animal guessing game easier and faster.",
        "tech_stack": ["Python With Libraries", "AI Integration", "API Integration"],
        "github": "https://github.com/AAK1003/projectportfollioproj7/blob/main/projectsaddedtoportfollio/project6WebScraper.py"
    }

    }

@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS)

@app.route("/project/<project_id>")
def project_detail(project_id):
    project = PROJECTS.get(project_id)
    if not project:
        abort(404)
    return render_template("project_detail.html", project = project)

if __name__ == "__main__":
    app.run(debug = True)