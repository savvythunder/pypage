# Core Components

The HTML Generator library provides a comprehensive set of core components that form the foundation of your web applications. These components are designed with modern web standards, accessibility, and performance in mind.

## Page Component

The `Page` component is the root container for your HTML documents, providing structure and metadata management.

### Basic Usage

```python
from html_generator import Page

# Create a basic page
page = Page("My Application", "Welcome to my app")

# Add content
page.add_content(Heading("Hello World", level=1))
page.add_content(Paragraph("This is a generated webpage."))

# Generate HTML
html = page.generate_html()
print(html)
```

### Advanced Configuration

```python
# Page with custom settings
page = Page(
    title="Advanced Application",
    description="Feature-rich web application",
    favicon="/static/favicon.ico",
    lang="en",
    viewport="width=device-width, initial-scale=1.0"
)

# Set theme and framework
page.set_theme('bootstrap')  # bootstrap, tailwind, bulma, material

# Add metadata
page.set_meta_description("Comprehensive web application built with HTML Generator")
page.set_meta_keywords(["web", "application", "python", "html"])
page.add_canonical_url("https://example.com/my-app")

# Custom CSS and JavaScript
page.add_css_link("/static/css/custom.css")
page.add_js_script("/static/js/app.js", defer=True)

# Inline styles and scripts
page.add_custom_css("""
.custom-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
}
""")
```

### Page Methods

```python
# Content management
page.add_content(component)          # Add single component
page.add_multiple_content([c1, c2])  # Add multiple components
page.insert_content(index, component) # Insert at specific position
page.remove_content(component)       # Remove component

# Styling and assets
page.add_css_link(href, media="all")
page.add_js_script(src, async=False, defer=False)
page.add_preload(href, as_type, type=None)

# SEO and metadata
page.set_title(title)
page.set_meta_description(description)
page.add_meta_tag(name, content)
page.add_schema_markup(data)

# Advanced features
page.enable_dark_mode()
page.enable_debug_view()
page.run()  # Open in browser
```

## Basic Elements

### Heading Component

```python
from html_generator import Heading

# Different heading levels
h1 = Heading("Main Title", level=1)
h2 = Heading("Section Title", level=2, css_class="text-primary")
h3 = Heading("Subsection", level=3, id="subsection-1")

# With custom styling
styled_heading = Heading("Custom Heading", level=2)
styled_heading.add_style("color", "#007bff")
styled_heading.add_style("font-weight", "600")
```

### Paragraph Component

```python
from html_generator import Paragraph

# Basic paragraph
p1 = Paragraph("This is a simple paragraph.")

# Paragraph with styling
p2 = Paragraph("Important notice", css_class="alert alert-info")

# Paragraph with inline elements
p3 = Paragraph([
    "This paragraph contains ",
    Link("https://example.com", "a link"),
    " and ",
    Element("strong", content="bold text"),
    "."
])
```

### Link Component

```python
from html_generator import Link

# External link
external = Link("https://example.com", "Visit Example")

# Internal link
internal = Link("/about", "About Us")

# Link with attributes
email_link = Link("mailto:contact@example.com", "Contact Us")
email_link.set_attribute("target", "_blank")
email_link.set_attribute("rel", "noopener noreferrer")

# Button-styled link
button_link = Link("/signup", "Sign Up", css_class="btn btn-primary")
```

### Image Component

```python
from html_generator import Image

# Basic image
img = Image("photo.jpg", "Description of the photo")

# Responsive image with multiple sources
responsive_img = Image(
    src="large.jpg",
    alt="Responsive image",
    css_class="img-fluid"
)
responsive_img.set_attribute("srcset", "small.jpg 480w, medium.jpg 768w, large.jpg 1200w")
responsive_img.set_attribute("sizes", "(max-width: 768px) 100vw, 50vw")

# Lazy-loaded image
lazy_img = Image("heavy-image.jpg", "Large image")
lazy_img.set_attribute("loading", "lazy")
lazy_img.set_attribute("decoding", "async")
```

## Container Components

### Generic Container

```python
from html_generator import Container

# Basic container
container = Container()
container.add_content(Heading("Section Title", 2))
container.add_content(Paragraph("Section content here."))

# Container with CSS classes
section = Container(css_class="container-fluid bg-light p-4")

# Semantic container
main_content = Container(tag='main', css_class="main-content")
sidebar = Container(tag='aside', css_class="sidebar")
```

### Div Component

```python
from html_generator import Div

# Basic div
div = Div(content=[
    Heading("Card Title", 3),
    Paragraph("Card content")
], css_class="card")

# Div with custom attributes
wrapper = Div(css_class="wrapper")
wrapper.set_attribute("data-component", "gallery")
wrapper.set_attribute("role", "region")
wrapper.set_attribute("aria-label", "Photo gallery")
```

### Section Component

```python
from html_generator import Section

# Semantic section
hero_section = Section(css_class="hero-section")
hero_section.add_content(Container([
    Heading("Welcome to Our Site", 1),
    Paragraph("Discover amazing features and functionality."),
    Link("/learn-more", "Learn More", css_class="btn btn-primary")
]))
```

## List Components

### HTML Lists

```python
from html_generator import HtmlList

# Unordered list
ul = HtmlList([
    "First item",
    "Second item", 
    "Third item"
], list_type="ul")

# Ordered list with custom styling
ol = HtmlList([
    "Step one: Prepare ingredients",
    "Step two: Mix thoroughly", 
    "Step three: Bake for 30 minutes"
], list_type="ol", css_class="procedure-list")

# Definition list
dl = HtmlList([
    {"term": "HTML", "definition": "HyperText Markup Language"},
    {"term": "CSS", "definition": "Cascading Style Sheets"},
    {"term": "JS", "definition": "JavaScript"}
], list_type="dl")

# Nested lists
nested_list = HtmlList([
    "Main item 1",
    HtmlList(["Sub item 1", "Sub item 2"]),
    "Main item 2"
])
```

## Card Component

The Card component provides a flexible content container with optional header and footer.

```python
from html_generator import Card

# Basic card
card = Card("Card Title", "This is the card content.")

# Card with custom styling
featured_card = Card(
    title="Featured Article",
    content="Discover the latest trends in web development.",
    css_class="card border-primary"
)

# Card with complex content
complex_card = Card("Product Details")
complex_card.add_content(Image("product.jpg", "Product image"))
complex_card.add_content(Paragraph("Detailed product description here."))
complex_card.add_content(Link("/buy-now", "Buy Now", css_class="btn btn-success"))

# Card with header and footer
full_card = Card(
    title="Complete Card",
    content="Main card content",
    css_class="card"
)
full_card.add_header(Paragraph("Card header content", css_class="card-header"))
full_card.add_footer(Paragraph("Card footer content", css_class="card-footer"))
```

## Styling and Customization

### CSS Classes

```python
# Add CSS classes
component = Paragraph("Text content")
component.add_class("text-center")
component.add_class("text-primary")
component.add_class("mb-3")

# Set multiple classes at once
component.set_css_class("text-center text-primary mb-3")

# Remove classes
component.remove_class("mb-3")
```

### Inline Styles

```python
# Add inline styles
element = Div("Content")
element.add_style("background-color", "#f8f9fa")
element.add_style("padding", "1rem")
element.add_style("border-radius", "0.5rem")

# Set multiple styles
element.set_style("background: #f8f9fa; padding: 1rem; border-radius: 0.5rem;")

# Style dictionary
styles = {
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "min-height": "100vh"
}
element.add_styles(styles)
```

### Custom Attributes

```python
# Set custom attributes
button = Element("button", content="Click Me")
button.set_attribute("type", "button")
button.set_attribute("data-toggle", "modal")
button.set_attribute("data-target", "#myModal")
button.set_attribute("aria-label", "Open modal dialog")

# Accessibility attributes
input_field = Element("input")
input_field.set_attribute("aria-required", "true")
input_field.set_attribute("aria-describedby", "help-text")
input_field.set_attribute("role", "textbox")
```

## Event Handling

### JavaScript Events

```python
# Click events
button = Element("button", content="Submit")
button.on_click("submitForm()")

# Form events
form = Element("form")
form.on_submit("return validateForm()")

# Mouse events
hover_div = Div("Hover me")
hover_div.on_hover("showTooltip()", "hideTooltip()")

# Change events
select = Element("select")
select.on_change("updateContent(this.value)")
```

### Custom Event Handlers

```python
# Complex event handling
interactive_element = Container()
interactive_element.set_attribute("onclick", """
    event.preventDefault();
    console.log('Element clicked');
    // Custom logic here
""")

# Event delegation
parent_container = Container()
parent_container.set_attribute("onclick", """
    if (event.target.matches('.clickable-item')) {
        handleItemClick(event.target);
    }
""")
```

## Responsive Design

### Bootstrap Integration

```python
# Bootstrap grid system
row = Container(css_class="row")

col1 = Container(css_class="col-md-6")
col1.add_content(Heading("Left Column", 3))
col1.add_content(Paragraph("Content for left column."))

col2 = Container(css_class="col-md-6")
col2.add_content(Heading("Right Column", 3))
col2.add_content(Paragraph("Content for right column."))

row.add_content(col1)
row.add_content(col2)

# Responsive utilities
mobile_only = Paragraph("Visible on mobile only", css_class="d-block d-md-none")
desktop_only = Paragraph("Visible on desktop only", css_class="d-none d-md-block")
```

### Custom Responsive Design

```python
# Add responsive CSS
page.add_custom_css("""
@media (max-width: 768px) {
    .responsive-section {
        padding: 1rem;
        font-size: 0.9rem;
    }
}

@media (min-width: 769px) {
    .responsive-section {
        padding: 2rem;
        font-size: 1rem;
    }
}
""")

# Use responsive classes
responsive_section = Section(css_class="responsive-section")
```

## Accessibility Features

### Semantic HTML

```python
# Use proper semantic elements
header = Container(tag="header")
nav = Container(tag="nav", css_class="navbar")
main = Container(tag="main", css_class="main-content")
aside = Container(tag="aside", css_class="sidebar")
footer = Container(tag="footer", css_class="site-footer")

# Heading hierarchy
page.add_content(Heading("Page Title", 1))  # Only one H1
page.add_content(Heading("Section", 2))
page.add_content(Heading("Subsection", 3))
```

### ARIA Labels

```python
# Accessible form
form_container = Container()
form_container.set_attribute("role", "form")
form_container.set_attribute("aria-label", "Contact form")

# Accessible navigation
nav_menu = Container(tag="nav")
nav_menu.set_attribute("role", "navigation")
nav_menu.set_attribute("aria-label", "Main navigation")

# Screen reader text
sr_text = Element("span", content="Opens in new window", css_class="visually-hidden")
external_link = Link("https://example.com", "External Site")
external_link.add_content(sr_text)
```

## Best Practices

### Component Organization

```python
# Create reusable component functions
def create_hero_section(title, subtitle, cta_text, cta_link):
    hero = Section(css_class="hero-section bg-primary text-white text-center py-5")
    container = Container(css_class="container")
    
    container.add_content(Heading(title, 1, css_class="display-4"))
    container.add_content(Paragraph(subtitle, css_class="lead"))
    container.add_content(Link(cta_link, cta_text, css_class="btn btn-light btn-lg"))
    
    hero.add_content(container)
    return hero

# Use in page
hero = create_hero_section(
    "Welcome to Our Platform", 
    "Build amazing web applications with ease",
    "Get Started",
    "/signup"
)
page.add_content(hero)
```

### Performance Optimization

```python
# Optimize images
optimized_image = Image("large-photo.jpg", "Photo description")
optimized_image.set_attribute("loading", "lazy")
optimized_image.set_attribute("decoding", "async")
optimized_image.set_attribute("width", "800")
optimized_image.set_attribute("height", "600")

# Preload critical resources
page.add_preload("/static/fonts/main.woff2", "font", "font/woff2")
page.add_preload("/static/images/hero.jpg", "image")

# Critical CSS
page.add_critical_css("""
.hero-section { 
    height: 100vh; 
    display: flex; 
    align-items: center; 
}
""")
```

### Error Handling

```python
# Safe content creation
def safe_create_component(component_type, content, **kwargs):
    try:
        if component_type == "heading":
            return Heading(content, **kwargs)
        elif component_type == "paragraph":
            return Paragraph(content, **kwargs)
        else:
            return Container(content=content, **kwargs)
    except Exception as e:
        # Log error and return fallback
        print(f"Error creating component: {e}")
        return Paragraph(f"Error: {str(e)}", css_class="text-danger")

# Use safe creation
safe_heading = safe_create_component("heading", "My Title", level=1)
```

## Next Steps

- Explore [Advanced Components](./advanced-components.md) for sophisticated UI elements
- Learn about [Modern UI Components](./ui-components.md) for interactive features
- Study [Layout System](../features/layout.md) for responsive design patterns
- Review [Styling Guide](../features/styling.md) for advanced customization techniques