# Modern UI Components

HTML Generator v3.0 introduces a comprehensive suite of modern UI components designed for contemporary web applications. These components provide interactive features, smooth animations, and accessibility compliance.

## Interactive Charts and Data Visualization

### InteractiveChart Component

Create dynamic, responsive charts powered by Chart.js:

```python
from html_generator import InteractiveChart

# Basic bar chart
chart_data = {
    'labels': ['January', 'February', 'March', 'April', 'May'],
    'datasets': [{
        'label': 'Sales ($)',
        'data': [12000, 19000, 3000, 5000, 2000],
        'backgroundColor': 'rgba(54, 162, 235, 0.5)',
        'borderColor': 'rgba(54, 162, 235, 1)',
        'borderWidth': 1
    }]
}

chart = InteractiveChart(
    chart_type='bar',
    data=chart_data,
    options={
        'responsive': True,
        'plugins': {
            'title': {
                'display': True,
                'text': 'Monthly Sales Report'
            }
        }
    }
)

page.add_content(chart)
```

### DataVisualization Component

Advanced data visualization with multiple chart types:

```python
from html_generator import DataVisualization

# Sales data
sales_data = [
    {'label': 'Q1', 'value': 15000},
    {'label': 'Q2', 'value': 23000},
    {'label': 'Q3', 'value': 18000},
    {'label': 'Q4', 'value': 31000}
]

# Create pie chart
pie_chart = DataVisualization(
    data=sales_data,
    chart_type='pie',
    title='Quarterly Sales Distribution'
)

# Create line chart
line_chart = DataVisualization(
    data=sales_data,
    chart_type='line',
    title='Sales Trend Over Time'
)

page.add_content(pie_chart)
page.add_content(line_chart)
```

## Advanced Form Builder

### AdvancedFormBuilder Component

Create sophisticated forms with real-time validation:

```python
from html_generator import AdvancedFormBuilder

# Create form builder
form = AdvancedFormBuilder(form_id='contact_form')

# Add fields with validation
form.add_field(
    field_type='text',
    name='full_name',
    label='Full Name',
    validation={
        'required': True,
        'minLength': 2,
        'maxLength': 50
    }
)

form.add_field(
    field_type='email',
    name='email',
    label='Email Address',
    validation={
        'required': True,
        'email': True
    }
)

form.add_field(
    field_type='select',
    name='department',
    label='Department',
    options={
        'options': [
            {'value': 'sales', 'text': 'Sales'},
            {'value': 'support', 'text': 'Support'},
            {'value': 'billing', 'text': 'Billing'}
        ]
    },
    validation={'required': True}
)

form.add_field(
    field_type='textarea',
    name='message',
    label='Message',
    options={'rows': 5},
    validation={
        'required': True,
        'minLength': 10,
        'maxLength': 500
    }
)

form.add_field(
    field_type='checkbox',
    name='newsletter',
    label='Subscribe to newsletter'
)

page.add_content(form)
```

### Form Validation Features

- **Real-time validation**: Instant feedback as users type
- **Custom validation rules**: Pattern matching, length constraints
- **Error messaging**: Clear, actionable error messages
- **Accessibility**: ARIA labels and screen reader support

## Micro-interactions and Animations

### MicroInteraction Component

Add engaging micro-interactions to any element:

```python
from html_generator import MicroInteraction, Button

# Create a button with hover animation
button = Button("Click Me!", "button", css_class="btn btn-primary")

# Add pulse animation on hover
interactive_button = MicroInteraction(
    element=button,
    interaction_type='hover',
    animation='pulse'
)

page.add_content(interactive_button)

# Bounce animation on click
bounce_card = MicroInteraction(
    element=Card("Clickable Card", "Click me for a bounce!"),
    interaction_type='click',
    animation='bounce'
)

page.add_content(bounce_card)
```

### Available Animations

- **pulse**: Gentle scaling effect
- **bounce**: Bouncing motion
- **shake**: Horizontal shake
- **glow**: Glowing border effect

### Custom Animation CSS

```python
# Add custom CSS for animations
page.add_custom_css("""
.custom-slide {
    transform: translateX(-100%);
    transition: transform 0.5s ease;
}

.custom-slide.active {
    transform: translateX(0);
}
""")
```

## Accessibility Compliance Checker

### AccessibilityChecker Component

Built-in accessibility compliance checking:

```python
from html_generator import AccessibilityChecker

# Add accessibility checker to your page
a11y_checker = AccessibilityChecker()
page.add_content(a11y_checker)
```

### Accessibility Features Checked

1. **Alt Text for Images**: Ensures all images have descriptive alt text
2. **Color Contrast**: Verifies WCAG contrast ratios
3. **Keyboard Navigation**: Checks tab order and focus management
4. **Semantic HTML**: Validates proper heading structure
5. **Focus Indicators**: Ensures visible focus states
6. **ARIA Labels**: Verifies screen reader compatibility

### Manual Accessibility Improvements

```python
# Proper heading hierarchy
page.add_content(Heading("Main Title", level=1))
page.add_content(Heading("Section Title", level=2))
page.add_content(Heading("Subsection", level=3))

# Images with alt text
image = Image(
    src="chart.png",
    alt="Bar chart showing 25% increase in sales over last quarter"
)

# ARIA labels for interactive elements
button = Button("Submit Form", "submit")
button.set_attribute("aria-label", "Submit contact form")
button.set_attribute("aria-describedby", "form-help-text")

# Focus management
modal = Modal("Important Notice", "This is critical information")
modal.set_attribute("aria-modal", "true")
modal.set_attribute("role", "dialog")
```

## Performance Optimization Features

### Built-in Performance Tools

```python
# Enable performance monitoring
page.enable_performance_monitoring()

# Add performance profiler widget
from html_generator import PerformanceProfiler
profiler = PerformanceProfiler()
page.add_content(profiler)

# Enable hot reload in development
from html_generator import HotReloadManager
if page.is_development():
    hot_reload = HotReloadManager(enabled=True)
    page.add_content(hot_reload)
```

### Image Optimization

```python
# Automatic image optimization
from html_generator import ImageOptimizer

# Enable lazy loading and WebP conversion
optimizer = ImageOptimizer()
page.add_content(optimizer)

# Use optimized images
image = Image("large-photo.jpg", "Beautiful landscape")
image.add_class("img-lazy")  # Enable lazy loading
image.set_attribute("data-src", "large-photo.jpg")  # Lazy load source
```

### Critical CSS Extraction

```python
# Extract critical CSS for above-the-fold content
from html_generator import CriticalCSSExtractor

extractor = CriticalCSSExtractor()
page.add_content(extractor)

# Use in production builds
if page.is_production():
    critical_css = extractor.extract()
    page.add_critical_css(critical_css)
```

## WebAssembly Integration

### High-Performance Rendering

```python
# Enable WebAssembly-powered rendering
from html_generator import WebAssemblyRenderer

wasm_renderer = WebAssemblyRenderer(enabled=True)
page.add_content(wasm_renderer)

# Use fast rendering for complex components
large_table = Table(data=large_dataset)
fast_table = wasm_renderer.fast_render(large_table)
page.add_content(fast_table)
```

## SEO Optimization

### Built-in SEO Tools

```python
# Add SEO optimizer
from html_generator import SEOOptimizer

seo = SEOOptimizer()
page.add_content(seo)

# Optimize page metadata
page.set_meta_description("Comprehensive HTML generator for modern web applications")
page.set_meta_keywords(["HTML", "generator", "Python", "web development"])
page.add_canonical_url("https://example.com/html-generator")

# Structured data
page.add_schema_markup({
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "HTML Generator",
    "description": "Python library for generating HTML"
})
```

## Best Practices

### Component Organization

```python
# Group related components
def create_contact_section():
    section = Container()
    section.add_content(Heading("Contact Us", level=2))
    
    # Add contact form
    form = AdvancedFormBuilder('contact')
    # ... configure form fields
    section.add_content(form)
    
    # Add contact info with micro-interactions
    info_card = Card("Get in Touch", "We'd love to hear from you!")
    interactive_info = MicroInteraction(info_card, 'hover', 'glow')
    section.add_content(interactive_info)
    
    return section

# Use in page
page.add_content(create_contact_section())
```

### Performance Guidelines

1. **Use lazy loading** for images and heavy components
2. **Enable WebAssembly** for performance-critical sections
3. **Extract critical CSS** for faster initial loads
4. **Implement proper caching** for static assets
5. **Monitor performance** with built-in profiling tools

### Accessibility Guidelines

1. **Test with accessibility checker** during development
2. **Use semantic HTML** elements appropriately
3. **Provide alternative text** for all images
4. **Ensure keyboard navigation** works properly
5. **Maintain proper color contrast** ratios

## Next Steps

- Explore [Performance Tools](./performance.md) for optimization techniques
- Learn about [WebAssembly Integration](./webassembly.md) for high-performance applications
- Check out [Advanced Examples](../examples/advanced.md) for real-world implementations
- Review [Accessibility Guidelines](./accessibility.md) for inclusive design