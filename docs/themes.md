# 🎨 Theme Customization Guide

Create beautiful, custom themes for your PyPage applications with complete control over styling and appearance.

## Built-in Themes

PyPage comes with several professional themes out of the box:

### Bootstrap Theme (Default)
```python
page = Page("My Site", theme="bootstrap")
```
- Modern Bootstrap 5 styling
- Dark mode support
- Responsive components
- Professional appearance

### Material Design
```python
page = Page("My Site", theme="material")
```
- Google Material Design principles
- Elevation and shadows
- Smooth animations
- Card-based layouts

### Tailwind CSS
```python
page = Page("My Site", theme="tailwind")
```
- Utility-first approach
- Minimal design
- High customization
- Modern aesthetics

### Bulma Framework
```python
page = Page("My Site", theme="bulma")
```
- Clean, modern interface
- Flexbox-based
- Easy customization
- Lightweight

## Custom Theme Creation

### 1. CSS-Based Themes

Create custom styles with the CSS Builder:

```python
from pypage import CSSBuilder, Page

# Create custom CSS
css = CSSBuilder()

# Define color palette
css.add_rule(':root', {
    '--primary-color': '#6c5ce7',
    '--secondary-color': '#a29bfe',
    '--accent-color': '#fd79a8',
    '--background-color': '#f8f9fa',
    '--text-color': '#2d3436'
})

# Custom button styles
css.add_rule('.btn-custom', {
    'background': 'linear-gradient(135deg, var(--primary-color), var(--secondary-color))',
    'border': 'none',
    'color': 'white',
    'padding': '12px 24px',
    'border-radius': '25px',
    'font-weight': '600',
    'transition': 'all 0.3s ease',
    'box-shadow': '0 4px 15px rgba(108, 92, 231, 0.3)'
})

css.add_rule('.btn-custom:hover', {
    'transform': 'translateY(-2px)',
    'box-shadow': '0 6px 20px rgba(108, 92, 231, 0.4)'
})

# Apply to page
page = Page("Custom Theme Demo")
page.custom_css = css.render()
```

### 2. Component-Level Theming

Override individual component styles:

```python
# Custom card with theme
custom_card = Card([
    Heading("Beautiful Card", 3),
    Paragraph("This card uses custom styling")
], style={
    'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'color': 'white',
    'border': 'none',
    'border-radius': '15px',
    'padding': '2rem'
})

# Custom button with animations
animated_button = Button(
    "Click Me", 
    "button",
    css_class="btn-custom",
    style={
        'animation': 'pulse 2s infinite'
    }
)
```

### 3. Dark Mode Themes

Create sophisticated dark mode experiences:

```python
# Advanced dark mode CSS
dark_css = CSSBuilder()

# Dark mode variables
dark_css.add_rule('[data-theme="dark"]', {
    '--bg-primary': '#1a1a1a',
    '--bg-secondary': '#2d2d2d',
    '--text-primary': '#ffffff',
    '--text-secondary': '#b0b0b0',
    '--accent': '#4a9eff',
    '--border': '#404040'
})

# Dark mode card styling
dark_css.add_rule('[data-theme="dark"] .card', {
    'background-color': 'var(--bg-secondary)',
    'border-color': 'var(--border)',
    'color': 'var(--text-primary)'
})

page.custom_css = dark_css.render()
page.add_content(DarkModeToggle(position="top-right"))
```

## Advanced Theming Techniques

### 1. Responsive Theme Variations

```python
css = CSSBuilder()

# Base styles
css.add_rule('.hero-section', {
    'padding': '4rem 0',
    'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
})

# Responsive adjustments
css.responsive_breakpoints('.hero-section',
    sm={'padding': '2rem 0'},
    md={'padding': '3rem 0'},
    lg={'padding': '4rem 0'},
    xl={'padding': '5rem 0'}
)
```

### 2. Animation-Enhanced Themes

```python
# Add smooth transitions and animations
css.add_rule('*', {
    'transition': 'all 0.3s ease'
})

# Hover effects
css.add_rule('.card:hover', {
    'transform': 'translateY(-5px)',
    'box-shadow': '0 10px 25px rgba(0,0,0,0.1)'
})

# Entrance animations
css.add_keyframes('fadeInUp', {
    '0%': {'opacity': '0', 'transform': 'translateY(30px)'},
    '100%': {'opacity': '1', 'transform': 'translateY(0)'}
})

css.add_rule('.animate-entrance', {
    'animation': 'fadeInUp 0.6s ease-out'
})
```

### 3. Typography Themes

```python
# Custom font integration
css.add_rule('@import', 'url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap")')

css.add_rule('body', {
    'font-family': '"Inter", -apple-system, BlinkMacSystemFont, sans-serif',
    'font-weight': '400',
    'line-height': '1.6',
    'color': '#2d3748'
})

# Heading styles
css.add_rule('h1, h2, h3, h4, h5, h6', {
    'font-weight': '600',
    'line-height': '1.3',
    'margin-bottom': '1rem'
})
```

## Theme Templates

### 1. Minimal Theme
```python
def create_minimal_theme():
    css = CSSBuilder()
    
    css.add_rule(':root', {
        '--primary': '#000000',
        '--secondary': '#f5f5f5',
        '--accent': '#0066cc',
        '--text': '#333333'
    })
    
    css.add_rule('body', {
        'font-family': '"Helvetica Neue", Arial, sans-serif',
        'color': 'var(--text)',
        'line-height': '1.6'
    })
    
    css.add_rule('.btn', {
        'border-radius': '0',
        'border': '2px solid var(--primary)',
        'font-weight': '500'
    })
    
    return css.render()

page = Page("Minimal Design")
page.custom_css = create_minimal_theme()
```

### 2. Colorful Theme
```python
def create_colorful_theme():
    css = CSSBuilder()
    
    # Vibrant color palette
    colors = {
        '--primary': '#ff6b6b',
        '--secondary': '#4ecdc4',
        '--tertiary': '#45b7d1',
        '--quaternary': '#f9ca24',
        '--success': '#6c5ce7'
    }
    
    css.add_rule(':root', colors)
    
    # Gradient backgrounds
    css.add_rule('.hero', {
        'background': 'linear-gradient(135deg, var(--primary), var(--secondary))'
    })
    
    # Colorful buttons
    css.add_rule('.btn-primary', {
        'background': 'linear-gradient(45deg, var(--primary), var(--tertiary))',
        'border': 'none'
    })
    
    return css.render()

page = Page("Colorful Design")
page.custom_css = create_colorful_theme()
```

### 3. Professional Theme
```python
def create_professional_theme():
    css = CSSBuilder()
    
    css.add_rule(':root', {
        '--primary': '#2c3e50',
        '--secondary': '#34495e',
        '--accent': '#3498db',
        '--light': '#ecf0f1',
        '--dark': '#2c3e50'
    })
    
    # Professional spacing
    css.add_rule('.section', {
        'padding': '4rem 0'
    })
    
    # Subtle shadows
    css.add_rule('.card', {
        'box-shadow': '0 2px 10px rgba(44, 62, 80, 0.1)',
        'border': 'none'
    })
    
    return css.render()
```

## Theme Integration

### With Flask Applications
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    page = Page("My App")
    page.custom_css = create_minimal_theme()
    return page.generate_html()
```

### Theme Switching
```python
def create_theme_switcher():
    """Create a dynamic theme switcher"""
    switcher = Select("theme", [
        {"value": "default", "label": "Default"},
        {"value": "dark", "label": "Dark Mode"},
        {"value": "minimal", "label": "Minimal"},
        {"value": "colorful", "label": "Colorful"}
    ])
    
    # JavaScript for theme switching
    js = """
    document.querySelector('select[name="theme"]').addEventListener('change', function(e) {
        document.body.className = 'theme-' + e.target.value;
    });
    """
    
    return switcher, js
```

## Best Practices

### 1. Performance Optimization
- Use CSS custom properties for easy theme switching
- Minimize CSS file size with efficient selectors
- Leverage browser caching for theme assets

### 2. Accessibility
- Ensure sufficient color contrast ratios
- Test themes with screen readers
- Provide high contrast alternatives

### 3. Responsive Design
- Design themes mobile-first
- Test across different screen sizes
- Use flexible units (rem, em, %)

### 4. Consistency
- Maintain consistent spacing scales
- Use a limited color palette
- Follow design system principles

This comprehensive theming system allows you to create unique, professional designs that perfectly match your brand and requirements.