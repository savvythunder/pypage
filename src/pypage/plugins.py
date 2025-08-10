"""
Plugin system for extending HTML generator components
"""
from typing import Dict, Any, Callable, Optional, Type, List
from .elements import Element
from .components import ComponentBase

class PluginRegistry:
    """Registry for managing custom components and plugins"""
    
    def __init__(self):
        self.components: Dict[str, Type[Element]] = {}
        self.templates: Dict[str, Callable] = {}
        self.hooks: Dict[str, List[Callable]] = {}
        self.filters: Dict[str, Callable] = {}
    
    def register_component(self, name: str, component_class: Type[Element]):
        """Register a custom component"""
        self.components[name] = component_class
        return component_class
    
    def register_template(self, name: str, template_func: Callable):
        """Register a custom template function"""
        self.templates[name] = template_func
        return template_func
    
    def register_hook(self, event: str, callback: Callable):
        """Register a hook for specific events"""
        if event not in self.hooks:
            self.hooks[event] = []
        self.hooks[event].append(callback)
        return callback
    
    def register_filter(self, name: str, filter_func: Callable):
        """Register a content filter"""
        self.filters[name] = filter_func
        return filter_func
    
    def get_component(self, name: str) -> Optional[Type[Element]]:
        """Get a registered component by name"""
        return self.components.get(name)
    
    def get_template(self, name: str) -> Optional[Callable]:
        """Get a registered template by name"""
        return self.templates.get(name)
    
    def execute_hooks(self, event: str, *args, **kwargs):
        """Execute all hooks for a specific event"""
        results = []
        for hook in self.hooks.get(event, []):
            try:
                result = hook(*args, **kwargs)
                results.append(result)
            except Exception as e:
                print(f"Hook execution error for {event}: {e}")
        return results
    
    def apply_filter(self, filter_name: str, content: str, *args, **kwargs) -> str:
        """Apply a registered filter to content"""
        filter_func = self.filters.get(filter_name)
        if filter_func:
            try:
                return filter_func(content, *args, **kwargs)
            except Exception as e:
                print(f"Filter error for {filter_name}: {e}")
        return content
    
    def list_components(self) -> List[str]:
        """List all registered component names"""
        return list(self.components.keys())
    
    def list_templates(self) -> List[str]:
        """List all registered template names"""
        return list(self.templates.keys())

# Global plugin registry
plugin_registry = PluginRegistry()

def register_component(name: Optional[str] = None):
    """Decorator to register a component"""
    def decorator(cls: Type[Element]):
        component_name = name or cls.__name__
        plugin_registry.register_component(component_name, cls)
        return cls
    return decorator

def register_template(name: Optional[str] = None):
    """Decorator to register a template function"""
    def decorator(func: Callable):
        template_name = name or func.__name__
        plugin_registry.register_template(template_name, func)
        return func
    return decorator

def register_hook(event: str):
    """Decorator to register a hook function"""
    def decorator(func: Callable):
        plugin_registry.register_hook(event, func)
        return func
    return decorator

def register_filter(name: Optional[str] = None):
    """Decorator to register a filter function"""
    def decorator(func: Callable):
        filter_name = name or func.__name__
        plugin_registry.register_filter(filter_name, func)
        return func
    return decorator

# Example plugin components
@register_component("Timeline")
class Timeline(ComponentBase):
    """Timeline component for displaying chronological events"""
    
    def __init__(self, events: List[Dict[str, str]], orientation: str = "vertical", 
                 css_class: Optional[str] = None):
        timeline_class = f"timeline timeline-{orientation}"
        if css_class:
            timeline_class += f" {css_class}"
        
        super().__init__(css_class=timeline_class)
        self.events = events
        self.orientation = orientation
        
        # Build timeline HTML
        timeline_html = ""
        for i, event in enumerate(events):
            item_class = "timeline-item"
            if i % 2 == 0 and orientation == "vertical":
                item_class += " timeline-item-left"
            else:
                item_class += " timeline-item-right"
            
            timeline_html += f"""
            <div class="{item_class}">
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <h5 class="timeline-title">{event.get('title', '')}</h5>
                    <p class="timeline-date">{event.get('date', '')}</p>
                    <p class="timeline-description">{event.get('description', '')}</p>
                </div>
            </div>
            """
        
        self.content = timeline_html
    
    def render(self):
        attrs = self.render_attributes()
        
        # Timeline CSS
        timeline_css = """
        <style>
        .timeline {
            position: relative;
            padding: 20px 0;
        }
        
        .timeline-vertical::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            width: 2px;
            height: 100%;
            background: #007bff;
            transform: translateX(-50%);
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 30px;
            width: 45%;
        }
        
        .timeline-item-left {
            left: 0;
            text-align: right;
        }
        
        .timeline-item-right {
            left: 55%;
            text-align: left;
        }
        
        .timeline-marker {
            position: absolute;
            top: 0;
            width: 12px;
            height: 12px;
            background: #007bff;
            border: 3px solid #fff;
            border-radius: 50%;
            box-shadow: 0 0 0 3px #007bff;
        }
        
        .timeline-item-left .timeline-marker {
            right: -6px;
        }
        
        .timeline-item-right .timeline-marker {
            left: -6px;
        }
        
        .timeline-content {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .timeline-title {
            margin: 0 0 5px 0;
            color: #007bff;
        }
        
        .timeline-date {
            font-size: 0.9em;
            color: #6c757d;
            margin: 0 0 10px 0;
        }
        
        .timeline-description {
            margin: 0;
        }
        
        .timeline-horizontal {
            display: flex;
            overflow-x: auto;
            padding: 20px 0;
        }
        
        .timeline-horizontal .timeline-item {
            flex: 0 0 300px;
            margin-right: 20px;
            width: auto;
        }
        </style>
        """
        
        return f"{timeline_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

@register_component("StatCard")
class StatCard(ComponentBase):
    """Statistics card component for dashboards"""
    
    def __init__(self, label: str, value: str, icon: str = "", 
                 delta: str = "", delta_type: str = "neutral", 
                 css_class: Optional[str] = None):
        card_class = "stat-card card"
        if css_class:
            card_class += f" {css_class}"
        
        super().__init__(css_class=card_class)
        
        # Delta styling
        delta_class = f"stat-delta stat-delta-{delta_type}"
        delta_symbol = ""
        if delta_type == "positive":
            delta_symbol = "↗"
        elif delta_type == "negative":
            delta_symbol = "↘"
        
        card_html = f"""
        <div class="card-body text-center">
            {f'<i class="{icon} stat-icon"></i>' if icon else ''}
            <h3 class="stat-value">{value}</h3>
            <p class="stat-label">{label}</p>
            {f'<small class="{delta_class}">{delta_symbol} {delta}</small>' if delta else ''}
        </div>
        """
        
        self.content = card_html
    
    def render(self):
        attrs = self.render_attributes()
        
        stat_css = """
        <style>
        .stat-card {
            min-height: 120px;
            transition: transform 0.2s;
        }
        
        .stat-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .stat-icon {
            font-size: 2rem;
            color: #007bff;
            margin-bottom: 10px;
        }
        
        .stat-value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0 5px 0;
            color: #212529;
        }
        
        .stat-label {
            color: #6c757d;
            margin: 0 0 10px 0;
            font-weight: 500;
        }
        
        .stat-delta-positive {
            color: #28a745;
        }
        
        .stat-delta-negative {
            color: #dc3545;
        }
        
        .stat-delta-neutral {
            color: #6c757d;
        }
        </style>
        """
        
        return f"{stat_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

@register_component("CodeBlock")
class CodeBlock(ComponentBase):
    """Code block component with syntax highlighting"""
    
    def __init__(self, code: str, language: str = "python", 
                 show_line_numbers: bool = True, theme: str = "default",
                 css_class: Optional[str] = None):
        code_class = f"code-block language-{language}"
        if css_class:
            code_class += f" {css_class}"
        
        super().__init__(css_class=code_class)
        self.code = code
        self.language = language
        self.show_line_numbers = show_line_numbers
        self.theme = theme
        
        # Generate line numbers if needed
        lines = code.split('\n')
        if show_line_numbers:
            line_numbers = '\n'.join(str(i+1) for i in range(len(lines)))
            code_html = f"""
            <div class="code-container">
                <div class="line-numbers">{line_numbers}</div>
                <pre class="code-content"><code class="language-{language}">{code}</code></pre>
            </div>
            """
        else:
            code_html = f'<pre><code class="language-{language}">{code}</code></pre>'
        
        self.content = code_html
    
    def render(self):
        attrs = self.render_attributes()
        
        code_css = """
        <style>
        .code-block {
            margin: 1rem 0;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .code-container {
            display: flex;
            background: #f8f9fa;
            border: 1px solid #e9ecef;
        }
        
        .line-numbers {
            background: #e9ecef;
            color: #6c757d;
            padding: 1rem 0.5rem;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            line-height: 1.5;
            text-align: right;
            min-width: 3rem;
            user-select: none;
        }
        
        .code-content {
            flex: 1;
            margin: 0;
            padding: 1rem;
            background: #fff;
            color: #212529;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            line-height: 1.5;
            overflow-x: auto;
        }
        
        .code-content code {
            background: none;
            padding: 0;
            color: inherit;
        }
        
        /* Simple syntax highlighting */
        .language-python .keyword { color: #007bff; font-weight: bold; }
        .language-python .string { color: #28a745; }
        .language-python .comment { color: #6c757d; font-style: italic; }
        .language-python .number { color: #fd7e14; }
        </style>
        """
        
        return f"{code_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

# Example filters
@register_filter("markdown_to_html")
def markdown_to_html(content: str) -> str:
    """Simple markdown to HTML filter"""
    # Basic markdown parsing
    content = content.replace('**', '<strong>').replace('**', '</strong>')
    content = content.replace('*', '<em>').replace('*', '</em>')
    content = content.replace('\n\n', '</p><p>')
    content = f'<p>{content}</p>'
    return content

@register_filter("truncate")
def truncate_filter(content: str, length: int = 100, suffix: str = "...") -> str:
    """Truncate text to specified length"""
    if len(content) <= length:
        return content
    return content[:length].rstrip() + suffix

# Example hooks
@register_hook("before_render")
def log_render_start(component_name: str):
    """Log when component rendering starts"""
    print(f"Rendering component: {component_name}")

@register_hook("after_render")
def log_render_end(component_name: str, html_length: int):
    """Log when component rendering completes"""
    print(f"Completed rendering {component_name}: {html_length} characters")

# Plugin loader utility
def load_plugin_from_file(filepath: str):
    """Load a plugin from a Python file"""
    import importlib.util
    import sys
    
    spec = importlib.util.spec_from_file_location("plugin", filepath)
    plugin_module = importlib.util.module_from_spec(spec)
    sys.modules["plugin"] = plugin_module
    spec.loader.exec_module(plugin_module)
    
    return plugin_module

def create_plugin_template(name: str, component_type: str = "ComponentBase") -> str:
    """Create a template for a new plugin"""
    template = f'''"""
{name} plugin for HTML generator
"""
from html_generator.plugins import register_component, ComponentBase
from html_generator.elements import Element
from typing import Optional

@register_component("{name}")
class {name}(ComponentBase):
    """Custom {name} component"""
    
    def __init__(self, css_class: Optional[str] = None):
        super().__init__(css_class=css_class)
        
        # Add your component logic here
        self.content = "<p>Custom {name} component</p>"
    
    def render(self):
        attrs = self.render_attributes()
        
        # Add custom CSS if needed
        css = """
        <style>
        .{name.lower()} {{
            /* Your custom styles */
        }}
        </style>
        """
        
        return f"{{css}}<{{self.tag}}{{attrs}}>{{self.content}}</{{self.tag}}>"
'''
    return template