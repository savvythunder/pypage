# HTML Generator Flask Application

## Project Overview
A Flask web application that provides an interactive HTML generator using the PyPage library. Users can write Python code to generate HTML pages using a comprehensive component library.

## Architecture
- **Backend**: Flask with SQLAlchemy for database operations
- **Frontend**: Bootstrap 5 with custom CSS and JavaScript
- **HTML Generation**: Custom PyPage library with comprehensive component system
- **Database**: PostgreSQL (production) / SQLite (development)
- **File Structure**:
  - `app.py` - Flask application setup and configuration
  - `main.py` - Application entry point
  - `models.py` - Database models
  - `routes/` - Flask blueprints for different sections
  - `pypage/` - HTML generator library
  - `templates/` - Jinja2 templates
  - `static/` - CSS, JS, and other static assets

## Key Features
- Interactive code editor for HTML generation
- Gallery of generated pages
- Live preview functionality
- Example code library
- Page management (create, edit, delete)
- Database storage of generated pages

## Recent Changes
- **PyPI Package Creation (January 10, 2025)**: Converted project into a complete PyPI package
  - Created comprehensive testing application in `testing/` folder for documentation
  - Added PyPI package structure with setup.py, pyproject.toml, MANIFEST.in
  - Implemented CLI tools with `pypage` command for project creation
  - Added package metadata, license (MIT), and changelog
  - Successfully built wheel package for distribution
- Fixed import path from `html_generator` to `pypage` for proper module resolution
- Updated Flask configuration for Replit environment compatibility
- Ensured proper database setup with SQLAlchemy
- Migrated from Replit Agent to standard Replit environment

## User Preferences
None documented yet.

## Development Notes
- Uses Bootstrap 5 with custom dark theme
- Code execution happens in sandboxed environment with limited globals
- Generated pages are saved both to database and filesystem
- Application runs on port 5000 with gunicorn in production