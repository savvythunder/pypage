from typing import Dict, Any, Optional

class CSSBuilder:
    """CSS builder for creating inline and external styles"""
    
    def __init__(self):
        self.rules = {}
        self.media_queries = {}

    def add_rule(self, selector: str, properties: Dict[str, str]):
        """Add a CSS rule"""
        self.rules[selector] = properties
        return self

    def add_media_query(self, media: str, rules: Dict[str, Dict[str, str]]):
        """Add media query rules"""
        self.media_queries[media] = rules
        return self

    def responsive_breakpoints(self, selector: str, 
                             xs: Optional[Dict[str, str]] = None,
                             sm: Optional[Dict[str, str]] = None,
                             md: Optional[Dict[str, str]] = None,
                             lg: Optional[Dict[str, str]] = None,
                             xl: Optional[Dict[str, str]] = None):
        """Add responsive breakpoint rules"""
        if xs:
            self.rules[selector] = xs
        if sm:
            self.add_media_query("(min-width: 576px)", {selector: sm})
        if md:
            self.add_media_query("(min-width: 768px)", {selector: md})
        if lg:
            self.add_media_query("(min-width: 992px)", {selector: lg})
        if xl:
            self.add_media_query("(min-width: 1200px)", {selector: xl})
        return self

    def render(self):
        """Render the CSS as a string"""
        css = ""
        
        # Regular rules
        for selector, properties in self.rules.items():
            css += f"{selector} {{\n"
            for prop, value in properties.items():
                css += f"    {prop}: {value};\n"
            css += "}\n\n"
        
        # Media queries
        for media, rules in self.media_queries.items():
            css += f"@media {media} {{\n"
            for selector, properties in rules.items():
                css += f"    {selector} {{\n"
                for prop, value in properties.items():
                    css += f"        {prop}: {value};\n"
                css += "    }\n"
            css += "}\n\n"
        
        return css

class Style:
    """Individual style builder with method chaining"""
    
    def __init__(self, selector: str):
        self.selector = selector
        self.properties = {}

    def color(self, value: str):
        """Set color property"""
        self.properties['color'] = value
        return self

    def background_color(self, value: str):
        """Set background-color property"""
        self.properties['background-color'] = value
        return self

    def font_size(self, value: str):
        """Set font-size property"""
        self.properties['font-size'] = value
        return self

    def font_weight(self, value: str):
        """Set font-weight property"""
        self.properties['font-weight'] = value
        return self

    def margin(self, value: str):
        """Set margin property"""
        self.properties['margin'] = value
        return self

    def padding(self, value: str):
        """Set padding property"""
        self.properties['padding'] = value
        return self

    def width(self, value: str):
        """Set width property"""
        self.properties['width'] = value
        return self

    def height(self, value: str):
        """Set height property"""
        self.properties['height'] = value
        return self

    def display(self, value: str):
        """Set display property"""
        self.properties['display'] = value
        return self

    def text_align(self, value: str):
        """Set text-align property"""
        self.properties['text-align'] = value
        return self

    def border(self, value: str):
        """Set border property"""
        self.properties['border'] = value
        return self

    def border_radius(self, value: str):
        """Set border-radius property"""
        self.properties['border-radius'] = value
        return self

    def box_shadow(self, value: str):
        """Set box-shadow property"""
        self.properties['box-shadow'] = value
        return self

    def custom(self, property_name: str, value: str):
        """Set custom CSS property"""
        self.properties[property_name] = value
        return self

    def render(self):
        """Render the style as CSS"""
        if not self.properties:
            return ""
        
        css = f"{self.selector} {{\n"
        for prop, value in self.properties.items():
            css += f"    {prop}: {value};\n"
        css += "}\n"
        return css
