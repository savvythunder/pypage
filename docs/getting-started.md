# Getting Started

Welcome to the HTML Generator library! This guide will help you get up and running quickly with creating dynamic web pages using Python.

## What is HTML Generator?

HTML Generator is a powerful Python library that allows you to create HTML documents programmatically using an intuitive, object-oriented approach. Instead of writing raw HTML, you can use Python classes and methods to build your web pages.

## Key Features

### Core Capabilities
- **Component-Based Architecture**: Build pages using reusable components
- **Responsive Design**: Built-in Bootstrap integration for mobile-friendly layouts
- **Form Handling**: Advanced form components with validation
- **Template System**: Reusable templates with slot support
- **Theme Support**: Multiple UI frameworks (Bootstrap, Tailwind, Bulma, Material Design)

### Modern Features (v3.0)
- **Dark Mode Support**: Complete dark mode system with toggle
- **Animations**: FadeIn, SlideUp, AnimateOnScroll components
- **Visual Debug Mode**: Developer tools for debugging components
- **Plugin System**: Extensible architecture for custom components
- **Export Capabilities**: JSON serialization and PDF export
- **Performance Tools**: Hot reload, profiling, and optimization

### Web Interface
- **Code Editor**: Syntax-highlighted editor with live preview
- **Visual Tools**: Navbar builder and CSS configurator
- **Gallery System**: Manage and organize your generated pages
- **API Access**: RESTful API for programmatic access

## Installation

### Prerequisites
- Python 3.11 or higher
- Flask 3.1+
- PostgreSQL (for database storage)

### Basic Installation

```bash
# Install dependencies
pip install flask flask-sqlalchemy gunicorn psycopg2-binary

# Clone or set up the project
git clone <repository-url>
cd html-generator

# Install the library
pip install -e .
```

### Web Application Setup

```bash
# Set environment variables
export DATABASE_URL="postgresql://user:password@localhost/html_generator"
export SESSION_SECRET="your-secret-key"

# Initialize database
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Run the application
gunicorn --bind 0.0.0.0:5000 main:app
```

## Your First Page

### Basic Example

```python
from html_generator import Page, Heading, Paragraph, Card

# Create a new page
page = Page("My First Page", "Welcome to HTML Generator")

# Add content
page.add_content(Heading("Hello World!", level=1))
page.add_content(Paragraph("This is my first generated webpage."))

# Add a card component
card = Card("Getting Started", "You're now ready to build amazing web pages!")
page.add_content(card)

# Generate HTML
html = page.generate_html()
print(html)
```

### With Modern Features

```python
from html_generator import *

# Create page with dark mode support
page = Page("Modern Page", "Advanced Features Demo")
page.set_theme('bootstrap')

# Add dark mode toggle
page.add_content(DarkModeToggle(position="top-right"))

# Add animated content
animated_heading = FadeIn(
    Heading("Welcome to the Future", level=1, css_class="text-center")
)
page.add_content(animated_heading)

# Add interactive chart
chart_data = {
    'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'datasets': [{
        'label': 'Sales',
        'data': [12, 19, 3, 5, 2]
    }]
}
chart = InteractiveChart('bar', chart_data)
page.add_content(chart)

# Generate and run
html = page.generate_html()
page.run()  # Opens in browser
```

## Project Structure

```
html-generator/
├── html_generator/          # Core library
│   ├── __init__.py         # Main exports
│   ├── page.py             # Page component
│   ├── elements.py         # Basic elements
│   ├── components.py       # Advanced components
│   ├── ui_components.py    # Modern UI components
│   ├── performance_tools.py # Performance features
│   └── ...
├── templates/              # Web interface templates
├── static/                 # CSS and JavaScript assets
├── routes/                 # Flask route handlers
├── docs/                   # Documentation
└── app.py                  # Flask application
```

## Web Interface

### Accessing the Interface

1. Start the web application
2. Open your browser to `http://localhost:5000`
3. Navigate through the interface:
   - **Editor**: Write and test Python code
   - **Gallery**: View generated pages
   - **Examples**: Browse code examples
   - **Tools**: Visual configuration tools

### Using the Code Editor

1. Go to the Editor page
2. Write your Python code using HTML Generator components
3. Set a page title
4. Click "Generate Page" to create and preview
5. Use the gallery to manage your creations

### Visual Tools

- **Navbar Builder**: Create navigation bars visually
- **CSS Builder**: Build responsive CSS rules
- **Performance Profiler**: Monitor page performance
- **SEO Optimizer**: Check search engine optimization

## Next Steps

Now that you're set up, explore these topics:

1. **[Core Components](./library/core-components.md)**: Learn about basic building blocks
2. **[Advanced Components](./library/advanced-components.md)**: Discover powerful UI elements
3. **[Modern Features](./features/modern-ui.md)**: Explore animations, dark mode, and more
4. **[Performance Guide](./features/performance.md)**: Optimize your applications
5. **[Examples](./examples/basic.md)**: See practical use cases

## Getting Help

- Check the [API Reference](./web-app/api-reference.md) for detailed component documentation
- Browse [Examples](./examples/basic.md) for inspiration
- Read the [Architecture Guide](./development/architecture.md) to understand the system
- Consult the [Troubleshooting Guide](./development/troubleshooting.md) for common issues

Ready to build something amazing? Let's dive into the [Core Components](./library/core-components.md)!