from .css import CSSBuilder
from typing import List, Dict, Any, Optional
import tempfile
import webbrowser
import os

class Page:
    def __init__(self, title: str, header_text: str, logo_url: Optional[str] = None, 
                 nav_links: Optional[List[Dict[str, Any]]] = None, header_class: Optional[str] = None,
                 css_framework: str = "bootstrap", custom_css: Optional[str] = None,
                 use_modern_navbar: bool = True):
        self.title = title
        self.header_text = header_text
        self.logo_url = logo_url
        self.nav_links = nav_links if nav_links is not None else []
        self.header_class = header_class
        self.body_content = []
        self.css_framework = css_framework
        self.custom_css = custom_css
        self.meta_tags = {}
        self.scripts = []
        self.css_links = []
        self.body_classes = []
        self.container_class = "container"
        self.use_modern_navbar = use_modern_navbar
        self.navbar_config = {
            'brand': {'name': 'NexusLabs', 'icon': '🌟'},
            'style': 'modern',
            'dropdown_support': True,
            'mobile_responsive': True
        }
        
        # Template manager
        self.template_manager = None
        
        # Set default CSS framework
        if css_framework == "bootstrap":
            self.add_css_link("https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css")
            self.add_script("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js")

    def add_meta_tag(self, name: str, content: str):
        """Add a meta tag to the page"""
        self.meta_tags[name] = content
        return self

    def add_css_link(self, href: str):
        """Add a CSS link to the page"""
        self.css_links.append(href)
        return self

    def add_script(self, src: str):
        """Add a JavaScript script to the page"""
        self.scripts.append(src)
        return self

    def add_body_class(self, class_name: str):
        """Add a class to the body element"""
        self.body_classes.append(class_name)
        return self

    def set_container_class(self, class_name: str):
        """Set the container class for the main content"""
        self.container_class = class_name
        return self

    def add_navbar(self, nav_links: List[Dict[str, Any]]):
        """Add navigation links to the page"""
        self.nav_links.extend(nav_links)
        return self
    
    def configure_navbar(self, brand_name: Optional[str] = None, brand_icon: Optional[str] = None, 
                        style: str = 'modern', dropdown_support: bool = True,
                        mobile_responsive: bool = True):
        """Configure the modern navigation bar"""
        self.navbar_config.update({
            'brand': {'name': brand_name if brand_name is not None else self.navbar_config['brand']['name'],
                     'icon': brand_icon if brand_icon is not None else self.navbar_config['brand']['icon']},
            'style': style,
            'dropdown_support': dropdown_support,
            'mobile_responsive': mobile_responsive
        })
        return self

    def set_theme(self, theme: str):
        """Set a predefined theme for the page"""
        # Clear existing CSS links that are theme-related
        self.css_links = [link for link in self.css_links if 'bootstrap' not in link.lower()]
        
        if theme == "bootstrap":
            self.add_css_link("https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css")
        elif theme == "bootstrap-light":
            self.add_css_link("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css")
        elif theme == "tailwind":
            self.add_css_link("https://cdn.tailwindcss.com")
        elif theme == "bulma":
            self.add_css_link("https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css")
        elif theme == "material":
            self.add_css_link("https://fonts.googleapis.com/icon?family=Material+Icons")
            self.add_css_link("https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css")
            self.add_script("https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js")
        
        return self

    def use_template_manager(self, template_manager):
        """Set the template manager for this page"""
        self.template_manager = template_manager
        return self

    def use_template(self, template_name: str, slot_map: Optional[Dict[str, str]] = None):
        """Use a template with slot content"""
        if self.template_manager:
            template_content = self.template_manager.render_template(template_name, slot_map)
            self.add_content(template_content)
        return self

    def add_content(self, content):
        """Add content to the body of the page"""
        if hasattr(content, 'render'):
            self.body_content.append(content.render())
        else:
            self.body_content.append(str(content))
        return self

    def add_element(self, element):
        """Add an HTML element to the page"""
        return self.add_content(element)

    def render_meta_tags(self):
        """Render meta tags"""
        meta_html = ""
        for name, content in self.meta_tags.items():
            meta_html += f'    <meta name="{name}" content="{content}">\n'
        return meta_html

    def render_css_links(self):
        """Render CSS links"""
        css_html = ""
        for href in self.css_links:
            css_html += f'    <link rel="stylesheet" href="{href}">\n'
        return css_html

    def render_scripts(self):
        """Render JavaScript scripts"""
        script_html = ""
        for src in self.scripts:
            script_html += f'    <script src="{src}"></script>\n'
        return script_html

    def render_header(self):
        """Render the header section of the page"""
        logo_html = f'<img src="{self.logo_url}" alt="Logo" class="logo me-3" style="height: 40px;">' if self.logo_url else ""
        header_class_attr = f' class="{self.header_class}"' if self.header_class else ' class="bg-dark text-light py-3"'
        
        header_html = f"""
        <header{header_class_attr}>
            <div class="container">
                <div class="d-flex align-items-center justify-content-between">
                    <div class="d-flex align-items-center">
                        {logo_html}
                        <h1 class="h3 mb-0">{self.header_text}</h1>
                    </div>
                    {self.render_navbar()}
                </div>
            </div>
        </header>
        """
        return header_html

    def render_navbar(self):
        """Render the modern navigation bar"""
        if not self.nav_links and not self.use_modern_navbar:
            return ""
        
        if self.use_modern_navbar:
            return self.render_modern_navbar()
        else:
            return self.render_basic_navbar()
    
    def render_basic_navbar(self):
        """Render the basic navigation bar"""
        nav_items = ""
        for link in self.nav_links:
            if isinstance(link, dict):
                nav_items += f'<li class="nav-item"><a class="nav-link text-light" href="{link.get("url", "#")}">{link.get("text", "Link")}</a></li>'
            else:
                nav_items += f'<li class="nav-item"><a class="nav-link text-light" href="{link}">{link}</a></li>'
        
        return f"""
        <nav class="navbar-nav">
            <ul class="nav">
                {nav_items}
            </ul>
        </nav>
        """
    
    def render_modern_navbar(self):
        """Render the modern navigation bar with enhanced styling"""
        brand = self.navbar_config['brand']
        nav_items = ""
        
        for link in self.nav_links:
            if isinstance(link, dict):
                if 'dropdown' in link:
                    # Dropdown menu
                    dropdown_items = ""
                    for dropdown_item in link['dropdown']:
                        dropdown_items += f'''
                        <li class="dropdown-item">
                            <a href="{dropdown_item.get('url', '#')}" class="dropdown-link">{dropdown_item.get('text', 'Item')}</a>
                        </li>'''
                    
                    nav_items += f'''
                    <li class="nav-item">
                        <a href="{link.get('url', '#')}" class="nav-link">
                            {link.get('text', 'Link')}
                            <i>▼</i>
                        </a>
                        <ul class="dropdown-menu">
                            {dropdown_items}
                        </ul>
                    </li>'''
                else:
                    # Regular link
                    nav_items += f'''
                    <li class="nav-item">
                        <a href="{link.get('url', '#')}" class="nav-link">{link.get('text', 'Link')}</a>
                    </li>'''
            else:
                nav_items += f'''
                <li class="nav-item">
                    <a href="#" class="nav-link">{link}</a>
                </li>'''
        
        return f'''
        <nav class="navbar">
            <div class="nav-container">
                <a href="#" class="logo">
                    <span class="logo-icon">{brand['icon']}</span>
                    <span>{brand['name']}</span>
                </a>

                <button class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </button>

                <ul class="nav-links">
                    {nav_items}
                    <li class="nav-item">
                        <button class="nav-btn">Get Started</button>
                    </li>
                </ul>
            </div>
        </nav>'''

    def get_modern_navbar_css(self):
        """Get CSS for the modern navigation bar"""
        return '''
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .navbar {
            background: linear-gradient(135deg, #4a7dff 0%, #6a11cb 100%);
            padding: 1rem 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }
        
        .navbar.scrolled {
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            padding: 0.5rem 2rem;
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            color: white;
            font-size: 1.8rem;
            font-weight: 700;
            text-decoration: none;
            display: flex;
            align-items: center;
        }

        .logo-icon {
            margin-right: 10px;
            font-size: 2rem;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-item {
            position: relative;
            margin-left: 1.5rem;
        }

        .nav-link {
            color: rgba(255, 255, 255, 0.95);
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            padding: 0.5rem 1rem;
            display: flex;
            align-items: center;
            position: relative;
        }
        
        .nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 2px;
            background: white;
            transition: all 0.3s;
        }
        
        .nav-link:hover::after {
            width: 60%;
            left: 20%;
        }

        .nav-link:hover {
            color: white;
        }

        .nav-link i {
            margin-left: 5px;
            font-size: 0.9rem;
            transition: transform 0.3s;
        }

        .dropdown-menu {
            position: absolute;
            top: 100%;
            left: 0;
            background-color: white;
            border-radius: 0.75rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            list-style: none;
            width: 220px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            transform: translateY(15px);
            z-index: 999;
            border: 1px solid rgba(0, 0, 0, 0.05);
            padding: 0.5rem 0;
        }

        .dropdown-menu.show {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .dropdown-item {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #f0f0f0;
        }

        .dropdown-item:last-child {
            border-bottom: none;
        }

        .dropdown-link {
            color: #333;
            text-decoration: none;
            font-size: 0.95rem;
            transition: color 0.2s;
            display: block;
        }

        .dropdown-link:hover {
            color: #667eea;
        }

        .nav-btn {
            background-color: white;
            color: #4a7dff;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 2rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            letter-spacing: 0.5px;
        }

        .nav-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .hamburger {
            display: none;
            cursor: pointer;
            width: 30px;
            height: 21px;
            position: relative;
            background: transparent;
            border: none;
            outline: none;
        }

        .hamburger span {
            display: block;
            position: absolute;
            height: 3px;
            width: 100%;
            background: white;
            border-radius: 3px;
            opacity: 1;
            left: 0;
            transform: rotate(0deg);
            transition: all 0.3s;
        }

        .hamburger span:nth-child(1) {
            top: 0px;
        }

        .hamburger span:nth-child(2), .hamburger span:nth-child(3) {
            top: 9px;
        }

        .hamburger span:nth-child(4) {
            top: 18px;
        }

        .hamburger.open span:nth-child(1),
        .hamburger.open span:nth-child(4) {
            top: 9px;
            width: 0%;
            left: 50%;
        }

        .hamburger.open span:nth-child(2) {
            transform: rotate(45deg);
        }

        .hamburger.open span:nth-child(3) {
            transform: rotate(-45deg);
        }

        @media (max-width: 992px) {
            .hamburger {
                display: block;
            }

            .nav-links {
                position: fixed;
                top: 85px;
                left: -100%;
                width: 80%;
                height: calc(100vh - 85px);
                background-color: white;
                flex-direction: column;
                align-items: flex-start;
                padding: 2rem;
                transition: all 0.5s;
                box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
            }

            .nav-links.active {
                left: 0;
            }

            .nav-item {
                margin: 1rem 0;
                width: 100%;
            }

            .nav-link {
                color: #333;
                font-size: 1.2rem;
                padding: 0.5rem 0;
            }

            .dropdown-menu {
                position: static;
                width: 100%;
                display: none;
                border-radius: 0;
                box-shadow: none;
                opacity: 1;
                visibility: visible;
                transform: none;
                transition: none;
                margin-top: 0.5rem;
            }

            .dropdown-menu.show {
                display: block;
            }

            .dropdown-item {
                padding: 0.5rem 0;
            }

            .dropdown-link {
                font-size: 1rem;
                padding-left: 1rem;
            }

            .nav-btn {
                width: 100%;
                text-align: left;
                padding: 0.75rem 0;
                background-color: transparent;
                color: #667eea;
                box-shadow: none;
                font-size: 1.2rem;
            }

            .nav-btn:hover {
                transform: none;
                box-shadow: none;
            }
        }
        '''

    def get_modern_navbar_js(self):
        """Get JavaScript for the modern navigation bar"""
        return '''
        // Mobile menu toggle and scroll effect
        const navbar = document.querySelector('.navbar');
        const hamburger = document.querySelector('.hamburger');
        const navLinks = document.querySelector('.nav-links');
        const navItems = document.querySelectorAll('.nav-item');
        
        // Add scroll effect
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
        
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('open');
            navLinks.classList.toggle('active');
        });
        
        // Close mobile menu when clicking a link
        navItems.forEach(item => {
            const link = item.querySelector('.nav-link');
            if (link) {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 992) {
                        hamburger.classList.remove('open');
                        navLinks.classList.remove('active');
                    }
                });
            }
            
            // Toggle dropdowns on mobile
            const dropdownToggle = item.querySelector('.nav-link i');
            if (dropdownToggle) {
                dropdownToggle.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const dropdown = item.querySelector('.dropdown-menu');
                    dropdown.classList.toggle('show');
                });
            }
        });
        
        // Desktop dropdown functionality
        navItems.forEach(item => {
            if (window.innerWidth > 992) {
                const link = item.querySelector('.nav-link');
                const dropdown = item.querySelector('.dropdown-menu');
                
                if (dropdown) {
                    item.addEventListener('mouseenter', () => {
                        dropdown.classList.add('show');
                    });
                    
                    item.addEventListener('mouseleave', () => {
                        dropdown.classList.remove('show');
                    });
                }
            }
        });
        
        // Resize event listener
        window.addEventListener('resize', () => {
            if (window.innerWidth > 992) {
                hamburger.classList.remove('open');
                navLinks.classList.remove('active');
                
                // Hide all dropdowns on desktop
                document.querySelectorAll('.dropdown-menu').forEach(dropdown => {
                    dropdown.classList.remove('show');
                });
            }
        });
        '''

    def generate_html(self):
        """Generate the complete HTML for the page"""
        body_class_attr = f' class="{" ".join(self.body_classes)}"' if self.body_classes else ""
        body = "\n".join(self.body_content)
        
        # Combine custom CSS with modern navbar CSS if needed
        all_css = ""
        if self.use_modern_navbar:
            all_css += self.get_modern_navbar_css()
        if self.custom_css:
            all_css += "\n" + self.custom_css
        
        custom_css_tag = f"<style>\n{all_css}\n    </style>" if all_css else ""
        
        # Add modern navbar JavaScript if needed
        navbar_js = ""
        if self.use_modern_navbar:
            navbar_js = f"<script>\n{self.get_modern_navbar_js()}\n    </script>"
        
        html = f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
{self.render_meta_tags()}{self.render_css_links()}    {custom_css_tag}
</head>
<body{body_class_attr}>
    {self.render_header()}
    <main class="{self.container_class} mt-4">
        {body}
    </main>
{self.render_scripts()}    {navbar_js}
</body>
</html>"""
        return html

    def save_to_file(self, filename: str):
        """Save the generated HTML to a file"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.generate_html())
        return self
    
    def run(self, port: int = 8000, auto_open: bool = True):
        """Run the webpage directly in the browser (development mode)"""
        html_content = self.generate_html()
        
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.html', 
                                              delete=False, encoding='utf-8')
        temp_file.write(html_content)
        temp_file.close()
        
        if auto_open:
            # Open in browser
            webbrowser.open(f'file://{temp_file.name}')
            print(f"Website opened in browser: {temp_file.name}")
        else:
            print(f"HTML file created: {temp_file.name}")
        
        return temp_file.name

class Heading:
    def __init__(self, text: str, level: int = 1, css_class: Optional[str] = None, 
                 id_attr: Optional[str] = None):
        self.text = text
        self.level = level
        self.css_class = css_class
        self.id_attr = id_attr

    def render(self):
        """Render the heading as HTML"""
        if not (1 <= self.level <= 6):
            raise ValueError("Heading level must be between 1 and 6.")
        
        class_attr = f' class="{self.css_class}"' if self.css_class else ""
        id_attr = f' id="{self.id_attr}"' if self.id_attr else ""
        
        return f"<h{self.level}{class_attr}{id_attr}>{self.text}</h{self.level}>"

    def set_class(self, css_class: str):
        """Set CSS class for the heading"""
        self.css_class = css_class
        return self

    def set_id(self, id_attr: str):
        """Set ID attribute for the heading"""
        self.id_attr = id_attr
        return self
