# 📦 Installation Guide

Complete installation instructions for PyPage with all features and dependencies.

## System Requirements

- **Python 3.8+** (Python 3.11+ recommended)
- **pip** package manager
- **Modern web browser** for development server

## Installation Options

### 🚀 Quick Install (Recommended)

For most users, the basic installation includes all core features:

```bash
pip install pypage
```

This includes:
- ✅ Core components (Page, Container, Card, etc.)
- ✅ Bootstrap 5 integration
- ✅ Dark mode support
- ✅ Basic animations
- ✅ Responsive design
- ✅ Flask integration
- ✅ CLI tools

### 🎨 With PDF Export

For PDF generation capabilities:

```bash
pip install pypage[pdf]
```

Additional features:
- ✅ PDF export via WeasyPrint
- ✅ ReportLab integration
- ✅ Print-optimized layouts

### 📊 With Charts & Visualization

For data visualization components:

```bash
pip install pypage[charts]
```

Additional features:
- ✅ Interactive charts (Chart.js)
- ✅ Matplotlib integration
- ✅ Plotly support
- ✅ KPI cards and dashboards

### 🛠️ Development Installation

For contributors and advanced users:

```bash
pip install pypage[dev]
```

Additional features:
- ✅ Testing frameworks (pytest, coverage)
- ✅ Code formatting (black, isort)
- ✅ Linting (flake8, mypy)
- ✅ Pre-commit hooks

### 🌟 Full Installation

Get everything PyPage has to offer:

```bash
pip install pypage[full]
```

Includes all features:
- ✅ PDF export capabilities
- ✅ Chart and visualization tools
- ✅ Development tools
- ✅ Performance optimizations
- ✅ WebAssembly integration

## Alternative Installation Methods

### Using Poetry

```bash
poetry add pypage
# or with extras
poetry add pypage[full]
```

### Using Conda

```bash
conda install -c conda-forge pypage
```

### Using pipx (CLI tools only)

```bash
pipx install pypage
```

### Development from Source

```bash
git clone https://github.com/pypage/pypage.git
cd pypage
pip install -e .[dev]
```

## Verify Installation

Test your installation:

```python
import pypage
print(f"PyPage version: {pypage.__version__}")

# Quick test
from pypage import Page, Heading
page = Page("Test", "Installation successful!")
page.add_content(Heading("PyPage is working! 🎉", 1))
print("✅ Installation verified!")
```

Or use the CLI:

```bash
pypage --version
pypage create test-project --template basic
```

## Optional Dependencies

### For Enhanced Performance

```bash
# WebAssembly support (experimental)
pip install wasmtime

# Faster JSON processing
pip install orjson

# Image optimization
pip install Pillow
```

### For Additional Features

```bash
# Advanced CSS processing
pip install rcssmin

# JavaScript minification  
pip install jsmin

# Syntax highlighting
pip install pygments
```

## Troubleshooting

### Common Issues

**ModuleNotFoundError: No module named 'pypage'**
```bash
# Ensure you're in the correct virtual environment
which python
pip list | grep pypage
```

**Import errors with extras**
```bash
# Reinstall with specific extras
pip uninstall pypage
pip install pypage[full]
```

**Permission errors on macOS/Linux**
```bash
# Use user installation
pip install --user pypage
```

**WeasyPrint installation issues**
```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0

# On macOS
brew install pango
```

### Virtual Environment Setup

Recommended for all installations:

```bash
# Create virtual environment
python -m venv pypage-env

# Activate (Windows)
pypage-env\Scripts\activate

# Activate (macOS/Linux)
source pypage-env/bin/activate

# Install PyPage
pip install pypage[full]
```

### Docker Installation

For containerized environments:

```dockerfile
FROM python:3.11-slim

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install PyPage
RUN pip install pypage[full]

# Your application code
COPY . /app
WORKDIR /app
```

## Version Compatibility

| PyPage Version | Python Version | Features |
|----------------|----------------|----------|
| 3.0.x | 3.8+ | All features, latest components |
| 2.x.x | 3.7+ | Legacy components, basic features |
| 1.x.x | 3.6+ | Original HTML generator |

## Getting Help

If you encounter installation issues:

1. **Check the [FAQ](faq.md)** for common solutions
2. **Search existing issues** on GitHub
3. **Create a new issue** with:
   - Your operating system
   - Python version (`python --version`)
   - Full error message
   - Installation command used

## Next Steps

After successful installation:

- **[🚀 Quick Start](quick-start.md)** - Build your first page
- **[📚 Component Reference](component_reference.md)** - Explore all components
- **[💡 Examples](examples/)** - See real-world projects
- **[🎮 Interactive Playground](../test/)** - Test components live

Welcome to PyPage! 🎉