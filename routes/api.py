from flask import Blueprint, request, jsonify
from pypage import Page, Heading, Paragraph, HtmlList, Image, Card, Container
from models import GeneratedPage, db
import uuid
import re
import os

api_bp = Blueprint('api', __name__)

@api_bp.route('/generate', methods=['POST'])
def api_generate():
    """API endpoint to generate HTML from code"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    code = data.get('code', '')
    title = data.get('title', 'Generated Page')
    save_to_db = data.get('save', True)
    
    if not code.strip():
        return jsonify({'error': 'Code is required'}), 400
    
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
            return jsonify({'error': 'Code must create a Page object and assign it to variable "page"'}), 400
        
        # Generate HTML
        html_content = page.generate_html()
        
        response_data = {
            'html': html_content,
            'title': title
        }
        
        if save_to_db:
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
            
            response_data['id'] = generated_page.id
            response_data['filename'] = filename
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({'error': f'Error generating page: {str(e)}'}), 500

@api_bp.route('/pages', methods=['GET'])
def api_list_pages():
    """API endpoint to list all generated pages"""
    pages = GeneratedPage.query.order_by(GeneratedPage.created_at.desc()).all()
    
    pages_data = []
    for page in pages:
        pages_data.append({
            'id': page.id,
            'title': page.title,
            'filename': page.filename,
            'created_at': page.created_at.isoformat(),
            'updated_at': page.updated_at.isoformat()
        })
    
    return jsonify({'pages': pages_data})

@api_bp.route('/pages/<int:page_id>', methods=['GET'])
def api_get_page(page_id):
    """API endpoint to get a specific page"""
    page = GeneratedPage.query.get_or_404(page_id)
    
    return jsonify({
        'id': page.id,
        'title': page.title,
        'filename': page.filename,
        'code': page.code,
        'html': page.html_content,
        'created_at': page.created_at.isoformat(),
        'updated_at': page.updated_at.isoformat()
    })

@api_bp.route('/pages/<int:page_id>', methods=['DELETE'])
def api_delete_page(page_id):
    """API endpoint to delete a page"""
    page = GeneratedPage.query.get_or_404(page_id)
    
    # Delete file if it exists
    file_path = os.path.join('generated_pages', page.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    
    # Delete from database
    db.session.delete(page)
    db.session.commit()
    
    return jsonify({'message': f'Page "{page.title}" deleted successfully'})
