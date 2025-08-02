# Templates Directory

This directory contains the Jinja2 templates for the HTML Generator web application, providing a consistent and responsive user interface built with Bootstrap 5.

## Template Structure

### Base Template System
- `base.html` - Main layout template with navigation, footer, and common elements
- All other templates extend the base template for consistency

### Page Templates
- `index.html` - Home page with overview and getting started
- `editor.html` - Interactive code editor with syntax highlighting
- `gallery.html` - Generated page gallery with grid/list views
- `examples.html` - Code examples and template showcase
- `preview.html` - Generated page preview iframe container

### Configuration Templates
- `navbar_config.html` - Visual navbar builder interface
- `css_builder.html` - Interactive CSS rule builder

## Template Features

### Modern UI Design
- **Bootstrap 5**: Latest responsive framework
- **Dark Theme**: Built-in dark mode support
- **Mobile First**: Responsive design for all devices
- **Accessibility**: WCAG compliant markup
- **Performance**: Optimized loading and rendering

### Interactive Components
- **Code Editor**: CodeMirror integration with Python syntax highlighting
- **Live Preview**: Real-time HTML generation and preview
- **Drag & Drop**: File upload and reordering
- **Modal Dialogs**: Bootstrap modal integration
- **Toast Notifications**: User feedback system

### Progressive Enhancement
- **JavaScript Optional**: Core functionality works without JS
- **Enhanced UX**: JavaScript improves but doesn't break experience
- **Graceful Degradation**: Fallbacks for older browsers
- **Fast Loading**: Critical CSS inlined, non-critical deferred

## Template Organization

### Layout Structure

```html
<!-- base.html structure -->
<!DOCTYPE html>
<html lang="en" data-bs-theme="auto">
<head>
    <!-- Meta tags, title, CSS -->
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg">...</nav>
    
    <!-- Main content area -->
    <main class="container-fluid">
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    <footer class="bg-dark text-light">...</footer>
    
    <!-- JavaScript -->
    <script src="..."></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

### Block System

Templates use Jinja2 blocks for customization:

- `{% block title %}` - Page title
- `{% block extra_head %}` - Additional head content
- `{% block content %}` - Main page content
- `{% block scripts %}` - Page-specific JavaScript

### Template Inheritance Example

```html
<!-- editor.html -->
{% extends "base.html" %}

{% block title %}Code Editor{% endblock %}

{% block extra_head %}
<!-- CodeMirror CSS -->
<link rel="stylesheet" href="...">
{% endblock %}

{% block content %}
<!-- Editor interface -->
<div class="row">
    <div class="col-lg-6">
        <!-- Code editor -->
    </div>
    <div class="col-lg-6">
        <!-- Preview panel -->
    </div>
</div>
{% endblock %}

{% block scripts %}
<!-- CodeMirror JavaScript -->
<script src="..."></script>
<!-- Editor functionality -->
<script>
// Editor setup code
</script>
{% endblock %}
```

## Responsive Design

### Bootstrap Grid System

```html
<!-- Mobile-first responsive layout -->
<div class="container-fluid">
    <div class="row">
        <!-- Main content -->
        <div class="col-12 col-lg-8">
            <main>...</main>
        </div>
        
        <!-- Sidebar -->
        <div class="col-12 col-lg-4">
            <aside>...</aside>
        </div>
    </div>
</div>
```

### Breakpoint Strategy

- **xs** (0px+): Single column, stacked layout
- **sm** (576px+): Small adjustments, still mostly stacked
- **md** (768px+): Tablet layout with some side-by-side
- **lg** (992px+): Desktop layout with full sidebar
- **xl** (1200px+): Large desktop with wider containers

### Component Responsiveness

```html
<!-- Responsive navigation -->
<nav class="navbar navbar-expand-lg">
    <div class="container">
        <!-- Brand -->
        <a class="navbar-brand" href="/">HTML Generator</a>
        
        <!-- Mobile toggle -->
        <button class="navbar-toggler" type="button" 
                data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Collapsible menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">...</ul>
        </div>
    </div>
</nav>
```

## Dark Mode Implementation

### Theme Toggle System

```html
<!-- Theme toggle button -->
<div class="dropdown">
    <button class="btn btn-outline-secondary dropdown-toggle" 
            type="button" data-bs-toggle="dropdown" aria-expanded="false">
        <i class="fas fa-palette me-2"></i>Theme
    </button>
    <ul class="dropdown-menu">
        <li><button class="dropdown-item" data-bs-theme-value="light">Light</button></li>
        <li><button class="dropdown-item" data-bs-theme-value="dark">Dark</button></li>
        <li><button class="dropdown-item" data-bs-theme-value="auto">Auto</button></li>
    </ul>
</div>
```

### Theme Persistence

```javascript
// Theme management
(() => {
    'use strict'
    
    const getStoredTheme = () => localStorage.getItem('theme')
    const setStoredTheme = theme => localStorage.setItem('theme', theme)
    
    const getPreferredTheme = () => {
        const storedTheme = getStoredTheme()
        if (storedTheme) {
            return storedTheme
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
    
    const setTheme = theme => {
        if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-bs-theme', 'dark')
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme)
        }
    }
    
    setTheme(getPreferredTheme())
    
    document.querySelectorAll('[data-bs-theme-value]')
        .forEach(toggle => {
            toggle.addEventListener('click', () => {
                const theme = toggle.getAttribute('data-bs-theme-value')
                setStoredTheme(theme)
                setTheme(theme)
            })
        })
})()
```

## Accessibility Features

### Semantic HTML

```html
<!-- Proper landmark structure -->
<header>
    <nav role="navigation" aria-label="Main navigation">...</nav>
</header>

<main role="main" aria-label="Main content">
    <section aria-labelledby="main-heading">
        <h1 id="main-heading">Page Title</h1>
        <!-- Content -->
    </section>
</main>

<aside role="complementary" aria-label="Sidebar">...</aside>

<footer role="contentinfo">...</footer>
```

### ARIA Labels and Roles

```html
<!-- Form accessibility -->
<form novalidate>
    <div class="mb-3">
        <label for="page-title" class="form-label">Page Title *</label>
        <input type="text" class="form-control" id="page-title" 
               name="title" required aria-describedby="title-help">
        <div id="title-help" class="form-text">
            Enter a descriptive title for your page
        </div>
        <div class="invalid-feedback" id="title-error"></div>
    </div>
</form>

<!-- Interactive elements -->
<button type="button" class="btn btn-primary" 
        aria-describedby="generate-help" aria-expanded="false">
    Generate Page
</button>
```

### Focus Management

```css
/* High contrast focus indicators */
:focus-visible {
    outline: 3px solid #0066cc;
    outline-offset: 2px;
}

/* Skip link for keyboard users */
.visually-hidden-focusable {
    position: absolute !important;
    width: 1px !important;
    height: 1px !important;
    overflow: hidden !important;
}

.visually-hidden-focusable:focus {
    position: static !important;
    width: auto !important;
    height: auto !important;
    overflow: visible !important;
    background: #000;
    color: #fff;
    padding: 0.5rem;
}
```

## Performance Optimization

### Critical CSS Inlining

```html
<!-- Inline critical styles in head -->
<style>
/* Critical above-the-fold styles */
.navbar { /* Essential navigation styles */ }
.hero-section { /* Landing page hero styles */ }
.container { /* Layout container styles */ }
</style>

<!-- Preload non-critical CSS -->
<link rel="preload" href="/static/css/non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/static/css/non-critical.css"></noscript>
```

### Resource Loading

```html
<!-- Optimized resource loading -->
<head>
    <!-- DNS prefetch for external resources -->
    <link rel="dns-prefetch" href="//fonts.googleapis.com">
    <link rel="dns-prefetch" href="//cdnjs.cloudflare.com">
    
    <!-- Preload critical fonts -->
    <link rel="preload" href="/static/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
    
    <!-- Critical CSS inlined -->
    <style>/* Critical styles */</style>
    
    <!-- Non-critical CSS preloaded -->
    <link rel="preload" href="/static/css/app.css" as="style" onload="this.rel='stylesheet'">
</head>

<body>
    <!-- Content -->
    
    <!-- JavaScript loaded after content -->
    <script src="/static/js/app.js" defer></script>
</body>
```

### Image Optimization

```html
<!-- Responsive, optimized images -->
<picture>
    <source srcset="/static/images/hero.webp" type="image/webp">
    <source srcset="/static/images/hero.jpg" type="image/jpeg">
    <img src="/static/images/hero.jpg" 
         alt="HTML Generator interface"
         loading="lazy"
         decoding="async"
         width="800" 
         height="400">
</picture>

<!-- Lazy loaded images -->
<img src="/static/images/placeholder.jpg"
     data-src="/static/images/actual.jpg"
     alt="Description"
     loading="lazy"
     class="lazy-image">
```

## JavaScript Integration

### Progressive Enhancement Pattern

```html
<!-- HTML that works without JavaScript -->
<form action="/editor/generate" method="post" class="code-form">
    <div class="mb-3">
        <label for="code" class="form-label">Python Code</label>
        <textarea class="form-control" id="code" name="code" rows="10" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Generate HTML</button>
</form>

<!-- JavaScript enhancement -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.code-form');
    const codeTextarea = document.getElementById('code');
    
    // Enhance with CodeMirror if available
    if (typeof CodeMirror !== 'undefined') {
        const editor = CodeMirror.fromTextArea(codeTextarea, {
            mode: 'python',
            theme: 'dracula',
            lineNumbers: true,
            autoCloseBrackets: true
        });
        
        // AJAX form submission
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            // Enhanced AJAX handling
        });
    }
});
</script>
```

### Component JavaScript

```html
<!-- Gallery component with JavaScript enhancement -->
<div class="gallery" data-component="gallery">
    <!-- Server-rendered gallery items -->
    <div class="gallery-items">
        {% for page in pages %}
        <div class="gallery-item" data-page-id="{{ page.id }}">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{ page.title }}</h5>
                    <p class="card-text">{{ page.description }}</p>
                    <a href="/preview/{{ page.id }}" class="btn btn-primary">View</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <!-- Enhanced features with JavaScript -->
    <div class="gallery-controls" style="display: none;">
        <button class="btn btn-outline-secondary" data-action="grid-view">Grid</button>
        <button class="btn btn-outline-secondary" data-action="list-view">List</button>
        <input type="search" placeholder="Search pages..." class="form-control d-inline-block w-auto">
    </div>
</div>

<script>
// Gallery enhancement
document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.querySelector('[data-component="gallery"]');
    if (gallery) {
        // Show enhanced controls
        const controls = gallery.querySelector('.gallery-controls');
        controls.style.display = 'block';
        
        // Add search functionality
        // Add view switching
        // Add filtering
    }
});
</script>
```

## Template Development Guidelines

### Code Organization
1. Use consistent indentation (2 spaces)
2. Keep templates focused and modular
3. Use meaningful variable names
4. Comment complex logic
5. Follow Bootstrap conventions

### Performance Best Practices
1. Minimize HTTP requests
2. Optimize critical rendering path
3. Use proper caching headers
4. Implement lazy loading
5. Compress assets

### Accessibility Standards
1. Use semantic HTML elements
2. Provide proper ARIA labels
3. Ensure keyboard navigation
4. Test with screen readers
5. Maintain color contrast ratios

### Testing Templates
1. Test across browsers and devices
2. Validate HTML markup
3. Check accessibility compliance
4. Test with JavaScript disabled
5. Verify responsive behavior

## Next Steps

- Review individual template files for specific implementations
- Check [UI Components Guide](../docs/library/ui-components.md) for component details
- Study [Accessibility Features](../docs/features/accessibility.md) for inclusive design
- Explore [Performance Guide](../docs/features/performance.md) for optimization techniques