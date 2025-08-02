# Modern UI Components

HTML Generator v3.0 introduces a comprehensive suite of modern UI components designed for interactive, accessible, and performant web applications. These components provide cutting-edge functionality while maintaining ease of use.

## Interactive Charts and Data Visualization

### InteractiveChart Component

Create dynamic, responsive charts powered by Chart.js for data visualization:

```python
from html_generator import InteractiveChart

# Sales performance chart
sales_data = {
    'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'datasets': [{
        'label': 'Revenue ($)',
        'data': [12000, 19000, 15000, 25000, 22000, 30000],
        'backgroundColor': 'rgba(54, 162, 235, 0.2)',
        'borderColor': 'rgba(54, 162, 235, 1)',
        'borderWidth': 2,
        'tension': 0.4
    }]
}

chart = InteractiveChart(
    chart_type='line',
    data=sales_data,
    options={
        'responsive': True,
        'plugins': {
            'title': {
                'display': True,
                'text': 'Monthly Revenue Trend'
            },
            'legend': {
                'position': 'bottom'
            }
        },
        'scales': {
            'y': {
                'beginAtZero': True,
                'ticks': {
                    'callback': 'function(value) { return "$" + value.toLocaleString(); }'
                }
            }
        }
    },
    canvas_id='revenue_chart'
)

page.add_content(chart)
```

### Available Chart Types

```python
# Bar Chart
bar_chart = InteractiveChart('bar', data, options)

# Line Chart
line_chart = InteractiveChart('line', data, options)

# Pie Chart
pie_chart = InteractiveChart('pie', data, options)

# Doughnut Chart
doughnut_chart = InteractiveChart('doughnut', data, options)

# Radar Chart
radar_chart = InteractiveChart('radar', data, options)

# Scatter Plot
scatter_chart = InteractiveChart('scatter', data, options)
```

### DataVisualization Component

Advanced data visualization with automatic formatting:

```python
from html_generator import DataVisualization

# Quarterly performance data
quarterly_data = [
    {'label': 'Q1 2024', 'value': 45000, 'color': '#FF6384'},
    {'label': 'Q2 2024', 'value': 52000, 'color': '#36A2EB'},
    {'label': 'Q3 2024', 'value': 48000, 'color': '#FFCE56'},
    {'label': 'Q4 2024', 'value': 61000, 'color': '#4BC0C0'}
]

# Automatic pie chart with styling
quarterly_viz = DataVisualization(
    data=quarterly_data,
    chart_type='pie',
    title='Quarterly Revenue Distribution',
    css_class='chart-container'
)

page.add_content(quarterly_viz)

# Dashboard with multiple charts
dashboard = Container(css_class='dashboard-grid')

# Revenue trend
revenue_trend = DataVisualization(
    data=[
        {'label': 'Week 1', 'value': 12000},
        {'label': 'Week 2', 'value': 15000},
        {'label': 'Week 3', 'value': 13500},
        {'label': 'Week 4', 'value': 18000}
    ],
    chart_type='line',
    title='Weekly Revenue'
)

# User engagement
engagement_data = DataVisualization(
    data=[
        {'label': 'Active Users', 'value': 2500},
        {'label': 'New Signups', 'value': 180},
        {'label': 'Returning Users', 'value': 1850}
    ],
    chart_type='bar',
    title='User Engagement Metrics'
)

dashboard.add_content(revenue_trend)
dashboard.add_content(engagement_data)
page.add_content(dashboard)
```

## Advanced Form Builder

### AdvancedFormBuilder Component

Create sophisticated forms with real-time validation and modern UI patterns:

```python
from html_generator import AdvancedFormBuilder

# Contact form with comprehensive validation
contact_form = AdvancedFormBuilder(form_id='contact_form')

# Personal information section
contact_form.add_field(
    field_type='text',
    name='first_name',
    label='First Name *',
    validation={
        'required': True,
        'minLength': 2,
        'maxLength': 50,
        'pattern': '^[A-Za-z\\s]+$',
        'patternMessage': 'Name can only contain letters and spaces'
    },
    options={
        'placeholder': 'Enter your first name',
        'autocomplete': 'given-name'
    }
)

contact_form.add_field(
    field_type='text',
    name='last_name',
    label='Last Name *',
    validation={
        'required': True,
        'minLength': 2,
        'maxLength': 50
    },
    options={
        'placeholder': 'Enter your last name',
        'autocomplete': 'family-name'
    }
)

# Contact information
contact_form.add_field(
    field_type='email',
    name='email',
    label='Email Address *',
    validation={
        'required': True,
        'email': True
    },
    options={
        'placeholder': 'your.email@example.com',
        'autocomplete': 'email'
    }
)

contact_form.add_field(
    field_type='text',
    name='phone',
    label='Phone Number',
    validation={
        'pattern': '^[\\+]?[1-9][\\d]{0,15}$',
        'patternMessage': 'Please enter a valid phone number'
    },
    options={
        'placeholder': '+1 (555) 123-4567',
        'autocomplete': 'tel'
    }
)

# Inquiry details
contact_form.add_field(
    field_type='select',
    name='inquiry_type',
    label='Type of Inquiry *',
    validation={'required': True},
    options={
        'options': [
            {'value': '', 'text': 'Please select...'},
            {'value': 'general', 'text': 'General Question'},
            {'value': 'support', 'text': 'Technical Support'},
            {'value': 'sales', 'text': 'Sales Inquiry'},
            {'value': 'partnership', 'text': 'Partnership Opportunity'},
            {'value': 'feedback', 'text': 'Feedback & Suggestions'}
        ]
    }
)

contact_form.add_field(
    field_type='textarea',
    name='message',
    label='Message *',
    validation={
        'required': True,
        'minLength': 10,
        'maxLength': 1000
    },
    options={
        'rows': 5,
        'placeholder': 'Please describe your inquiry in detail...'
    }
)

# Preferences
contact_form.add_field(
    field_type='radio',
    name='contact_preference',
    label='Preferred Contact Method *',
    validation={'required': True},
    options={
        'options': [
            {'value': 'email', 'text': 'Email'},
            {'value': 'phone', 'text': 'Phone'},
            {'value': 'either', 'text': 'Either is fine'}
        ]
    }
)

# Consent
contact_form.add_field(
    field_type='checkbox',
    name='newsletter',
    label='Subscribe to our newsletter for updates and news'
)

contact_form.add_field(
    field_type='checkbox',
    name='privacy_consent',
    label='I agree to the Privacy Policy and Terms of Service *',
    validation={'required': True}
)

page.add_content(contact_form)
```

### Form Validation Features

The AdvancedFormBuilder includes comprehensive validation:

- **Real-time validation**: Instant feedback as users type
- **Custom patterns**: Regular expression validation
- **Accessibility compliance**: ARIA labels and error announcements
- **Multiple field types**: Text, email, password, select, textarea, checkbox, radio, file, date, number
- **Visual feedback**: Success/error states with styling
- **Keyboard navigation**: Full keyboard accessibility

### Custom Form Styling

```python
# Add custom form styles
page.add_custom_css("""
.advanced-form {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    background: #f8f9fa;
    border-radius: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-field {
    margin-bottom: 1.5rem;
}

.form-label {
    font-weight: 600;
    color: #495057;
    margin-bottom: 0.5rem;
}

.form-control:focus {
    border-color: #80bdff;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.form-control.is-valid {
    border-color: #28a745;
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2328a745' d='m2.3 6.73l.4-.4 1.4-1.4 2.1-2.1-.4-.4-1.7 1.7-1.4-1.4-.4.4z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.375em + 0.1875rem) center;
    background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.form-control.is-invalid {
    border-color: #dc3545;
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath d='m5.8 4.6l.4 1.4.4-1.4m0 2.5h-.8'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right calc(0.375em + 0.1875rem) center;
    background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}
""")
```

## Micro-interactions and Animations

### MicroInteraction Component

Add engaging micro-interactions to enhance user experience:

```python
from html_generator import MicroInteraction

# Button with pulse animation on hover
cta_button = Button("Get Started", "button", css_class="btn btn-primary btn-lg")
interactive_cta = MicroInteraction(
    element=cta_button,
    interaction_type='hover',
    animation='pulse'
)

# Card with bounce animation on click
feature_card = Card(
    title="Amazing Feature",
    content="Discover what makes our platform special.",
    css_class="feature-card"
)
bouncy_card = MicroInteraction(
    element=feature_card,
    interaction_type='click',
    animation='bounce'
)

# Image with glow effect on hover
hero_image = Image("hero-banner.jpg", "Our amazing product")
glowing_image = MicroInteraction(
    element=hero_image,
    interaction_type='hover',
    animation='glow'
)

# Navigation items with shake animation for errors
nav_item = Link("/important", "Important Page")
error_nav = MicroInteraction(
    element=nav_item,
    interaction_type='click',
    animation='shake'
)

page.add_content(interactive_cta)
page.add_content(bouncy_card)
page.add_content(glowing_image)
```

### Animation Types

Available animations include:

- **pulse**: Gentle scaling effect for drawing attention
- **bounce**: Bouncing motion for playful interactions
- **shake**: Horizontal shake for error states or alerts
- **glow**: Glowing border effect for highlighting

### Custom Animations

```python
# Create custom micro-interaction with CSS
page.add_custom_css("""
@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.slide-in-element {
    animation: slideIn 0.5s ease-out;
}

@keyframes fadeInUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.fade-in-up {
    animation: fadeInUp 0.6s ease-out;
}
""")

# Apply custom animations
animated_section = Section(css_class="slide-in-element")
animated_content = Container(css_class="fade-in-up")
```

## Accessibility Compliance Checker

### AccessibilityChecker Component

Built-in accessibility analysis and compliance reporting:

```python
from html_generator import AccessibilityChecker

# Add accessibility checker to your page
a11y_checker = AccessibilityChecker()
page.add_content(a11y_checker)
```

### Accessibility Features Checked

The AccessibilityChecker automatically analyzes:

1. **Alt Text for Images**: Ensures all images have descriptive alternative text
2. **Color Contrast**: Verifies WCAG AA contrast ratios (4.5:1 minimum)
3. **Keyboard Navigation**: Checks tab order and focus management
4. **Semantic HTML**: Validates proper heading structure and landmarks
5. **Focus Indicators**: Ensures visible focus states for interactive elements
6. **ARIA Labels**: Verifies screen reader compatibility and proper labeling

### Real-time Accessibility Monitoring

```python
# Enable continuous accessibility monitoring
page.add_custom_js("""
// Real-time accessibility monitoring
class AccessibilityMonitor {
    constructor() {
        this.init();
    }
    
    init() {
        // Monitor DOM changes
        const observer = new MutationObserver(this.checkAccessibility.bind(this));
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['alt', 'aria-label', 'role', 'tabindex']
        });
        
        // Initial check
        this.checkAccessibility();
    }
    
    checkAccessibility() {
        this.checkImageAltText();
        this.checkFormLabels();
        this.checkHeadingStructure();
        this.checkColorContrast();
    }
    
    checkImageAltText() {
        const images = document.querySelectorAll('img:not([alt])');
        if (images.length > 0) {
            console.warn(`${images.length} images missing alt text:`, images);
        }
    }
    
    checkFormLabels() {
        const inputs = document.querySelectorAll('input:not([aria-label]):not([aria-labelledby])');
        const unlabeled = Array.from(inputs).filter(input => 
            !document.querySelector(`label[for="${input.id}"]`)
        );
        
        if (unlabeled.length > 0) {
            console.warn(`${unlabeled.length} form inputs missing labels:`, unlabeled);
        }
    }
    
    checkHeadingStructure() {
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        const levels = Array.from(headings).map(h => parseInt(h.tagName.charAt(1)));
        
        // Check for proper hierarchy
        for (let i = 1; i < levels.length; i++) {
            if (levels[i] - levels[i-1] > 1) {
                console.warn('Heading structure issue: skipping levels', headings[i]);
            }
        }
    }
    
    checkColorContrast() {
        // Simplified contrast checking
        const elements = document.querySelectorAll('*');
        elements.forEach(el => {
            const style = getComputedStyle(el);
            const color = style.color;
            const background = style.backgroundColor;
            
            // Basic contrast ratio check would go here
            // This is a simplified version
        });
    }
}

// Initialize accessibility monitor
document.addEventListener('DOMContentLoaded', () => {
    new AccessibilityMonitor();
});
""")
```

### Accessibility Best Practices

```python
# Create accessible components by default
def create_accessible_button(text, action, primary=False):
    """Create an accessible button with proper attributes"""
    btn_class = "btn btn-primary" if primary else "btn btn-secondary"
    button = Button(text, "button", css_class=btn_class)
    
    # Add accessibility attributes
    button.set_attribute("aria-label", f"{text} button")
    button.set_attribute("role", "button")
    
    if action:
        button.set_attribute("onclick", action)
    
    return button

def create_accessible_form_field(field_type, name, label, required=False):
    """Create an accessible form field with proper labeling"""
    field_id = f"field_{name}"
    
    # Create label
    label_element = Element("label", content=label, attributes={
        "for": field_id,
        "class": "form-label"
    })
    
    # Create input
    input_element = Element("input", attributes={
        "type": field_type,
        "id": field_id,
        "name": name,
        "class": "form-control"
    })
    
    if required:
        input_element.set_attribute("required", "true")
        input_element.set_attribute("aria-required", "true")
        label_element.content += " *"
    
    # Create container
    container = Container(css_class="mb-3")
    container.add_content(label_element)
    container.add_content(input_element)
    
    return container

# Usage
accessible_button = create_accessible_button("Submit Form", "submitForm()", primary=True)
accessible_field = create_accessible_form_field("email", "user_email", "Email Address", required=True)
```

## Component Integration Examples

### Complete Dashboard

```python
def create_analytics_dashboard():
    """Create a complete analytics dashboard with modern components"""
    
    # Dashboard container
    dashboard = Container(css_class="dashboard container-fluid")
    
    # Header section
    header = Container(css_class="dashboard-header d-flex justify-content-between align-items-center mb-4")
    header.add_content(Heading("Analytics Dashboard", 1, css_class="h3 mb-0"))
    
    # Refresh button with micro-interaction
    refresh_btn = Button("Refresh Data", "button", css_class="btn btn-outline-primary")
    interactive_refresh = MicroInteraction(refresh_btn, 'click', 'pulse')
    header.add_content(interactive_refresh)
    
    dashboard.add_content(header)
    
    # Key metrics row
    metrics_row = Container(css_class="row mb-4")
    
    metrics = [
        {"title": "Total Revenue", "value": "$125,430", "change": "+12.5%", "color": "success"},
        {"title": "Active Users", "value": "2,847", "change": "+8.2%", "color": "info"},
        {"title": "Conversion Rate", "value": "3.24%", "change": "-2.1%", "color": "warning"},
        {"title": "Avg. Order Value", "value": "$89.32", "change": "+15.3%", "color": "success"}
    ]
    
    for metric in metrics:
        col = Container(css_class="col-md-3 mb-3")
        
        card = Card(
            title=metric["title"],
            content=f"""
                <div class="h2 text-{metric['color']} mb-1">{metric['value']}</div>
                <small class="text-{metric['color']}">{metric['change']} from last month</small>
            """,
            css_class="card h-100 border-0 shadow-sm"
        )
        
        # Add hover animation
        animated_card = MicroInteraction(card, 'hover', 'glow')
        col.add_content(animated_card)
        metrics_row.add_content(col)
    
    dashboard.add_content(metrics_row)
    
    # Charts section
    charts_row = Container(css_class="row")
    
    # Revenue chart
    revenue_col = Container(css_class="col-lg-8 mb-4")
    revenue_data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'datasets': [{
            'label': 'Revenue',
            'data': [12000, 19000, 15000, 25000, 22000, 30000],
            'borderColor': '#007bff',
            'backgroundColor': 'rgba(0, 123, 255, 0.1)',
            'tension': 0.4
        }]
    }
    
    revenue_chart = InteractiveChart(
        'line', 
        revenue_data, 
        {
            'responsive': True,
            'plugins': {
                'title': {'display': True, 'text': 'Revenue Trend'},
                'legend': {'display': False}
            }
        }
    )
    revenue_col.add_content(revenue_chart)
    
    # User distribution chart
    users_col = Container(css_class="col-lg-4 mb-4")
    users_data = [
        {'label': 'Desktop', 'value': 1890},
        {'label': 'Mobile', 'value': 757},
        {'label': 'Tablet', 'value': 200}
    ]
    
    users_chart = DataVisualization(
        users_data,
        'doughnut',
        'User Distribution'
    )
    users_col.add_content(users_chart)
    
    charts_row.add_content(revenue_col)
    charts_row.add_content(users_col)
    dashboard.add_content(charts_row)
    
    # Add accessibility checker
    a11y_checker = AccessibilityChecker()
    dashboard.add_content(a11y_checker)
    
    return dashboard

# Use the dashboard
dashboard = create_analytics_dashboard()
page.add_content(dashboard)
```

### Interactive Contact Section

```python
def create_contact_section():
    """Create an interactive contact section with modern components"""
    
    section = Section(css_class="contact-section py-5 bg-light")
    container = Container(css_class="container")
    
    # Section header
    header = Container(css_class="text-center mb-5")
    header.add_content(Heading("Get in Touch", 2, css_class="display-5 mb-3"))
    header.add_content(Paragraph(
        "We'd love to hear from you. Send us a message and we'll respond as soon as possible.",
        css_class="lead text-muted"
    ))
    
    container.add_content(header)
    
    # Contact content row
    content_row = Container(css_class="row align-items-start")
    
    # Contact information
    info_col = Container(css_class="col-lg-4 mb-4")
    
    contact_info = Card(
        title="Contact Information",
        content="",
        css_class="card h-100 border-0 shadow"
    )
    
    # Contact details with icons
    contact_details = [
        {"icon": "fas fa-map-marker-alt", "title": "Address", "content": "123 Business St<br>City, State 12345"},
        {"icon": "fas fa-phone", "title": "Phone", "content": "+1 (555) 123-4567"},
        {"icon": "fas fa-envelope", "title": "Email", "content": "contact@example.com"},
        {"icon": "fas fa-clock", "title": "Hours", "content": "Mon - Fri: 9:00 AM - 6:00 PM"}
    ]
    
    for detail in contact_details:
        detail_div = Container(css_class="d-flex mb-3")
        icon_div = Container(css_class="flex-shrink-0 me-3")
        icon_div.add_content(Element("i", css_class=f"{detail['icon']} fa-lg text-primary"))
        
        content_div = Container()
        content_div.add_content(Heading(detail['title'], 6, css_class="mb-1"))
        content_div.add_content(Element("p", content=detail['content'], css_class="text-muted mb-0"))
        
        detail_div.add_content(icon_div)
        detail_div.add_content(content_div)
        contact_info.add_content(detail_div)
    
    # Add hover animation to contact info
    animated_info = MicroInteraction(contact_info, 'hover', 'glow')
    info_col.add_content(animated_info)
    
    # Contact form
    form_col = Container(css_class="col-lg-8")
    
    contact_form = AdvancedFormBuilder(form_id='main_contact_form')
    
    # Form fields
    contact_form.add_field('text', 'name', 'Full Name *', 
                          validation={'required': True, 'minLength': 2})
    contact_form.add_field('email', 'email', 'Email Address *', 
                          validation={'required': True, 'email': True})
    contact_form.add_field('text', 'subject', 'Subject *', 
                          validation={'required': True, 'minLength': 5})
    contact_form.add_field('textarea', 'message', 'Message *', 
                          validation={'required': True, 'minLength': 10},
                          options={'rows': 5})
    
    # Submit button with animation
    submit_btn = Button("Send Message", "submit", css_class="btn btn-primary btn-lg")
    animated_submit = MicroInteraction(submit_btn, 'click', 'pulse')
    
    form_container = Container(css_class="card border-0 shadow")
    form_body = Container(css_class="card-body p-4")
    form_body.add_content(contact_form)
    form_body.add_content(animated_submit)
    form_container.add_content(form_body)
    
    form_col.add_content(form_container)
    
    content_row.add_content(info_col)
    content_row.add_content(form_col)
    container.add_content(content_row)
    section.add_content(container)
    
    return section

# Add to page
contact_section = create_contact_section()
page.add_content(contact_section)
```

## Performance Considerations

### Optimizing Chart Rendering

```python
# Lazy load charts for better performance
chart_container = Container(css_class="chart-container")
chart_container.set_attribute("data-lazy-load", "revenue-chart")

# Add intersection observer for lazy loading
page.add_custom_js("""
const chartObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const container = entry.target;
            const chartType = container.dataset.lazyLoad;
            
            // Load chart data and render
            loadChart(chartType, container);
            chartObserver.unobserve(container);
        }
    });
});

document.querySelectorAll('[data-lazy-load]').forEach(el => {
    chartObserver.observe(el);
});
""")
```

### Form Performance Optimization

```python
# Debounced validation for better performance
page.add_custom_js("""
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounced validation
document.querySelectorAll('.advanced-form input').forEach(input => {
    const debouncedValidate = debounce((e) => {
        validateField(e.target);
    }, 300);
    
    input.addEventListener('input', debouncedValidate);
});
""")
```

## Next Steps

- Explore [Performance Tools](../features/performance.md) for optimization techniques
- Learn about [WebAssembly Integration](../features/webassembly.md) for high-performance rendering
- Study [Accessibility Features](../features/accessibility.md) for inclusive design
- Review [Advanced Examples](../examples/advanced.md) for real-world implementations