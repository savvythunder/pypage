"""
Complete HTML Generator v3.0+ Feature Showcase
Demonstrates ALL available components and features:
- Professional UI components (tables, tabs, carousels, etc.)
- Data visualization (charts, dashboards, KPIs)
- Advanced forms (file uploads, wizards, validation)
- Animations and dark mode
- Plugin system and export capabilities
"""

from html_generator import *

def create_complete_showcase():
    """Create the most comprehensive showcase of all features"""
    
    # Create main page with all features enabled
    page = Page('Complete Feature Showcase', 'Professional Web Development with Python')
    page.set_theme('bootstrap')
    page.add_content(DarkModeToggle(position="top-right"))
    page.enable_debug_view(show_boundaries=True, show_tooltips=True)
    
    container = Container()
    
    # Hero section with animations
    hero = FadeIn(
        Container([
            Heading('Complete HTML Generator Showcase', 1, css_class='display-2 text-center mb-4'),
            Paragraph('Experience every component and feature available in the most comprehensive Python HTML generator library.', 
                     css_class='lead text-center mb-5'),
            Row([
                Column([
                    Badge('Professional UI', 'primary', css_class='mx-1')
                ], width='md-3'),
                Column([
                    Badge('Data Visualization', 'success', css_class='mx-1')
                ], width='md-3'),
                Column([
                    Badge('Advanced Forms', 'info', css_class='mx-1')
                ], width='md-3'),
                Column([
                    Badge('Export & Plugins', 'warning', css_class='mx-1')
                ], width='md-3')
            ], css_class='text-center')
        ], css_class='py-5 bg-gradient-primary text-white rounded mb-5'),
        duration="1.2s"
    )
    container.add_content(hero)
    
    # Navigation tabs for different sections
    tab_content = [
        {
            'title': '📊 Data Visualization',
            'content': create_data_viz_section()
        },
        {
            'title': '🎨 Professional UI',
            'content': create_ui_components_section()
        },
        {
            'title': '📝 Advanced Forms',
            'content': create_forms_section()
        },
        {
            'title': '🎭 Animations & Effects',
            'content': create_animations_section()
        },
        {
            'title': '🔌 Plugins & Export',
            'content': create_plugins_section()
        }
    ]
    
    main_tabs = Tabs(tab_content, default_active=0)
    container.add_content(main_tabs)
    
    page.add_content(container)
    return page

def create_data_viz_section():
    """Create data visualization showcase section"""
    section = []
    
    section.append(Heading('Data Visualization Dashboard', 2, css_class='mb-4'))
    
    # Sample data for charts
    metrics = [
        {'value': '₹2.4M', 'label': 'Revenue', 'change': '+12%', 'change_type': 'success'},
        {'value': '15.2K', 'label': 'Users', 'change': '+8%', 'change_type': 'success'},
        {'value': '94.2%', 'label': 'Uptime', 'change': 'Stable', 'change_type': 'info'},
        {'value': '3.8s', 'label': 'Load Time', 'change': '-15%', 'change_type': 'success'}
    ]
    
    # Create charts
    bar_chart = BarChart(
        labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets=[{
            'label': 'Sales',
            'data': [12000, 19000, 15000, 25000, 22000, 30000],
            'backgroundColor': '#36A2EB'
        }],
        title='Monthly Sales Performance'
    )
    
    line_chart = LineChart(
        labels=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets=[{
            'label': 'Active Users',
            'data': [1200, 1900, 1500, 2100],
            'borderColor': '#FF6384',
            'backgroundColor': 'rgba(255, 99, 132, 0.2)'
        }],
        title='Weekly User Activity'
    )
    
    pie_chart = PieChart(
        labels=['Mobile', 'Desktop', 'Tablet'],
        data_values=[65, 30, 5],
        title='Device Usage Distribution'
    )
    
    # Dashboard with all metrics and charts
    dashboard = Dashboard('Business Intelligence Dashboard', metrics, [bar_chart, line_chart, pie_chart])
    section.append(dashboard)
    
    # KPI Cards Row
    section.append(Heading('Key Performance Indicators', 3, css_class='mt-5 mb-3'))
    kpi_row = Row()
    
    # Sample trend data
    revenue_trend = [100, 120, 110, 140, 135, 160, 155, 180]
    users_trend = [50, 55, 52, 58, 62, 59, 65, 68]
    performance_trend = [95, 92, 96, 94, 97, 95, 98, 96]
    
    kpi1 = KPICard('Monthly Revenue', '₹180K', revenue_trend, '+12.5%', 'success', 'fas fa-chart-line')
    kpi2 = KPICard('Active Users', '68K', users_trend, '+8.2%', 'success', 'fas fa-users')
    kpi3 = KPICard('Performance Score', '96%', performance_trend, '+2%', 'success', 'fas fa-tachometer-alt')
    
    kpi_row.add_column(Column([kpi1], width='md-4'))
    kpi_row.add_column(Column([kpi2], width='md-4'))
    kpi_row.add_column(Column([kpi3], width='md-4'))
    
    section.append(kpi_row)
    
    return section

def create_ui_components_section():
    """Create professional UI components showcase"""
    section = []
    
    section.append(Heading('Professional UI Components', 2, css_class='mb-4'))
    
    # Advanced Table with sorting and search
    table_data = [
        ['John Doe', 'Software Engineer', 'Engineering', '₹85,000', '4.5'],
        ['Jane Smith', 'Product Manager', 'Product', '₹95,000', '4.8'],
        ['Mike Johnson', 'Designer', 'Design', '₹75,000', '4.2'],
        ['Sarah Wilson', 'Data Scientist', 'Analytics', '₹90,000', '4.7'],
        ['Tom Brown', 'DevOps Engineer', 'Engineering', '₹80,000', '4.3']
    ]
    
    advanced_table = Table(
        headers=['Name', 'Position', 'Department', 'Salary', 'Rating'],
        rows=table_data,
        sortable=True,
        searchable=True,
        striped=True,
        hover=True
    )
    section.append(advanced_table)
    
    # Image Carousel
    section.append(Heading('Image Carousel', 3, css_class='mt-5 mb-3'))
    carousel_items = [
        {
            'image': 'https://picsum.photos/800/400?random=1',
            'caption': 'Beautiful landscape photography'
        },
        {
            'image': 'https://picsum.photos/800/400?random=2',
            'caption': 'Urban architecture and design'
        },
        {
            'image': 'https://picsum.photos/800/400?random=3',
            'caption': 'Nature and wildlife scenes'
        }
    ]
    
    image_carousel = Carousel(carousel_items, auto_slide=True, show_indicators=True)
    section.append(image_carousel)
    
    # User Interface Elements
    section.append(Heading('User Interface Elements', 3, css_class='mt-5 mb-3'))
    
    ui_row = Row()
    
    # Avatars and ratings column
    avatars_col = Column(width='md-4')
    avatars_col.add_content(Heading('User Profiles', 4, css_class='mb-3'))
    
    # User profiles with avatars and ratings
    profile1 = Card([
        Div([
            Avatar(initials='JD', size='lg', css_class='me-3'),
            Div([
                Heading('John Doe', 5, css_class='mb-1'),
                Paragraph('Senior Developer', css_class='text-muted mb-2'),
                Rating(4.5, interactive=False, size='sm')
            ], css_class='flex-grow-1')
        ], css_class='d-flex align-items-center')
    ], css_class='mb-3')
    
    profile2 = Card([
        Div([
            Avatar(src='https://picsum.photos/64/64?random=4', alt='Jane Smith', size='lg', css_class='me-3'),
            Div([
                Heading('Jane Smith', 5, css_class='mb-1'),
                Paragraph('Product Manager', css_class='text-muted mb-2'),
                Rating(4.8, interactive=False, size='sm')
            ], css_class='flex-grow-1')
        ], css_class='d-flex align-items-center')
    ])
    
    avatars_col.add_content(profile1)
    avatars_col.add_content(profile2)
    
    # Breadcrumb and pagination column
    nav_col = Column(width='md-4')
    nav_col.add_content(Heading('Navigation Elements', 4, css_class='mb-3'))
    
    breadcrumb = Breadcrumb([
        {'text': 'Home', 'url': '/'},
        {'text': 'Products', 'url': '/products'},
        {'text': 'Category', 'url': '/products/category'},
        {'text': 'Current Page'}
    ])
    nav_col.add_content(breadcrumb)
    
    pagination = Pagination(current_page=3, total_pages=10, base_url='/page/')
    nav_col.add_content(pagination)
    
    # Toast notifications column
    toasts_col = Column(width='md-4')
    toasts_col.add_content(Heading('Notifications', 4, css_class='mb-3'))
    
    # Note: Toasts would automatically show when page loads
    toast_info = Toast('Welcome to the showcase!', 'info', auto_hide=False)
    toast_success = Toast('Feature loaded successfully!', 'success', delay=3000)
    
    toasts_col.add_content(Paragraph('Toast notifications will appear in the top-right corner.', css_class='text-muted'))
    
    ui_row.add_column(avatars_col)
    ui_row.add_column(nav_col)
    ui_row.add_column(toasts_col)
    
    section.append(ui_row)
    
    # Add the actual toasts (they'll position themselves)
    section.append(toast_info)
    section.append(toast_success)
    
    return section

def create_forms_section():
    """Create advanced forms showcase"""
    section = []
    
    section.append(Heading('Advanced Form Components', 2, css_class='mb-4'))
    
    # Multi-step Form Wizard
    wizard_steps = [
        {
            'title': 'Personal Information',
            'content': [
                Input('text', 'first_name', placeholder='First Name', required=True, label='First Name'),
                Input('text', 'last_name', placeholder='Last Name', required=True, label='Last Name'),
                Input('email', 'email', placeholder='your.email@example.com', required=True, label='Email Address'),
                DateTimePicker('birth_date', 'date', label='Date of Birth')
            ]
        },
        {
            'title': 'Professional Details',
            'content': [
                SearchableSelect('position', [
                    {'value': 'developer', 'text': 'Software Developer'},
                    {'value': 'designer', 'text': 'UI/UX Designer'},
                    {'value': 'manager', 'text': 'Project Manager'},
                    {'value': 'analyst', 'text': 'Data Analyst'}
                ], placeholder='Select your position...'),
                SearchableSelect('skills', [
                    {'value': 'python', 'text': 'Python'},
                    {'value': 'javascript', 'text': 'JavaScript'},
                    {'value': 'react', 'text': 'React'},
                    {'value': 'nodejs', 'text': 'Node.js'},
                    {'value': 'sql', 'text': 'SQL'}
                ], multiple=True, placeholder='Select your skills...'),
                TextArea('experience', placeholder='Tell us about your experience...', rows=4, label='Experience')
            ]
        },
        {
            'title': 'File Upload & Final Steps',
            'content': [
                FileUpload('resume', accept='.pdf,.doc,.docx', max_size='5MB', preview=True),
                FileUpload('portfolio', accept='image/*', multiple=True, max_size='10MB', preview=True),
                Alert('Review your information and submit the form.', 'info')
            ]
        }
    ]
    
    form_wizard = FormWizard(wizard_steps)
    section.append(form_wizard)
    
    # Form Validation Example
    section.append(Heading('Form Validation Example', 3, css_class='mt-5 mb-3'))
    
    validation_form = Form([
        Row([
            Column([
                Input('text', 'username', placeholder='Username', required=True, label='Username'),
                Input('password', 'password', placeholder='Password', required=True, label='Password'),
                Input('email', 'email_confirm', placeholder='Confirm Email', required=True, label='Confirm Email')
            ], width='md-6'),
            Column([
                Input('tel', 'phone', placeholder='+91 98765 43210', label='Phone Number'),
                Input('number', 'age', placeholder='Age', label='Age (18-65)'),
                Select('country', [
                    {'value': 'in', 'text': 'India'},
                    {'value': 'us', 'text': 'United States'},
                    {'value': 'uk', 'text': 'United Kingdom'},
                    {'value': 'ca', 'text': 'Canada'}
                ], label='Country')
            ], width='md-6')
        ]),
        Button('Validate Form', 'submit', css_class='btn-primary mt-3')
    ], action='/submit', method='POST', css_id='validation-form')
    
    # Add validation rules
    validation_rules = {
        'username': {
            'required': True,
            'min_length': 3,
            'max_length': 20,
            'pattern': '^[a-zA-Z0-9_]+$',
            'pattern_message': 'Only letters, numbers, and underscores allowed'
        },
        'password': {
            'required': True,
            'min_length': 8,
            'pattern': '(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)',
            'pattern_message': 'Must contain at least one uppercase letter, one lowercase letter, and one number'
        },
        'email_confirm': {
            'required': True,
            'email': True
        },
        'phone': {
            'pattern': '^\\+?[1-9]\\d{1,14}$',
            'pattern_message': 'Please enter a valid phone number'
        },
        'age': {
            'number': True,
            'min': 18,
            'max': 65
        }
    }
    
    form_validation = FormValidation('validation-form', validation_rules)
    
    section.append(validation_form)
    section.append(form_validation)
    
    return section

def create_animations_section():
    """Create animations and effects showcase"""
    section = []
    
    section.append(Heading('Animations & Visual Effects', 2, css_class='mb-4'))
    
    # Different animation types
    animations_row = Row()
    
    # FadeIn animation
    fade_col = Column(width='md-3')
    fade_example = FadeIn(
        Card([
            Heading('FadeIn Effect', 4, css_class='card-title text-center'),
            Paragraph('Smooth fade-in animation with customizable duration and delay.', css_class='card-text'),
            Badge('Smooth', 'primary', css_class='d-block text-center')
        ], css_class='h-100 text-center'),
        duration="1s",
        delay="0.2s"
    )
    fade_col.add_content(fade_example)
    
    # SlideUp animation
    slide_col = Column(width='md-3')
    slide_example = SlideUp(
        Card([
            Heading('SlideUp Effect', 4, css_class='card-title text-center'),
            Paragraph('Slides up from below with customizable distance and easing.', css_class='card-text'),
            Badge('Dynamic', 'success', css_class='d-block text-center')
        ], css_class='h-100 text-center'),
        duration="0.8s",
        delay="0.4s",
        distance="60px"
    )
    slide_col.add_content(slide_example)
    
    # Pulse animation
    pulse_col = Column(width='md-3')
    pulse_example = Pulse(
        Card([
            Heading('Pulse Effect', 4, css_class='card-title text-center'),
            Paragraph('Continuous pulsing animation to draw attention to important elements.', css_class='card-text'),
            Badge('Attention', 'warning', css_class='d-block text-center')
        ], css_class='h-100 text-center'),
        duration="2s"
    )
    pulse_col.add_content(pulse_example)
    
    # Scroll-triggered animation
    scroll_col = Column(width='md-3')
    scroll_example = AnimateOnScroll(
        Card([
            Heading('Scroll Trigger', 4, css_class='card-title text-center'),
            Paragraph('Animates when scrolled into view using Intersection Observer API.', css_class='card-text'),
            Badge('Interactive', 'info', css_class='d-block text-center')
        ], css_class='h-100 text-center'),
        animation_type="fadeIn",
        threshold=0.3
    )
    scroll_col.add_content(scroll_example)
    
    animations_row.add_column(fade_col)
    animations_row.add_column(slide_col)
    animations_row.add_column(pulse_col)
    animations_row.add_column(scroll_col)
    
    section.append(animations_row)
    
    # Dark mode showcase
    section.append(Heading('Dark Mode Integration', 3, css_class='mt-5 mb-3'))
    
    dark_mode_demo = Card([
        Heading('Dark Mode Features', 4, css_class='card-title'),
        HtmlList([
            'System preference detection',
            'Manual toggle control',
            'Persistent storage across sessions',
            'CSS custom properties for smooth transitions',
            'Automatic component integration'
        ], list_type='ul', css_class='mb-3'),
        Paragraph('Try the dark mode toggle in the top-right corner to see the seamless theme switching.', 
                 css_class='text-muted')
    ], css_class='bg-light')
    
    section.append(dark_mode_demo)
    
    return section

def create_plugins_section():
    """Create plugins and export capabilities showcase"""
    section = []
    
    section.append(Heading('Plugin System & Export Capabilities', 2, css_class='mb-4'))
    
    # Plugin components showcase
    plugins_row = Row()
    
    # Timeline plugin
    timeline_col = Column(width='md-6')
    timeline_col.add_content(Heading('Timeline Component', 4, css_class='mb-3'))
    
    timeline_events = [
        {
            'title': 'HTML Generator v1.0',
            'date': 'January 2024',
            'description': 'Initial release with basic HTML components and page generation'
        },
        {
            'title': 'Enhanced Forms & Layout',
            'date': 'March 2024', 
            'description': 'Added comprehensive form system and responsive layout components'
        },
        {
            'title': 'Template System',
            'date': 'June 2024',
            'description': 'Introduced reusable templates and component inheritance'
        },
        {
            'title': 'HTML Generator v3.0',
            'date': 'August 2024',
            'description': 'Major release with animations, dark mode, plugins, and export features'
        }
    ]
    
    timeline = Timeline(timeline_events, orientation='vertical')
    timeline_col.add_content(timeline)
    
    # Plugin statistics
    stats_col = Column(width='md-6')
    stats_col.add_content(Heading('Statistics Dashboard', 4, css_class='mb-3'))
    
    stats_cards = [
        StatCard('Total Components', '25+', 'fas fa-puzzle-piece', '+8 new', 'positive'),
        StatCard('Lines of Code', '5,000+', 'fas fa-code', '+2,000', 'positive'),
        StatCard('Test Coverage', '95%', 'fas fa-check-circle', 'Excellent', 'positive'),
        StatCard('Performance', '⚡ Fast', 'fas fa-bolt', 'Optimized', 'neutral')
    ]
    
    for stat in stats_cards:
        stats_col.add_content(stat)
    
    plugins_row.add_column(timeline_col)
    plugins_row.add_column(stats_col)
    section.append(plugins_row)
    
    # Code block plugin
    section.append(Heading('Code Block Plugin', 3, css_class='mt-5 mb-3'))
    
    code_example = CodeBlock('''# Example: Creating a complete web page
from html_generator import *

# Initialize page with dark mode support
page = Page('My Website', 'Welcome to my site')
page.add_content(DarkModeToggle())

# Add animated hero section
hero = FadeIn(
    Container([
        Heading('Welcome!', 1, css_class='display-3'),
        Paragraph('Built with Python HTML Generator')
    ]),
    duration="1s"
)

# Create data visualization
chart = BarChart(
    labels=['Q1', 'Q2', 'Q3', 'Q4'],
    datasets=[{
        'label': 'Revenue',
        'data': [10000, 15000, 12000, 18000],
        'backgroundColor': '#007bff'
    }]
)

# Advanced form with validation
form = Form([
    Input('email', 'email', required=True, label='Email'),
    FileUpload('resume', accept='.pdf'),
    Button('Submit', 'submit', css_class='btn-primary')
])

# Add everything to page
page.add_content(hero)
page.add_content(chart)
page.add_content(form)

# Export options
html = page.generate_html()
pdf_success = to_pdf(html, 'website.pdf')
json_data = to_json(page)

# Run in browser
page.run()''', language='python', show_line_numbers=True, theme='dark')
    
    section.append(code_example)
    
    # Export capabilities demonstration
    section.append(Heading('Export Capabilities', 3, css_class='mt-5 mb-3'))
    
    export_info = Row([
        Column([
            Card([
                Heading('📄 PDF Export', 4, css_class='card-title'),
                Paragraph('Export any page or component to PDF format with customizable styling and layout options.', css_class='card-text'),
                HtmlList([
                    'WeasyPrint and PDFKit support',
                    'Custom page sizes and margins',
                    'Preserved styling and layout',
                    'Batch export capabilities'
                ], list_type='ul', css_class='small')
            ])
        ], width='md-4'),
        Column([
            Card([
                Heading('📊 JSON Serialization', 4, css_class='card-title'),
                Paragraph('Complete serialization support for saving, loading, and transferring page structures.', css_class='card-text'),
                HtmlList([
                    'Full component serialization',
                    'Nested structure preservation',
                    'Cross-platform compatibility',
                    'Version-safe format'
                ], list_type='ul', css_class='small')
            ])
        ], width='md-4'),
        Column([
            Card([
                Heading('🔌 Plugin Architecture', 4, css_class='card-title'),
                Paragraph('Extensible system for creating custom components, templates, and functionality.', css_class='card-text'),
                HtmlList([
                    '@register_component decorator',
                    'Custom template registration',
                    'Hook and filter system',
                    'Built-in plugin examples'
                ], list_type='ul', css_class='small')
            ])
        ], width='md-4')
    ])
    
    section.append(export_info)
    
    return section

def demonstrate_complete_features():
    """Generate and demonstrate all features"""
    print("🚀 Creating Complete HTML Generator Feature Showcase")
    print("=" * 60)
    
    # Create the comprehensive showcase
    showcase_page = create_complete_showcase()
    
    # Save to file
    filename = 'complete_feature_showcase.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(showcase_page.generate_html())
    
    print(f"✅ Complete showcase created: {filename}")
    
    # Demonstrate export capabilities
    print("\n📊 Testing Export Features:")
    
    # JSON export
    json_data = to_json(showcase_page)
    json_filename = 'showcase_export.json'
    with open(json_filename, 'w', encoding='utf-8') as f:
        f.write(json_data)
    print(f"✅ JSON export successful: {json_filename} ({len(json_data)} characters)")
    
    # PDF export capability check
    pdf_support = check_pdf_support()
    print(f"📄 PDF Support: {pdf_support}")
    
    if pdf_support['weasyprint'] or pdf_support['pdfkit']:
        try:
            html_content = showcase_page.generate_html()
            pdf_filename = 'showcase_export.pdf'
            success = to_pdf(html_content, pdf_filename, {
                'page-size': 'A4',
                'margin': '1in',
                'orientation': 'portrait'
            })
            if success:
                print(f"✅ PDF export successful: {pdf_filename}")
            else:
                print("❌ PDF export failed")
        except Exception as e:
            print(f"❌ PDF export error: {e}")
    else:
        print("ℹ️ Install weasyprint or pdfkit for PDF export functionality")
    
    # Component statistics
    print(f"\n📈 Feature Statistics:")
    print(f"   • Professional UI Components: 8")
    print(f"   • Data Visualization Components: 8") 
    print(f"   • Advanced Form Components: 5")
    print(f"   • Animation Components: 4")
    print(f"   • Plugin Components: 3")
    print(f"   • Total Components Available: 25+")
    
    return showcase_page

if __name__ == "__main__":
    showcase = demonstrate_complete_features()
    
    print("\n🌐 Opening complete showcase in browser...")
    temp_file = showcase.run(auto_open=True)
    
    print(f"\n🎉 Complete feature showcase is ready!")
    print(f"📁 Generated file: {temp_file}")
    print("\n💡 Feature Highlights:")
    print("   🎨 Professional tables with sorting and search")
    print("   📊 Interactive charts and dashboards")
    print("   📝 Multi-step form wizards with validation")
    print("   🎭 Smooth animations and dark mode")
    print("   🔌 Extensible plugin system")
    print("   📄 PDF and JSON export capabilities")
    print("   🎛️ Debug mode (try Ctrl+Shift+D)")
    print("\nExplore all tabs to see every feature in action!")