"""
Advanced UI components for professional web applications
"""
from typing import Optional, List, Dict, Any, Union
from .elements import Element
from .components import ComponentBase

class Table(ComponentBase):
    """Advanced table component with sorting, filtering, and pagination"""
    
    def __init__(self, headers: List[str], rows: List[List[str]], 
                 striped: bool = True, hover: bool = True, bordered: bool = False,
                 sortable: bool = False, searchable: bool = False,
                 pagination: bool = False, css_class: Optional[str] = None):
        table_class = "table"
        if striped:
            table_class += " table-striped"
        if hover:
            table_class += " table-hover"
        if bordered:
            table_class += " table-bordered"
        if css_class:
            table_class += f" {css_class}"
        
        super().__init__(css_class="table-responsive")
        self.headers = headers
        self.rows = rows
        self.sortable = sortable
        self.searchable = searchable
        self.pagination = pagination
        
        # Build table HTML
        table_html = f'<table class="{table_class}" id="data-table">'
        
        # Headers
        table_html += '<thead class="table-dark"><tr>'
        for i, header in enumerate(headers):
            sort_attr = f' data-sort="{i}" style="cursor: pointer;"' if sortable else ''
            sort_icon = ' <i class="sort-icon">⇅</i>' if sortable else ''
            table_html += f'<th{sort_attr}>{header}{sort_icon}</th>'
        table_html += '</tr></thead>'
        
        # Body
        table_html += '<tbody>'
        for row in rows:
            table_html += '<tr>'
            for cell in row:
                table_html += f'<td>{cell}</td>'
            table_html += '</tr>'
        table_html += '</tbody></table>'
        
        # Add search and pagination if needed
        if searchable:
            search_html = '''
            <div class="mb-3">
                <input type="text" class="form-control" id="table-search" placeholder="Search table...">
            </div>
            '''
            table_html = search_html + table_html
        
        if pagination:
            pagination_html = '''
            <nav aria-label="Table pagination">
                <ul class="pagination justify-content-center" id="table-pagination">
                    <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item"><a class="page-link" href="#">Next</a></li>
                </ul>
            </nav>
            '''
            table_html += pagination_html
        
        self.content = table_html
    
    def render(self):
        attrs = self.render_attributes()
        
        # Table functionality CSS and JS
        table_css = """
        <style>
        .table th[data-sort] {
            user-select: none;
        }
        .table th[data-sort]:hover {
            background-color: rgba(0,0,0,0.1);
        }
        .sort-icon {
            opacity: 0.5;
            font-size: 0.8em;
        }
        .table th.sort-asc .sort-icon::before {
            content: '↑';
        }
        .table th.sort-desc .sort-icon::before {
            content: '↓';
        }
        </style>
        """
        
        table_js = """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Table sorting
            const sortHeaders = document.querySelectorAll('th[data-sort]');
            sortHeaders.forEach(header => {
                header.addEventListener('click', function() {
                    const column = parseInt(this.dataset.sort);
                    const table = document.getElementById('data-table');
                    const tbody = table.querySelector('tbody');
                    const rows = Array.from(tbody.querySelectorAll('tr'));
                    
                    const isAsc = this.classList.contains('sort-asc');
                    
                    // Remove all sort classes
                    sortHeaders.forEach(h => h.classList.remove('sort-asc', 'sort-desc'));
                    
                    // Add appropriate class
                    if (isAsc) {
                        this.classList.add('sort-desc');
                    } else {
                        this.classList.add('sort-asc');
                    }
                    
                    rows.sort((a, b) => {
                        const aVal = a.cells[column].textContent.trim();
                        const bVal = b.cells[column].textContent.trim();
                        
                        if (isAsc) {
                            return bVal.localeCompare(aVal, undefined, {numeric: true});
                        } else {
                            return aVal.localeCompare(bVal, undefined, {numeric: true});
                        }
                    });
                    
                    rows.forEach(row => tbody.appendChild(row));
                });
            });
            
            // Table search
            const searchInput = document.getElementById('table-search');
            if (searchInput) {
                searchInput.addEventListener('input', function() {
                    const filter = this.value.toLowerCase();
                    const table = document.getElementById('data-table');
                    const rows = table.querySelectorAll('tbody tr');
                    
                    rows.forEach(row => {
                        const text = row.textContent.toLowerCase();
                        row.style.display = text.includes(filter) ? '' : 'none';
                    });
                });
            }
        });
        </script>
        """
        
        return f"{table_css}{table_js}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class Tabs(ComponentBase):
    """Interactive tabs component"""
    
    def __init__(self, tabs: List[Dict[str, Any]], default_active: int = 0, 
                 css_class: Optional[str] = None):
        tabs_class = "tabs-container"
        if css_class:
            tabs_class += f" {css_class}"
        
        super().__init__(css_class=tabs_class)
        self.tabs = tabs
        self.default_active = default_active
        
        # Generate unique ID
        import uuid
        self.tabs_id = f"tabs-{str(uuid.uuid4())[:8]}"
        
        # Build tabs HTML
        nav_html = f'<ul class="nav nav-tabs" id="{self.tabs_id}-nav" role="tablist">'
        content_html = f'<div class="tab-content" id="{self.tabs_id}-content">'
        
        for i, tab in enumerate(tabs):
            tab_id = f"{self.tabs_id}-tab-{i}"
            is_active = i == default_active
            active_class = " active" if is_active else ""
            
            # Tab navigation
            nav_html += f'''
            <li class="nav-item" role="presentation">
                <button class="nav-link{active_class}" id="{tab_id}-tab" 
                        data-bs-toggle="tab" data-bs-target="#{tab_id}" 
                        type="button" role="tab" aria-controls="{tab_id}" 
                        aria-selected="{str(is_active).lower()}">
                    {tab.get('title', f'Tab {i+1}')}
                </button>
            </li>
            '''
            
            # Tab content
            content = tab.get('content', '')
            if hasattr(content, 'render'):
                content = content.render()
            elif isinstance(content, list):
                content = ''.join([item.render() if hasattr(item, 'render') else str(item) for item in content])
            
            content_html += f'''
            <div class="tab-pane fade{" show active" if is_active else ""}" 
                 id="{tab_id}" role="tabpanel" aria-labelledby="{tab_id}-tab">
                <div class="p-3">{content}</div>
            </div>
            '''
        
        nav_html += '</ul>'
        content_html += '</div>'
        
        self.content = nav_html + content_html

class Carousel(ComponentBase):
    """Image/content carousel component"""
    
    def __init__(self, items: List[Dict[str, Any]], auto_slide: bool = True,
                 show_indicators: bool = True, show_controls: bool = True,
                 css_class: Optional[str] = None):
        carousel_class = "carousel slide"
        if css_class:
            carousel_class += f" {css_class}"
        
        super().__init__(css_class=carousel_class)
        self.items = items
        self.auto_slide = auto_slide
        
        # Generate unique ID
        import uuid
        self.carousel_id = f"carousel-{str(uuid.uuid4())[:8]}"
        
        # Set carousel attributes
        self.set_id(self.carousel_id)
        if auto_slide:
            self.set_attribute('data-bs-ride', 'carousel')
        
        # Build carousel HTML
        carousel_html = ""
        
        # Indicators
        if show_indicators:
            indicators_html = '<div class="carousel-indicators">'
            for i in range(len(items)):
                active_class = " active" if i == 0 else ""
                indicators_html += f'''
                <button type="button" data-bs-target="#{self.carousel_id}" 
                        data-bs-slide-to="{i}" class="{active_class.strip()}"
                        aria-current="true" aria-label="Slide {i+1}"></button>
                '''
            indicators_html += '</div>'
            carousel_html += indicators_html
        
        # Carousel inner
        inner_html = '<div class="carousel-inner">'
        for i, item in enumerate(items):
            active_class = " active" if i == 0 else ""
            
            if 'image' in item:
                # Image slide
                alt_text = item.get('alt', f'Slide {i+1}')
                caption = item.get('caption', '')
                
                slide_html = f'''
                <div class="carousel-item{active_class}">
                    <img src="{item['image']}" class="d-block w-100" alt="{alt_text}">
                    {f'<div class="carousel-caption d-none d-md-block"><p>{caption}</p></div>' if caption else ''}
                </div>
                '''
            else:
                # Content slide
                content = item.get('content', '')
                if hasattr(content, 'render'):
                    content = content.render()
                
                slide_html = f'''
                <div class="carousel-item{active_class}">
                    <div class="d-block w-100 p-5 bg-light text-center">
                        {content}
                    </div>
                </div>
                '''
            
            inner_html += slide_html
        
        inner_html += '</div>'
        carousel_html += inner_html
        
        # Controls
        if show_controls:
            controls_html = f'''
            <button class="carousel-control-prev" type="button" 
                    data-bs-target="#{self.carousel_id}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" 
                    data-bs-target="#{self.carousel_id}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
            '''
            carousel_html += controls_html
        
        self.content = carousel_html

class Breadcrumb(ComponentBase):
    """Navigation breadcrumb component"""
    
    def __init__(self, items: List[Dict[str, str]], css_class: Optional[str] = None):
        breadcrumb_class = "breadcrumb-container"
        if css_class:
            breadcrumb_class += f" {css_class}"
        
        super().__init__(css_class=breadcrumb_class)
        
        breadcrumb_html = '<nav aria-label="breadcrumb"><ol class="breadcrumb">'
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            text = item.get('text', 'Page')
            url = item.get('url', '#')
            
            if is_last or not url or url == '#':
                breadcrumb_html += f'<li class="breadcrumb-item active" aria-current="page">{text}</li>'
            else:
                breadcrumb_html += f'<li class="breadcrumb-item"><a href="{url}">{text}</a></li>'
        
        breadcrumb_html += '</ol></nav>'
        self.content = breadcrumb_html

class Pagination(ComponentBase):
    """Pagination component for multi-page content"""
    
    def __init__(self, current_page: int, total_pages: int, base_url: str = "#",
                 max_visible: int = 5, css_class: Optional[str] = None):
        pagination_class = "pagination-container"
        if css_class:
            pagination_class += f" {css_class}"
        
        super().__init__(css_class=pagination_class)
        
        pagination_html = '<nav aria-label="Page navigation"><ul class="pagination justify-content-center">'
        
        # Previous button
        prev_disabled = "disabled" if current_page <= 1 else ""
        prev_url = f"{base_url}{current_page - 1}" if current_page > 1 else "#"
        pagination_html += f'''
        <li class="page-item {prev_disabled}">
            <a class="page-link" href="{prev_url}" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        '''
        
        # Page numbers
        start_page = max(1, current_page - max_visible // 2)
        end_page = min(total_pages, start_page + max_visible - 1)
        
        if start_page > 1:
            pagination_html += f'<li class="page-item"><a class="page-link" href="{base_url}1">1</a></li>'
            if start_page > 2:
                pagination_html += '<li class="page-item disabled"><span class="page-link">...</span></li>'
        
        for page in range(start_page, end_page + 1):
            active_class = "active" if page == current_page else ""
            pagination_html += f'''
            <li class="page-item {active_class}">
                <a class="page-link" href="{base_url}{page}">{page}</a>
            </li>
            '''
        
        if end_page < total_pages:
            if end_page < total_pages - 1:
                pagination_html += '<li class="page-item disabled"><span class="page-link">...</span></li>'
            pagination_html += f'<li class="page-item"><a class="page-link" href="{base_url}{total_pages}">{total_pages}</a></li>'
        
        # Next button
        next_disabled = "disabled" if current_page >= total_pages else ""
        next_url = f"{base_url}{current_page + 1}" if current_page < total_pages else "#"
        pagination_html += f'''
        <li class="page-item {next_disabled}">
            <a class="page-link" href="{next_url}" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
        '''
        
        pagination_html += '</ul></nav>'
        self.content = pagination_html

class Toast(ComponentBase):
    """Toast notification component"""
    
    def __init__(self, message: str, toast_type: str = "info", 
                 auto_hide: bool = True, delay: int = 5000,
                 position: str = "top-end", css_class: Optional[str] = None):
        toast_class = f"toast align-items-center text-white bg-{toast_type} border-0"
        if css_class:
            toast_class += f" {css_class}"
        
        super().__init__(css_class=toast_class)
        
        # Generate unique ID
        import uuid
        self.toast_id = f"toast-{str(uuid.uuid4())[:8]}"
        self.set_id(self.toast_id)
        
        # Set toast attributes
        self.set_attribute('role', 'alert')
        self.set_attribute('aria-live', 'assertive')
        self.set_attribute('aria-atomic', 'true')
        if auto_hide:
            self.set_attribute('data-bs-autohide', 'true')
            self.set_attribute('data-bs-delay', str(delay))
        
        toast_html = f'''
        <div class="d-flex">
            <div class="toast-body">{message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" 
                    data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        '''
        
        self.content = toast_html
        
        # Add positioning container
        self.position = position
    
    def render(self):
        attrs = self.render_attributes()
        
        # Toast container and positioning
        position_classes = {
            'top-start': 'top-0 start-0',
            'top-center': 'top-0 start-50 translate-middle-x',
            'top-end': 'top-0 end-0',
            'middle-start': 'top-50 start-0 translate-middle-y',
            'middle-center': 'top-50 start-50 translate-middle',
            'middle-end': 'top-50 end-0 translate-middle-y',
            'bottom-start': 'bottom-0 start-0',
            'bottom-center': 'bottom-0 start-50 translate-middle-x',
            'bottom-end': 'bottom-0 end-0'
        }
        
        position_class = position_classes.get(self.position, 'top-0 end-0')
        
        container_html = f'''
        <div class="toast-container position-fixed {position_class} p-3" style="z-index: 11;">
            <{self.tag}{attrs}>{self.content}</{self.tag}>
        </div>
        '''
        
        # Auto-show JavaScript
        toast_js = f'''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const toast = new bootstrap.Toast(document.getElementById('{self.toast_id}'));
            toast.show();
        }});
        </script>
        '''
        
        return container_html + toast_js

class Rating(ComponentBase):
    """Star rating component"""
    
    def __init__(self, value: float, max_rating: int = 5, 
                 interactive: bool = False, size: str = "md",
                 css_class: Optional[str] = None):
        rating_class = f"rating rating-{size}"
        if interactive:
            rating_class += " rating-interactive"
        if css_class:
            rating_class += f" {css_class}"
        
        super().__init__(css_class=rating_class)
        
        # Generate unique ID for interactive ratings
        if interactive:
            import uuid
            self.rating_id = f"rating-{str(uuid.uuid4())[:8]}"
            self.set_id(self.rating_id)
        
        # Build rating HTML
        rating_html = '<div class="rating-stars">'
        
        for i in range(1, max_rating + 1):
            if i <= value:
                star_class = "star star-filled"
                star_icon = "★"
            elif i - 0.5 <= value:
                star_class = "star star-half"
                star_icon = "☆"
            else:
                star_class = "star star-empty"
                star_icon = "☆"
            
            if interactive:
                rating_html += f'<span class="{star_class}" data-rating="{i}">{star_icon}</span>'
            else:
                rating_html += f'<span class="{star_class}">{star_icon}</span>'
        
        rating_html += f'</div><span class="rating-value">{value}/{max_rating}</span>'
        self.content = rating_html
    
    def render(self):
        attrs = self.render_attributes()
        
        rating_css = """
        <style>
        .rating {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .rating-stars {
            display: flex;
            gap: 0.2rem;
        }
        
        .star {
            color: #ddd;
            font-size: 1.2rem;
            transition: color 0.2s;
        }
        
        .star-filled {
            color: #ffc107;
        }
        
        .star-half {
            color: #ffc107;
        }
        
        .rating-interactive .star {
            cursor: pointer;
        }
        
        .rating-interactive .star:hover {
            color: #ffc107;
        }
        
        .rating-md .star {
            font-size: 1.2rem;
        }
        
        .rating-lg .star {
            font-size: 1.5rem;
        }
        
        .rating-sm .star {
            font-size: 1rem;
        }
        
        .rating-value {
            font-size: 0.9rem;
            color: #666;
            margin-left: 0.5rem;
        }
        </style>
        """
        
        return f"{rating_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class Avatar(ComponentBase):
    """User avatar component with fallback support"""
    
    def __init__(self, src: Optional[str] = None, alt: str = "Avatar",
                 size: str = "md", initials: Optional[str] = None,
                 css_class: Optional[str] = None):
        avatar_class = f"avatar avatar-{size}"
        if css_class:
            avatar_class += f" {css_class}"
        
        super().__init__(css_class=avatar_class)
        
        if src:
            # Image avatar
            avatar_html = f'<img src="{src}" alt="{alt}" class="avatar-img">'
        elif initials:
            # Initials avatar
            avatar_html = f'<div class="avatar-initials">{initials[:2].upper()}</div>'
        else:
            # Default avatar
            avatar_html = '<div class="avatar-default">👤</div>'
        
        self.content = avatar_html
    
    def render(self):
        attrs = self.render_attributes()
        
        avatar_css = """
        <style>
        .avatar {
            display: inline-block;
            border-radius: 50%;
            overflow: hidden;
            background-color: #e9ecef;
            text-align: center;
            vertical-align: middle;
        }
        
        .avatar-sm {
            width: 32px;
            height: 32px;
        }
        
        .avatar-md {
            width: 48px;
            height: 48px;
        }
        
        .avatar-lg {
            width: 64px;
            height: 64px;
        }
        
        .avatar-xl {
            width: 96px;
            height: 96px;
        }
        
        .avatar-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .avatar-initials {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #007bff;
            color: white;
            font-weight: bold;
        }
        
        .avatar-sm .avatar-initials {
            font-size: 0.75rem;
        }
        
        .avatar-md .avatar-initials {
            font-size: 1rem;
        }
        
        .avatar-lg .avatar-initials {
            font-size: 1.25rem;
        }
        
        .avatar-xl .avatar-initials {
            font-size: 1.5rem;
        }
        
        .avatar-default {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5em;
            color: #6c757d;
        }
        </style>
        """
        
        return f"{avatar_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"