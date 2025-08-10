# ❓ Frequently Asked Questions

Common questions and solutions for PyPage development.

## Getting Started

### Q: What makes PyPage different from other HTML generators?

**A:** PyPage combines the power of Python with modern web standards:
- **Component-based architecture** - Reusable, modular design
- **Built-in responsive design** - Mobile-first Bootstrap integration
- **Advanced features** - Dark mode, animations, charts out of the box
- **Production-ready** - PDF export, SEO optimization, accessibility tools
- **Developer-friendly** - Type hints, comprehensive documentation, CLI tools

### Q: Do I need to know HTML/CSS to use PyPage?

**A:** No! PyPage abstracts HTML/CSS complexity:
```python
# Instead of writing HTML/CSS
# <div class="card shadow-sm">
#   <h3 class="card-title">Hello</h3>
# </div>

# Just write Python
Card([Heading("Hello", 3)], css_class="shadow-sm")
```

However, basic HTML/CSS knowledge helps with customization.

### Q: Can I use PyPage with existing web frameworks?

**A:** Absolutely! PyPage integrates seamlessly:

**Flask Integration:**
```python
from flask import Flask
from pypage import Page, Heading

app = Flask(__name__)

@app.route('/')
def home():
    page = Page("My App")
    page.add_content(Heading("Welcome!", 1))
    return page.generate_html()
```

**Django Integration:**
```python
from django.http import HttpResponse
from pypage import Page

def home(request):
    page = Page("My Site")
    return HttpResponse(page.generate_html())
```

## Installation & Setup

### Q: I'm getting import errors. What's wrong?

**A:** Common solutions:

1. **Check your installation:**
```bash
pip list | grep pypage
```

2. **Reinstall with full features:**
```bash
pip uninstall pypage
pip install pypage[full]
```

3. **Virtual environment issues:**
```bash
which python
# Make sure you're in the right environment
```

### Q: How do I install optional dependencies?

**A:** Use extras during installation:
```bash
# For PDF export
pip install pypage[pdf]

# For charts and visualization
pip install pypage[charts]

# For development tools
pip install pypage[dev]

# Everything
pip install pypage[full]
```

### Q: PyPage is slow to import. How can I speed it up?

**A:** Use selective imports:
```python
# Instead of importing everything
from pypage import *

# Import only what you need
from pypage import Page, Card, Heading, Button
```

## Components & Usage

### Q: How do I create responsive layouts?

**A:** Use the Grid system:
```python
# Responsive columns
row = Row()
row.add_column(Column([
    Heading("Mobile: Full width", 3),
    Paragraph("Desktop: Half width")
], width="md-6"))  # 50% width on medium+ screens

row.add_column(Column([
    Heading("Second column", 3)
], width="md-6"))

page.add_content(row)
```

### Q: How do I add custom CSS?

**A:** Multiple approaches:

**1. CSS Builder (Recommended):**
```python
from pypage import CSSBuilder

css = CSSBuilder()
css.add_rule('.custom-button', {
    'background': 'linear-gradient(45deg, #ff6b6b, #4ecdc4)',
    'border': 'none',
    'color': 'white'
})

page.custom_css = css.render()
```

**2. Direct CSS:**
```python
page.custom_css = """
.custom-button {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    border: none;
    color: white;
}
"""
```

### Q: How do I handle forms and user input?

**A:** Use Form components with validation:
```python
form = Form(action="/submit", method="POST")

# Add fields with validation
form.add_field(Input("email", "email", placeholder="Email", required=True))
form.add_field(Input("password", "password", placeholder="Password", required=True))

# Custom validation
email_field = Input("email", "email")
email_field.add_validation("email", True)
email_field.add_validation("required", True)

form.add_field(Button("Submit", "submit", css_class="btn btn-primary"))
```

### Q: How do I create interactive components?

**A:** Add JavaScript event handlers:
```python
# Button with click handler
button = Button("Click Me", "button")
button.on_click = "alert('Hello from PyPage!')"

# Form with submit handler
form = Form()
form.on_submit = "return validateForm(this)"

# Custom JavaScript
page.custom_js = """
function validateForm(form) {
    // Your validation logic
    return true;
}
"""
```

## Styling & Themes

### Q: How do I implement dark mode?

**A:** PyPage has built-in dark mode support:
```python
# Add dark mode toggle
page.add_content(DarkModeToggle(position="top-right"))

# Customize dark mode styles
css = CSSBuilder()
css.add_rule('[data-theme="dark"] .custom-card', {
    'background-color': '#2d2d2d',
    'color': '#ffffff'
})
```

### Q: Can I use other CSS frameworks besides Bootstrap?

**A:** Yes! Change the theme:
```python
# Material Design
page = Page("My Site", theme="material")

# Tailwind CSS
page = Page("My Site", theme="tailwind")

# Bulma
page = Page("My Site", theme="bulma")

# Custom theme
page = Page("My Site", theme="custom")
page.custom_css = your_custom_css
```

### Q: How do I create animations?

**A:** Use animation components:
```python
# Fade in animation
animated_content = FadeIn(
    Card([Heading("Smooth entrance", 3)]),
    duration=500,
    delay=200
)

# Slide up animation
slide_content = SlideUp(
    Container([Paragraph("Slides up smoothly")]),
    distance=50
)

# Scroll-triggered animations
scroll_animation = AnimateOnScroll(
    Heading("Appears on scroll", 2),
    animation="fadeIn",
    trigger_offset=100
)
```

## Advanced Features

### Q: How do I export pages as PDF?

**A:** Use the built-in PDF export:
```python
# Install PDF dependencies first
# pip install pypage[pdf]

page = Page("My Document")
page.add_content(Heading("PDF Content", 1))

# Export as PDF
page.to_pdf("my_document.pdf")

# With custom options
page.to_pdf("styled.pdf", options={
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in'
})
```

### Q: How do I create charts and data visualizations?

**A:** Use chart components:
```python
# Install chart dependencies
# pip install pypage[charts]

# Create chart data
data = {
    "labels": ["January", "February", "March", "April"],
    "datasets": [{
        "label": "Sales",
        "data": [10, 19, 3, 5],
        "backgroundColor": "rgba(54, 162, 235, 0.2)",
        "borderColor": "rgba(54, 162, 235, 1)"
    }]
}

# Add chart to page
chart = BarChart("sales-chart", data)
page.add_content(chart)
```

### Q: How do I create plugins and custom components?

**A:** Use the plugin system:
```python
from pypage.plugins import register_component

@register_component
class MyCustomCard(ComponentBase):
    def __init__(self, title, content, color="primary"):
        self.title = title
        self.content = content
        self.color = color
    
    def render(self):
        return f"""
        <div class="custom-card border-{self.color}">
            <h4>{self.title}</h4>
            <p>{self.content}</p>
        </div>
        """

# Use your custom component
custom = MyCustomCard("My Title", "My content", "success")
page.add_content(custom)
```

## Performance & Production

### Q: How can I optimize PyPage performance?

**A:** Several optimization strategies:

1. **Use selective imports:**
```python
from pypage import Page, Card  # Only what you need
```

2. **Enable caching:**
```python
page = Page("My Site")
page.enable_caching = True
```

3. **Minimize CSS/JS:**
```python
page.minify_assets = True
```

4. **Use CDN for assets:**
```python
page.use_cdn = True
```

### Q: Is PyPage suitable for production?

**A:** Yes! PyPage is production-ready:
- **Performance optimized** - Efficient HTML generation
- **SEO friendly** - Proper meta tags and structure  
- **Accessible** - WCAG compliance tools
- **Scalable** - Works with any Python web framework
- **Secure** - No client-side vulnerabilities

### Q: How do I deploy PyPage applications?

**A:** Works with any Python deployment:

**Heroku:**
```python
# Procfile
web: gunicorn app:app

# requirements.txt
pypage[full]
flask
gunicorn
```

**Docker:**
```dockerfile
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Troubleshooting

### Q: My styles aren't applying. What's wrong?

**A:** Check these common issues:

1. **CSS specificity:**
```python
# Use more specific selectors
css.add_rule('.my-page .custom-button', styles)
```

2. **CSS order:**
```python
# Add !important for overrides
css.add_rule('.custom', {'color': 'red !important'})
```

3. **Theme conflicts:**
```python
# Check if theme styles override yours
page.set_theme('minimal')  # Try minimal theme
```

### Q: JavaScript isn't working. How do I debug?

**A:** Debug JavaScript issues:

1. **Check browser console** for errors
2. **Verify script placement:**
```python
# Add scripts at the end
page.custom_js = "console.log('Script loaded');"
```

3. **Use development mode:**
```python
page.debug_mode = True
page.run()  # Check console output
```

### Q: How do I report bugs or get help?

**A:** Multiple support channels:

1. **Check this FAQ** first
2. **Search existing issues** on GitHub
3. **Interactive playground** - Test components at `/test`
4. **Create detailed bug reports** with:
   - Python version
   - PyPage version
   - Minimal reproduction code
   - Expected vs actual behavior

### Q: Can I contribute to PyPage?

**A:** We welcome contributions!

1. **Fork the repository**
2. **Install development dependencies:**
```bash
pip install pypage[dev]
```

3. **Make your changes**
4. **Run tests:**
```bash
pytest
```

5. **Submit a pull request**

For more help, visit our [documentation](.) or [interactive playground](../test/).