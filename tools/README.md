# Tools Directory

This directory contains development tools, utilities, and web interfaces for the HTML Generator project. These tools enhance the development experience and provide visual interfaces for configuration and debugging.

## Directory Structure

```
tools/
├── README.md              # This documentation
└── web_interface/         # Visual web tools
    ├── README.md          # Web interface tools documentation
    ├── navbar_config.html # Visual navbar builder
    └── css_builder.html   # Interactive CSS builder
```

## Available Tools

### Web Interface Tools (`web_interface/`)

Visual tools accessible through the main web application:

- **Navbar Configuration Tool** - Visual interface for building navigation bars
- **CSS Builder** - Interactive CSS rule creation and editing

These tools are integrated into the main application and accessible through the Tools menu.

## Future Tool Categories

The tools directory is designed to accommodate various types of development utilities:

### Planned Additions

- **CLI Tools** - Command-line utilities for project management
- **Development Scripts** - Automation scripts for common tasks
- **Testing Utilities** - Specialized testing and validation tools
- **Deployment Tools** - Build and deployment automation
- **Code Generators** - Template and component generators

### Integration

Tools are integrated with the main application through:
- Route handlers in `routes/config.py`
- Menu links in the web interface
- API endpoints for data exchange
- Command-line interfaces where appropriate

## Usage

### Web Interface Tools

Access through the main application:
1. Start the HTML Generator web application
2. Navigate to the Tools section in the main menu
3. Select the desired tool
4. Use the visual interface to create configurations
5. Copy generated code or save directly to your project

### Command-Line Tools (Future)

Will be accessible through:
```bash
# Example future CLI commands
python -m tools.generator create-component MyComponent
python -m tools.build optimize-assets
python -m tools.test run-accessibility-checks
```

## Development Guidelines

When adding new tools:

1. **Organization** - Place tools in appropriate subdirectories
2. **Documentation** - Include README files for each tool category
3. **Integration** - Add proper route handlers and menu links
4. **Testing** - Include tests for tool functionality
5. **User Experience** - Maintain consistent UI/UX patterns

## Contributing

When contributing new tools:
- Follow the existing directory structure
- Add comprehensive documentation
- Include examples and usage instructions
- Test thoroughly across different environments
- Update this README with new tool descriptions

## Dependencies

Tools may have additional dependencies beyond the main application:
- Web tools use the same Flask/Bootstrap stack
- CLI tools may require additional Python packages
- Build tools may need external system dependencies

See individual tool documentation for specific requirements.