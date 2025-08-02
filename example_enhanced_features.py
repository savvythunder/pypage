#!/usr/bin/env python3
"""
Enhanced HTML Generator Library Example
=======================================

This example demonstrates all the new features added to the HTML generator library:

1. Enhanced Form Support
2. Layout System (Row, Column, Flex)
3. Style Customization (inline styles, class_name parameter)
4. Templating System with Slots
5. Component Inheritance and Custom Components
6. Built-in Themes
7. JavaScript Event Hooks
8. Advanced Components (Alert, Badge, ProgressBar, Modal, etc.)
"""

from html_generator import *

def create_comprehensive_example():
    # Create a page with theme support
    page = Page("Enhanced HTML Generator Demo", "Welcome to the Enhanced Library")
    page.set_theme("bootstrap")  # You can also use: bootstrap-light, tailwind, bulma, material
    
    # Add SEO meta tags
    page.add_meta_tag("description", "Demonstration of enhanced HTML generator features")
    page.add_meta_tag("keywords", "html, generator, python, bootstrap, forms")
    
    # 1. ENHANCED FORM SUPPORT
    # Create a comprehensive form with all input types
    contact_form = Form(action="/submit", method="POST", id_attr="contact-form")
    
    # Basic inputs with labels and validation
    contact_form.add_field(Input("text", "full_name", placeholder="Enter your full name", 
                                required=True, label="Full Name", id_attr="name-input"))
    
    contact_form.add_field(Input("email", "email", placeholder="your@email.com", 
                                required=True, label="Email Address"))
    
    contact_form.add_field(Input("tel", "phone", placeholder="+1 (555) 123-4567", 
                                label="Phone Number"))
    
    # TextArea with rows and cols
    contact_form.add_field(TextArea("message", placeholder="Tell us about your project...", 
                                   rows=5, cols=50, required=True, label="Message"))
    
    # Select with multiple options
    services = [
        {"value": "web", "text": "Web Development"},
        {"value": "mobile", "text": "Mobile App Development"},
        {"value": "design", "text": "UI/UX Design"},
        {"value": "consulting", "text": "Technical Consulting"}
    ]
    contact_form.add_field(Select("services", services, multiple=True, 
                                 label="Services Interested In"))
    
    # Submit button with JavaScript event
    submit_btn = Button("Send Message", "submit", css_class="btn-success")
    submit_btn.on_click("alert('Form submitted! (This is just a demo)')")
    contact_form.add_field(submit_btn)
    
    # 2. LAYOUT SYSTEM
    # Create a responsive layout using Row and Column
    layout_section = Section(css_class="my-5")
    layout_section.add_content(Heading("Responsive Layout System", 2))
    
    # Row with multiple columns
    feature_row = Row()
    
    # Column 1 - Feature card
    col1 = Column(width="md-4")
    feature1 = FeatureCard("Easy to Use", 
                          "Simple, intuitive API for rapid development", 
                          "fas fa-rocket")
    col1.add_content(feature1)
    feature_row.add_column(col1)
    
    # Column 2 - Feature card
    col2 = Column(width="md-4")
    feature2 = FeatureCard("Flexible", 
                          "Extensive customization options and themes", 
                          "fas fa-cogs")
    col2.add_content(feature2)
    feature_row.add_column(col2)
    
    # Column 3 - Feature card
    col3 = Column(width="md-4")
    feature3 = FeatureCard("Modern", 
                          "Built with latest web standards and practices", 
                          "fas fa-star")
    col3.add_content(feature3)
    feature_row.add_column(col3)
    
    layout_section.add_content(feature_row)
    
    # 3. FLEXBOX LAYOUT
    flex_section = Section(css_class="my-5")
    flex_section.add_content(Heading("Flexbox Components", 2))
    
    # Flex container with centered content
    flex_demo = Flex(direction="row", justify="center", align="center", 
                    css_class="border p-4")
    flex_demo.set_style("min-height: 200px; background: #f8f9fa;")
    
    # Add items to flex container
    flex_demo.add_item(Badge("New", "primary", css_class="me-2"))
    flex_demo.add_item(Badge("Featured", "success", css_class="me-2"))
    flex_demo.add_item(Badge("Popular", "warning"))
    
    flex_section.add_content(flex_demo)
    
    # 4. STYLE CUSTOMIZATION
    styled_section = Section(css_class="my-5")
    styled_section.add_content(Heading("Style Customization", 2))
    
    # Element with inline styles and custom classes
    styled_div = Div("This div has custom styling!", 
                    css_class="custom-styled-element p-3 rounded")
    styled_div.set_style("background: linear-gradient(45deg, #667eea 0%, #764ba2 100%); color: white; text-align: center;")
    styled_div.add_style("box-shadow: 0 4px 6px rgba(0,0,0,0.1);")
    styled_div.on_hover("this.style.transform='scale(1.05)'")
    
    styled_section.add_content(styled_div)
    
    # 5. TEMPLATING SYSTEM
    template_section = Section(css_class="my-5")
    template_section.add_content(Heading("Template System", 2))
    
    # Create and use a template manager
    template_manager = TemplateManager()
    
    # Register predefined templates
    template_manager.register_template(create_hero_template())
    template_manager.register_template(create_footer_template())
    
    # Use template with custom content
    page.use_template_manager(template_manager)
    hero_content = template_manager.render_template("hero", {
        "title": "Welcome to Our Platform",
        "subtitle": "Build amazing websites with our enhanced HTML generator",
        "actions": '<a href="#features" class="btn btn-light btn-lg">Explore Features</a>'
    })
    template_section.add_content(hero_content)
    
    # 6. ADVANCED COMPONENTS
    components_section = Section(css_class="my-5")
    components_section.add_content(Heading("Advanced Components", 2))
    
    # Alert component
    alert = Alert("This is a success alert with dismiss functionality!", 
                 "success", dismissible=True)
    components_section.add_content(alert)
    
    # Progress bar
    progress = ProgressBar(75, label="75% Complete", bar_type="info", 
                          striped=True, animated=True)
    components_section.add_content(progress)
    
    # Accordion
    accordion = Accordion("demo-accordion")
    accordion.add_item("What is this library?", 
                      "This is an enhanced Python library for generating HTML with modern components.", 
                      expanded=True)
    accordion.add_item("How do I use it?", 
                      "Simply import the components and start building your pages programmatically.")
    accordion.add_item("Is it responsive?", 
                      "Yes! All components are built with Bootstrap and are fully responsive.")
    
    components_section.add_content(accordion)
    
    # Modal
    modal = Modal("demo-modal", "Demo Modal", 
                 "This is a demonstration of the modal component. You can add any content here!",
                 footer='<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>')
    
    # Button to trigger modal
    modal_btn = Button("Open Modal", "button", css_class="btn-primary mt-3")
    modal_btn.set_attribute("data-bs-toggle", "modal")
    modal_btn.set_attribute("data-bs-target", "#demo-modal")
    
    components_section.add_content(modal_btn)
    components_section.add_content(modal)
    
    # 7. CUSTOM COMPONENT INHERITANCE
    inheritance_section = Section(css_class="my-5")
    inheritance_section.add_content(Heading("Custom Component Inheritance", 2))
    
    # Create a custom component by extending ComponentBase
    class PricingCard(ComponentBase):
        def __init__(self, title, price, features, highlight=False):
            card_class = "col-md-4 mb-4"
            super().__init__(css_class=card_class)
            
            highlight_class = "border-primary" if highlight else ""
            card_html = f'''
            <div class="card h-100 text-center {highlight_class}">
                <div class="card-header">
                    <h4>{title}</h4>
                </div>
                <div class="card-body">
                    <h2 class="card-title text-primary">${price}<small class="text-muted">/mo</small></h2>
                    <ul class="list-unstyled mt-3 mb-4">
            '''
            
            for feature in features:
                card_html += f'<li>{feature}</li>'
            
            card_html += '''
                    </ul>
                    <button type="button" class="btn btn-lg btn-block btn-primary">Choose Plan</button>
                </div>
            </div>
            '''
            
            self.content = card_html
    
    # Use custom component
    pricing_row = Row()
    pricing_row.add_column(PricingCard("Basic", "9.99", ["10 GB Storage", "Email Support", "Basic Features"]))
    pricing_row.add_column(PricingCard("Pro", "19.99", ["100 GB Storage", "Priority Support", "Advanced Features", "API Access"], highlight=True))
    pricing_row.add_column(PricingCard("Enterprise", "49.99", ["Unlimited Storage", "24/7 Support", "All Features", "Custom Integration"]))
    
    inheritance_section.add_content(pricing_row)
    
    # Add all sections to page
    main_container = Container()
    main_container.add_content(Heading("Enhanced HTML Generator Library", 1, css_class="text-center mb-5"))
    main_container.add_content(Paragraph("This page demonstrates all the new features added to the HTML generator library.", 
                                        css_class="lead text-center mb-5"))
    
    # Form section
    form_section = Section(css_class="mb-5")
    form_section.add_content(Heading("Contact Form Demo", 2))
    form_section.add_content(contact_form)
    main_container.add_content(form_section)
    
    main_container.add_content(layout_section)
    main_container.add_content(flex_section)
    main_container.add_content(styled_section)
    main_container.add_content(template_section)
    main_container.add_content(components_section)
    main_container.add_content(inheritance_section)
    
    page.add_content(main_container)
    
    # Add Font Awesome for icons
    page.add_css_link("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css")
    
    # Add some custom CSS
    custom_styles = """
    <style>
    .custom-styled-element {
        transition: all 0.3s ease;
    }
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    </style>
    """
    page.add_content(custom_styles)
    
    return page

if __name__ == "__main__":
    # Create and run the example
    page = create_comprehensive_example()
    
    # Generate the HTML file
    with open("enhanced_features_demo.html", "w") as f:
        f.write(page.generate_html())
    
    print("Enhanced features demo generated: enhanced_features_demo.html")
    
    # Optionally run the page directly
    # page.run()  # This would open the HTML in your browser