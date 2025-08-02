"""
Visual debug tools for HTML generator development
"""
from typing import Optional, Dict, Any, List
from .elements import Element

class DebugMode:
    """Debug mode manager for visual debugging"""
    
    def __init__(self):
        self.enabled = False
        self.show_boundaries = True
        self.show_component_names = True
        self.show_ids = True
        self.show_tooltips = True
        self.outline_color = "#ff0000"
        self.text_color = "#ffffff"
        self.background_color = "rgba(255, 0, 0, 0.1)"
    
    def enable(self, show_boundaries: bool = True, show_component_names: bool = True,
               show_ids: bool = True, show_tooltips: bool = True):
        """Enable debug mode with specified options"""
        self.enabled = True
        self.show_boundaries = show_boundaries
        self.show_component_names = show_component_names
        self.show_ids = show_ids
        self.show_tooltips = show_tooltips
    
    def disable(self):
        """Disable debug mode"""
        self.enabled = False
    
    def generate_debug_css(self) -> str:
        """Generate CSS for debug visualization"""
        if not self.enabled:
            return ""
        
        css = f"""
        <style>
        /* Debug Mode Styles */
        .debug-enabled * {{
            outline: 1px dashed {self.outline_color} !important;
            position: relative !important;
        }}
        
        .debug-info {{
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            background: {self.outline_color} !important;
            color: {self.text_color} !important;
            font-size: 10px !important;
            padding: 2px 4px !important;
            z-index: 9999 !important;
            font-family: monospace !important;
            line-height: 1 !important;
            border-radius: 2px !important;
            white-space: nowrap !important;
            pointer-events: none !important;
        }}
        
        .debug-tooltip {{
            position: absolute !important;
            background: rgba(0, 0, 0, 0.9) !important;
            color: white !important;
            padding: 8px !important;
            border-radius: 4px !important;
            font-size: 12px !important;
            font-family: monospace !important;
            z-index: 10000 !important;
            max-width: 300px !important;
            white-space: pre-line !important;
            opacity: 0 !important;
            transition: opacity 0.2s !important;
            pointer-events: none !important;
        }}
        
        .debug-enabled *:hover .debug-tooltip {{
            opacity: 1 !important;
        }}
        
        .debug-component-boundary {{
            background: {self.background_color} !important;
        }}
        
        .debug-highlight {{
            animation: debugPulse 2s infinite !important;
        }}
        
        @keyframes debugPulse {{
            0%, 100% {{ outline-color: {self.outline_color}; }}
            50% {{ outline-color: #00ff00; }}
        }}
        </style>
        """
        
        return css
    
    def generate_debug_js(self) -> str:
        """Generate JavaScript for debug functionality"""
        if not self.enabled:
            return ""
        
        js = """
        <script>
        // Debug Mode JavaScript
        document.addEventListener('DOMContentLoaded', function() {
            enableDebugMode();
            
            // Add debug panel
            createDebugPanel();
            
            // Keyboard shortcuts
            document.addEventListener('keydown', function(e) {
                if (e.ctrlKey && e.shiftKey && e.key === 'D') {
                    toggleDebugMode();
                }
            });
        });
        
        function enableDebugMode() {
            document.body.classList.add('debug-enabled');
            addDebugInfo();
        }
        
        function disableDebugMode() {
            document.body.classList.remove('debug-enabled');
            removeDebugInfo();
        }
        
        function toggleDebugMode() {
            if (document.body.classList.contains('debug-enabled')) {
                disableDebugMode();
            } else {
                enableDebugMode();
            }
        }
        
        function addDebugInfo() {
            const elements = document.querySelectorAll('*:not(.debug-info):not(.debug-tooltip):not(.debug-panel)');
            
            elements.forEach((el, index) => {
                if (el.tagName && !el.classList.contains('debug-info')) {
                    const debugInfo = document.createElement('div');
                    debugInfo.className = 'debug-info';
                    
                    let infoText = el.tagName.toLowerCase();
                    if (el.id) infoText += '#' + el.id;
                    if (el.className && typeof el.className === 'string') {
                        const classes = el.className.split(' ').filter(c => !c.startsWith('debug-'));
                        if (classes.length > 0) {
                            infoText += '.' + classes.slice(0, 2).join('.');
                            if (classes.length > 2) infoText += '...';
                        }
                    }
                    
                    debugInfo.textContent = infoText;
                    
                    // Add tooltip with detailed info
                    const tooltip = document.createElement('div');
                    tooltip.className = 'debug-tooltip';
                    tooltip.innerHTML = getElementDebugInfo(el);
                    
                    el.style.position = 'relative';
                    el.appendChild(debugInfo);
                    el.appendChild(tooltip);
                }
            });
        }
        
        function removeDebugInfo() {
            document.querySelectorAll('.debug-info, .debug-tooltip').forEach(el => el.remove());
        }
        
        function getElementDebugInfo(element) {
            const info = [];
            info.push(`Tag: ${element.tagName.toLowerCase()}`);
            if (element.id) info.push(`ID: ${element.id}`);
            if (element.className && typeof element.className === 'string') {
                const classes = element.className.split(' ').filter(c => c && !c.startsWith('debug-'));
                if (classes.length > 0) info.push(`Classes: ${classes.join(', ')}`);
            }
            
            const computedStyle = window.getComputedStyle(element);
            info.push(`Display: ${computedStyle.display}`);
            info.push(`Position: ${computedStyle.position}`);
            
            const rect = element.getBoundingClientRect();
            info.push(`Size: ${Math.round(rect.width)}x${Math.round(rect.height)}px`);
            info.push(`Pos: ${Math.round(rect.left)}, ${Math.round(rect.top)}`);
            
            return info.join('\\n');
        }
        
        function createDebugPanel() {
            const panel = document.createElement('div');
            panel.className = 'debug-panel';
            panel.style.cssText = `
                position: fixed;
                top: 10px;
                left: 10px;
                background: rgba(0, 0, 0, 0.9);
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-family: monospace;
                font-size: 12px;
                z-index: 10001;
                max-width: 250px;
            `;
            
            panel.innerHTML = `
                <div><strong>Debug Mode Active</strong></div>
                <div>Ctrl+Shift+D: Toggle</div>
                <div>Hover elements for info</div>
                <button onclick="highlightAllComponents()" style="margin-top: 5px; font-size: 10px;">Highlight All</button>
            `;
            
            document.body.appendChild(panel);
        }
        
        function highlightAllComponents() {
            document.querySelectorAll('*').forEach(el => {
                if (!el.classList.contains('debug-info') && !el.classList.contains('debug-tooltip') && !el.classList.contains('debug-panel')) {
                    el.classList.add('debug-highlight');
                    setTimeout(() => el.classList.remove('debug-highlight'), 3000);
                }
            });
        }
        </script>
        """
        
        return js

class DebugWrapper(Element):
    """Wrapper component that adds debug information to any element"""
    
    def __init__(self, content, component_name: str = "Unknown", 
                 debug_info: Optional[Dict[str, Any]] = None, css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.content = content
        self.component_name = component_name
        self.debug_info = debug_info or {}
        
        # Add debug class
        debug_class = "debug-component"
        if self.css_class:
            self.css_class += f" {debug_class}"
        else:
            self.css_class = debug_class
    
    def render(self):
        attrs = self.render_attributes()
        content_html = ""
        if hasattr(self.content, 'render'):
            content_html = self.content.render()
        else:
            content_html = str(self.content)
        
        # Add debug attributes
        debug_attrs = f' data-component="{self.component_name}"'
        for key, value in self.debug_info.items():
            debug_attrs += f' data-debug-{key}="{value}"'
        
        return f"<{self.tag}{attrs}{debug_attrs}>{content_html}</{self.tag}>"

# Global debug mode instance
debug_mode = DebugMode()

def enable_debug_view(show_boundaries: bool = True, show_component_names: bool = True,
                     show_ids: bool = True, show_tooltips: bool = True):
    """Enable visual debug mode"""
    debug_mode.enable(show_boundaries, show_component_names, show_ids, show_tooltips)

def disable_debug_view():
    """Disable visual debug mode"""
    debug_mode.disable()

def get_debug_css() -> str:
    """Get debug mode CSS"""
    return debug_mode.generate_debug_css()

def get_debug_js() -> str:
    """Get debug mode JavaScript"""
    return debug_mode.generate_debug_js()