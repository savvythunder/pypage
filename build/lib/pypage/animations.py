"""
Animation and transition support for HTML generator components
"""
from typing import Optional, Dict, Any
from .elements import Element

class Animation:
    """Base animation class for CSS animations"""
    
    def __init__(self, name: str, duration: str = "0.3s", timing: str = "ease-in-out", 
                 delay: str = "0s", fill_mode: str = "forwards"):
        self.name = name
        self.duration = duration
        self.timing = timing
        self.delay = delay
        self.fill_mode = fill_mode
    
    def to_css(self) -> str:
        """Generate CSS animation property"""
        return f"animation: {self.name} {self.duration} {self.timing} {self.delay} {self.fill_mode};"

class FadeIn(Element):
    """Fade in animation wrapper"""
    
    def __init__(self, content, duration: str = "0.5s", delay: str = "0s", 
                 css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.content = content
        self.duration = duration
        self.delay = delay
        
        # Add animation styles
        animation_style = f"opacity: 0; animation: fadeIn {duration} ease-in-out {delay} forwards;"
        if self.style:
            self.style += f" {animation_style}"
        else:
            self.style = animation_style
    
    def render(self):
        attrs = self.render_attributes()
        content_html = ""
        if hasattr(self.content, 'render'):
            content_html = self.content.render()
        else:
            content_html = str(self.content)
        
        # Add CSS keyframes
        css = """
        <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
        """
        
        return f"{css}<{self.tag}{attrs}>{content_html}</{self.tag}>"

class SlideUp(Element):
    """Slide up animation wrapper"""
    
    def __init__(self, content, duration: str = "0.5s", delay: str = "0s", 
                 distance: str = "30px", css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.content = content
        self.duration = duration
        self.delay = delay
        self.distance = distance
        
        # Add animation styles
        animation_style = f"transform: translateY({distance}); opacity: 0; animation: slideUp {duration} ease-out {delay} forwards;"
        if self.style:
            self.style += f" {animation_style}"
        else:
            self.style = animation_style
    
    def render(self):
        attrs = self.render_attributes()
        content_html = ""
        if hasattr(self.content, 'render'):
            content_html = self.content.render()
        else:
            content_html = str(self.content)
        
        # Add CSS keyframes
        css = f"""
        <style>
        @keyframes slideUp {{
            from {{ 
                transform: translateY({self.distance}); 
                opacity: 0; 
            }}
            to {{ 
                transform: translateY(0); 
                opacity: 1; 
            }}
        }}
        </style>
        """
        
        return f"{css}<{self.tag}{attrs}>{content_html}</{self.tag}>"

class AnimateOnScroll(Element):
    """Animate element when it comes into view"""
    
    def __init__(self, content, animation_type: str = "fadeIn", 
                 duration: str = "0.6s", threshold: float = 0.1, 
                 css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.content = content
        self.animation_type = animation_type
        self.duration = duration
        self.threshold = threshold
        
        # Add observer class
        observer_class = "animate-on-scroll"
        if self.css_class:
            self.css_class += f" {observer_class}"
        else:
            self.css_class = observer_class
    
    def render(self):
        attrs = self.render_attributes()
        content_html = ""
        if hasattr(self.content, 'render'):
            content_html = self.content.render()
        else:
            content_html = str(self.content)
        
        # Animation CSS and JavaScript
        animation_css = f"""
        <style>
        .animate-on-scroll {{
            opacity: 0;
            transform: translateY(30px);
            transition: all {self.duration} ease-out;
        }}
        
        .animate-on-scroll.animated {{
            opacity: 1;
            transform: translateY(0);
        }}
        
        .animate-on-scroll.fade-in.animated {{
            animation: fadeInScroll {self.duration} ease-out forwards;
        }}
        
        .animate-on-scroll.slide-up.animated {{
            animation: slideUpScroll {self.duration} ease-out forwards;
        }}
        
        @keyframes fadeInScroll {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        
        @keyframes slideUpScroll {{
            from {{ 
                opacity: 0; 
                transform: translateY(30px); 
            }}
            to {{ 
                opacity: 1; 
                transform: translateY(0); 
            }}
        }}
        </style>
        """
        
        animation_js = f"""
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const observerOptions = {{
                threshold: {self.threshold},
                rootMargin: '0px 0px -50px 0px'
            }};
            
            const observer = new IntersectionObserver(function(entries) {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('animated');
                        if ('{self.animation_type}' === 'fadeIn') {{
                            entry.target.classList.add('fade-in');
                        }} else if ('{self.animation_type}' === 'slideUp') {{
                            entry.target.classList.add('slide-up');
                        }}
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, observerOptions);
            
            document.querySelectorAll('.animate-on-scroll').forEach(el => {{
                observer.observe(el);
            }});
        }});
        </script>
        """
        
        return f"{animation_css}{animation_js}<{self.tag}{attrs}>{content_html}</{self.tag}>"

class Pulse(Element):
    """Pulse animation for highlighting elements"""
    
    def __init__(self, content, duration: str = "1s", css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.content = content
        self.duration = duration
        
        # Add pulse class
        pulse_class = "pulse-animation"
        if self.css_class:
            self.css_class += f" {pulse_class}"
        else:
            self.css_class = pulse_class
    
    def render(self):
        attrs = self.render_attributes()
        content_html = ""
        if hasattr(self.content, 'render'):
            content_html = self.content.render()
        else:
            content_html = str(self.content)
        
        css = f"""
        <style>
        .pulse-animation {{
            animation: pulse {self.duration} infinite;
        }}
        
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        </style>
        """
        
        return f"{css}<{self.tag}{attrs}>{content_html}</{self.tag}>"