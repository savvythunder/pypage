# Web Interface Tools

This directory contains visual tools and utilities for the HTML Generator web interface. These tools provide user-friendly interfaces for configuration, debugging, and development tasks.

## Available Tools

### Configuration Tools
- `navbar_config.html` - Visual navbar builder interface
- `css_builder.html` - Interactive CSS rule builder

### Tool Descriptions

#### Navbar Configuration Tool
The navbar configuration tool provides a visual interface for building navigation bars with:
- Drag-and-drop menu item organization
- Brand logo and text configuration
- Mobile responsive settings
- Color scheme selection
- Real-time preview

#### CSS Builder Tool
The CSS builder offers an interactive way to create CSS rules with:
- Visual property editors
- Responsive breakpoint management
- Color picker integration
- Font selection tools
- Live preview of generated CSS

## Integration

These tools are integrated into the main web application through:
- Route handlers in `routes/config.py`
- Navigation links in the main interface
- Modal dialogs for quick access
- API endpoints for saving configurations

## Usage

Access these tools through the main web interface:
1. Navigate to the Tools menu
2. Select the desired configuration tool
3. Use the visual interface to create your configuration
4. Copy the generated code or save directly to your project

## Development

When adding new tools:
1. Create the HTML template in this directory
2. Add corresponding routes in `routes/config.py`
3. Update the main navigation to include the new tool
4. Add documentation for the tool's features and usage

## File Structure

```
tools/web_interface/
├── README.md              # This documentation
├── navbar_config.html     # Navbar builder interface
├── css_builder.html       # CSS rule builder interface
└── [future tools]         # Additional tools as needed
```

## Future Enhancements

Planned additions to the tools directory:
- Theme builder interface
- Component library browser
- Performance optimization dashboard
- Accessibility testing tools
- SEO analysis interface
- Image optimization tools