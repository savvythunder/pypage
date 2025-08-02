from typing import List as ListType, Dict, Any, Optional, Union
from .elements import Element, Container, Paragraph
from .page import Heading

class ComponentBase(Element):
    """Base class for creating custom components"""
    
    def __init__(self, tag: str = "div", css_class: Optional[str] = None, 
                 id_attr: Optional[str] = None, style: Optional[str] = None):
        super().__init__(tag, css_class=css_class, id_attr=id_attr, style=style)
        self.child_elements = []
    
    def add_element(self, element):
        """Add a child element to this component"""
        self.child_elements.append(element)
        return self
    
    def render(self):
        """Render the component with all child elements"""
        content = ""
        for element in self.child_elements:
            if hasattr(element, 'render'):
                content += element.render()
            else:
                content += str(element)
        
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>{content}</{self.tag}>"

class HeroSection(ComponentBase):
    """Hero section component"""
    
    def __init__(self, title: str, subtitle: str = "", button_text: str = "",
                 button_url: str = "#", background_class: str = "bg-primary text-white",
                 css_class: Optional[str] = None):
        hero_class = f"hero-section {background_class} text-center py-5"
        if css_class:
            hero_class += f" {css_class}"
        
        super().__init__(css_class=hero_class)
        
        # Build hero content
        container = Container()
        container.add_content(f'<h1 class="display-4">{title}</h1>')
        
        if subtitle:
            container.add_content(f'<p class="lead">{subtitle}</p>')
        
        if button_text:
            container.add_content(f'<a href="{button_url}" class="btn btn-light btn-lg mt-3">{button_text}</a>')
        
        self.add_element(container)

class FeatureCard(ComponentBase):
    """Feature card component"""
    
    def __init__(self, title: str, description: str, icon: str = "",
                 css_class: Optional[str] = None):
        card_class = "col-md-4 mb-4"
        if css_class:
            card_class += f" {css_class}"
        
        super().__init__(css_class=card_class)
        
        # Build card content
        card_html = '<div class="card h-100 text-center">'
        card_html += '<div class="card-body">'
        
        if icon:
            card_html += f'<div class="mb-3"><i class="{icon} fa-3x text-primary"></i></div>'
        
        card_html += f'<h5 class="card-title">{title}</h5>'
        card_html += f'<p class="card-text">{description}</p>'
        card_html += '</div></div>'
        
        self.content = card_html

class Navbar(ComponentBase):
    """Navigation bar component"""
    
    def __init__(self, brand_name: str, brand_url: str = "#", 
                 nav_items: Optional[ListType[Dict[str, str]]] = None,
                 theme: str = "dark", css_class: Optional[str] = None):
        navbar_class = f"navbar navbar-expand-lg navbar-{theme}"
        if theme == "dark":
            navbar_class += " bg-dark"
        else:
            navbar_class += " bg-light"
            
        if css_class:
            navbar_class += f" {css_class}"
        
        super().__init__(tag="nav", css_class=navbar_class)
        
        # Build navbar content
        navbar_html = f'''
        <div class="container">
            <a class="navbar-brand" href="{brand_url}">{brand_name}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
        '''
        
        if nav_items:
            for item in nav_items:
                navbar_html += f'<li class="nav-item">'
                navbar_html += f'<a class="nav-link" href="{item.get("url", "#")}">{item.get("text", "Link")}</a>'
                navbar_html += '</li>'
        
        navbar_html += '''
                </ul>
            </div>
        </div>
        '''
        
        self.content = navbar_html

class Alert(ComponentBase):
    """Bootstrap alert component"""
    
    def __init__(self, message: str, alert_type: str = "info", dismissible: bool = False,
                 css_class: Optional[str] = None):
        alert_class = f"alert alert-{alert_type}"
        if dismissible:
            alert_class += " alert-dismissible fade show"
        
        if css_class:
            alert_class += f" {css_class}"
        
        super().__init__(css_class=alert_class)
        
        alert_html = message
        if dismissible:
            alert_html += '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>'
        
        self.content = alert_html

class Badge(Element):
    """Bootstrap badge component"""
    
    def __init__(self, text: str, badge_type: str = "secondary", 
                 css_class: Optional[str] = None):
        badge_class = f"badge bg-{badge_type}"
        if css_class:
            badge_class += f" {css_class}"
        
        super().__init__("span", text, css_class=badge_class)

class ProgressBar(ComponentBase):
    """Bootstrap progress bar component"""
    
    def __init__(self, value: int, max_value: int = 100, label: str = "",
                 bar_type: str = "primary", striped: bool = False, 
                 animated: bool = False, css_class: Optional[str] = None):
        progress_class = "progress"
        if css_class:
            progress_class += f" {css_class}"
        
        super().__init__(css_class=progress_class)
        
        percentage = (value / max_value) * 100
        bar_class = f"progress-bar bg-{bar_type}"
        
        if striped:
            bar_class += " progress-bar-striped"
        if animated:
            bar_class += " progress-bar-animated"
        
        progress_html = f'''<div class="{bar_class}" role="progressbar" style="width: {percentage}%" aria-valuenow="{value}" aria-valuemin="0" aria-valuemax="{max_value}">{label}</div>'''
        
        self.content = progress_html
    
    def render(self):
        """Override render to use content instead of child_elements"""
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>{self.content}</{self.tag}>"

class Accordion(ComponentBase):
    """Bootstrap accordion component"""
    
    def __init__(self, accordion_id: str = "accordion", css_class: Optional[str] = None):
        accordion_class = "accordion"
        if css_class:
            accordion_class += f" {css_class}"
        
        super().__init__(css_class=accordion_class)
        self.set_id(accordion_id)
        self.accordion_id = accordion_id
        self.items = []
    
    def add_item(self, title: str, content: str, expanded: bool = False):
        """Add an accordion item"""
        item_id = f"{self.accordion_id}-item-{len(self.items)}"
        collapse_id = f"{self.accordion_id}-collapse-{len(self.items)}"
        
        item_html = f'''
        <div class="accordion-item">
            <h2 class="accordion-header" id="{item_id}">
                <button class="accordion-button{'collapsed' if not expanded else ''}" 
                        type="button" 
                        data-bs-toggle="collapse" 
                        data-bs-target="#{collapse_id}">
                    {title}
                </button>
            </h2>
            <div id="{collapse_id}" 
                 class="accordion-collapse collapse{' show' if expanded else ''}" 
                 data-bs-parent="#{self.accordion_id}">
                <div class="accordion-body">
                    {content}
                </div>
            </div>
        </div>
        '''
        
        self.items.append(item_html)
        return self
    
    def render(self):
        """Render the accordion with all items"""
        self.content = "".join(self.items)
        return super().render()

class Modal(ComponentBase):
    """Bootstrap modal component"""
    
    def __init__(self, modal_id: str, title: str, body: str, 
                 footer: str = "", size: str = "", css_class: Optional[str] = None):
        modal_class = "modal fade"
        if css_class:
            modal_class += f" {css_class}"
        
        super().__init__(css_class=modal_class)
        self.set_id(modal_id)
        
        dialog_class = "modal-dialog"
        if size:
            dialog_class += f" modal-{size}"
        
        modal_html = f'''
        <div class="{dialog_class}">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    {body}
                </div>
        '''
        
        if footer:
            modal_html += f'<div class="modal-footer">{footer}</div>'
        
        modal_html += '''
            </div>
        </div>
        '''
        
        self.content = modal_html