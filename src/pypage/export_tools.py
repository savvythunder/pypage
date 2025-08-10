"""
Export functionality for HTML generator - PDF and JSON support
"""
import json
from typing import Dict, Any, Optional, List, Union
from .elements import Element
from .page import Page

class ExportManager:
    """Manager for exporting HTML generator content to various formats"""
    
    def __init__(self):
        self.pdf_available = False
        self.json_available = True
        
        # Try to import PDF libraries
        try:
            import weasyprint
            self.pdf_library = "weasyprint"
            self.pdf_available = True
        except ImportError:
            try:
                import pdfkit
                self.pdf_library = "pdfkit"
                self.pdf_available = True
            except ImportError:
                self.pdf_library = None

    def to_dict(self, element: Union[Element, Page]) -> Dict[str, Any]:
        """Convert element to dictionary representation"""
        if isinstance(element, Page):
            return self._page_to_dict(element)
        elif isinstance(element, Element):
            return self._element_to_dict(element)
        else:
            raise TypeError(f"Cannot serialize object of type {type(element)}")
    
    def from_dict(self, data: Dict[str, Any]) -> Union[Element, Page]:
        """Create element from dictionary representation"""
        if data.get('type') == 'Page':
            return self._dict_to_page(data)
        else:
            return self._dict_to_element(data)
    
    def to_json(self, element: Union[Element, Page], indent: int = 2) -> str:
        """Convert element to JSON string"""
        return json.dumps(self.to_dict(element), indent=indent)
    
    def from_json(self, json_str: str) -> Union[Element, Page]:
        """Create element from JSON string"""
        data = json.loads(json_str)
        return self.from_dict(data)
    
    def to_pdf(self, html_content: str, output_path: str, 
               options: Optional[Dict[str, Any]] = None) -> bool:
        """Export HTML to PDF"""
        if not self.pdf_available:
            raise ImportError("No PDF library available. Install weasyprint or pdfkit.")
        
        try:
            if self.pdf_library == "weasyprint":
                return self._export_with_weasyprint(html_content, output_path, options)
            elif self.pdf_library == "pdfkit":
                return self._export_with_pdfkit(html_content, output_path, options)
        except Exception as e:
            print(f"PDF export failed: {e}")
            return False
        
        return False
    
    def _page_to_dict(self, page: Page) -> Dict[str, Any]:
        """Convert Page to dictionary"""
        return {
            'type': 'Page',
            'title': page.title,
            'header_text': page.header_text,
            'logo_url': getattr(page, 'logo_url', None),
            'theme': getattr(page, 'current_theme', 'bootstrap'),
            'content': [self._element_to_dict(elem) for elem in page.content],
            'custom_css': getattr(page, 'custom_css', []),
            'custom_js': getattr(page, 'custom_js', []),
            'meta_tags': getattr(page, 'meta_tags', {}),
            'navbar': self._element_to_dict(page.navbar) if hasattr(page, 'navbar') and page.navbar else None
        }
    
    def _element_to_dict(self, element: Element) -> Dict[str, Any]:
        """Convert Element to dictionary"""
        data = {
            'type': 'Element',
            'class_name': element.__class__.__name__,
            'tag': element.tag,
            'css_class': element.css_class,
            'id_attr': element.id_attr,
            'style': element.style,
            'attributes': getattr(element, 'attributes', {})
        }
        
        # Handle content
        if hasattr(element, 'content'):
            if isinstance(element.content, list):
                data['content'] = [
                    self._element_to_dict(item) if hasattr(item, 'render') else str(item)
                    for item in element.content
                ]
            elif hasattr(element.content, 'render'):
                data['content'] = self._element_to_dict(element.content)
            else:
                data['content'] = str(element.content)
        
        # Handle child elements
        if hasattr(element, 'child_elements'):
            data['child_elements'] = [
                self._element_to_dict(child) if hasattr(child, 'render') else str(child)
                for child in element.child_elements
            ]
        
        # Handle special element properties
        if hasattr(element, 'fields'):  # Form elements
            data['fields'] = [self._element_to_dict(field) for field in element.fields]
        
        if hasattr(element, 'columns'):  # Row elements
            data['columns'] = [self._element_to_dict(col) for col in element.columns]
        
        return data
    
    def _dict_to_page(self, data: Dict[str, Any]) -> Page:
        """Create Page from dictionary"""
        from .page import Page
        
        page = Page(data['title'], data['header_text'], data.get('logo_url'))
        
        # Set theme
        if 'theme' in data:
            page.set_theme(data['theme'])
        
        # Add content
        for content_data in data.get('content', []):
            if isinstance(content_data, dict):
                element = self._dict_to_element(content_data)
                page.add_content(element)
            else:
                page.add_content(str(content_data))
        
        # Add custom CSS and JS
        for css in data.get('custom_css', []):
            page.add_css(css)
        
        for js in data.get('custom_js', []):
            page.add_js(js)
        
        # Add meta tags
        for name, content in data.get('meta_tags', {}).items():
            page.add_meta_tag(name, content)
        
        return page
    
    def _dict_to_element(self, data: Dict[str, Any]) -> Element:
        """Create Element from dictionary"""
        from .elements import Element, Container, Div, Paragraph
        from .forms import Form, Input, Button, TextArea, Select
        from .layout import Row, Column, Flex
        from .components import Alert, Badge, ProgressBar, Accordion, Modal
        
        class_name = data.get('class_name', 'Element')
        
        # Map class names to actual classes
        class_map = {
            'Element': Element,
            'Container': Container,
            'Div': Div,
            'Paragraph': Paragraph,
            'Form': Form,
            'Input': Input,
            'Button': Button,
            'TextArea': TextArea,
            'Select': Select,
            'Row': Row,
            'Column': Column,
            'Flex': Flex,
            'Alert': Alert,
            'Badge': Badge,
            'ProgressBar': ProgressBar,
            'Accordion': Accordion,
            'Modal': Modal
        }
        
        ElementClass = class_map.get(class_name, Element)
        
        # Create basic element
        element = ElementClass.__new__(ElementClass)
        element.tag = data.get('tag', 'div')
        element.css_class = data.get('css_class')
        element.id_attr = data.get('id_attr')
        element.style = data.get('style')
        element.attributes = data.get('attributes', {})
        
        # Handle content
        if 'content' in data:
            content = data['content']
            if isinstance(content, list):
                element.content = [
                    self._dict_to_element(item) if isinstance(item, dict) else str(item)
                    for item in content
                ]
            elif isinstance(content, dict):
                element.content = self._dict_to_element(content)
            else:
                element.content = str(content)
        
        # Handle child elements
        if 'child_elements' in data:
            element.child_elements = [
                self._dict_to_element(child) if isinstance(child, dict) else str(child)
                for child in data['child_elements']
            ]
        
        # Handle special properties
        if 'fields' in data:
            element.fields = [self._dict_to_element(field) for field in data['fields']]
        
        if 'columns' in data:
            element.columns = [self._dict_to_element(col) for col in data['columns']]
        
        return element
    
    def _export_with_weasyprint(self, html_content: str, output_path: str, 
                               options: Optional[Dict[str, Any]] = None) -> bool:
        """Export using WeasyPrint"""
        try:
            import weasyprint
            
            # Default options
            default_options = {
                'page_size': 'A4',
                'margin': '1in'
            }
            if options:
                default_options.update(options)
            
            # Create HTML document
            html_doc = weasyprint.HTML(string=html_content)
            
            # Generate PDF
            html_doc.write_pdf(output_path)
            return True
            
        except Exception as e:
            print(f"WeasyPrint export failed: {e}")
            return False
    
    def _export_with_pdfkit(self, html_content: str, output_path: str, 
                           options: Optional[Dict[str, Any]] = None) -> bool:
        """Export using pdfkit"""
        try:
            import pdfkit
            
            # Default options
            default_options = {
                'page-size': 'A4',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None
            }
            if options:
                default_options.update(options)
            
            # Generate PDF
            pdfkit.from_string(html_content, output_path, options=default_options)
            return True
            
        except Exception as e:
            print(f"pdfkit export failed: {e}")
            return False

class SerializableMixin:
    """Mixin to add serialization capabilities to components"""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert this component to dictionary"""
        export_manager = ExportManager()
        return export_manager.to_dict(self)
    
    def to_json(self, indent: int = 2) -> str:
        """Convert this component to JSON"""
        export_manager = ExportManager()
        return export_manager.to_json(self, indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create component from dictionary"""
        export_manager = ExportManager()
        return export_manager.from_dict(data)
    
    @classmethod
    def from_json(cls, json_str: str):
        """Create component from JSON"""
        export_manager = ExportManager()
        return export_manager.from_json(json_str)

# Global export manager instance
export_manager = ExportManager()

def to_dict(element: Union[Element, Page]) -> Dict[str, Any]:
    """Convert element to dictionary"""
    return export_manager.to_dict(element)

def from_dict(data: Dict[str, Any]) -> Union[Element, Page]:
    """Create element from dictionary"""
    return export_manager.from_dict(data)

def to_json(element: Union[Element, Page], indent: int = 2) -> str:
    """Convert element to JSON"""
    return export_manager.to_json(element, indent)

def from_json(json_str: str) -> Union[Element, Page]:
    """Create element from JSON"""
    return export_manager.from_json(json_str)

def to_pdf(html_content: str, output_path: str, 
           options: Optional[Dict[str, Any]] = None) -> bool:
    """Export HTML to PDF"""
    return export_manager.to_pdf(html_content, output_path, options)

def check_pdf_support() -> Dict[str, Any]:
    """Check which PDF libraries are available"""
    info = {
        'weasyprint': False,
        'pdfkit': False,
        'recommended': None
    }
    
    try:
        import weasyprint
        info['weasyprint'] = True
        info['recommended'] = 'weasyprint'
    except ImportError:
        pass
    
    try:
        import pdfkit
        info['pdfkit'] = True
        if not info['recommended']:
            info['recommended'] = 'pdfkit'
    except ImportError:
        pass
    
    return info