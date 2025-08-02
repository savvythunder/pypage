"""
HTML Generator v3.0 - Complete Feature Showcase
This example demonstrates all the new features added in version 3.0:
- Dark mode toggle with system preference support
- Animation support (FadeIn, SlideUp, AnimateOnScroll, Pulse)
- Visual debug mode for development
- Plugin system for extensibility
- Export capabilities (PDF and JSON)
- Enhanced components and styling
"""

from html_generator import *
import json

def create_v3_showcase():
    """Create a comprehensive showcase of v3.0 features"""
    
    # Create main page with dark mode support
    page = Page('HTML Generator v3.0 Showcase', 'Next-Generation Web Development')
    page.set_theme('bootstrap')
    
    # Add dark mode toggle in top-right corner
    page.add_content(DarkModeToggle(position="top-right", icon_light="☀️", icon_dark="🌙"))
    
    # Enable debug mode (try Ctrl+Shift+D in browser)
    page.enable_debug_view(show_boundaries=True, show_tooltips=True)
    
    # Main container
    container = Container()
    
    # Hero section with fade-in animation
    hero = FadeIn(
        Container([
            Heading('Welcome to HTML Generator v3.0', 1, css_class='display-3 text-center mb-4'),
            Paragraph('Experience the power of programmatic web development with animations, dark mode, and advanced features.', 
                     css_class='lead text-center mb-5'),
            Div([
                Badge('v3.0', 'primary'), ' ',
                Badge('NEW', 'success'), ' ',
                Badge('Dark Mode', 'info'), ' ',
                Badge('Animations', 'warning'), ' ',
                Badge('Plugins', 'danger')
            ], css_class='text-center mb-4')
        ], css_class='py-5 bg-light rounded'),
        duration="1s"
    )
    container.add_content(hero)
    
    # Animation showcase section
    container.add_content(Heading('Animation Showcase', 2, css_class='text-center my-5'))
    
    animations_row = Row()
    
    # FadeIn example
    fade_col = Column(width='md-3')
    fade_example = FadeIn(
        Card([
            Heading('FadeIn', 4, css_class='card-title'),
            Paragraph('This card fades in smoothly when the page loads.', css_class='card-text'),
            Badge('Smooth', 'primary')
        ], css_class='h-100'),
        duration="0.8s",
        delay="0.2s"
    )
    fade_col.add_content(fade_example)
    
    # SlideUp example
    slide_col = Column(width='md-3')
    slide_example = SlideUp(
        Card([
            Heading('SlideUp', 4, css_class='card-title'),
            Paragraph('This card slides up from below with a smooth transition.', css_class='card-text'),
            Badge('Dynamic', 'success')
        ], css_class='h-100'),
        duration="0.8s",
        delay="0.4s",
        distance="50px"
    )
    slide_col.add_content(slide_example)
    
    # AnimateOnScroll example
    scroll_col = Column(width='md-3')
    scroll_example = AnimateOnScroll(
        Card([
            Heading('AnimateOnScroll', 4, css_class='card-title'),
            Paragraph('This card animates when you scroll it into view.', css_class='card-text'),
            Badge('Interactive', 'info')
        ], css_class='h-100'),
        animation_type="slideUp",
        threshold=0.2
    )
    scroll_col.add_content(scroll_example)
    
    # Pulse example
    pulse_col = Column(width='md-3')
    pulse_example = Pulse(
        Card([
            Heading('Pulse', 4, css_class='card-title'),
            Paragraph('This card pulses to draw attention.', css_class='card-text'),
            Badge('Attention', 'warning')
        ], css_class='h-100'),
        duration="2s"
    )
    pulse_col.add_content(pulse_example)
    
    animations_row.add_column(fade_col)
    animations_row.add_column(slide_col)
    animations_row.add_column(scroll_col)
    animations_row.add_column(pulse_col)
    container.add_content(animations_row)
    
    # Plugin System Showcase
    container.add_content(Heading('Plugin System Components', 2, css_class='text-center my-5'))
    
    plugins_row = Row()
    
    # Timeline component
    timeline_col = Column(width='md-4')
    timeline = Timeline([
        {
            'title': 'Version 1.0',
            'date': 'January 2024',
            'description': 'Initial release with basic components'
        },
        {
            'title': 'Version 2.0',
            'date': 'June 2024',
            'description': 'Added forms, layout system, and templates'
        },
        {
            'title': 'Version 3.0',
            'date': 'August 2024',
            'description': 'Major update with animations, dark mode, and plugins'
        }
    ], orientation='vertical')
    timeline_col.add_content(timeline)
    
    # StatCard component
    stats_col = Column(width='md-8')
    stats_row = Row()
    
    stat1 = StatCard('Active Users', '2,847', 'fas fa-users', '+15%', 'positive')
    stat2 = StatCard('Components', '25+', 'fas fa-puzzle-piece', '+8 new', 'positive')
    stat3 = StatCard('Performance', '98%', 'fas fa-tachometer-alt', '+2%', 'positive')
    stat4 = StatCard('Satisfaction', '4.9/5', 'fas fa-star', 'Stable', 'neutral')
    
    stats_row.add_column(Column([stat1], width='md-3'))
    stats_row.add_column(Column([stat2], width='md-3'))
    stats_row.add_column(Column([stat3], width='md-3'))
    stats_row.add_column(Column([stat4], width='md-3'))
    
    stats_col.add_content(stats_row)
    
    plugins_row.add_column(timeline_col)
    plugins_row.add_column(stats_col)
    container.add_content(plugins_row)
    
    # Code showcase
    container.add_content(Heading('Code Examples', 2, css_class='text-center my-5'))
    
    code_examples = Row()
    
    # Python code example
    python_col = Column(width='md-6')
    python_code = CodeBlock('''# Create animated components
from html_generator import *

page = Page('My Site', 'Welcome')
page.add_content(DarkModeToggle())

# Animated hero section
hero = FadeIn(
    Container([
        Heading('Welcome!', 1),
        Paragraph('Smooth animations!')
    ]),
    duration="1s"
)

# Timeline component
timeline = Timeline([
    {'title': 'Step 1', 'date': '2024', 'description': 'Start'},
    {'title': 'Step 2', 'date': '2024', 'description': 'Progress'}
])

page.add_content(hero)
page.add_content(timeline)

# Enable debug mode
page.enable_debug_view()

# Generate and run
page.run()  # Opens in browser''', language='python', show_line_numbers=True, theme='dark')
    python_col.add_content(python_code)
    
    # Export example
    export_col = Column(width='md-6')
    export_code = CodeBlock('''# Export capabilities
from html_generator import *

# Create any component
page = Page('Export Demo', 'Multiple Formats')
page.add_content(Heading('Hello World', 1))

# Export to JSON
json_data = to_json(page)
print("Page exported to JSON")

# Restore from JSON
restored_page = from_json(json_data)

# Export to PDF (requires weasyprint)
html = page.generate_html()
success = to_pdf(html, 'output.pdf', {
    'page-size': 'A4',
    'margin': '1in'
})

# Component serialization
component = Alert('Success!', 'success')
data = component.to_dict()
restored = Alert.from_dict(data)''', language='python', show_line_numbers=True, theme='dark')
    export_col.add_content(export_code)
    
    code_examples.add_column(python_col)
    code_examples.add_column(export_col)
    container.add_content(code_examples)
    
    # Enhanced form example with animations
    container.add_content(Heading('Enhanced Interactive Form', 2, css_class='text-center my-5'))
    
    form_section = AnimateOnScroll(
        Card([
            Heading('Contact Us', 3, css_class='card-title'),
            Form([
                Input('text', 'name', placeholder='Your full name', required=True, label='Name'),
                Input('email', 'email', placeholder='your.email@example.com', required=True, label='Email Address'),
                Select('interest', [
                    {'value': 'web', 'text': 'Web Development'},
                    {'value': 'mobile', 'text': 'Mobile Apps'},
                    {'value': 'design', 'text': 'UI/UX Design'},
                    {'value': 'consulting', 'text': 'Consulting'}
                ], multiple=True, label='Areas of Interest'),
                TextArea('message', placeholder='Tell us about your project...', rows=4, label='Message'),
                Row([
                    Column([
                        Button('Send Message', 'submit', css_class='btn-primary')
                    ], width='md-6'),
                    Column([
                        Button('Reset Form', 'reset', css_class='btn-outline-secondary')
                    ], width='md-6')
                ])
            ], action='/contact', method='POST', css_class='p-4')
        ], css_class='mx-auto', style='max-width: 600px;'),
        animation_type='fadeIn'
    )
    container.add_content(form_section)
    
    # Advanced components showcase
    container.add_content(Heading('Advanced Components', 2, css_class='text-center my-5'))
    
    # Progress indicators
    progress_section = Row()
    
    progress_col = Column(width='md-8')
    progress_col.add_content(Heading('Project Progress', 4))
    progress_col.add_content(ProgressBar(85, label='Overall Completion (85%)', bar_type='success', striped=True, animated=True))
    progress_col.add_content(ProgressBar(92, label='Frontend (92%)', bar_type='info', striped=True))
    progress_col.add_content(ProgressBar(78, label='Backend (78%)', bar_type='warning', striped=True))
    progress_col.add_content(ProgressBar(65, label='Testing (65%)', bar_type='danger', striped=True))
    
    alerts_col = Column(width='md-4')
    alerts_col.add_content(Alert('All systems operational!', 'success', dismissible=True))
    alerts_col.add_content(Alert('New features available in v3.0', 'info', dismissible=True))
    alerts_col.add_content(Alert('Debug mode is enabled', 'warning', dismissible=True))
    
    progress_section.add_column(progress_col)
    progress_section.add_column(alerts_col)
    container.add_content(progress_section)
    
    # Accordion with detailed documentation
    container.add_content(Heading('Feature Documentation', 2, css_class='text-center my-5'))
    
    docs_accordion = Accordion('v3-features')
    
    # Dark Mode documentation
    dark_mode_docs = '''
    <h5>Dark Mode Features:</h5>
    <ul>
        <li><strong>System Preference Detection:</strong> Automatically detects user's system theme preference</li>
        <li><strong>Manual Toggle:</strong> Floating toggle button for manual switching</li>
        <li><strong>Persistent Storage:</strong> Remembers user's choice across sessions</li>
        <li><strong>CSS Variables:</strong> Uses modern CSS custom properties for smooth transitions</li>
        <li><strong>Component Integration:</strong> All components automatically support dark mode</li>
    </ul>
    <p>The dark mode toggle can be positioned anywhere and customized with different icons.</p>
    '''
    docs_accordion.add_item('Dark Mode System', dark_mode_docs, expanded=True)
    
    # Animation documentation
    animation_docs = '''
    <h5>Animation Components:</h5>
    <ul>
        <li><strong>FadeIn:</strong> Smooth opacity transition from 0 to 1</li>
        <li><strong>SlideUp:</strong> Slides element from below with customizable distance</li>
        <li><strong>AnimateOnScroll:</strong> Triggers animations when elements enter viewport</li>
        <li><strong>Pulse:</strong> Continuous scaling animation for attention-grabbing</li>
    </ul>
    <p>All animations support custom duration, delay, and easing functions. The IntersectionObserver API provides smooth scroll-triggered animations.</p>
    '''
    docs_accordion.add_item('Animation System', animation_docs)
    
    # Debug documentation
    debug_docs = '''
    <h5>Debug Mode Features:</h5>
    <ul>
        <li><strong>Visual Boundaries:</strong> Shows component boundaries with colored outlines</li>
        <li><strong>Component Names:</strong> Displays component type and classes</li>
        <li><strong>Interactive Tooltips:</strong> Hover for detailed component information</li>
        <li><strong>Keyboard Shortcuts:</strong> Press Ctrl+Shift+D to toggle debug view</li>
        <li><strong>Debug Panel:</strong> Floating panel with debug controls</li>
    </ul>
    <p>Essential for development and troubleshooting layout issues.</p>
    '''
    docs_accordion.add_item('Debug Tools', debug_docs)
    
    # Plugin documentation
    plugin_docs = '''
    <h5>Plugin System:</h5>
    <ul>
        <li><strong>Component Registration:</strong> @register_component decorator for custom components</li>
        <li><strong>Template Registration:</strong> @register_template for reusable templates</li>
        <li><strong>Hook System:</strong> @register_hook for event-driven functionality</li>
        <li><strong>Filter System:</strong> @register_filter for content transformation</li>
        <li><strong>Built-in Plugins:</strong> Timeline, StatCard, and CodeBlock components</li>
    </ul>
    <p>Extend the library with your own components and functionality.</p>
    '''
    docs_accordion.add_item('Plugin Architecture', plugin_docs)
    
    container.add_content(docs_accordion)
    
    # Modal example
    modal = Modal(
        'v3-modal',
        'HTML Generator v3.0 Complete!',
        '''
        <p>Congratulations! You've explored all the major features of HTML Generator v3.0:</p>
        <ul>
            <li>✅ Dark mode with system preferences</li>
            <li>✅ Smooth animations and transitions</li>
            <li>✅ Visual debug mode for development</li>
            <li>✅ Extensible plugin system</li>
            <li>✅ PDF and JSON export capabilities</li>
            <li>✅ Enhanced components and styling</li>
        </ul>
        <p class="mt-3"><strong>Ready to build amazing websites with Python?</strong></p>
        ''',
        footer='<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Start Building!</button>'
    )
    
    modal_trigger = Button('🎉 View Feature Summary', 'button', css_class='btn-lg btn-success d-block mx-auto my-5')
    modal_trigger.set_attribute('data-bs-toggle', 'modal')
    modal_trigger.set_attribute('data-bs-target', '#v3-modal')
    
    container.add_content(modal_trigger)
    container.add_content(modal)
    
    # Footer with additional information
    footer = Div([
        Heading('What\'s Next?', 3, css_class='text-center mb-4'),
        Row([
            Column([
                Card([
                    Heading('🚀 Performance', 5, css_class='card-title'),
                    Paragraph('Optimized rendering and minimal CSS/JS footprint', css_class='card-text small')
                ])
            ], width='md-3'),
            Column([
                Card([
                    Heading('🔧 Customization', 5, css_class='card-title'),
                    Paragraph('Full control over styling and behavior', css_class='card-text small')
                ])
            ], width='md-3'),
            Column([
                Card([
                    Heading('📱 Responsive', 5, css_class='card-title'),
                    Paragraph('Mobile-first design with Bootstrap integration', css_class='card-text small')
                ])
            ], width='md-3'),
            Column([
                Card([
                    Heading('🔌 Extensible', 5, css_class='card-title'),
                    Paragraph('Plugin system for unlimited customization', css_class='card-text small')
                ])
            ], width='md-3')
        ])
    ], css_class='py-5 mt-5 bg-light rounded')
    
    container.add_content(footer)
    page.add_content(container)
    
    return page

def demonstrate_export_features():
    """Demonstrate the export capabilities"""
    print("🔄 Demonstrating Export Features...")
    
    # Create a simple page for export testing
    export_page = Page('Export Test', 'Testing Export Functionality')
    export_page.add_content(Heading('Export Test Page', 1))
    export_page.add_content(Paragraph('This page demonstrates export capabilities.'))
    export_page.add_content(Alert('Export successful!', 'success'))
    
    # Test JSON export
    print("📄 Testing JSON export...")
    json_data = to_json(export_page)
    print(f"✅ JSON export successful: {len(json_data)} characters")
    
    # Test JSON import
    print("📥 Testing JSON import...")
    restored_page = from_json(json_data)
    print("✅ JSON import successful")
    
    # Test PDF export capability check
    print("🖨️ Checking PDF export capability...")
    pdf_support = check_pdf_support()
    print(f"PDF Support: {pdf_support}")
    
    if pdf_support['weasyprint'] or pdf_support['pdfkit']:
        try:
            html_content = export_page.generate_html()
            success = to_pdf(html_content, 'export_test.pdf')
            if success:
                print("✅ PDF export successful: export_test.pdf")
            else:
                print("❌ PDF export failed")
        except Exception as e:
            print(f"❌ PDF export error: {e}")
    else:
        print("ℹ️ No PDF libraries available. Install weasyprint or pdfkit for PDF export.")
    
    return json_data

if __name__ == "__main__":
    print("🚀 HTML Generator v3.0 Feature Showcase")
    print("=" * 50)
    
    # Create the showcase page
    showcase_page = create_v3_showcase()
    
    # Save to file
    with open('v3_feature_showcase.html', 'w', encoding='utf-8') as f:
        f.write(showcase_page.generate_html())
    
    print("✅ Feature showcase created: v3_feature_showcase.html")
    
    # Demonstrate export features
    json_export = demonstrate_export_features()
    
    # Save JSON export for reference
    with open('page_export_example.json', 'w', encoding='utf-8') as f:
        f.write(json_export)
    
    print("✅ JSON export example saved: page_export_example.json")
    
    # Run the showcase (opens in browser)
    print("🌐 Opening showcase in browser...")
    
    # Create page instance for running
    page = create_v3_showcase()
    temp_file = page.run(auto_open=True)
    
    print(f"🎉 Showcase opened in browser: {temp_file}")
    print("\n💡 Tips:")
    print("- Try the dark mode toggle in the top-right corner")
    print("- Press Ctrl+Shift+D to toggle debug mode")
    print("- Scroll down to see scroll-triggered animations")
    print("- Click the feature summary button for a modal demo")