"""
Dark mode toggle and theme management for HTML generator
"""
from typing import Optional, Dict, Any
from .elements import Element

class DarkModeToggle(Element):
    """Dark mode toggle component with system preference detection"""
    
    def __init__(self, position: str = "top-right", icon_light: str = "☀️", 
                 icon_dark: str = "🌙", css_class: Optional[str] = None):
        super().__init__("div", css_class=css_class)
        self.position = position
        self.icon_light = icon_light
        self.icon_dark = icon_dark
        
        # Add toggle class
        toggle_class = f"dark-mode-toggle {position}"
        if self.css_class:
            self.css_class += f" {toggle_class}"
        else:
            self.css_class = toggle_class
    
    def render(self):
        attrs = self.render_attributes()
        
        # Position styles
        position_styles = {
            "top-right": "position: fixed; top: 20px; right: 20px; z-index: 1000;",
            "top-left": "position: fixed; top: 20px; left: 20px; z-index: 1000;",
            "inline": "display: inline-block;"
        }
        
        position_style = position_styles.get(self.position, position_styles["top-right"])
        
        toggle_html = f"""
        <button id="darkModeToggle" class="btn btn-outline-secondary" 
                style="{position_style}" 
                title="Toggle dark/light mode">
            <span id="darkModeIcon">{self.icon_light}</span>
        </button>
        """
        
        # CSS for dark mode
        dark_mode_css = """
        <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #212529;
            --card-bg: #ffffff;
            --border-color: #dee2e6;
            --navbar-bg: #f8f9fa;
            --navbar-text: #212529;
        }
        
        [data-theme="dark"] {
            --bg-color: #212529;
            --text-color: #ffffff;
            --card-bg: #343a40;
            --border-color: #495057;
            --navbar-bg: #343a40;
            --navbar-text: #ffffff;
        }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        
        .card {
            background-color: var(--card-bg);
            border-color: var(--border-color);
        }
        
        .navbar {
            background-color: var(--navbar-bg) !important;
        }
        
        .navbar .navbar-brand,
        .navbar .nav-link {
            color: var(--navbar-text) !important;
        }
        
        .dark-mode-toggle {
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            border: 2px solid var(--border-color);
            background-color: var(--card-bg);
            color: var(--text-color);
            transition: all 0.3s ease;
        }
        
        .dark-mode-toggle:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        [data-theme="dark"] .form-control {
            background-color: var(--card-bg);
            border-color: var(--border-color);
            color: var(--text-color);
        }
        
        [data-theme="dark"] .form-control:focus {
            background-color: var(--card-bg);
            border-color: #80bdff;
            color: var(--text-color);
        }
        </style>
        """
        
        # JavaScript for dark mode functionality
        dark_mode_js = f"""
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const toggle = document.getElementById('darkModeToggle');
            const icon = document.getElementById('darkModeIcon');
            const body = document.body;
            
            // Check for system preference and stored preference
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const storedTheme = localStorage.getItem('theme');
            
            // Initialize theme
            let currentTheme = storedTheme || (systemPrefersDark ? 'dark' : 'light');
            setTheme(currentTheme);
            
            // Toggle functionality
            toggle.addEventListener('click', function() {{
                currentTheme = currentTheme === 'light' ? 'dark' : 'light';
                setTheme(currentTheme);
                localStorage.setItem('theme', currentTheme);
            }});
            
            // Listen for system theme changes
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {{
                if (!localStorage.getItem('theme')) {{
                    setTheme(e.matches ? 'dark' : 'light');
                }}
            }});
            
            function setTheme(theme) {{
                if (theme === 'dark') {{
                    body.setAttribute('data-theme', 'dark');
                    icon.textContent = '{self.icon_dark}';
                }} else {{
                    body.removeAttribute('data-theme');
                    icon.textContent = '{self.icon_light}';
                }}
            }}
        }});
        </script>
        """
        
        # Add meta tag for color scheme
        meta_tag = '<meta name="color-scheme" content="light dark">'
        
        return f"{meta_tag}{dark_mode_css}{dark_mode_js}<{self.tag}{attrs}>{toggle_html}</{self.tag}>"

class ThemeProvider:
    """Utility class for managing theme CSS variables"""
    
    def __init__(self):
        self.themes = {
            'light': {
                '--bg-color': '#ffffff',
                '--text-color': '#212529',
                '--card-bg': '#ffffff',
                '--border-color': '#dee2e6',
                '--primary-color': '#007bff',
                '--secondary-color': '#6c757d'
            },
            'dark': {
                '--bg-color': '#212529',
                '--text-color': '#ffffff',
                '--card-bg': '#343a40',
                '--border-color': '#495057',
                '--primary-color': '#0d6efd',
                '--secondary-color': '#6c757d'
            }
        }
    
    def add_custom_theme(self, name: str, variables: Dict[str, str]):
        """Add a custom theme with CSS variables"""
        self.themes[name] = variables
    
    def generate_theme_css(self) -> str:
        """Generate CSS for all registered themes"""
        css = ":root {\n"
        for var, value in self.themes['light'].items():
            css += f"    {var}: {value};\n"
        css += "}\n\n"
        
        for theme_name, variables in self.themes.items():
            if theme_name != 'light':
                css += f'[data-theme="{theme_name}"] {{\n'
                for var, value in variables.items():
                    css += f"    {var}: {value};\n"
                css += "}\n\n"
        
        return f"<style>\n{css}</style>"

def create_auto_dark_mode() -> str:
    """Create automatic dark mode CSS that respects system preferences"""
    return """
    <style>
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #212529;
            --text-color: #ffffff;
            --card-bg: #343a40;
            --border-color: #495057;
        }
        
        body {
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        
        .card, .form-control {
            background-color: var(--card-bg);
            border-color: var(--border-color);
            color: var(--text-color);
        }
    }
    </style>
    <meta name="color-scheme" content="light dark">
    """