# HTML Generator Library

Core library for programmatic HTML generation with modern web development features.

## Overview

This directory contains the HTML Generator library modules that provide a comprehensive set of tools for creating dynamic web applications using Python.

## Module Structure

### Core Modules
- `__init__.py` - Main library exports and version information
- `page.py` - Page component and core page management
- `elements.py` - Basic HTML elements (Heading, Paragraph, etc.)
- `components.py` - Advanced UI components
- `css.py` - CSS builder and styling utilities

### Enhanced Modules
- `ui_components.py` - Modern UI components (charts, forms, interactions)
- `performance_tools.py` - Performance optimization and monitoring
- `webassembly_integration.py` - WebAssembly features and optimizations
- `forms.py` - Form components and validation
- `layout.py` - Layout system (Grid, Flexbox)

### Advanced Features
- `animations.py` - Animation framework
- `dark_mode.py` - Dark mode support
- `debug_tools.py` - Visual debugging tools
- `plugins.py` - Plugin system and extensibility
- `export_tools.py` - Export capabilities (PDF, JSON)

### Specialized Components
- `advanced_components.py` - Professional UI components
- `data_visualization.py` - Chart and data visualization
- `forms_advanced.py` - Advanced form controls
- `templates.py` - Template system

## Key Features

### Modern UI Components
- Interactive charts and data visualization
- Advanced form builders with real-time validation
- Micro-interactions and smooth animations
- Accessibility compliance checking

### Performance Optimization
- Hot reload for development
- WebAssembly integration for high-performance rendering
- Critical CSS extraction
- Image optimization with WebP support
- Code splitting and lazy loading

### Developer Experience
- Component testing framework
- Performance profiling tools
- SEO optimization checker
- Visual debugging capabilities

### Enterprise Features
- Plugin architecture for extensibility
- Export capabilities (PDF, JSON)
- Theme system with multiple frameworks
- Advanced template management

## Usage Examples

### Basic Component Usage

```python
from html_generator import Page, Heading, Paragraph, Card

# Create a simple page
page = Page("My Application", "Welcome")
page.add_content(Heading("Hello World", level=1))
page.add_content(Paragraph("This is generated content."))

# Add a card component
card = Card("Feature", "Amazing functionality awaits!")
page.add_content(card)

# Generate HTML
html = page.generate_html()
```

### Modern UI Features

```python
from html_generator import *

# Page with dark mode and animations
page = Page("Modern App", "Advanced Features")
page.set_theme('bootstrap')
page.add_content(DarkModeToggle())

# Animated content
animated_section = FadeIn(
    Container([
        Heading("Interactive Dashboard", 2),
        InteractiveChart('bar', chart_data),
        AdvancedFormBuilder().add_field('text', 'name', 'Name')
    ])
)
page.add_content(animated_section)
```

### Performance Optimization

```python
# Enable performance features
page.enable_performance_monitoring()
page.add_content(PerformanceProfiler())
page.add_content(WebAssemblyRenderer())

# Optimize images
optimizer = ImageOptimizer()
page.add_content(optimizer)

# Extract critical CSS
extractor = CriticalCSSExtractor()
critical_css = extractor.extract()
page.add_critical_css(critical_css)
```

## Architecture

### Component Hierarchy
```
ComponentBase
├── Element (Basic HTML elements)
├── Page (Main page container)
├── Container (Layout containers)
├── Form Components
├── UI Components
└── Advanced Components
```

### Plugin System
```python
# Register custom components
@register_component
class CustomWidget(ComponentBase):
    def render(self):
        return "<div class='custom-widget'>...</div>"

# Use plugins
plugin_manager.load_plugin('custom_widgets')
widget = CustomWidget()
```

### Theme Integration
```python
# Support for multiple CSS frameworks
page.set_theme('bootstrap')  # Bootstrap 5
page.set_theme('tailwind')   # Tailwind CSS
page.set_theme('bulma')      # Bulma
page.set_theme('material')   # Material Design
```

## Development Guidelines

### Adding New Components

1. Inherit from `ComponentBase`
2. Implement the `render()` method
3. Add appropriate CSS classes and styling
4. Include accessibility features
5. Write unit tests
6. Update documentation

### Performance Considerations

- Use lazy loading for heavy components
- Implement efficient rendering algorithms
- Cache compiled templates
- Minimize DOM operations
- Use WebAssembly for computationally intensive tasks

### Accessibility Standards

- Follow WCAG 2.1 guidelines
- Include ARIA labels and roles
- Ensure keyboard navigation
- Provide alternative text for images
- Maintain proper heading hierarchy

## Testing

```bash
# Run unit tests
python -m pytest tests/

# Run performance tests
python -m pytest tests/performance/

# Run accessibility tests
python -m pytest tests/accessibility/
```

## Documentation

Detailed documentation is available in the `docs/` directory:

- [Getting Started](../docs/getting-started.md)
- [API Reference](../docs/library/core-components.md)
- [Performance Guide](../docs/features/performance.md)
- [Examples](../docs/examples/basic.md)

## Contributing

See [Contributing Guidelines](../docs/development/contributing.md) for information on:

- Code style and conventions
- Testing requirements
- Documentation standards
- Pull request process

## Version History

- **3.0.0** (August 2025) - Major release with modern UI components, performance tools, and WebAssembly integration
- **2.0.0** - Enhanced form system and layout components
- **1.0.0** - Initial release with basic HTML generation