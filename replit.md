# HTML Generator Web Application

## Overview

This is a Flask-based web application that provides a Python HTML generator library with a web interface for creating, editing, and managing HTML pages programmatically. Users can write Python code to generate responsive web pages using an object-oriented approach, with components like Page, Heading, Paragraph, Lists, Images, and Forms. The application features a code editor with syntax highlighting, live preview functionality, a gallery system for managing generated pages, and now includes enhanced modern navigation bars, a page.run() method for direct execution, and visual configuration tools.

## Recent Changes (August 2025)

- **Added page.run() method**: Users can now run websites directly from Python code using `page.run()` which opens the generated HTML in a browser
- **Enhanced Navigation Bar**: Implemented modern navigation bar with gradient styling, dropdown support, mobile responsiveness, and hamburger menu
- **Configuration Web Interface**: Created visual tools for navbar configuration and CSS building accessible through the Tools menu
- **Improved CSS Handling**: Enhanced CSS builder with responsive breakpoints, method chaining, and visual CSS rule editor
- **Modern UI Components**: Added sticky navigation, scroll effects, and improved mobile experience
- **Major Library Enhancement (August 2, 2025)**: Implemented comprehensive feature expansion including:
  - Enhanced form support with improved validation, labels, and multiple selection
  - Complete layout system with Row, Column, and Flex components for responsive design
  - Advanced style customization with inline styles, class_name parameter, and JavaScript event hooks
  - Template system with slots for reusable HTML blocks and predefined templates
  - Component inheritance system allowing custom component creation via ComponentBase
  - Built-in theme support (Bootstrap, Tailwind, Bulma, Material Design)
  - Advanced components: Alert, Badge, ProgressBar, Accordion, Modal, enhanced Navbar
  - Comprehensive example file and documentation guide

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with a base template system for consistent UI
- **CSS Framework**: Bootstrap 5 with dark theme for responsive design
- **JavaScript Libraries**: CodeMirror for syntax highlighting and code editing
- **UI Components**: Interactive code editor, live preview iframe, gallery grid/list views
- **Responsive Design**: Mobile-first approach with Bootstrap breakpoints

### Backend Architecture
- **Web Framework**: Flask with Blueprint-based route organization
- **Route Structure**: Separated into main routes (web pages), API routes (JSON endpoints), and config routes (visual tools)
- **Code Execution**: Safe Python code execution using exec() with controlled globals
- **File Management**: Generated HTML files stored in `generated_pages` directory and temporary files for page.run()
- **Session Management**: Flask sessions with configurable secret key
- **Configuration Tools**: Visual navbar builder and CSS editor with live preview capabilities

### HTML Generator Library
- **Object-Oriented Design**: Component-based architecture with enhanced base Element class supporting style and event handling
- **Core Components**: Page, Heading, Paragraph, List, Image, Card, Container classes with improved customization
- **Enhanced Form System**: Comprehensive form handling with Input, Button, Select, TextArea, validation, labels, and multiple selection support
- **Layout System**: Complete responsive layout with Row, Column, and Flex components supporting Bootstrap grid and flexbox patterns
- **Style Customization**: Inline style support, class_name parameter, add_style/set_style methods, and JavaScript event hooks (on_click, on_submit, on_change, on_hover)
- **Template System**: Reusable HTML templates with slot support, TemplateManager, and predefined templates (hero, card grid, footer)
- **Component Inheritance**: ComponentBase class enabling custom component creation and inheritance from existing components
- **Theme Support**: Built-in theme system supporting Bootstrap (dark/light), Tailwind, Bulma, and Material Design with Page.set_theme() method
- **Advanced Components**: Alert, Badge, ProgressBar, Accordion, Modal, enhanced Navbar with extensive customization options
- **CSS Integration**: Built-in CSS framework support with custom styling options and method chaining
- **Responsive Features**: CSS builder with media query support and breakpoint helpers
- **Modern Navigation**: Enhanced navbar system with dropdown support, mobile responsiveness, and custom branding
- **Direct Execution**: page.run() method for instant browser preview and local development
- **Advanced CSS Builder**: Method chaining CSS creation with responsive breakpoint management

### Data Storage Solutions
- **Database**: SQLAlchemy ORM with SQLite default (configurable via DATABASE_URL)
- **Models**: GeneratedPage model storing page metadata, code, and HTML content
- **Connection Pooling**: Configured with pool recycling and pre-ping for reliability
- **File Storage**: Static HTML files saved to filesystem for direct viewing

### Authentication and Authorization
- **Current State**: No authentication implemented (open access)
- **Session Security**: Session secret key from environment variables
- **Code Execution Security**: Limited global scope for user code execution

## External Dependencies

### Core Dependencies
- **Flask**: Web framework and routing
- **SQLAlchemy**: Database ORM and connection management
- **Jinja2**: Template rendering (included with Flask)

### Frontend Libraries
- **Bootstrap 5**: CSS framework loaded from Replit CDN
- **Font Awesome**: Icon library from CDN
- **CodeMirror**: Code editor with Python syntax highlighting and Dracula theme

### Development Tools
- **Python Standard Library**: os, logging, datetime, uuid, re modules
- **Database**: SQLite for development (PostgreSQL-ready via DATABASE_URL)

### External Services
- **CDN Resources**: Bootstrap, Font Awesome, and CodeMirror loaded from CDNs
- **No External APIs**: Application runs entirely self-contained

### Environment Configuration
- **DATABASE_URL**: Database connection string (defaults to SQLite)
- **SESSION_SECRET**: Flask session encryption key (defaults to development key)
- **File System**: Local storage for generated HTML files and static assets