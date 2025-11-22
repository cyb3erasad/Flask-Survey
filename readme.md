# Flask Survey Project Documentation

## Social Media Time Spending Survey

A modern, interactive Flask web application designed to collect and analyze user responses about their social media usage patterns. The survey features a beautiful, responsive UI with real-time data visualization and results tracking.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Features](#features)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)
8. [File Documentation](#file-documentation)
9. [Database Schema](#database-schema)
10. [API Endpoints](#api-endpoints)
11. [Deployment](#deployment)
12. [Troubleshooting](#troubleshooting)

---

## Project Overview

This Flask survey application collects responses from users about their social media habits and time spending patterns. The collected data is stored in a MySQL database and can be viewed through an interactive results page. The application features a modern, colorful, and fully responsive design that works seamlessly across all devices.

**Target Audience:** Anyone interested in understanding social media consumption patterns

**Use Cases:**
- Market research on social media usage
- Academic studies on digital behavior
- Business analytics for social media strategies
- User engagement analysis

---

## Project Structure

```
flask-survey-project/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables (not in repo)
├── .gitignore              # Git ignore file
├── templates/              # HTML templates folder
│   ├── survey.html         # Survey form page
│   ├── success.html        # Success confirmation page
│   └── results.html        # Results display page
├── static/                 # Static files folder
│   └── style.css          # Styling (modern responsive design)
└── README.md              # Project readme
```

---

## Features

### Core Features
- **Interactive Survey Form** - User-friendly form with multiple question types (text, email, radio buttons, checkboxes, textarea)
- **Data Storage** - Responses stored securely in MySQL database
- **Results Page** - View all collected survey responses in real-time
- **Success Confirmation** - User feedback after successful submission
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
- **Modern UI** - Colorful gradient backgrounds, smooth animations, glassmorphism effects

### Technical Features
- **Environment-based Configuration** - Secure credential management
- **Error Handling** - Graceful error management with database rollback
- **Database ORM** - SQLAlchemy for robust database operations
- **Static File Serving** - CSS and assets efficiently served
- **Cross-Platform Compatible** - Works on Windows, Mac, and Linux

---

## Requirements

### System Requirements
- Python 3.8 or higher
- MySQL Server 5.7 or higher
- Git (for version control)
- pip (Python package manager)

### Python Dependencies
```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
PyMySQL==1.1.0
SQLAlchemy==2.0.0
python-dotenv==1.0.0
Werkzeug==2.3.0
```

---

## Installation

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/cyb3erasad/Flask-Survey.git
cd flask-survey
```

### Step 2: Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create MySQL Database

Open MySQL Workbench or command line and run:

```sql
CREATE DATABASE survey_db;
USE survey_db;
```

The tables will be created automatically when you run the app for the first time.

### Step 5: Create Environment File

Create a `.env` file in the project root:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=survey_db
MYSQL_PORT=3306
```

Replace `your_password` with your actual MySQL password.

---

## Configuration

### Environment Variables

The application uses the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `MYSQL_HOST` | MySQL server hostname | localhost |
| `MYSQL_USER` | MySQL username | root |
| `MYSQL_PASSWORD` | MySQL password | pass |
| `MYSQL_DATABASE` | Database name | survey_db |
| `MYSQL_PORT` | MySQL port | 3306 |

### Local Development (.env.local)

For development, create `.env.local`:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_local_password
MYSQL_DATABASE=survey_db_local
DEBUG=True
```

### Production Deployment

For Vercel, Railway, or PythonAnywhere, set environment variables through the platform's dashboard instead of `.env` file.

---

## Running the Application

### Local Development

```bash
# Make sure virtual environment is activated
python app.py
```

The application will run at: `http://localhost:5000`

### With Debug Mode

Debug mode is automatically enabled for local development:

```bash
# In app.py, debug=True is set for development
python app.py
```

### Production Mode

For production, modify the last line in `app.py`:

```python
if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode
```

---

## File Documentation

### app.py

The main Flask application file containing:

- **Database Configuration** - Connects to MySQL using environment variables
- **SurveyResponse Model** - SQLAlchemy model defining the database table structure
- **Route Handlers** - Four main routes for survey functionality

**Key Functions:**

- `survey()` - Displays the survey form (GET request)
- `submit()` - Handles form submission and saves to database (POST request)
- `success()` - Shows success confirmation page
- `results()` - Displays all collected responses

### templates/survey.html

The main survey form page containing:

- Form fields for user information (name, email)
- Multiple question types:
  - Q1: Text input about daily social media time
  - Q2: Checkboxes for favorite platforms
  - Q3: Radio buttons for usage purpose
  - Q4: Dropdown for most used platform
  - Q5: Textarea for additional comments
- Submit button with validation
- Responsive form layout

### templates/success.html

Success confirmation page displayed after form submission:

- Success message confirmation
- Encouragement text
- Link to view results
- Link to take another survey
- Celebration animations

### templates/results.html

Results display page showing all collected survey responses:

- Summary statistics
- List of all responses in table or card format
- Response count
- Individual user responses with timestamps
- Option to export or analyze data
- Responsive data display

### static/style.css

Modern, responsive stylesheet featuring:

- **Gradient Backgrounds** - Animated gradient backgrounds
- **Responsive Design** - Mobile-first approach with media breakpoints
- **Interactive Elements** - Hover effects, transitions, animations
- **Accessibility** - Proper contrast ratios and semantic styling
- **Modern Effects** - Glassmorphism, shadows, smooth transitions

**Key Design Elements:**

- Animated gradient background
- Card-based layout with rounded corners
- Smooth hover animations
- Mobile breakpoints at 768px and 480px
- Gradient buttons with shine effects
- Shadow effects for depth

### requirements.txt

Lists all Python package dependencies and their versions:

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
PyMySQL==1.1.0
SQLAlchemy==2.0.0
python-dotenv==1.0.0
Werkzeug==2.3.0
```

---

## Database Schema

### SurveyResponse Table

```sql
CREATE TABLE survey_response (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    q1 VARCHAR(200),
    q2 VARCHAR(200),
    q3 VARCHAR(200),
    q4 VARCHAR(200),
    q5 VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Unique identifier for each response |
| name | String(100) | Respondent's full name |
| email | String(100) | Respondent's email address |
| q1 | String(200) | Time spent on social media daily |
| q2 | String(200) | Favorite social media platforms |
| q3 | String(200) | Primary purpose of social media use |
| q4 | String(200) | Most frequently used platform |
| q5 | String(200) | Additional comments/feedback |

---

## API Endpoints

### 1. Survey Form Page

**Endpoint:** `GET /`

**Description:** Displays the survey form

**Response:** HTML page with survey form

**Example:**
```
http://localhost:5000/
```

### 2. Submit Survey Response

**Endpoint:** `POST /submit`

**Description:** Processes form submission and saves to database

**Parameters:**
```
name: string (required)
email: string (required)
q1: string (required)
q2: array of strings (optional)
q3: string (required)
q4: string (required)
q5: string (required)
```

**Response:** Redirects to `/success` page

**Example:**
```bash
curl -X POST http://localhost:5000/submit \
  -d "name=John Doe" \
  -d "email=john@example.com" \
  -d "q1=3 hours" \
  -d "q2=Instagram" \
  -d "q3=Entertainment"
```

### 3. Success Page

**Endpoint:** `GET /success`

**Description:** Shows confirmation after successful submission

**Response:** HTML success confirmation page

**Example:**
```
http://localhost:5000/success
```

### 4. Results Page

**Endpoint:** `GET /results`

**Description:** Displays all collected survey responses

**Response:** HTML page with results table/cards

**Example:**
```
http://localhost:5000/results
```

---

## Deployment

### Deploy on Railway.app (Recommended)

1. Push project to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "Start a New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway auto-detects Python and creates MySQL database
6. Set environment variables in Railway dashboard
7. Deploy and get live URL

### Deploy on PythonAnywhere

1. Create account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Use Bash console to clone GitHub repo
3. Create virtual environment
4. Configure WSGI file with environment variables
5. Set static files mapping
6. Reload web app
7. Access at `username.pythonanywhere.com`

### Deploy on Vercel

1. Create `vercel.json` in project root
2. Push to GitHub
3. Go to [vercel.com](https://vercel.com)
4. Import GitHub repository
5. Add environment variables
6. Deploy
7. Get live URL

**Note:** For Vercel, use external MySQL service (PlanetScale, Railway) as Vercel doesn't support persistent connections.

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Database Connection Error

**Error:** `Connection refused` or `No such file or directory`

**Solution:**
- Ensure MySQL server is running
- Check database credentials in `.env` file
- Verify MySQL port (default 3306)
- Test connection using MySQL Workbench

#### 2. Module Not Found Error

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows

# Install requirements
pip install -r requirements.txt
```

#### 3. Static Files Not Loading

**Error:** CSS not applied, images not showing

**Solution:**
- Verify `static` folder exists
- Check file paths in HTML templates
- Restart Flask development server
- Clear browser cache (Ctrl+Shift+Delete)

#### 4. Form Submission Not Working

**Error:** 405 Method Not Allowed

**Solution:**
- Ensure form method is `POST` in HTML
- Verify route uses `methods=["POST"]`
- Check form action attribute points to `/submit`

#### 5. Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Kill process on port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

#### 6. Environment Variables Not Loading

**Error:** Connection errors, None values in database

**Solution:**
- Verify `.env` file exists in project root
- Restart Flask application
- Check for typos in variable names
- Ensure `.env` is in `.gitignore`

### Debug Mode

Enable debug mode to see detailed error messages:

1. In `app.py`, set `debug=True`
2. Flask will show error stack traces
3. Changes to code auto-reload the server

---

## Best Practices

### Security

- Never commit `.env` file to Git
- Use strong MySQL passwords
- Validate and sanitize user input
- Use HTTPS in production
- Keep dependencies updated

### Performance

- Use database indexes on frequently queried fields
- Implement pagination for large result sets
- Cache static files
- Use connection pooling for database

### Code Quality

- Add unit tests for routes
- Use logging for debugging
- Follow PEP 8 style guidelines
- Add type hints to functions
- Document custom functions

### Maintenance

- Regular database backups
- Monitor error logs
- Update dependencies quarterly
- Version control all changes
- Document any modifications

---

## Support & Contributing

### Getting Help

- Check troubleshooting section above
- Review Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- Check SQLAlchemy docs: [sqlalchemy.org](https://www.sqlalchemy.org)
- Stack Overflow: Tag questions with `flask` and `mysql`

### Contributing

To contribute improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This project is open source and available under the MIT License.

---

## Version History

**v1.0.0** - Initial Release
- Basic survey functionality
- MySQL database integration
- Modern responsive design
- Results page with data display

---

## Contact & Feedback

For questions, suggestions, or bug reports, please reach out or create an issue on GitHub.

**Last Updated:** November 2024