#!/usr/bin/env python3
"""
Command Line Interface for PyPage Library
"""

import argparse
import sys
import os
from typing import Optional

def create_project(name: str, template: str = "basic") -> None:
    """Create a new PyPage project"""
    print(f"Creating new PyPage project: {name}")
    
    # Create project directory
    os.makedirs(name, exist_ok=True)
    
    # Create basic project structure
    if template == "basic":
        create_basic_project(name)
    elif template == "flask":
        create_flask_project(name)
    elif template == "full":
        create_full_project(name)
    
    print(f"Project '{name}' created successfully!")
    print(f"To get started:")
    print(f"  cd {name}")
    print(f"  python main.py")

def create_basic_project(name: str) -> None:
    """Create a basic PyPage project"""
    main_py = '''#!/usr/bin/env python3
"""
Basic PyPage Example
"""

from pypage import *

# Create a new page
page = Page("My Website", "Welcome to PyPage!")

# Add content
page.add_content(Heading("Hello, World!", 1))
page.add_content(Paragraph("This is your first PyPage project."))

# Add a card
card = Card([
    Heading("Getting Started", 3),
    Paragraph("Edit this file to customize your website."),
    Button("Learn More", "button", css_class="btn-primary")
])
page.add_content(card)

# Generate and save HTML
html = page.generate_html()

with open("index.html", "w") as f:
    f.write(html)

print("Website generated! Open index.html in your browser.")
'''
    
    with open(os.path.join(name, "main.py"), "w") as f:
        f.write(main_py)

def create_flask_project(name: str) -> None:
    """Create a Flask-based PyPage project"""
    app_py = '''#!/usr/bin/env python3
"""
Flask PyPage Application
"""

from flask import Flask, render_template_string
from pypage import *

app = Flask(__name__)

@app.route('/')
def index():
    # Create page using PyPage
    page = Page("Flask + PyPage", "Dynamic Web Generation")
    
    page.add_content(Heading("Flask Integration", 1))
    page.add_content(Paragraph("This page is generated dynamically using PyPage with Flask."))
    
    # Add navigation
    nav_links = [
        {"url": "/", "text": "Home"},
        {"url": "/about", "text": "About"},
        {"url": "/contact", "text": "Contact"}
    ]
    page.add_navbar(nav_links)
    
    # Generate HTML
    html = page.generate_html()
    return html

@app.route('/about')
def about():
    page = Page("About", "About Our Project")
    page.add_content(Heading("About PyPage", 1))
    page.add_content(Paragraph("PyPage is a powerful HTML generation library."))
    return page.generate_html()

if __name__ == '__main__':
    app.run(debug=True)
'''
    
    with open(os.path.join(name, "app.py"), "w") as f:
        f.write(app_py)

def create_full_project(name: str) -> None:
    """Create a full-featured PyPage project"""
    create_flask_project(name)
    
    # Add additional files for full project
    config_py = '''
class Config:
    SECRET_KEY = 'your-secret-key-here'
    DEBUG = True
'''
    
    with open(os.path.join(name, "config.py"), "w") as f:
        f.write(config_py)

def generate_docs() -> None:
    """Generate documentation from PyPage components"""
    print("Generating PyPage documentation...")
    
    from pypage import *
    
    # Create documentation page
    page = Page("PyPage Documentation", "Complete Component Reference")
    
    # Add sections for each component type
    page.add_content(Heading("PyPage Documentation", 1))
    page.add_content(Paragraph("Complete reference for all PyPage components."))
    
    # Generate and save
    html = page.generate_html()
    with open("docs.html", "w") as f:
        f.write(html)
    
    print("Documentation generated: docs.html")

def version() -> str:
    """Get PyPage version"""
    try:
        from pypage import __version__
        return __version__
    except ImportError:
        return "3.0.0"

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="PyPage - Enhanced HTML Generator Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  pypage create myproject              Create a basic project
  pypage create myapp --template flask Create a Flask project
  pypage docs                          Generate documentation
  pypage --version                     Show version
        """
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"PyPage {version()}"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new PyPage project")
    create_parser.add_argument("name", help="Project name")
    create_parser.add_argument(
        "--template", 
        choices=["basic", "flask", "full"], 
        default="basic",
        help="Project template to use"
    )
    
    # Docs command
    docs_parser = subparsers.add_parser("docs", help="Generate documentation")
    
    args = parser.parse_args()
    
    if args.command == "create":
        create_project(args.name, args.template)
    elif args.command == "docs":
        generate_docs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()