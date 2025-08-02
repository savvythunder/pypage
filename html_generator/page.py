from .css import CSSBuilder
from typing import List, Dict, Any, Optional

class Page:
    def __init__(self, title: str, header_text: str, logo_url: Optional[str] = None, 
                 nav_links: Optional[List[str]] = None, header_class: Optional[str] = None,
                 css_framework: str = "bootstrap", custom_css: Optional[str] = None):
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

    def add_navbar(self, nav_links: List[str]):
        """Add navigation links to the page"""
        self.nav_links.extend(nav_links)
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
        """Render the navigation bar"""
        if not self.nav_links:
            return ""
        
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

    def generate_html(self):
        """Generate the complete HTML for the page"""
        body_class_attr = f' class="{" ".join(self.body_classes)}"' if self.body_classes else ""
        body = "\n".join(self.body_content)
        
        custom_css_tag = f"<style>\n{self.custom_css}\n    </style>" if self.custom_css else ""
        
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
{self.render_scripts()}</body>
</html>"""
        return html

    def save_to_file(self, filename: str):
        """Save the generated HTML to a file"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.generate_html())
        return self

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
