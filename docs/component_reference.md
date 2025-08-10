# PyPage Component Reference

Complete documentation for all PyPage components with attributes, methods, and usage examples.

## Table of Contents

1. [Core Components](#core-components)
2. [Layout Components](#layout-components)
3. [Form Components](#form-components)
4. [UI Components](#ui-components)
5. [Advanced Components](#advanced-components)
6. [Data Visualization](#data-visualization)
7. [Animation Components](#animation-components)
8. [Utility Components](#utility-components)

## Core Components

### Page

The main container for all HTML content with theme and configuration support.

**Constructor:**
```python
Page(title: str, description: str = "", theme: str = "bootstrap", lang: str = "en")
```

**Attributes:**
- `title` (str): Page title displayed in browser tab
- `description` (str): Meta description for SEO
- `theme` (str): CSS theme ('bootstrap', 'material', 'tailwind', 'bulma')
- `lang` (str): Page language code
- `content` (list): List of page content elements
- `navbar` (Navbar): Navigation bar component
- `custom_css` (str): Additional CSS styles
- `custom_js` (str): Additional JavaScript code

**Methods:**
- `add_content(element)`: Add content to the page
- `add_navbar(links)`: Add navigation bar with links
- `set_theme(theme_name)`: Change page theme
- `generate_html()`: Generate complete HTML output
- `save_to_file(filename)`: Save HTML to file
- `run(port=8000)`: Start development server
- `enable_debug_view()`: Enable visual debugging mode
- `to_json()`: Serialize page to JSON
- `to_pdf(filename)`: Export page as PDF

**Example:**
```python
page = Page("My Website", "Welcome to my site", theme="bootstrap")
page.add_content(Heading("Welcome", 1))
page.add_content(Paragraph("This is my website."))
html = page.generate_html()
```

### Container

A wrapper element for organizing content with responsive layout support.

**Constructor:**
```python
Container(content: list = None, fluid: bool = False, css_class: str = "", style: dict = None)
```

**Attributes:**
- `content` (list): Child elements
- `fluid` (bool): Use full-width container
- `css_class` (str): CSS classes
- `style` (dict): Inline styles

**Methods:**
- `add_content(element)`: Add child element
- `set_fluid(fluid)`: Set container width mode

**Example:**
```python
container = Container([
    Heading("Section Title", 2),
    Paragraph("Section content here.")
], fluid=True)
```

### Element

Base class for all HTML elements with common functionality.

**Constructor:**
```python
Element(tag: str, content: str = "", attributes: dict = None, css_class: str = "", style: dict = None)
```

**Attributes:**
- `tag` (str): HTML tag name
- `content` (str): Element content
- `attributes` (dict): HTML attributes
- `css_class` (str): CSS classes
- `style` (dict): Inline styles

**Methods:**
- `add_class(class_name)`: Add CSS class
- `add_style(property, value)`: Add inline style
- `set_attribute(name, value)`: Set HTML attribute
- `render()`: Generate HTML string

## Layout Components

### Row

Bootstrap grid row for responsive layout.

**Constructor:**
```python
Row(columns: list = None, css_class: str = "", style: dict = None)
```

**Attributes:**
- `columns` (list): Column components
- `css_class` (str): Additional CSS classes
- `style` (dict): Inline styles

**Methods:**
- `add_column(column)`: Add column to row
- `set_gutter(size)`: Set column spacing

**Example:**
```python
row = Row()
row.add_column(Column([Heading("Left", 3)], width="md-6"))
row.add_column(Column([Heading("Right", 3)], width="md-6"))
```

### Column

Bootstrap grid column with responsive width options.

**Constructor:**
```python
Column(content: list = None, width: str = "12", css_class: str = "", style: dict = None)
```

**Attributes:**
- `content` (list): Column content
- `width` (str): Bootstrap column width (e.g., "md-6", "lg-4")
- `css_class` (str): Additional CSS classes
- `style` (dict): Inline styles

**Methods:**
- `add_content(element)`: Add content to column
- `set_width(width)`: Set responsive width

### Flex

Flexbox container for advanced layout control.

**Constructor:**
```python
Flex(content: list = None, direction: str = "row", justify: str = "start", align: str = "start", wrap: bool = False)
```

**Attributes:**
- `content` (list): Flex items
- `direction` (str): Flex direction ('row', 'column', 'row-reverse', 'column-reverse')
- `justify` (str): Justify content ('start', 'center', 'end', 'between', 'around', 'evenly')
- `align` (str): Align items ('start', 'center', 'end', 'stretch', 'baseline')
- `wrap` (bool): Allow flex wrap

**Example:**
```python
flex = Flex([
    Div("Item 1"),
    Div("Item 2"),
    Div("Item 3")
], direction="row", justify="between", align="center")
```

## Form Components

### Form

HTML form container with validation support.

**Constructor:**
```python
Form(action: str = "", method: str = "POST", fields: list = None, css_class: str = "")
```

**Attributes:**
- `action` (str): Form submission URL
- `method` (str): HTTP method ('GET', 'POST')
- `fields` (list): Form field elements
- `css_class` (str): CSS classes
- `validation` (bool): Enable client-side validation

**Methods:**
- `add_field(field)`: Add form field
- `add_validation(field_name, rules)`: Add validation rules
- `set_submit_handler(handler)`: Set JavaScript submit handler

### Input

HTML input element with various types and validation.

**Constructor:**
```python
Input(name: str, input_type: str = "text", placeholder: str = "", value: str = "", required: bool = False)
```

**Attributes:**
- `name` (str): Input name attribute
- `input_type` (str): Input type ('text', 'email', 'password', 'number', 'date', etc.)
- `placeholder` (str): Placeholder text
- `value` (str): Default value
- `required` (bool): Required field
- `validation_rules` (dict): Client-side validation rules

**Methods:**
- `add_validation(rule_type, value)`: Add validation rule
- `set_pattern(pattern)`: Set validation pattern

**Example:**
```python
email_input = Input("email", "email", placeholder="Enter your email", required=True)
email_input.add_validation("email", True)
```

### TextArea

Multi-line text input element.

**Constructor:**
```python
TextArea(name: str, placeholder: str = "", rows: int = 4, cols: int = 50, value: str = "")
```

**Attributes:**
- `name` (str): Textarea name
- `placeholder` (str): Placeholder text
- `rows` (int): Number of rows
- `cols` (int): Number of columns
- `value` (str): Default content

### Select

Dropdown selection element with single or multiple selection.

**Constructor:**
```python
Select(name: str, options: list, selected: str = "", multiple: bool = False)
```

**Attributes:**
- `name` (str): Select name
- `options` (list): Option values and labels
- `selected` (str/list): Selected value(s)
- `multiple` (bool): Allow multiple selection

**Methods:**
- `add_option(value, label)`: Add option
- `set_selected(value)`: Set selected option

## UI Components

### Card

Bootstrap card component for content organization.

**Constructor:**
```python
Card(content: list = None, title: str = "", css_class: str = "", style: dict = None)
```

**Attributes:**
- `content` (list): Card content
- `title` (str): Card title
- `header` (str): Card header
- `footer` (str): Card footer
- `css_class` (str): CSS classes
- `style` (dict): Inline styles

**Methods:**
- `set_header(header)`: Set card header
- `set_footer(footer)`: Set card footer
- `add_content(element)`: Add content to card body

### Modal

Bootstrap modal dialog component.

**Constructor:**
```python
Modal(modal_id: str, title: str, content: list = None, size: str = "md")
```

**Attributes:**
- `modal_id` (str): Unique modal ID
- `title` (str): Modal title
- `content` (list): Modal body content
- `size` (str): Modal size ('sm', 'md', 'lg', 'xl')
- `backdrop` (bool): Backdrop behavior
- `keyboard` (bool): Keyboard close enabled

**Methods:**
- `add_content(element)`: Add content to modal body
- `add_footer_button(button)`: Add button to modal footer
- `set_backdrop(backdrop)`: Set backdrop behavior

### Alert

Bootstrap alert component for notifications.

**Constructor:**
```python
Alert(message: str, alert_type: str = "info", dismissible: bool = False)
```

**Attributes:**
- `message` (str): Alert message
- `alert_type` (str): Alert type ('primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark')
- `dismissible` (bool): Show close button
- `icon` (str): Alert icon class

### Badge

Bootstrap badge component for labels and counters.

**Constructor:**
```python
Badge(text: str, badge_type: str = "secondary", pill: bool = False)
```

**Attributes:**
- `text` (str): Badge text
- `badge_type` (str): Badge type ('primary', 'secondary', 'success', etc.)
- `pill` (bool): Pill-shaped badge

### ProgressBar

Bootstrap progress bar component.

**Constructor:**
```python
ProgressBar(value: int, max_value: int = 100, label: str = "", animated: bool = False, striped: bool = False)
```

**Attributes:**
- `value` (int): Current progress value
- `max_value` (int): Maximum value
- `label` (str): Progress label
- `animated` (bool): Animated progress
- `striped` (bool): Striped appearance
- `color` (str): Progress bar color

## Advanced Components

### Navbar

Navigation bar with responsive design and dropdown support.

**Constructor:**
```python
Navbar(brand: str = "", links: list = None, fixed: str = "", expand: str = "lg")
```

**Attributes:**
- `brand` (str): Brand text or logo
- `links` (list): Navigation links
- `fixed` (str): Fixed position ('top', 'bottom')
- `expand` (str): Responsive breakpoint ('sm', 'md', 'lg', 'xl')
- `dark` (bool): Dark theme
- `bg_color` (str): Background color

**Methods:**
- `add_link(url, text, dropdown=None)`: Add navigation link
- `add_dropdown(text, items)`: Add dropdown menu
- `set_brand(brand, url=None)`: Set brand text/logo

### Table

Responsive table component with sorting and filtering.

**Constructor:**
```python
Table(headers: list, rows: list = None, striped: bool = False, bordered: bool = False, hover: bool = False)
```

**Attributes:**
- `headers` (list): Table headers
- `rows` (list): Table data rows
- `striped` (bool): Striped rows
- `bordered` (bool): Bordered table
- `hover` (bool): Hover effect
- `responsive` (bool): Responsive wrapper
- `sortable` (bool): Sortable columns

**Methods:**
- `add_row(row_data)`: Add table row
- `set_sortable(sortable)`: Enable/disable sorting
- `add_filter(column, filter_type)`: Add column filter

### Tabs

Bootstrap tabs component for content organization.

**Constructor:**
```python
Tabs(tabs: list = None, active_tab: int = 0)
```

**Attributes:**
- `tabs` (list): Tab items with title and content
- `active_tab` (int): Active tab index
- `fade` (bool): Fade transition effect

**Methods:**
- `add_tab(title, content)`: Add new tab
- `set_active(index)`: Set active tab

### Accordion

Bootstrap accordion component for collapsible content.

**Constructor:**
```python
Accordion(items: list = None, accordion_id: str = None)
```

**Attributes:**
- `items` (list): Accordion items
- `accordion_id` (str): Unique accordion ID
- `flush` (bool): Flush design

**Methods:**
- `add_item(title, content, expanded=False)`: Add accordion item

## Data Visualization

### Chart

Interactive chart component using Chart.js.

**Constructor:**
```python
Chart(chart_id: str, chart_type: str, data: dict, options: dict = None)
```

**Attributes:**
- `chart_id` (str): Unique chart ID
- `chart_type` (str): Chart type ('bar', 'line', 'pie', 'doughnut', 'radar', 'scatter')
- `data` (dict): Chart data
- `options` (dict): Chart configuration options
- `responsive` (bool): Responsive chart

**Methods:**
- `update_data(data)`: Update chart data
- `set_options(options)`: Set chart options

### BarChart

Specialized bar chart component.

**Constructor:**
```python
BarChart(chart_id: str, data: dict, horizontal: bool = False)
```

### LineChart

Specialized line chart component.

**Constructor:**
```python
LineChart(chart_id: str, data: dict, smooth: bool = True)
```

### PieChart

Specialized pie chart component.

**Constructor:**
```python
PieChart(chart_id: str, data: dict, doughnut: bool = False)
```

### KPICard

Key Performance Indicator card with metrics display.

**Constructor:**
```python
KPICard(title: str, value: str, change: str = "", icon: str = "", color: str = "primary")
```

**Attributes:**
- `title` (str): KPI title
- `value` (str): Current value
- `change` (str): Change indicator
- `icon` (str): Icon class
- `color` (str): Card color theme

## Animation Components

### FadeIn

Fade-in animation wrapper.

**Constructor:**
```python
FadeIn(content, duration: int = 500, delay: int = 0)
```

**Attributes:**
- `content`: Content to animate
- `duration` (int): Animation duration in milliseconds
- `delay` (int): Animation delay in milliseconds
- `easing` (str): Animation easing function

### SlideUp

Slide-up animation wrapper.

**Constructor:**
```python
SlideUp(content, duration: int = 500, delay: int = 0, distance: int = 50)
```

**Attributes:**
- `content`: Content to animate
- `duration` (int): Animation duration
- `delay` (int): Animation delay
- `distance` (int): Slide distance in pixels

### AnimateOnScroll

Scroll-triggered animation wrapper.

**Constructor:**
```python
AnimateOnScroll(content, animation: str = "fadeIn", trigger_offset: int = 100)
```

**Attributes:**
- `content`: Content to animate
- `animation` (str): Animation type
- `trigger_offset` (int): Scroll trigger offset
- `repeat` (bool): Repeat animation

### Pulse

Pulse animation for attention.

**Constructor:**
```python
Pulse(content, duration: int = 1000, infinite: bool = True)
```

## Utility Components

### DarkModeToggle

Dark mode toggle switch with system preference detection.

**Constructor:**
```python
DarkModeToggle(position: str = "top-right", persist: bool = True)
```

**Attributes:**
- `position` (str): Toggle position ('top-right', 'top-left', 'bottom-right', 'bottom-left')
- `persist` (bool): Save preference to localStorage
- `auto_detect` (bool): Detect system preference

### Breadcrumb

Navigation breadcrumb component.

**Constructor:**
```python
Breadcrumb(items: list)
```

**Attributes:**
- `items` (list): Breadcrumb items with text and URL

### Pagination

Pagination component for page navigation.

**Constructor:**
```python
Pagination(current_page: int, total_pages: int, base_url: str = "")
```

**Attributes:**
- `current_page` (int): Current page number
- `total_pages` (int): Total number of pages
- `base_url` (str): Base URL for page links
- `show_first_last` (bool): Show first/last page links

### Spinner

Loading spinner component.

**Constructor:**
```python
Spinner(size: str = "md", color: str = "primary", text: str = "")
```

**Attributes:**
- `size` (str): Spinner size ('sm', 'md', 'lg')
- `color` (str): Spinner color
- `text` (str): Loading text

## CSS Builder

### CSSBuilder

Programmatic CSS generation with responsive breakpoints.

**Constructor:**
```python
CSSBuilder()
```

**Methods:**
- `add_rule(selector, properties)`: Add CSS rule
- `responsive_breakpoints(selector, **breakpoints)`: Add responsive rules
- `add_keyframes(name, frames)`: Add CSS animation keyframes
- `add_media_query(query, rules)`: Add media query
- `render()`: Generate CSS string

**Example:**
```python
css = CSSBuilder()
css.add_rule('.custom-button', {
    'background': 'linear-gradient(45deg, #007bff, #6610f2)',
    'border': 'none',
    'color': 'white',
    'padding': '10px 20px',
    'border-radius': '5px'
})
css.responsive_breakpoints('.custom-button', 
    sm={'padding': '8px 16px'},
    md={'padding': '10px 20px'},
    lg={'padding': '12px 24px'}
)
```

This comprehensive reference covers all PyPage components with their attributes, methods, and usage examples. Each component is designed to be intuitive while providing powerful customization options for creating modern, responsive web interfaces.