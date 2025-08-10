"""
Documentation routes for the HTML generator web interface
"""
from flask import Blueprint, render_template, jsonify
from pypage import *

docs_bp = Blueprint('docs', __name__, url_prefix='/docs')

@docs_bp.route('/')
def documentation_home():
    """Comprehensive documentation page showcasing all HTML generator features"""
    
    # Create a comprehensive documentation page
    page = Page('HTML Generator v3.0 Documentation', 'Complete Feature Guide')
    page.set_theme('bootstrap')
    
    # Add dark mode toggle
    page.add_content(DarkModeToggle(position="top-right"))
    
    # Main container
    container = Container()
    
    # Hero section with animations
    hero_content = SlideUp(
        Container([
            Heading('HTML Generator v3.0', 1, css_class='display-4 text-center mb-4'),
            Paragraph('A comprehensive Python library for generating HTML with advanced features including dark mode, animations, debugging tools, plugins, and export capabilities.', 
                     css_class='lead text-center mb-5'),
            Div([
                Badge('NEW', 'primary'), ' ',
                Badge('Dark Mode', 'info'), ' ',
                Badge('Animations', 'success'), ' ',
                Badge('Plugins', 'warning'), ' ',
                Badge('PDF Export', 'danger')
            ], css_class='text-center mb-4')
        ])
    )
    container.add_content(hero_content)
    
    # Feature showcase using layout system
    features_row = Row()
    
    # Column 1 - Core Components
    col1 = Column(width='lg-4')
    core_section = FadeIn(
        Card([
            Heading('Core Components', 3, css_class='card-title'),
            Paragraph('Essential building blocks for web pages:', css_class='card-text'),
            HtmlList([
                'Page - Main page container with themes',
                'Container, Div, Section - Layout containers',
                'Heading, Paragraph - Typography elements',
                'Image, Link - Media and navigation',
                'Card - Content cards with styling'
            ], list_type='ul', css_class='mb-3'),
            CodeBlock('''from pypage import *

page = Page('My Site', 'Welcome')
page.set_theme('bootstrap')

container = Container()
container.add_content(Heading('Hello World', 1))
container.add_content(Paragraph('This is a paragraph.'))

page.add_content(container)
html = page.generate_html()''', language='python', show_line_numbers=False)
        ], css_class='h-100')
    )
    col1.add_content(core_section)
    
    # Column 2 - Enhanced Forms
    col2 = Column(width='lg-4')
    forms_section = FadeIn(
        Card([
            Heading('Enhanced Forms', 3, css_class='card-title'),
            Paragraph('Complete form system with validation:', css_class='card-text'),
            HtmlList([
                'Form - Form container with action/method',
                'Input - Text, email, password, etc.',
                'TextArea - Multi-line text input',
                'Select - Dropdown with multiple selection',
                'Button - Submit and action buttons'
            ], list_type='ul', css_class='mb-3'),
            CodeBlock('''form = Form(action='/submit', method='POST')
form.add_field(Input('text', 'name', label='Name', required=True))
form.add_field(Input('email', 'email', label='Email'))
form.add_field(TextArea('message', label='Message', rows=4))
form.add_field(Select('category', [
    {'value': 'web', 'text': 'Web Dev'},
    {'value': 'mobile', 'text': 'Mobile'}
], label='Service'))
form.add_field(Button('Submit', 'submit'))''', language='python', show_line_numbers=False)
        ], css_class='h-100')
    )
    col2.add_content(forms_section)
    
    # Column 3 - Layout System
    col3 = Column(width='lg-4')
    layout_section = FadeIn(
        Card([
            Heading('Responsive Layout', 3, css_class='card-title'),
            Paragraph('Bootstrap-powered responsive layouts:', css_class='card-text'),
            HtmlList([
                'Row - Horizontal container for columns',
                'Column - Responsive grid columns',
                'Flex - Flexbox layouts with alignment',
                'Responsive breakpoints (sm, md, lg, xl)',
                'Auto-sizing and custom widths'
            ], list_type='ul', css_class='mb-3'),
            CodeBlock('''row = Row()
col1 = Column(width='md-6')
col1.add_content(Card(['Content 1']))

col2 = Column(width='md-6')
col2.add_content(Card(['Content 2']))

row.add_column(col1)
row.add_column(col2)

# Flexbox example
flex = Flex(direction='column', align='center')
flex.add_item(Badge('Centered', 'primary'))
flex.add_item(Badge('Content', 'success'))''', language='python', show_line_numbers=False)
        ], css_class='h-100')
    )
    col3.add_content(layout_section)
    
    features_row.add_column(col1)
    features_row.add_column(col2)
    features_row.add_column(col3)
    container.add_content(features_row)
    
    # Advanced Features Section
    container.add_content(Heading('Advanced Features', 2, css_class='text-center my-5'))
    
    advanced_row = Row()
    
    # Animations
    anim_col = Column(width='md-6')
    anim_content = AnimateOnScroll(
        Card([
            Heading('Animations & Transitions', 3, css_class='card-title'),
            Paragraph('Add smooth animations to enhance UX:', css_class='card-text'),
            Alert('Animation components make your pages come alive!', 'info'),
            CodeBlock('''# Fade in animation
content = FadeIn(
    Paragraph('This fades in smoothly'),
    duration='0.8s'
)

# Slide up animation
content = SlideUp(
    Card(['This slides up from bottom']),
    distance='50px'
)

# Scroll-triggered animations
content = AnimateOnScroll(
    Alert('Appears when scrolled into view', 'success'),
    animation_type='slideUp'
)

# Pulse animation for attention
important = Pulse(
    Badge('Important!', 'danger'),
    duration='1.5s'
)''', language='python', show_line_numbers=False)
        ], css_class='h-100')
    )
    anim_col.add_content(anim_content)
    
    # Dark Mode
    dark_col = Column(width='md-6')
    dark_content = AnimateOnScroll(
        Card([
            Heading('Dark Mode Support', 3, css_class='card-title'),
            Paragraph('Built-in dark mode with system preferences:', css_class='card-text'),
            Badge('Try the toggle in top-right!', 'warning'),
            CodeBlock('''# Add dark mode toggle
page.add_content(DarkModeToggle(
    position='top-right',
    icon_light='☀️',
    icon_dark='🌙'
))

# Auto dark mode (respects system)
page.add_css(create_auto_dark_mode())

# Theme provider for custom themes
theme_provider = ThemeProvider()
theme_provider.add_custom_theme('ocean', {
    '--bg-color': '#001133',
    '--text-color': '#ffffff',
    '--primary-color': '#00aaff'
})''', language='python', show_line_numbers=False)
        ], css_class='h-100')
    )
    dark_col.add_content(dark_content)
    
    advanced_row.add_column(anim_col)
    advanced_row.add_column(dark_col)
    container.add_content(advanced_row)
    
    # Developer Tools Section
    container.add_content(Heading('Developer Tools', 2, css_class='text-center my-5'))
    
    dev_row = Row()
    
    # Debug Tools
    debug_col = Column(width='md-4')
    debug_content = Card([
        Heading('Visual Debug Mode', 4, css_class='card-title'),
        Paragraph('Debug your layouts visually:', css_class='card-text small'),
        CodeBlock('''# Enable debug mode
page.enable_debug_view(
    show_boundaries=True,
    show_component_names=True,
    show_tooltips=True
)

# Or use debug wrapper
debug_component = DebugWrapper(
    my_component,
    component_name="MyCustomComponent"
)''', language='python', show_line_numbers=False),
        Badge('Ctrl+Shift+D in browser', 'info', css_class='mt-2')
    ], css_class='h-100')
    debug_col.add_content(debug_content)
    
    # Plugin System
    plugin_col = Column(width='md-4')
    plugin_content = Card([
        Heading('Plugin System', 4, css_class='card-title'),
        Paragraph('Extend with custom components:', css_class='card-text small'),
        CodeBlock('''@register_component("MyWidget")
class MyWidget(ComponentBase):
    def __init__(self, title, content):
        super().__init__()
        self.content = f"""
        <div class="my-widget">
            <h4>{title}</h4>
            <p>{content}</p>
        </div>
        """

# Use plugin component
widget = MyWidget("Hello", "World")''', language='python', show_line_numbers=False),
        Badge('Extensible', 'success', css_class='mt-2')
    ], css_class='h-100')
    plugin_col.add_content(plugin_content)
    
    # Export Tools
    export_col = Column(width='md-4')
    export_content = Card([
        Heading('Export Capabilities', 4, css_class='card-title'),
        Paragraph('Export to multiple formats:', css_class='card-text small'),
        CodeBlock('''# Export to JSON
json_data = to_json(page)
restored = from_json(json_data)

# Export to PDF (requires weasyprint)
html = page.generate_html()
success = to_pdf(html, 'output.pdf')

# Component serialization
component_dict = component.to_dict()
restored_component = ComponentBase.from_dict(component_dict)''', language='python', show_line_numbers=False),
        Badge('JSON & PDF', 'primary', css_class='mt-2')
    ], css_class='h-100')
    export_col.add_content(export_content)
    
    dev_row.add_column(debug_col)
    dev_row.add_column(plugin_col)
    dev_row.add_column(export_col)
    container.add_content(dev_row)
    
    # Advanced Components Section
    container.add_content(Heading('Advanced Components', 2, css_class='text-center my-5'))
    
    # Create accordion with examples
    accordion = Accordion('feature-examples')
    
    # Timeline example
    timeline_example = CodeBlock('''timeline = Timeline([
    {
        'title': 'Project Started',
        'date': 'January 2024',
        'description': 'Initial development began'
    },
    {
        'title': 'Beta Release',
        'date': 'March 2024', 
        'description': 'First public beta with core features'
    },
    {
        'title': 'v3.0 Release',
        'date': 'August 2024',
        'description': 'Major update with animations and dark mode'
    }
], orientation='vertical')''', language='python')
    
    accordion.add_item(
        'Timeline Component',
        f'Create chronological displays:\n{timeline_example.render()}',
        expanded=True
    )
    
    # StatCard example
    stat_example = CodeBlock('''stat_grid = Row()
stat_grid.add_column(Column([
    StatCard('Users', '1,234', 'fas fa-users', '+12%', 'positive')
], width='md-3'))
stat_grid.add_column(Column([
    StatCard('Revenue', '$45,678', 'fas fa-dollar', '+8%', 'positive')
], width='md-3'))
stat_grid.add_column(Column([
    StatCard('Conversion', '3.2%', 'fas fa-chart', '-2%', 'negative')
], width='md-3'))
stat_grid.add_column(Column([
    StatCard('Bounce Rate', '65%', 'fas fa-exit', '+5%', 'neutral')
], width='md-3'))''', language='python')
    
    accordion.add_item(
        'StatCard Component',
        f'Dashboard statistics cards:\n{stat_example.render()}'
    )
    
    # Modal example
    modal_example = CodeBlock('''modal = Modal(
    'demo-modal',
    'Feature Demo',
    'This modal showcases the advanced modal component with custom styling.',
    footer='<button class="btn btn-primary">Got it!</button>'
)

trigger = Button('Open Modal', 'button')
trigger.set_attribute('data-bs-toggle', 'modal')
trigger.set_attribute('data-bs-target', '#demo-modal')''', language='python')
    
    accordion.add_item(
        'Modal Component',
        f'Interactive modal dialogs:\n{modal_example.render()}'
    )
    
    container.add_content(accordion)
    
    # Getting Started Section
    container.add_content(Heading('Getting Started', 2, css_class='text-center my-5'))
    
    getting_started = Card([
        Heading('Quick Start Guide', 3, css_class='card-title'),
        Paragraph('Get up and running in minutes:', css_class='card-text'),
        CodeBlock('''# 1. Import the library
from pypage import *

# 2. Create a page with theme
page = Page('My Amazing Site', 'Welcome to the Future')
page.set_theme('bootstrap')  # or 'tailwind', 'bulma', 'material'

# 3. Add dark mode support
page.add_content(DarkModeToggle())

# 4. Create content with animations
hero = FadeIn(
    Container([
        Heading('Welcome!', 1, css_class='display-4 text-center'),
        Paragraph('Build amazing websites with Python', css_class='lead text-center')
    ])
)

# 5. Add interactive forms
contact_form = Form(action='/contact')
contact_form.add_field(Input('text', 'name', label='Name', required=True))
contact_form.add_field(Input('email', 'email', label='Email', required=True))
contact_form.add_field(TextArea('message', label='Message', rows=4))
contact_form.add_field(Button('Send Message', 'submit', css_class='btn-primary'))

# 6. Use responsive layout
layout = Row()
layout.add_column(Column([hero], width='md-8'))
layout.add_column(Column([contact_form], width='md-4'))

page.add_content(layout)

# 7. Enable debug mode for development
page.enable_debug_view()

# 8. Generate and run
html = page.generate_html()
page.run()  # Opens in browser automatically''', language='python')
    ], css_class='mx-auto', style='max-width: 1000px;')
    
    container.add_content(getting_started)
    
    # Footer with links
    footer_content = Div([
        Heading('Ready to Start Building?', 3, css_class='text-center mb-4'),
        Div([
            Link('Try the Web Interface', '/', css_class='btn btn-primary me-3'),
            Link('View Examples', '/examples', css_class='btn btn-outline-primary me-3'),
            Link('API Reference', '/api', css_class='btn btn-outline-secondary')
        ], css_class='text-center')
    ], css_class='text-center py-5 mt-5 bg-light rounded')
    
    container.add_content(footer_content)
    page.add_content(container)
    
    # Generate the documentation HTML
    return page.generate_html()

@docs_bp.route('/examples')
def examples():
    """Examples page with live demos"""
    page = Page('HTML Generator Examples', 'Live Demos')
    page.set_theme('bootstrap')
    page.add_content(DarkModeToggle())
    
    container = Container()
    container.add_content(Heading('Live Examples', 1, css_class='text-center mb-5'))
    
    # Example cards
    examples_row = Row()
    
    # Animation example
    anim_card = Card([
        Heading('Animation Demo', 4),
        FadeIn(Alert('This alert fades in!', 'success')),
        SlideUp(Badge('This badge slides up!', 'primary')),
        AnimateOnScroll(Paragraph('This appears when you scroll to it!'), animation_type='fadeIn')
    ])
    examples_row.add_column(Column([anim_card], width='md-4'))
    
    # Form example
    form_card = Card([
        Heading('Form Demo', 4),
        Form([
            Input('text', 'demo_name', placeholder='Your name', label='Name'),
            Select('demo_category', [
                {'value': 'feedback', 'text': 'Feedback'},
                {'value': 'question', 'text': 'Question'}
            ], label='Category'),
            TextArea('demo_message', placeholder='Your message...', rows=3, label='Message'),
            Button('Demo Submit', 'button', css_class='btn-outline-primary')
        ], action='#')
    ])
    examples_row.add_column(Column([form_card], width='md-4'))
    
    # Components example
    comp_card = Card([
        Heading('Components Demo', 4),
        Alert('Success! All components working.', 'success', dismissible=True),
        Div([
            Badge('NEW', 'primary'), ' ',
            Badge('FEATURED', 'success'), ' ',
            Badge('POPULAR', 'warning')
        ], css_class='mb-3'),
        ProgressBar(75, label='75% Complete', bar_type='info', striped=True)
    ])
    examples_row.add_column(Column([comp_card], width='md-4'))
    
    container.add_content(examples_row)
    page.add_content(container)
    
    return page.generate_html()

@docs_bp.route('/api')
def api_reference():
    """API reference page"""
    page = Page('API Reference', 'Complete API Documentation')
    page.set_theme('bootstrap')
    page.add_content(DarkModeToggle())
    
    container = Container()
    container.add_content(Heading('API Reference', 1, css_class='text-center mb-5'))
    
    # API sections
    api_accordion = Accordion('api-reference')
    
    # Core API
    core_api = '''
    <h5>Page Class</h5>
    <code>Page(title, header_text, logo_url=None)</code>
    <p>Main page container with theme support.</p>
    
    <h5>Methods:</h5>
    <ul>
        <li><code>set_theme(theme)</code> - Set page theme (bootstrap, tailwind, bulma, material)</li>
        <li><code>add_content(content)</code> - Add content to page</li>
        <li><code>add_css(css)</code> - Add custom CSS</li>
        <li><code>add_js(js)</code> - Add custom JavaScript</li>
        <li><code>enable_debug_view()</code> - Enable visual debug mode</li>
        <li><code>generate_html()</code> - Generate complete HTML</li>
        <li><code>run()</code> - Open page in browser</li>
    </ul>
    '''
    api_accordion.add_item('Core API', core_api, expanded=True)
    
    # Components API
    components_api = '''
    <h5>Form Components</h5>
    <ul>
        <li><code>Form(action, method='POST')</code></li>
        <li><code>Input(input_type, name, label=None, required=False)</code></li>
        <li><code>TextArea(name, rows=3, cols=40, label=None)</code></li>
        <li><code>Select(name, options, multiple=False, label=None)</code></li>
        <li><code>Button(text, button_type='button')</code></li>
    </ul>
    
    <h5>Layout Components</h5>
    <ul>
        <li><code>Row()</code></li>
        <li><code>Column(width='auto')</code></li>
        <li><code>Flex(direction='row', justify='start', align='start')</code></li>
    </ul>
    
    <h5>Advanced Components</h5>
    <ul>
        <li><code>Alert(message, alert_type='info', dismissible=False)</code></li>
        <li><code>Badge(text, badge_type='secondary')</code></li>
        <li><code>ProgressBar(value, max_value=100, label='')</code></li>
        <li><code>Modal(modal_id, title, content, footer='')</code></li>
        <li><code>Accordion(accordion_id)</code></li>
    </ul>
    '''
    api_accordion.add_item('Components API', components_api)
    
    # Animation API
    animation_api = '''
    <h5>Animation Components</h5>
    <ul>
        <li><code>FadeIn(content, duration='0.5s', delay='0s')</code></li>
        <li><code>SlideUp(content, duration='0.5s', distance='30px')</code></li>
        <li><code>AnimateOnScroll(content, animation_type='fadeIn')</code></li>
        <li><code>Pulse(content, duration='1s')</code></li>
    </ul>
    
    <h5>Dark Mode</h5>
    <ul>
        <li><code>DarkModeToggle(position='top-right')</code></li>
        <li><code>create_auto_dark_mode()</code> - Auto system preference</li>
    </ul>
    '''
    api_accordion.add_item('Animation & Dark Mode API', animation_api)
    
    # Plugin API
    plugin_api = '''
    <h5>Plugin System</h5>
    <ul>
        <li><code>@register_component("Name")</code> - Register custom component</li>
        <li><code>@register_template("name")</code> - Register template function</li>
        <li><code>@register_hook("event")</code> - Register event hook</li>
        <li><code>@register_filter("name")</code> - Register content filter</li>
    </ul>
    
    <h5>Export Tools</h5>
    <ul>
        <li><code>to_json(element)</code> - Serialize to JSON</li>
        <li><code>from_json(json_str)</code> - Deserialize from JSON</li>
        <li><code>to_pdf(html, output_path)</code> - Export to PDF</li>
        <li><code>check_pdf_support()</code> - Check PDF library availability</li>
    </ul>
    '''
    api_accordion.add_item('Plugin & Export API', plugin_api)
    
    container.add_content(api_accordion)
    page.add_content(container)
    
    return page.generate_html()

@docs_bp.route('/features')
def features_json():
    """JSON endpoint with feature information"""
    features = {
        'version': '3.0.0',
        'core_features': [
            'Enhanced form support with validation',
            'Responsive layout system (Row, Column, Flex)',
            'Template system with slots',
            'Component inheritance',
            'Built-in theme support',
            'Advanced components'
        ],
        'new_features': [
            'Dark mode toggle with system preferences',
            'Animation support (FadeIn, SlideUp, AnimateOnScroll)',
            'Visual debug mode for development',
            'Plugin system for extensibility',
            'PDF and JSON export capabilities'
        ],
        'themes': ['bootstrap', 'tailwind', 'bulma', 'material'],
        'export_formats': ['HTML', 'JSON', 'PDF'],
        'animation_types': ['FadeIn', 'SlideUp', 'AnimateOnScroll', 'Pulse']
    }
    return jsonify(features)