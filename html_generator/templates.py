from typing import Dict, Optional, Any
from .elements import Element

class Template:
    """Template class for reusable HTML blocks"""
    
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.slots = {}
    
    def define_slot(self, slot_name: str, default_content: str = ""):
        """Define a slot in the template"""
        self.slots[slot_name] = default_content
        return self
    
    def render(self, slot_map: Optional[Dict[str, str]] = None):
        """Render the template with slot content"""
        if slot_map is None:
            slot_map = {}
            
        rendered_content = self.content
        
        # Replace slots with provided content or defaults
        for slot_name, default_content in self.slots.items():
            slot_placeholder = f"{{{{ {slot_name} }}}}"
            slot_content = slot_map.get(slot_name, default_content)
            rendered_content = rendered_content.replace(slot_placeholder, slot_content)
        
        return rendered_content

class Slot(Element):
    """Slot element for template placeholders"""
    
    def __init__(self, name: str, default_content: str = "", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        self.slot_name = name
        self.default_content = default_content
        super().__init__("div", default_content, css_class=css_class, id_attr=id_attr)
    
    def render(self):
        """Render the slot as a placeholder"""
        return f"{{ {self.slot_name} }}"

class TemplateManager:
    """Manager for handling multiple templates"""
    
    def __init__(self):
        self.templates = {}
    
    def register_template(self, template: Template):
        """Register a template"""
        self.templates[template.name] = template
        return self
    
    def get_template(self, name: str) -> Optional[Template]:
        """Get a template by name"""
        return self.templates.get(name)
    
    def render_template(self, name: str, slot_map: Optional[Dict[str, str]] = None):
        """Render a template by name"""
        template = self.get_template(name)
        if template:
            return template.render(slot_map)
        return f"<!-- Template '{name}' not found -->"

# Common template definitions
def create_hero_template():
    """Create a hero section template"""
    hero_template = Template("hero", """
    <div class="hero-section bg-primary text-white text-center py-5">
        <div class="container">
            <h1 class="display-4">{{ title }}</h1>
            <p class="lead">{{ subtitle }}</p>
            <div class="hero-actions">
                {{ actions }}
            </div>
        </div>
    </div>
    """)
    hero_template.define_slot("title", "Welcome")
    hero_template.define_slot("subtitle", "Your amazing website")
    hero_template.define_slot("actions", "")
    return hero_template

def create_card_grid_template():
    """Create a card grid template"""
    card_grid_template = Template("card_grid", """
    <div class="container my-5">
        <div class="row">
            <div class="col-12 text-center mb-4">
                <h2>{{ section_title }}</h2>
                <p class="text-muted">{{ section_subtitle }}</p>
            </div>
        </div>
        <div class="row">
            {{ cards }}
        </div>
    </div>
    """)
    card_grid_template.define_slot("section_title", "Features")
    card_grid_template.define_slot("section_subtitle", "Discover what we offer")
    card_grid_template.define_slot("cards", "")
    return card_grid_template

def create_footer_template():
    """Create a footer template"""
    footer_template = Template("footer", """
    <footer class="bg-dark text-white py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h5>{{ company_name }}</h5>
                    <p>{{ company_description }}</p>
                </div>
                <div class="col-md-6">
                    <h5>Links</h5>
                    {{ links }}
                </div>
            </div>
            <hr class="my-3">
            <div class="text-center">
                <small>&copy; 2025 {{ company_name }}. {{ copyright_text }}</small>
            </div>
        </div>
    </footer>
    """)
    footer_template.define_slot("company_name", "Your Company")
    footer_template.define_slot("company_description", "Building amazing web experiences.")
    footer_template.define_slot("links", "")
    footer_template.define_slot("copyright_text", "All rights reserved.")
    return footer_template