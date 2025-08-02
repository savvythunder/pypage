from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from html_generator import Page, Heading, Paragraph, HtmlList, Image, Card, Container
from models import GeneratedPage, db
import uuid
import re

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Homepage with overview of the HTML generator"""
    return render_template('index.html')

@main_bp.route('/editor')
def editor():
    """Code editor for creating webpages"""
    return render_template('editor.html')

@main_bp.route('/gallery')
def gallery():
    """Gallery of generated webpages"""
    pages = GeneratedPage.query.order_by(GeneratedPage.created_at.desc()).all()
    return render_template('gallery.html', pages=pages)

@main_bp.route('/generate', methods=['POST'])
def generate_page():
    """Generate a webpage from code"""
    code = request.form.get('code', '')
    title = request.form.get('title', 'Generated Page')
    
    if not code.strip():
        flash('Please provide code to generate a page.', 'error')
        return redirect(url_for('main.editor'))
    
    try:
        # Create a safe execution environment
        exec_globals = {
            'Page': Page,
            'Heading': Heading,
            'Paragraph': Paragraph,
            'List': HtmlList,
            'Image': Image,
            'Card': Card,
            'Container': Container,
            'page': None
        }
        
        # Execute the user code
        exec(code, exec_globals)
        
        # Get the page object
        page = exec_globals.get('page')
        if not page or not isinstance(page, Page):
            flash('Code must create a Page object and assign it to variable "page".', 'error')
            return redirect(url_for('main.editor'))
        
        # Generate HTML
        html_content = page.generate_html()
        
        # Create unique filename
        safe_title = re.sub(r'[^a-zA-Z0-9_-]', '', title.replace(' ', '_'))
        filename = f"{safe_title}_{uuid.uuid4().hex[:8]}.html"
        
        # Save to database
        generated_page = GeneratedPage()
        generated_page.title = title
        generated_page.filename = filename
        generated_page.code = code
        generated_page.html_content = html_content
        db.session.add(generated_page)
        db.session.commit()
        
        # Save to file
        file_path = os.path.join('generated_pages', filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        flash(f'Page "{title}" generated successfully!', 'success')
        return redirect(url_for('main.preview', page_id=generated_page.id))
        
    except Exception as e:
        flash(f'Error generating page: {str(e)}', 'error')
        return redirect(url_for('main.editor'))

@main_bp.route('/preview/<int:page_id>')
def preview(page_id):
    """Preview a generated page"""
    page = GeneratedPage.query.get_or_404(page_id)
    return render_template('preview.html', page=page)

@main_bp.route('/view/<int:page_id>')
def view_page(page_id):
    """View the generated HTML directly"""
    page = GeneratedPage.query.get_or_404(page_id)
    return page.html_content

@main_bp.route('/edit/<int:page_id>')
def edit_page(page_id):
    """Edit an existing page"""
    page = GeneratedPage.query.get_or_404(page_id)
    return render_template('editor.html', page=page)

@main_bp.route('/delete/<int:page_id>', methods=['POST'])
def delete_page(page_id):
    """Delete a generated page"""
    page = GeneratedPage.query.get_or_404(page_id)
    
    # Delete file if it exists
    file_path = os.path.join('generated_pages', page.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Delete from database
    db.session.delete(page)
    db.session.commit()
    
    flash(f'Page "{page.title}" deleted successfully!', 'success')
    return redirect(url_for('main.gallery'))

@main_bp.route('/examples')
def examples():
    """Show code examples"""
    examples = [
        {
            'title': 'Basic Page',
            'code': '''# Create a basic page
page = Page("My Website", "Welcome to My Site")
page.add_content(Heading("About Us", 2))
page.add_content(Paragraph("This is a simple webpage created with the HTML generator."))
'''
        },
        {
            'title': 'Modern Navigation Bar',
            'code': '''# Create a page with modern navigation
page = Page("My Blog", "John's Blog", use_modern_navbar=True)

# Configure the navbar brand
page.configure_navbar(
    brand_name="MyBrand",
    brand_icon="🚀",
    style="modern"
)

# Add navigation links with dropdown
nav_links = [
    {"url": "/", "text": "Home"},
    {"url": "/about", "text": "About"},
    {
        "url": "/services", 
        "text": "Services",
        "dropdown": [
            {"url": "/web-dev", "text": "Web Development"},
            {"url": "/mobile", "text": "Mobile Apps"}
        ]
    },
    {"url": "/contact", "text": "Contact"}
]
page.add_navbar(nav_links)
page.add_content(Heading("Welcome to My Blog", 1))
page.add_content(Paragraph("Experience the modern navigation bar with dropdown support and mobile responsiveness."))

# Run the website directly
page.run()
'''
        },
        {
            'title': 'Page with Enhanced CSS',
            'code': '''# Create a page with custom CSS styling
from html_generator.css import CSSBuilder, Style

page = Page("Styled Page", "Beautiful Design")

# Create custom CSS using the CSS builder
css_builder = CSSBuilder()
css_builder.add_rule(".custom-header", {
    "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "color": "white",
    "padding": "2rem",
    "border-radius": "10px",
    "text-align": "center"
})

# Add responsive breakpoints
css_builder.responsive_breakpoints(".custom-header",
    sm={"font-size": "1.2rem"},
    md={"font-size": "1.5rem"},
    lg={"font-size": "2rem"}
)

# Apply the custom CSS
page.custom_css = css_builder.render()

# Add content
page.add_content(Heading("Styled Header", 1, css_class="custom-header"))
page.add_content(Paragraph("This header uses custom CSS with responsive design."))

# Run the website
page.run()
'''
        },
        {
            'title': 'Card Layout',
            'code': '''# Create a page with cards
page = Page("Services", "Our Services")
page.add_content(Container())

# Add some cards
card1 = Card("Web Development", "We create modern, responsive websites.")
card1.add_class("mb-4")
page.add_content(card1)

card2 = Card("Mobile Apps", "Native and cross-platform mobile applications.")
card2.add_class("mb-4")
page.add_content(card2)
'''
        },
        {
            'title': 'Lists and Images',
            'code': '''# Create a page with lists and images
page = Page("Portfolio", "My Work")

page.add_content(Heading("Skills", 2))
skills_list = List([
    "Python Programming",
    "Web Development",
    "Database Design",
    "UI/UX Design"
], ordered=False)
skills_list.add_class("list-group list-group-flush")
page.add_content(skills_list)

page.add_content(Heading("Featured Project", 2))
page.add_content(Image("https://via.placeholder.com/600x300", "Project Screenshot"))
page.add_content(Paragraph("This is my latest project showcasing modern web technologies."))
'''
        }
    ]
    
    return render_template('examples.html', examples=examples)
