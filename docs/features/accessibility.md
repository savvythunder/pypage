# Accessibility Features

HTML Generator v3.0 includes comprehensive accessibility features to ensure your web applications are inclusive and compliant with WCAG 2.1 guidelines. This guide covers all accessibility tools and best practices.

## Accessibility Checker Component

### Built-in Accessibility Analysis

```python
from html_generator import AccessibilityChecker

# Add accessibility checker to your page
a11y_checker = AccessibilityChecker()
page.add_content(a11y_checker)
```

### Features Checked

1. **Alt Text for Images**: Ensures all images have descriptive alternative text
2. **Color Contrast**: Verifies WCAG AA contrast ratios (4.5:1 for normal text)
3. **Keyboard Navigation**: Checks tab order and focus management
4. **Semantic HTML**: Validates proper heading structure and landmarks
5. **Focus Indicators**: Ensures visible focus states for interactive elements
6. **ARIA Labels**: Verifies screen reader compatibility

### Real-time Analysis

The accessibility checker provides:
- **Live scoring**: Real-time accessibility score (0-100%)
- **Detailed reports**: Specific issues with line numbers
- **Actionable recommendations**: Clear steps to fix problems
- **Priority levels**: High, medium, and low priority issues

## Semantic HTML Structure

### Proper Heading Hierarchy

```python
# Correct heading structure
page.add_content(Heading("Main Page Title", level=1))  # H1 - only one per page
page.add_content(Heading("Section Title", level=2))    # H2 - main sections
page.add_content(Heading("Subsection", level=3))       # H3 - subsections

# Avoid skipping levels
# ❌ Don't jump from H1 to H3
# ✅ Use proper hierarchy: H1 → H2 → H3
```

### Landmark Elements

```python
# Use semantic HTML landmarks
header = Element('header', content=[
    Navbar(brand="My App", items=[...])
])

main_content = Element('main', content=[
    Element('section', content=[
        Heading("Welcome", level=1),
        Paragraph("Main content here...")
    ])
])

sidebar = Element('aside', content=[
    Heading("Related Links", level=2),
    # Sidebar content
])

footer = Element('footer', content=[
    Paragraph("© 2025 My Company")
])

page.add_content(header)
page.add_content(main_content)
page.add_content(sidebar)
page.add_content(footer)
```

## ARIA Labels and Roles

### Adding ARIA Attributes

```python
# Interactive elements with ARIA labels
button = Button("Submit Form", button_type="submit")
button.set_attribute("aria-label", "Submit contact form")
button.set_attribute("aria-describedby", "form-help-text")

# Form inputs with labels
form = AdvancedFormBuilder()
form.add_field(
    field_type='email',
    name='email',
    label='Email Address',
    options={
        'aria-required': 'true',
        'aria-describedby': 'email-help'
    }
)

# Help text with proper ID
help_text = Paragraph("We'll never share your email address", css_class="form-text")
help_text.set_attribute("id", "email-help")
```

### Common ARIA Patterns

```python
# Modal dialogs
modal = Modal("Important Notice", "Critical information")
modal.set_attribute("role", "dialog")
modal.set_attribute("aria-modal", "true")
modal.set_attribute("aria-labelledby", "modal-title")
modal.set_attribute("aria-describedby", "modal-content")

# Tab navigation
tabs = Tabs([
    {"title": "Tab 1", "content": "Content 1"},
    {"title": "Tab 2", "content": "Content 2"}
])
tabs.set_attribute("role", "tablist")

# Expandable content
accordion = Accordion([
    {"title": "Section 1", "content": "Expandable content"}
])
accordion.set_attribute("aria-expanded", "false")
```

## Keyboard Navigation

### Focus Management

```python
# Ensure proper tab order
form_container = Container()

# Skip link for keyboard users
skip_link = Link("#main-content", "Skip to main content", css_class="visually-hidden-focusable")
form_container.add_content(skip_link)

# Proper tab order with tabindex
input1 = Input("text", "first_name", tabindex=1)
input2 = Input("text", "last_name", tabindex=2)
submit_btn = Button("Submit", "submit", tabindex=3)

form_container.add_content(input1)
form_container.add_content(input2)
form_container.add_content(submit_btn)
```

### Custom Focus Styles

```python
# Add focus-visible styles
page.add_custom_css("""
/* High contrast focus indicators */
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
    outline: 3px solid #005fcc;
    outline-offset: 2px;
}

/* Skip link styling */
.visually-hidden-focusable {
    position: absolute !important;
    width: 1px !important;
    height: 1px !important;
    overflow: hidden !important;
    clip: rect(1px, 1px, 1px, 1px) !important;
    white-space: nowrap !important;
}

.visually-hidden-focusable:focus {
    position: static !important;
    width: auto !important;
    height: auto !important;
    overflow: visible !important;
    clip: auto !important;
    white-space: normal !important;
    background: #000;
    color: #fff;
    padding: 0.5rem;
    text-decoration: none;
}
""")
```

## Color and Contrast

### WCAG Contrast Compliance

```python
# High contrast color scheme
page.add_custom_css("""
/* WCAG AA compliant colors */
.high-contrast {
    background-color: #ffffff;  /* White background */
    color: #212529;             /* Dark text (21:1 ratio) */
}

.primary-button {
    background-color: #0056b3;  /* Blue with 4.5:1 ratio on white */
    color: #ffffff;
    border: 2px solid #0056b3;
}

.warning-text {
    background-color: #fff3cd;  /* Light yellow background */
    color: #856404;             /* Dark brown text (7:1 ratio) */
    border: 1px solid #ffeaa7;
}

.error-text {
    background-color: #f8d7da;  /* Light red background */
    color: #721c24;             /* Dark red text (4.8:1 ratio) */
}
""")
```

### Color-blind Friendly Design

```python
# Use patterns and icons, not just color
def create_status_indicator(status, message):
    container = Container(css_class=f"status-{status}")
    
    # Icon for visual indication
    if status == 'success':
        icon = Element('i', css_class="fas fa-check-circle", attributes={'aria-hidden': 'true'})
    elif status == 'warning':
        icon = Element('i', css_class="fas fa-exclamation-triangle", attributes={'aria-hidden': 'true'})
    elif status == 'error':
        icon = Element('i', css_class="fas fa-times-circle", attributes={'aria-hidden': 'true'})
    
    # Text description for screen readers
    sr_text = Element('span', content=f"{status.title()}: ", css_class="visually-hidden")
    
    container.add_content(icon)
    container.add_content(sr_text)
    container.add_content(Paragraph(message))
    
    return container

# Usage
success_msg = create_status_indicator('success', 'Form submitted successfully')
```

## Images and Media

### Descriptive Alt Text

```python
# Informative images with descriptive alt text
chart_image = Image(
    src="sales-chart.png",
    alt="Bar chart showing 25% increase in Q4 sales compared to Q3, with revenue growing from $80K to $100K"
)

# Decorative images
decorative_image = Image(
    src="decorative-border.png",
    alt="",  # Empty alt for decorative images
    attributes={'role': 'presentation'}
)

# Complex images with long descriptions
complex_chart = Image(
    src="detailed-analytics.png",
    alt="Monthly website analytics dashboard",
    attributes={
        'aria-describedby': 'chart-description'
    }
)

# Detailed description
chart_description = Element('div', 
    id="chart-description",
    content="""
    Detailed Analytics Report: 
    Page views increased 40% from January (10K) to December (14K).
    Bounce rate decreased from 65% to 45%.
    Top traffic sources: Organic search (60%), Direct (25%), Social media (15%).
    """
)
```

### Video and Audio Accessibility

```python
# Video with captions and transcript
video_container = Container()

video = Element('video', attributes={
    'controls': 'true',
    'aria-describedby': 'video-transcript'
})

# Add multiple sources
video.add_content(Element('source', attributes={
    'src': 'video.mp4',
    'type': 'video/mp4'
}))

# Captions track
video.add_content(Element('track', attributes={
    'kind': 'captions',
    'src': 'captions.vtt',
    'srclang': 'en',
    'label': 'English captions'
}))

# Transcript
transcript = Element('details', content=[
    Element('summary', content="Video Transcript"),
    Element('p', content="[Full video transcript content here...]")
])
transcript.set_attribute('id', 'video-transcript')

video_container.add_content(video)
video_container.add_content(transcript)
```

## Forms Accessibility

### Accessible Form Design

```python
# Create accessible form
accessible_form = AdvancedFormBuilder(form_id='contact_form')

# Required field with proper labeling
accessible_form.add_field(
    field_type='text',
    name='full_name',
    label='Full Name *',
    validation={'required': True},
    options={
        'aria-required': 'true',
        'aria-describedby': 'name-help'
    }
)

# Help text
name_help = Paragraph("Enter your first and last name", css_class="form-text")
name_help.set_attribute('id', 'name-help')

# Error handling
accessible_form.add_field(
    field_type='email',
    name='email',
    label='Email Address *',
    validation={'required': True, 'email': True},
    options={
        'aria-required': 'true',
        'aria-describedby': 'email-help email-error',
        'aria-invalid': 'false'  # Will be updated by validation
    }
)

# Fieldset for grouped inputs
personal_info = Element('fieldset', content=[
    Element('legend', content="Personal Information"),
    # Form fields here
])
```

### Form Validation Accessibility

```python
# Add custom validation with accessibility
page.add_custom_js("""
function validateAccessibleForm(form) {
    const errors = [];
    
    // Validate each field
    form.querySelectorAll('[aria-required="true"]').forEach(field => {
        if (!field.value.trim()) {
            errors.push({
                field: field,
                message: `${field.labels[0].textContent} is required`
            });
        }
    });
    
    // Display errors accessibly
    errors.forEach(error => {
        const errorElement = document.getElementById(error.field.name + '-error');
        if (errorElement) {
            errorElement.textContent = error.message;
            error.field.setAttribute('aria-invalid', 'true');
            error.field.setAttribute('aria-describedby', 
                error.field.getAttribute('aria-describedby') + ' ' + errorElement.id
            );
        }
    });
    
    // Announce errors to screen readers
    if (errors.length > 0) {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'polite');
        announcement.textContent = `${errors.length} error(s) found. Please review the form.`;
        document.body.appendChild(announcement);
        
        // Focus first error field
        errors[0].field.focus();
        
        // Remove announcement after delay
        setTimeout(() => announcement.remove(), 3000);
    }
    
    return errors.length === 0;
}
""")
```

## Screen Reader Support

### ARIA Live Regions

```python
# Status announcements
status_region = Element('div', attributes={
    'aria-live': 'polite',
    'aria-atomic': 'true',
    'id': 'status-announcements',
    'class': 'visually-hidden'
})

# Dynamic content updates
def announce_status(message):
    return f"""
    document.getElementById('status-announcements').textContent = '{message}';
    """

# Usage in interactive components
save_button = Button("Save Changes", "button")
save_button.set_attribute("onclick", f"""
    // Save logic here
    {announce_status('Changes saved successfully')}
""")
```

### Screen Reader Testing

```python
# Add screen reader testing utilities
def add_screen_reader_debug():
    """Add debugging info for screen reader testing"""
    
    debug_info = Element('div', attributes={
        'id': 'sr-debug',
        'class': 'visually-hidden',
        'aria-live': 'assertive'
    })
    
    # JavaScript to help with testing
    debug_script = """
    // Screen reader debugging
    function debugScreenReader() {
        const focusedElement = document.activeElement;
        const debugDiv = document.getElementById('sr-debug');
        
        if (focusedElement && debugDiv) {
            const info = [
                `Tag: ${focusedElement.tagName}`,
                `Text: ${focusedElement.textContent || focusedElement.value || 'No text'}`,
                `ARIA Label: ${focusedElement.getAttribute('aria-label') || 'None'}`,
                `Role: ${focusedElement.getAttribute('role') || 'Default'}`,
                `Described by: ${focusedElement.getAttribute('aria-describedby') || 'None'}`
            ].join(' | ');
            
            debugDiv.textContent = info;
        }
    }
    
    // Add focus listener for debugging
    document.addEventListener('focus', debugScreenReader, true);
    """
    
    return debug_info, debug_script
```

## Mobile Accessibility

### Touch Target Sizing

```python
# Ensure adequate touch target sizes (44px minimum)
page.add_custom_css("""
/* Minimum touch target sizes */
button,
input[type="button"],
input[type="submit"],
input[type="reset"],
.btn {
    min-height: 44px;
    min-width: 44px;
    padding: 12px 16px;
}

/* Touch-friendly form controls */
input[type="text"],
input[type="email"],
input[type="password"],
select,
textarea {
    min-height: 44px;
    padding: 12px;
    font-size: 16px; /* Prevents zoom on iOS */
}

/* Adequate spacing between interactive elements */
.form-group + .form-group {
    margin-top: 16px;
}

button + button,
.btn + .btn {
    margin-left: 8px;
}
""")
```

### Responsive Font Sizes

```python
# Scalable, accessible typography
page.add_custom_css("""
/* Responsive, accessible font sizes */
html {
    font-size: 100%; /* 16px base */
}

body {
    font-size: 1rem;
    line-height: 1.5;
}

h1 { font-size: clamp(1.75rem, 4vw, 2.5rem); }
h2 { font-size: clamp(1.5rem, 3.5vw, 2rem); }
h3 { font-size: clamp(1.25rem, 3vw, 1.75rem); }

/* High contrast mode support */
@media (prefers-contrast: high) {
    body {
        background: #ffffff;
        color: #000000;
    }
    
    button, .btn {
        border: 2px solid currentColor;
    }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
""")
```

## Testing and Validation

### Automated Testing

```python
# Accessibility testing with the checker component
def run_accessibility_tests(page):
    """Run comprehensive accessibility tests"""
    
    a11y_checker = AccessibilityChecker()
    results = a11y_checker.analyze_page(page)
    
    # Generate report
    report = {
        'score': results['score'],
        'issues': results['issues'],
        'recommendations': results['recommendations'],
        'timestamp': datetime.now().isoformat()
    }
    
    return report

# Integration with testing framework
def test_page_accessibility():
    page = create_test_page()
    results = run_accessibility_tests(page)
    
    assert results['score'] >= 80, f"Accessibility score too low: {results['score']}"
    
    # Check for critical issues
    critical_issues = [issue for issue in results['issues'] if issue['severity'] == 'high']
    assert len(critical_issues) == 0, f"Critical accessibility issues found: {critical_issues}"
```

### Manual Testing Checklist

```python
# Manual testing guidelines
accessibility_checklist = """
Manual Accessibility Testing Checklist:

□ Keyboard Navigation
  - Tab through all interactive elements
  - Ensure logical tab order
  - All functionality available via keyboard
  - Visible focus indicators

□ Screen Reader Testing
  - Test with NVDA, JAWS, or VoiceOver
  - Verify proper heading structure
  - Check ARIA labels and descriptions
  - Ensure form labels are announced

□ Visual Testing
  - Test at 200% zoom
  - Check color contrast ratios
  - Verify without color (grayscale)
  - Test with high contrast mode

□ Mobile Testing
  - Touch targets at least 44px
  - Readable text without zooming
  - Proper viewport configuration
  - Gesture accessibility

□ Cognitive Accessibility
  - Clear, simple language
  - Consistent navigation
  - Error prevention and recovery
  - Sufficient time for tasks
"""

print(accessibility_checklist)
```

## Best Practices Summary

### Do's ✅

1. **Use semantic HTML**: Proper elements for their intended purpose
2. **Provide alternative text**: Descriptive alt text for images
3. **Ensure keyboard access**: All functionality via keyboard
4. **Use sufficient contrast**: Meet WCAG AA standards (4.5:1)
5. **Label form controls**: Explicit labels for all inputs
6. **Structure content**: Logical heading hierarchy
7. **Test with users**: Include people with disabilities in testing

### Don'ts ❌

1. **Don't rely on color alone**: Use icons, patterns, or text
2. **Don't use placeholder as label**: Provide proper labels
3. **Don't auto-play media**: Require user interaction
4. **Don't use tiny text**: Minimum 12px font size
5. **Don't skip heading levels**: Maintain logical hierarchy
6. **Don't use generic link text**: Avoid "click here" or "read more"
7. **Don't ignore focus order**: Ensure logical tab sequence

## Next Steps

- Explore [Modern UI Components](./modern-ui.md) with accessibility in mind
- Review [Performance Optimization](./performance.md) for accessible performance
- Check [Advanced Examples](../examples/advanced.md) for accessible implementations
- Study [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) for comprehensive standards