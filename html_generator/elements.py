from typing import List as ListType, Dict, Any, Optional

class Element:
    """Base class for all HTML elements"""
    
    def __init__(self, tag: str, content: str = "", attributes: Optional[Dict[str, str]] = None,
                 css_class: Optional[str] = None, id_attr: Optional[str] = None,
                 style: Optional[str] = None, class_name: Optional[str] = None):
        self.tag = tag
        self.content = content
        self.attributes = attributes if attributes is not None else {}
        
        # Handle class_name parameter (alias for css_class)
        final_class = class_name or css_class
        if final_class:
            self.attributes['class'] = final_class
        if id_attr:
            self.attributes['id'] = id_attr
        if style:
            self.attributes['style'] = style

    def set_attribute(self, name: str, value: str):
        """Set an attribute on the element"""
        self.attributes[name] = value
        return self

    def add_class(self, css_class: str):
        """Add a CSS class to the element"""
        current_class = self.attributes.get('class', '')
        if current_class:
            self.attributes['class'] = f"{current_class} {css_class}"
        else:
            self.attributes['class'] = css_class
        return self

    def set_id(self, id_attr: str):
        """Set the ID attribute"""
        self.attributes['id'] = id_attr
        return self
    
    def set_style(self, style: str):
        """Set inline CSS styles"""
        self.attributes['style'] = style
        return self
    
    def add_style(self, style: str):
        """Add to existing inline CSS styles"""
        current_style = self.attributes.get('style', '')
        if current_style:
            # Add semicolon if not present
            if not current_style.rstrip().endswith(';'):
                current_style += '; '
            else:
                current_style += ' '
        self.attributes['style'] = current_style + style
        return self
    
    def set_event(self, event: str, handler: str):
        """Set JavaScript event handler"""
        self.attributes[event] = handler
        return self
    
    def on_click(self, handler: str):
        """Set onclick event handler"""
        return self.set_event('onclick', handler)
    
    def on_submit(self, handler: str):
        """Set onsubmit event handler"""
        return self.set_event('onsubmit', handler)
    
    def on_change(self, handler: str):
        """Set onchange event handler"""
        return self.set_event('onchange', handler)
    
    def on_hover(self, handler: str):
        """Set onmouseover event handler"""
        return self.set_event('onmouseover', handler)

    def render_attributes(self):
        """Render HTML attributes"""
        if not self.attributes:
            return ""
        attr_list = [f'{key}="{value}"' for key, value in self.attributes.items()]
        return " " + " ".join(attr_list)

    def render(self):
        """Render the element as HTML"""
        attrs = self.render_attributes()
        if self.content:
            return f"<{self.tag}{attrs}>{self.content}</{self.tag}>"
        else:
            return f"<{self.tag}{attrs}></{self.tag}>"

class Paragraph(Element):
    """Paragraph element"""
    
    def __init__(self, text: str, css_class: Optional[str] = None, id_attr: Optional[str] = None):
        super().__init__("p", text, css_class=css_class, id_attr=id_attr)

class HtmlList(Element):
    """List element (ul or ol)"""
    
    def __init__(self, items: ListType[str], ordered: bool = False, css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        tag = "ol" if ordered else "ul"
        self.items = items
        super().__init__(tag, css_class=css_class, id_attr=id_attr)

    def add_item(self, item: str):
        """Add an item to the list"""
        self.items.append(item)
        return self

    def render(self):
        """Render the list as HTML"""
        items_html = "".join(f"<li>{item}</li>" for item in self.items)
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>{items_html}</{self.tag}>"

class Image(Element):
    """Image element"""
    
    def __init__(self, src: str, alt: str = "", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None, width: Optional[str] = None, height: Optional[str] = None):
        super().__init__("img", css_class=css_class, id_attr=id_attr)
        self.set_attribute("src", src)
        self.set_attribute("alt", alt)
        if width:
            self.set_attribute("width", width)
        if height:
            self.set_attribute("height", height)

    def render(self):
        """Render the image as HTML"""
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>"

class Link(Element):
    """Anchor/Link element"""
    
    def __init__(self, text: str, href: str = "#", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None, target: Optional[str] = None):
        super().__init__("a", text, css_class=css_class, id_attr=id_attr)
        self.set_attribute("href", href)
        if target:
            self.set_attribute("target", target)

class Div(Element):
    """Div container element"""
    
    def __init__(self, content: str = "", css_class: Optional[str] = None, id_attr: Optional[str] = None):
        super().__init__("div", content, css_class=css_class, id_attr=id_attr)

    def add_content(self, content):
        """Add content to the div"""
        if hasattr(content, 'render'):
            self.content += content.render()
        else:
            self.content += str(content)
        return self

class Section(Element):
    """Section element"""
    
    def __init__(self, content: str = "", css_class: Optional[str] = None, id_attr: Optional[str] = None):
        super().__init__("section", content, css_class=css_class, id_attr=id_attr)

    def add_content(self, content):
        """Add content to the section"""
        if hasattr(content, 'render'):
            self.content += content.render()
        else:
            self.content += str(content)
        return self

class Card(Element):
    """Bootstrap card component"""
    
    def __init__(self, title: str = "", body: str = "", css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        self.title = title
        self.body = body
        card_class = "card"
        if css_class:
            card_class += f" {css_class}"
        super().__init__("div", css_class=card_class, id_attr=id_attr)

    def render(self):
        """Render the card as HTML"""
        title_html = f'<h5 class="card-title">{self.title}</h5>' if self.title else ""
        body_html = f'<p class="card-text">{self.body}</p>' if self.body else ""
        
        content = f"""
        <div class="card-body">
            {title_html}
            {body_html}
        </div>
        """
        
        attrs = self.render_attributes()
        return f"<{self.tag}{attrs}>{content}</{self.tag}>"

class Container(Element):
    """Bootstrap container"""
    
    def __init__(self, content: str = "", fluid: bool = False, css_class: Optional[str] = None,
                 id_attr: Optional[str] = None):
        container_class = "container-fluid" if fluid else "container"
        if css_class:
            container_class += f" {css_class}"
        super().__init__("div", content, css_class=container_class, id_attr=id_attr)

    def add_content(self, content):
        """Add content to the container"""
        if hasattr(content, 'render'):
            self.content += content.render()
        else:
            self.content += str(content)
        return self
