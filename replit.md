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
  - `src/pypage/` - HTML generator library
  - `test/` - Testing application and documentation examples
  - `docs/` - Complete documentation with component reference and images
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
- **Complete Documentation Overhaul (January 10, 2025)**: Enhanced README and documentation
  - Redesigned README with professional visual presentation and badges
  - Added comprehensive hero banner and feature showcase with SVG graphics
  - Created complete documentation structure with cross-references
  - Added quick-start guide, installation guide, theme customization, and FAQ
  - Created visual component gallery and architecture diagrams
  - Built complete component reference with detailed API documentation
  - Added professional theme showcase and development workflow diagrams
  - Enhanced visual presentation with custom SVG illustrations
- **PyPI Package Creation (January 10, 2025)**: Converted project into a complete PyPI package
  - Created comprehensive testing application in `test/` folder for documentation
  - Added PyPI package structure with setup.py, pyproject.toml, MANIFEST.in
  - Implemented CLI tools with `pypage` command for project creation
  - Added package metadata, license (MIT), and changelog
  - Successfully built wheel package for distribution
  - Moved library code to `src/` folder structure for proper packaging
  - Resolved conflicting readme files (removed readme.md, kept README.md)
  - Fixed all import paths to work with new src structure
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