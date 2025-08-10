# 🚀 Quick Start Guide

Get up and running with PyPage in just 5 minutes!

## Installation

Choose your installation method:

### Basic Installation
```bash
pip install pypage
```

### With All Features
```bash
pip install pypage[full]
```

### Development Installation
```bash
pip install pypage[dev]
```

## Your First Page

Create a file called `my_first_page.py`:

```python
from pypage import *

# Create a new page
page = Page("My First Website", "Welcome to PyPage!")

# Add a hero section
hero = Container([
    Heading("Welcome to PyPage! 🚀", 1, css_class="display-4 text-center"),
    Paragraph("Create beautiful websites with Python", css_class="lead text-center"),
    Div([
        Button("Get Started", "button", css_class="btn btn-primary btn-lg me-3"),
        Button("View Docs", "button", css_class="btn btn-outline-secondary btn-lg")
    ], css_class="text-center mt-4")
], css_class="py-5")

page.add_content(hero)

# Add feature cards
features_row = Row()
features = [
    ("🎨", "Beautiful Design", "Modern UI components with Bootstrap 5"),
    ("⚡", "Fast Development", "Write Python, get professional HTML"),
    ("📱", "Responsive", "Mobile-first design that works everywhere")
]

for icon, title, description in features:
    card = Card([
        Div(icon, css_class="display-4 text-center mb-3"),
        Heading(title, 4, css_class="text-center"),
        Paragraph(description, css_class="text-center text-muted")
    ], css_class="h-100")
    
    features_row.add_column(Column([card], width="md-4"))

page.add_content(Container([features_row], css_class="py-5"))

# Run the development server
page.run()
```

Run your page:
```bash
python my_first_page.py
```

Open your browser to `http://localhost:8000` and see your beautiful website!

## Next Steps

### 1. Explore Components
```python
# Try different components
page.add_content(Alert("Success! You're using PyPage", "success"))
page.add_content(Badge("New Feature", "primary"))

# Add a navigation bar
nav_links = [
    {"url": "/", "text": "Home"},
    {"url": "/about", "text": "About"},
    {"url": "/contact", "text": "Contact"}
]
page.add_navbar(nav_links, brand="My Website")
```

### 2. Add Dark Mode
```python
# Enable dark mode toggle
page.add_content(DarkModeToggle(position="top-right"))
```

### 3. Create Forms
```python
# Build interactive forms
form = Form(action="/submit", method="POST")
form.add_field(Input("name", "text", placeholder="Your Name", required=True))
form.add_field(Input("email", "email", placeholder="Your Email", required=True))
form.add_field(TextArea("message", placeholder="Your Message", rows=4))
form.add_field(Button("Send Message", "submit", css_class="btn btn-primary"))

page.add_content(Container([form], css_class="py-5"))
```

### 4. Add Animations
```python
# Animate your content
animated_section = FadeIn(
    Container([
        Heading("Smooth Animations", 2),
        Paragraph("Content that appears with beautiful transitions")
    ])
)
page.add_content(animated_section)
```

### 5. Export Your Page
```python
# Save as HTML file
page.save_to_file("my_website.html")

# Export as PDF (requires weasyprint)
page.to_pdf("my_website.pdf")

# Serialize to JSON
json_data = page.to_json()
```

## Project Templates

Use the CLI to create different project types:

### Basic Website
```bash
pypage create my-website --template basic
```

### Flask Application
```bash
pypage create my-app --template flask
```

### Full-Featured Project
```bash
pypage create my-project --template full
```

## What's Next?

- **[📚 Component Reference](component_reference.md)** - Learn about all available components
- **[🎨 Theming Guide](themes.md)** - Customize the look and feel
- **[📱 Responsive Design](responsive.md)** - Create mobile-friendly layouts
- **[🌙 Dark Mode](dark-mode.md)** - Implement dark mode support
- **[💡 Examples](examples/)** - Explore real-world examples

## Need Help?

- **[❓ FAQ](faq.md)** - Common questions and solutions
- **[🎮 Interactive Playground](../test/)** - Test components live
- **[📺 Video Tutorials](tutorials/)** - Step-by-step guides

Happy coding with PyPage! 🎉