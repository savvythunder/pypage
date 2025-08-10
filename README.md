# PyPage - Enhanced HTML Generator Library

PyPage is a comprehensive Python library for generating HTML programmatically with advanced features including dark mode, animations, responsive design, and modern UI components.

## 🚀 Features

- **Modern Components**: Comprehensive set of HTML components with Bootstrap 5 integration
- **Dark Mode**: Built-in dark mode support with system preference detection
- **Animations**: Smooth animations and transitions (fade, slide, scroll effects)
- **Responsive Design**: Mobile-first responsive components
- **Data Visualization**: Charts, graphs, and KPI cards
- **Advanced Forms**: Complete form system with validation
- **CSS Builder**: Programmatic CSS generation with responsive breakpoints
- **Export Tools**: PDF and JSON export capabilities
- **Plugin System**: Extensible architecture for custom components
- **Flask Integration**: Seamless integration with Flask applications

## 📦 Installation

```bash
# Basic installation
pip install pypage

# With PDF export support
pip install pypage[pdf]

# With chart support
pip install pypage[charts]

# Full installation with all features
pip install pypage[full]
```

## 🎯 Quick Start

```python
from pypage import *

# Create a new page
page = Page("My Website", "Welcome to PyPage!")

# Add content
page.add_content(Heading("Hello, World!", 1))
page.add_content(Paragraph("Build amazing websites with Python."))

# Add a styled card
card = Card([
    Heading("Getting Started", 3),
    Paragraph("PyPage makes HTML generation simple and powerful."),
    Button("Learn More", "button", css_class="btn-primary")
])
page.add_content(card)

# Generate HTML
html = page.generate_html()
print(html)
```

## 🌟 Advanced Features

### Dark Mode Support
```python
page = Page("Dark Mode Demo", "Theme Switching")
page.add_content(DarkModeToggle(position="top-right"))
page.add_content(Heading("Dark Mode Ready!", 1))
```

### Animations
```python
# Fade in animation
animated_content = FadeIn(
    Container([
        Heading("Smooth Animations", 2),
        Paragraph("Content that fades in beautifully.")
    ])
)
page.add_content(animated_content)
```

### Responsive Layout
```python
row = Row()
row.add_column(Column([
    Heading("Left Column", 3),
    Paragraph("Responsive content here.")
], width="md-6"))
row.add_column(Column([
    Heading("Right Column", 3), 
    Paragraph("More responsive content.")
], width="md-6"))
page.add_content(row)
```

### Data Visualization
```python
# Create a chart
chart_data = {
    "labels": ["Jan", "Feb", "Mar", "Apr"],
    "datasets": [{
        "label": "Sales",
        "data": [10, 19, 3, 5]
    }]
}
chart = BarChart("sales-chart", chart_data)
page.add_content(chart)
```

## 🛠️ CLI Tools

PyPage includes command-line tools for project generation:

```bash
# Create a new project
pypage create myproject

# Create a Flask project
pypage create myapp --template flask

# Generate documentation
pypage docs
```

## 📚 Component Library

PyPage includes a comprehensive set of components:

### Core Components
- `Page` - Main page container with theme support
- `Container`, `Div`, `Section` - Layout containers  
- `Heading`, `Paragraph` - Typography elements
- `Image`, `Link` - Media and navigation
- `Card` - Content cards with styling

### Form Components
- `Form` - Form container with validation
- `Input` - Text, email, password, and other input types
- `TextArea` - Multi-line text input
- `Select` - Dropdown with single/multiple selection
- `Button` - Submit and action buttons

### Layout System
- `Row`, `Column` - Responsive grid system
- `Flex` - Flexbox layouts
- `Navbar` - Navigation with dropdown support

### Advanced Components
- `Modal`, `Alert`, `Badge` - Interactive elements
- `Table`, `Tabs`, `Carousel` - Data display
- `ProgressBar`, `Accordion` - UI components
- `Chart`, `KPICard` - Data visualization

## 🎨 Styling and Themes

PyPage uses Bootstrap 5 by default with a custom dark theme:

```python
# Set theme
page.set_theme('bootstrap')  # or 'material', 'tailwind'

# Custom CSS
css_builder = CSSBuilder()
css_builder.add_rule('.custom', {
    'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'color': 'white'
})
page.custom_css = css_builder.render()
```

## 🧪 Testing

The library includes a comprehensive testing application:

```bash
cd testing
python app.py
```

Visit `http://localhost:5001` to run interactive tests and see component demonstrations.

## 📖 Documentation

- **Getting Started**: See the `docs/getting-started.md` guide
- **API Reference**: Complete API documentation in `docs/`
- **Examples**: Example projects in the `examples/` directory
- **Testing**: Interactive testing application in `testing/`

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- Bootstrap team for the excellent CSS framework
- Flask community for web framework inspiration
- All contributors who have helped improve PyPage

---

**PyPage** - Making HTML generation simple, powerful, and beautiful.