from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app import db
from models import GeneratedPage
import json

config_bp = Blueprint('config', __name__)

@config_bp.route('/navbar-config')
def navbar_config():
    """Show the navbar configuration interface"""
    return render_template('../tools/web_interface/navbar_config.html')

@config_bp.route('/navbar-config/preview', methods=['POST'])
def navbar_preview():
    """Generate preview of navbar configuration"""
    try:
        config_data = request.get_json()
        
        # Extract configuration
        brand_name = config_data.get('brand_name', 'Your Brand')
        brand_icon = config_data.get('brand_icon', '🌟')
        nav_links = config_data.get('nav_links', [])
        style = config_data.get('style', 'modern')
        
        # Create a temporary page object to generate navbar
        from pypage.page import Page
        temp_page = Page("Preview", "Header", use_modern_navbar=(style == 'modern'))
        temp_page.configure_navbar(brand_name=brand_name, brand_icon=brand_icon)
        temp_page.nav_links = nav_links
        
        # Generate just the navbar HTML
        navbar_html = temp_page.render_navbar()
        
        # Get CSS for the navbar
        navbar_css = ""
        if style == 'modern':
            navbar_css = temp_page.get_modern_navbar_css()
        
        return jsonify({
            'success': True,
            'navbar_html': navbar_html,
            'navbar_css': navbar_css
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@config_bp.route('/navbar-config/generate', methods=['POST'])
def generate_navbar_code():
    """Generate Python code for the navbar configuration"""
    try:
        config_data = request.get_json()
        
        # Extract configuration
        brand_name = config_data.get('brand_name', 'Your Brand')
        brand_icon = config_data.get('brand_icon', '🌟')
        nav_links = config_data.get('nav_links', [])
        style = config_data.get('style', 'modern')
        
        # Generate Python code
        nav_links_code = "[\n"
        for link in nav_links:
            if 'dropdown' in link and link['dropdown']:
                dropdown_items = "[\n"
                for item in link['dropdown']:
                    dropdown_items += f'        {{"url": "{item.get("url", "#")}", "text": "{item.get("text", "Item")}"}},\n'
                dropdown_items += "    ]"
                nav_links_code += f'    {{"url": "{link.get("url", "#")}", "text": "{link.get("text", "Link")}", "dropdown": {dropdown_items}}},\n'
            else:
                nav_links_code += f'    {{"url": "{link.get("url", "#")}", "text": "{link.get("text", "Link")}"}},\n'
        nav_links_code += "]"
        
        python_code = f'''# Create page with modern navigation
page = Page("Your Title", "Your Header", use_modern_navbar={style == 'modern'})

# Configure the navbar
page.configure_navbar(
    brand_name="{brand_name}",
    brand_icon="{brand_icon}",
    style="{style}",
    dropdown_support=True,
    mobile_responsive=True
)

# Add navigation links
nav_links = {nav_links_code}
page.add_navbar(nav_links)

# Add your content here
page.add_content(Heading("Welcome", 1))
page.add_content(Paragraph("Your content goes here"))

# Run the website
page.run()
'''
        
        return jsonify({
            'success': True,
            'python_code': python_code
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@config_bp.route('/css-builder')
def css_builder():
    """Show the CSS builder interface"""
    return render_template('../tools/web_interface/css_builder.html')

@config_bp.route('/css-builder/generate', methods=['POST'])
def generate_css():
    """Generate CSS from the builder configuration"""
    try:
        css_data = request.get_json()
        
        from pypage.css import CSSBuilder
        
        css_builder = CSSBuilder()
        
        # Process rules
        if 'rules' in css_data:
            for rule in css_data['rules']:
                selector = rule.get('selector', '')
                properties = rule.get('properties', {})
                css_builder.add_rule(selector, properties)
        
        # Process responsive rules
        if 'responsive' in css_data:
            for resp_rule in css_data['responsive']:
                selector = resp_rule.get('selector', '')
                breakpoints = resp_rule.get('breakpoints', {})
                css_builder.responsive_breakpoints(
                    selector,
                    xs=breakpoints.get('xs'),
                    sm=breakpoints.get('sm'),
                    md=breakpoints.get('md'),
                    lg=breakpoints.get('lg'),
                    xl=breakpoints.get('xl')
                )
        
        generated_css = css_builder.render()
        
        return jsonify({
            'success': True,
            'css': generated_css
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400