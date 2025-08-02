"""
Enhanced HTML Generator Library v3.0.0

This library provides a comprehensive set of components for generating HTML programmatically.
New Features in v3.0:
- Dark mode toggle with system preference support
- Animation and transition support (FadeIn, SlideUp, AnimateOnScroll)
- Visual debug mode for development
- Plugin system for extensibility
- Export capabilities (PDF and JSON)
- Enhanced components and styling
"""

# Core elements
from .page import Page, Heading
from .elements import Element, Paragraph, HtmlList, Image, Link, Div, Section, Card, Container
from .css import CSSBuilder, Style

# Enhanced forms
from .forms import Form, Input, Button, Select, TextArea

# Layout system
from .layout import Row, Column, Flex

# Templates
from .templates import Template, Slot, TemplateManager, create_hero_template, create_card_grid_template, create_footer_template

# Advanced components
from .components import (ComponentBase, HeroSection, FeatureCard, Navbar, Alert, Badge, 
                        ProgressBar, Accordion, Modal)

# Professional UI Components
from .advanced_components import Table, Tabs, Carousel, Breadcrumb, Pagination, Toast, Rating, Avatar

# Data Visualization
from .data_visualization import Chart, BarChart, LineChart, PieChart, DoughnutChart, Dashboard, SparklineChart, KPICard

# Advanced Forms
from .forms_advanced import FileUpload, DateTimePicker, FormWizard, FormValidation, SearchableSelect

# New Features - Animations
from .animations import FadeIn, SlideUp, AnimateOnScroll, Pulse, Animation

# New Features - Dark mode
from .dark_mode import DarkModeToggle, ThemeProvider, create_auto_dark_mode

# New Features - Debug tools
from .debug_tools import enable_debug_view, disable_debug_view, get_debug_css, get_debug_js, DebugWrapper

# New Features - Plugin system
from .plugins import (
    register_component, register_template, register_hook, register_filter,
    plugin_registry, Timeline, StatCard, CodeBlock
)

# New Features - Export tools
from .export_tools import (
    to_dict, from_dict, to_json, from_json, to_pdf, check_pdf_support,
    ExportManager, SerializableMixin
)

__version__ = "3.0.0"

__all__ = [
    # Core
    'Page', 'Heading', 'Element', 'Paragraph', 'HtmlList', 'Image', 'Link', 'Div', 'Section',
    'Card', 'Container', 'CSSBuilder', 'Style',
    
    # Forms
    'Form', 'Input', 'Button', 'Select', 'TextArea',
    
    # Layout
    'Row', 'Column', 'Flex',
    
    # Templates
    'Template', 'Slot', 'TemplateManager', 'create_hero_template', 
    'create_card_grid_template', 'create_footer_template',
    
    # Components
    'ComponentBase', 'HeroSection', 'FeatureCard', 'Navbar', 'Alert', 'Badge', 
    'ProgressBar', 'Accordion', 'Modal',
    
    # Professional UI Components
    'Table', 'Tabs', 'Carousel', 'Breadcrumb', 'Pagination', 'Toast', 'Rating', 'Avatar',
    
    # Data Visualization
    'Chart', 'BarChart', 'LineChart', 'PieChart', 'DoughnutChart', 'Dashboard', 
    'SparklineChart', 'KPICard',
    
    # Advanced Forms
    'FileUpload', 'DateTimePicker', 'FormWizard', 'FormValidation', 'SearchableSelect',
    
    # Animations
    'FadeIn', 'SlideUp', 'AnimateOnScroll', 'Pulse', 'Animation',
    
    # Dark mode
    'DarkModeToggle', 'ThemeProvider', 'create_auto_dark_mode',
    
    # Debug tools
    'enable_debug_view', 'disable_debug_view', 'get_debug_css', 'get_debug_js', 'DebugWrapper',
    
    # Plugin system
    'register_component', 'register_template', 'register_hook', 'register_filter',
    'plugin_registry', 'Timeline', 'StatCard', 'CodeBlock',
    
    # Export tools
    'to_dict', 'from_dict', 'to_json', 'from_json', 'to_pdf', 'check_pdf_support',
    'ExportManager', 'SerializableMixin'
]
