# Enhanced HTML Generator Library - Feature Guide

## Overview

This document describes all the enhanced features added to the HTML generator library, including forms, layout systems, styling, templating, component inheritance, themes, and JavaScript hooks.

## Table of Contents

1. [Enhanced Form Support](#enhanced-form-support)
2. [Layout System](#layout-system)
3. [Style Customization](#style-customization)
4. [Templating System](#templating-system)
5. [Component Inheritance](#component-inheritance)
6. [Built-in Themes](#built-in-themes)
7. [JavaScript Hooks & Events](#javascript-hooks--events)
8. [Advanced Components](#advanced-components)

## Enhanced Form Support

### Basic Form Usage

```python
from html_generator import Form, Input, Button, TextArea, Select

# Create a form
form = Form(action="/submit", method="POST", id_attr="contact-form")

# Add form fields
form.add_field(Input("text", "name", placeholder="Your name", required=True, label="Full Name"))
form.add_field(Input("email", "email", placeholder="your@email.com", required=True, label="Email"))
form.add_field(TextArea("message", placeholder="Your message...", rows=5, cols=50, label="Message"))

# Select with multiple options
options = [
    {"value": "web", "text": "Web Development"},
    {"value": "mobile", "text": "Mobile App Development"}
]
form.add_field(Select("services", options, multiple=True, label="Services"))

# Submit button
form.add_field(Button("Submit", "submit", css_class="btn-primary"))
```

### Form Components

#### Input
- **Types**: text, email, password, tel, url, number, date, etc.
- **Features**: placeholder, required validation, labels, custom CSS
- **Example**: `Input("email", "user_email", placeholder="Enter email", required=True, label="Email Address")`

#### TextArea
- **Features**: rows, cols, placeholder, labels, validation
- **Example**: `TextArea("comments", rows=5, cols=50, placeholder="Enter your comments...")`

#### Select
- **Features**: multiple selection, options with values and text, labels
- **Example**: `Select("categories", options, multiple=True, label="Choose categories")`

#### Button
- **Types**: submit, button, reset
- **Features**: custom styling, JavaScript events
- **Example**: `Button("Save", "submit", css_class="btn-success")`

## Layout System

### Row and Column System

```python
from html_generator import Row, Column

# Create a responsive row
row = Row()

# Add columns with different widths
col1 = Column(width="md-4")  # Bootstrap column classes
col2 = Column(width="md-8")

# Add content to columns
col1.add_content("Left column content")
col2.add_content("Right column content")

# Add columns to row
row.add_column(col1)
row.add_column(col2)
```

### Flexbox Layout

```python
from html_generator import Flex, Badge

# Create a flex container
flex_container = Flex(
    direction="row",        # row, column, row-reverse, column-reverse
    justify="center",       # start, end, center, between, around, evenly
    align="center",         # start, end, center, baseline, stretch
    wrap=True              # Enable flex-wrap
)

# Add items to flex container
flex_container.add_item(Badge("New", "primary"))
flex_container.add_item(Badge("Featured", "success"))
```

## Style Customization

### Inline Styles and CSS Classes

```python
from html_generator import Div

# Using class_name parameter (alias for css_class)
div1 = Div("Content", class_name="custom-class border rounded")

# Using inline styles
div2 = Div("Styled content", css_class="p-3")
div2.set_style("background: linear-gradient(45deg, #667eea, #764ba2); color: white;")
div2.add_style("box-shadow: 0 4px 6px rgba(0,0,0,0.1);")

# Method chaining for styles
div3 = Div("Chained styling").set_style("padding: 20px;").add_class("text-center")
```

### Available Style Methods

- `set_style(style)` - Set inline CSS styles
- `add_style(style)` - Add to existing inline styles
- `add_class(css_class)` - Add CSS classes
- `set_attribute(name, value)` - Set any HTML attribute

## Templating System

### Creating Templates

```python
from html_generator import Template, TemplateManager

# Create a template
hero_template = Template("hero", """
<div class="hero-section bg-primary text-white text-center py-5">
    <div class="container">
        <h1 class="display-4">{{ title }}</h1>
        <p class="lead">{{ subtitle }}</p>
        <div class="hero-actions">{{ actions }}</div>
    </div>
</div>
""")

# Define slots with defaults
hero_template.define_slot("title", "Welcome")
hero_template.define_slot("subtitle", "Your amazing website")
hero_template.define_slot("actions", "")
```

### Using Templates

```python
# Create template manager
template_manager = TemplateManager()
template_manager.register_template(hero_template)

# Use template with custom content
hero_content = template_manager.render_template("hero", {
    "title": "Welcome to Our Platform",
    "subtitle": "Build amazing websites",
    "actions": '<a href="#" class="btn btn-light">Get Started</a>'
})

# Add to page
page.add_content(hero_content)
```

### Predefined Templates

The library includes several predefined templates:

```python
from html_generator import create_hero_template, create_card_grid_template, create_footer_template

# Get predefined templates
hero = create_hero_template()
card_grid = create_card_grid_template()
footer = create_footer_template()
```

## Component Inheritance

### Creating Custom Components

```python
from html_generator import ComponentBase, Container

class CustomCard(ComponentBase):
    def __init__(self, title, content, highlight=False):
        super().__init__(css_class="custom-card")
        
        card_class = "card border-primary" if highlight else "card"
        card_html = f'''
        <div class="{card_class}">
            <div class="card-header">
                <h5>{title}</h5>
            </div>
            <div class="card-body">
                {content}
            </div>
        </div>
        '''
        self.content = card_html

# Usage
custom_card = CustomCard("My Title", "My content", highlight=True)
```

### Extending Existing Components

```python
from html_generator import Container

class HeroSection(Container):
    def __init__(self, title, subtitle, button_text="", button_url="#"):
        super().__init__(css_class="hero-section bg-primary text-white text-center py-5")
        
        self.add_content(f'<h1 class="display-4">{title}</h1>')
        self.add_content(f'<p class="lead">{subtitle}</p>')
        
        if button_text:
            self.add_content(f'<a href="{button_url}" class="btn btn-light btn-lg">{button_text}</a>')

# Usage
hero = HeroSection("Welcome", "Build amazing websites", "Get Started", "/signup")
```

## Built-in Themes

### Setting Page Themes

```python
from html_generator import Page

page = Page("My Site", "Welcome")

# Available themes
page.set_theme("bootstrap")        # Default dark Bootstrap theme
page.set_theme("bootstrap-light")  # Light Bootstrap theme
page.set_theme("tailwind")         # Tailwind CSS
page.set_theme("bulma")           # Bulma CSS framework
page.set_theme("material")        # Material Design

# Custom CSS
page.add_css_link("https://example.com/custom.css")
```

### Theme Features

- **Bootstrap**: Full Bootstrap 5 with dark/light variants
- **Tailwind**: Utility-first CSS framework
- **Bulma**: Modern CSS framework
- **Material**: Google Material Design components

## JavaScript Hooks & Events

### Event Handling

```python
from html_generator import Button, Div, Input

# Button with click event
button = Button("Click me", "button")
button.on_click("alert('Button clicked!')")

# Input with change event
input_field = Input("text", "username")
input_field.on_change("console.log('Input changed:', this.value)")

# Div with hover effects
div = Div("Hover over me")
div.on_hover("this.style.backgroundColor = '#f0f0f0'")

# Custom events
button.set_event("ondblclick", "console.log('Double clicked!')")
```

### Available Event Methods

- `on_click(handler)` - Mouse click events
- `on_submit(handler)` - Form submission
- `on_change(handler)` - Input value changes
- `on_hover(handler)` - Mouse hover (onmouseover)
- `set_event(event, handler)` - Any JavaScript event

## Advanced Components

### Alert Component

```python
from html_generator import Alert

# Basic alert
alert = Alert("Success! Your data has been saved.", "success")

# Dismissible alert
dismissible_alert = Alert("Warning! Check your input.", "warning", dismissible=True)

# Alert types: primary, secondary, success, danger, warning, info, light, dark
```

### Badge Component

```python
from html_generator import Badge

badge = Badge("New", "primary")
badge_secondary = Badge("42", "secondary")
```

### Progress Bar

```python
from html_generator import ProgressBar

# Basic progress bar
progress = ProgressBar(65, label="65% Complete")

# Styled progress bar
progress_fancy = ProgressBar(80, bar_type="success", striped=True, animated=True)
```

### Accordion

```python
from html_generator import Accordion

accordion = Accordion("my-accordion")
accordion.add_item("What is this?", "This is an accordion component.", expanded=True)
accordion.add_item("How does it work?", "Click to expand and collapse sections.")
accordion.add_item("Can I customize it?", "Yes, it's fully customizable.")
```

### Modal

```python
from html_generator import Modal, Button

# Create modal
modal = Modal("demo-modal", "Modal Title", "Modal content goes here...",
              footer='<button class="btn btn-primary">Save</button>')

# Button to trigger modal
trigger_btn = Button("Open Modal", "button", css_class="btn-primary")
trigger_btn.set_attribute("data-bs-toggle", "modal")
trigger_btn.set_attribute("data-bs-target", "#demo-modal")
```

### Navigation Bar

```python
from html_generator import Navbar

nav_items = [
    {"text": "Home", "url": "/"},
    {"text": "About", "url": "/about"},
    {"text": "Contact", "url": "/contact"}
]

navbar = Navbar("My Brand", "/", nav_items, theme="dark")
```

## Complete Example

Here's a comprehensive example using multiple features:

```python
from html_generator import *

# Create page with theme
page = Page("Enhanced Demo", "Feature Showcase")
page.set_theme("bootstrap")

# Create template manager
template_manager = TemplateManager()
template_manager.register_template(create_hero_template())
page.use_template_manager(template_manager)

# Add hero section using template
page.use_template("hero", {
    "title": "Enhanced HTML Generator",
    "subtitle": "Build modern websites with Python",
    "actions": '<a href="#features" class="btn btn-light btn-lg">Explore Features</a>'
})

# Layout with features
feature_row = Row()

# Feature cards
features = [
    ("Easy Forms", "Create complex forms with validation", "fas fa-wpforms"),
    ("Responsive Layout", "Built-in grid and flexbox support", "fas fa-th-large"),
    ("Rich Components", "Modals, alerts, progress bars, and more", "fas fa-puzzle-piece")
]

for title, desc, icon in features:
    col = Column(width="md-4")
    col.add_content(FeatureCard(title, desc, icon))
    feature_row.add_column(col)

# Contact form
form = Form(action="/contact", method="POST")
form.add_field(Input("text", "name", placeholder="Your name", required=True, label="Name"))
form.add_field(Input("email", "email", placeholder="Email", required=True, label="Email"))
form.add_field(TextArea("message", placeholder="Message...", rows=4, label="Message"))
form.add_field(Button("Send Message", "submit", css_class="btn-primary"))

# Add everything to page
container = Container()
container.add_content(feature_row)
container.add_content(Section([Heading("Contact Us", 2), form], css_class="mt-5"))

page.add_content(container)

# Generate HTML
with open("demo.html", "w") as f:
    f.write(page.generate_html())
```

## Migration Guide

### From Basic to Enhanced

If you're upgrading from the basic version:

1. **Forms**: Replace basic form elements with enhanced versions that support labels and validation
2. **Layout**: Use `Row` and `Column` instead of manual div structures
3. **Styling**: Use `class_name` parameter and style methods instead of manual CSS
4. **Components**: Replace custom HTML with built-in components like `Alert`, `Badge`, `Modal`
5. **Themes**: Use `page.set_theme()` instead of manual CSS framework links

### Backward Compatibility

All existing code will continue to work. New features are additive and don't break existing functionality.

## Performance Tips

1. **Template Reuse**: Register templates once and reuse them multiple times
2. **Component Inheritance**: Create base components for frequently used patterns
3. **CSS Frameworks**: Use built-in themes instead of loading multiple CSS files
4. **Event Delegation**: Use efficient JavaScript event handlers

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure to import new components: `from html_generator import Row, Column, Flex`
2. **Template Slots**: Ensure slot names in templates match the keys in slot_map
3. **Bootstrap Dependencies**: Some components require Bootstrap JavaScript for full functionality
4. **Event Handlers**: JavaScript events require proper escaping of quotes

### Debug Tips

1. Use `element.render()` to see generated HTML for individual components
2. Check browser console for JavaScript errors
3. Validate HTML output with online validators
4. Test responsive behavior with browser developer tools

## API Reference

For complete API documentation, see the docstrings in each module:

- `html_generator.forms` - Form components
- `html_generator.layout` - Layout system
- `html_generator.templates` - Template system
- `html_generator.components` - Advanced components
- `html_generator.elements` - Base elements with enhanced features
- `html_generator.page` - Page management with theme support