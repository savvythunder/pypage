from typing import List as ListType, Dict, Any, Optional
from .elements import Element

class Form(Element):
    """Form element with validation support"""
    
    def __init__(self, action: str = "", method: str = "POST", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        super().__init__("form", css_class=css_class, id_attr=id_attr)
        self.set_attribute("action", action)
        self.set_attribute("method", method)
        self.fields = []

    def add_field(self, field):
        """Add a form field"""
        self.fields.append(field)
        return self

    def render(self):
        """Render the form with all fields"""
        fields_html = "\n".join(field.render() for field in self.fields)
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>\n{fields_html}\n</{self.tag}>"

class Input(Element):
    """Input element"""
    
    def __init__(self, input_type: str = "text", name: str = "", value: str = "",
                 placeholder: str = "", required: bool = False, css_class: Optional[str] = None,
                 id_attr: Optional[str] = None, label: Optional[str] = None):
        super().__init__("input", css_class=css_class, id_attr=id_attr)
        self.set_attribute("type", input_type)
        self.set_attribute("name", name)
        if value:
            self.set_attribute("value", value)
        if placeholder:
            self.set_attribute("placeholder", placeholder)
        if required:
            self.set_attribute("required", "required")
        self.label = label

    def render(self):
        """Render the input with optional label"""
        input_html = f"<{self.tag}{self.render_attributes()}>"
        
        if self.label:
            label_for = self.attributes.get('id', self.attributes.get('name', ''))
            label_html = f'<label for="{label_for}" class="form-label">{self.label}</label>'
            return f'<div class="mb-3">{label_html}\n{input_html}</div>'
        
        return input_html

class TextArea(Element):
    """Textarea element"""
    
    def __init__(self, name: str = "", value: str = "", placeholder: str = "",
                 rows: int = 3, cols: Optional[int] = None, required: bool = False, 
                 css_class: Optional[str] = None, id_attr: Optional[str] = None, 
                 label: Optional[str] = None):
        super().__init__("textarea", value, css_class=css_class, id_attr=id_attr)
        self.set_attribute("name", name)
        self.set_attribute("rows", str(rows))
        if cols:
            self.set_attribute("cols", str(cols))
        if placeholder:
            self.set_attribute("placeholder", placeholder)
        if required:
            self.set_attribute("required", "required")
        self.label = label

    def render(self):
        """Render the textarea with optional label"""
        textarea_html = f"<{self.tag}{self.render_attributes()}>{self.content}</{self.tag}>"
        
        if self.label:
            label_for = self.attributes.get('id', self.attributes.get('name', ''))
            label_html = f'<label for="{label_for}" class="form-label">{self.label}</label>'
            return f'<div class="mb-3">{label_html}\n{textarea_html}</div>'
        
        return textarea_html

class Select(Element):
    """Select element"""
    
    def __init__(self, name: str = "", options: Optional[ListType[Dict[str, str]]] = None,
                 multiple: bool = False, required: bool = False, css_class: Optional[str] = None,
                 id_attr: Optional[str] = None, label: Optional[str] = None):
        super().__init__("select", css_class=css_class, id_attr=id_attr)
        self.set_attribute("name", name)
        if multiple:
            self.set_attribute("multiple", "multiple")
        if required:
            self.set_attribute("required", "required")
        self.options = options if options is not None else []
        self.label = label

    def add_option(self, value: str, text: str, selected: bool = False):
        """Add an option to the select"""
        self.options.append({"value": value, "text": text, "selected": str(selected)})
        return self

    def render(self):
        """Render the select with options"""
        options_html = ""
        for option in self.options:
            selected_attr = ' selected' if option.get('selected', False) else ''
            options_html += f'<option value="{option["value"]}"{selected_attr}>{option["text"]}</option>\n'
        
        select_html = f"<{self.tag}{self.render_attributes()}>\n{options_html}</{self.tag}>"
        
        if self.label:
            label_for = self.attributes.get('id', self.attributes.get('name', ''))
            label_html = f'<label for="{label_for}" class="form-label">{self.label}</label>'
            return f'<div class="mb-3">{label_html}\n{select_html}</div>'
        
        return select_html

class Button(Element):
    """Button element"""
    
    def __init__(self, text: str, button_type: str = "button", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None, onclick: Optional[str] = None):
        default_class = "btn btn-primary"
        if css_class:
            button_class = f"{default_class} {css_class}"
        else:
            button_class = default_class
            
        super().__init__("button", text, css_class=button_class, id_attr=id_attr)
        self.set_attribute("type", button_type)
        if onclick:
            self.set_attribute("onclick", onclick)
