"""
Modern UI Components for HTML Generator
Provides interactive charts, advanced forms, and modern UI elements
"""

from .elements import Element
from .components import ComponentBase
import json


class InteractiveChart(ComponentBase):
    """Interactive chart component using Chart.js"""
    
    def __init__(self, chart_type='bar', data=None, options=None, canvas_id=None, **kwargs):
        super().__init__(**kwargs)
        self.chart_type = chart_type
        self.data = data or {}
        self.options = options or {}
        self.canvas_id = canvas_id or f"chart_{id(self)}"
        
    def render(self):
        chart_config = {
            'type': self.chart_type,
            'data': self.data,
            'options': {
                'responsive': True,
                'maintainAspectRatio': False,
                **self.options
            }
        }
        
        return f'''<div class="chart-container {self.css_class}" style="position: relative; height: 400px; {self.style}">
    <canvas id="{self.canvas_id}"></canvas>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const ctx = document.getElementById('{self.canvas_id}').getContext('2d');
    new Chart(ctx, {json.dumps(chart_config)});
}});
</script>'''


class DataVisualization(ComponentBase):
    """Advanced data visualization with multiple chart types"""
    
    def __init__(self, data, chart_type='line', title='', **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.chart_type = chart_type
        self.title = title
        
    def render(self):
        chart_id = f"viz_{id(self)}"
        
        # Prepare data for different chart types
        if isinstance(self.data, list) and len(self.data) > 0:
            if isinstance(self.data[0], dict):
                labels = [item.get('label', str(i)) for i, item in enumerate(self.data)]
                values = [item.get('value', 0) for item in self.data]
            else:
                labels = [str(i) for i in range(len(self.data))]
                values = self.data
        else:
            labels = []
            values = []
            
        chart_data = {
            'labels': labels,
            'datasets': [{
                'label': self.title,
                'data': values,
                'backgroundColor': [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                'borderColor': [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 205, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                'borderWidth': 1
            }]
        }
        
        return f'''<div class="data-visualization {self.css_class}" style="{self.style}">
    {f'<h3 class="mb-3">{self.title}</h3>' if self.title else ''}
    <div style="position: relative; height: 400px;">
        <canvas id="{chart_id}"></canvas>
    </div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const ctx = document.getElementById('{chart_id}').getContext('2d');
    new Chart(ctx, {{
        type: '{self.chart_type}',
        data: {json.dumps(chart_data)},
        options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
                legend: {{
                    position: 'top',
                }},
                title: {{
                    display: false
                }}
            }}
        }}
    }});
}});
</script>'''


class AdvancedFormBuilder(ComponentBase):
    """Advanced form builder with validation and modern inputs"""
    
    def __init__(self, form_id=None, **kwargs):
        super().__init__(**kwargs)
        self.form_id = form_id or f"form_{id(self)}"
        self.fields = []
        self.validation_rules = {}
        
    def add_field(self, field_type, name, label='', options=None, validation=None):
        """Add a field to the form"""
        field = {
            'type': field_type,
            'name': name,
            'label': label,
            'options': options or {},
            'validation': validation or {}
        }
        self.fields.append(field)
        if validation:
            self.validation_rules[name] = validation
        return self
        
    def render_field(self, field):
        """Render individual form field"""
        field_type = field['type']
        name = field['name']
        label = field['label']
        options = field['options']
        validation = field['validation']
        
        # Common attributes
        required = 'required' if validation.get('required') else ''
        css_class = f"form-control {options.get('css_class', '')}"
        
        # Field wrapper
        wrapper_start = f'<div class="mb-3 form-field" data-field="{name}">'
        label_html = f'<label for="{name}" class="form-label">{label}</label>' if label else ''
        wrapper_end = '</div>'
        
        # Generate field based on type
        if field_type == 'text':
            field_html = f'<input type="text" class="{css_class}" id="{name}" name="{name}" {required}>'
        elif field_type == 'email':
            field_html = f'<input type="email" class="{css_class}" id="{name}" name="{name}" {required}>'
        elif field_type == 'password':
            field_html = f'<input type="password" class="{css_class}" id="{name}" name="{name}" {required}>'
        elif field_type == 'textarea':
            rows = options.get('rows', 3)
            field_html = f'<textarea class="{css_class}" id="{name}" name="{name}" rows="{rows}" {required}></textarea>'
        elif field_type == 'select':
            select_options = options.get('options', [])
            options_html = ''
            for opt in select_options:
                if isinstance(opt, dict):
                    value = opt.get('value', '')
                    text = opt.get('text', value)
                else:
                    value = text = str(opt)
                options_html += f'<option value="{value}">{text}</option>'
            field_html = f'<select class="{css_class}" id="{name}" name="{name}" {required}>{options_html}</select>'
        elif field_type == 'checkbox':
            field_html = f'<div class="form-check"><input class="form-check-input" type="checkbox" id="{name}" name="{name}"><label class="form-check-label" for="{name}">{label}</label></div>'
            label_html = ''  # Label is part of checkbox
        elif field_type == 'radio':
            radio_options = options.get('options', [])
            field_html = '<div class="form-check-group">'
            for i, opt in enumerate(radio_options):
                if isinstance(opt, dict):
                    value = opt.get('value', '')
                    text = opt.get('text', value)
                else:
                    value = text = str(opt)
                radio_id = f"{name}_{i}"
                field_html += f'''
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="{name}" id="{radio_id}" value="{value}" {required}>
                    <label class="form-check-label" for="{radio_id}">{text}</label>
                </div>'''
            field_html += '</div>'
        elif field_type == 'file':
            accept = options.get('accept', '')
            field_html = f'<input type="file" class="{css_class}" id="{name}" name="{name}" accept="{accept}" {required}>'
        elif field_type == 'date':
            field_html = f'<input type="date" class="{css_class}" id="{name}" name="{name}" {required}>'
        elif field_type == 'number':
            min_val = options.get('min', '')
            max_val = options.get('max', '')
            step = options.get('step', '')
            field_html = f'<input type="number" class="{css_class}" id="{name}" name="{name}" min="{min_val}" max="{max_val}" step="{step}" {required}>'
        else:
            field_html = f'<input type="text" class="{css_class}" id="{name}" name="{name}" {required}>'
            
        # Add validation feedback
        feedback_html = f'<div class="invalid-feedback" id="{name}_feedback"></div>'
        
        return wrapper_start + label_html + field_html + feedback_html + wrapper_end
        
    def render(self):
        """Render the complete form"""
        fields_html = ''.join([self.render_field(field) for field in self.fields])
        
        validation_js = f'''
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const form = document.getElementById('{self.form_id}');
    const validationRules = {json.dumps(self.validation_rules)};
    
    // Add real-time validation
    form.addEventListener('input', function(e) {{
        validateField(e.target, validationRules[e.target.name]);
    }});
    
    form.addEventListener('submit', function(e) {{
        let isValid = true;
        Object.keys(validationRules).forEach(fieldName => {{
            const field = form.querySelector(`[name="${{fieldName}}"]`);
            if (field && !validateField(field, validationRules[fieldName])) {{
                isValid = false;
            }}
        }});
        
        if (!isValid) {{
            e.preventDefault();
            e.stopPropagation();
        }}
        
        form.classList.add('was-validated');
    }});
    
    function validateField(field, rules) {{
        if (!rules) return true;
        
        const value = field.value.trim();
        const feedback = document.getElementById(field.name + '_feedback');
        
        // Required validation
        if (rules.required && !value) {{
            showError(field, feedback, 'This field is required');
            return false;
        }}
        
        // Minimum length
        if (rules.minLength && value.length < rules.minLength) {{
            showError(field, feedback, `Minimum length is ${{rules.minLength}} characters`);
            return false;
        }}
        
        // Maximum length
        if (rules.maxLength && value.length > rules.maxLength) {{
            showError(field, feedback, `Maximum length is ${{rules.maxLength}} characters`);
            return false;
        }}
        
        // Email validation
        if (rules.email && value && !isValidEmail(value)) {{
            showError(field, feedback, 'Please enter a valid email address');
            return false;
        }}
        
        // Pattern validation
        if (rules.pattern && value && !new RegExp(rules.pattern).test(value)) {{
            showError(field, feedback, rules.patternMessage || 'Invalid format');
            return false;
        }}
        
        showSuccess(field, feedback);
        return true;
    }}
    
    function showError(field, feedback, message) {{
        field.classList.add('is-invalid');
        field.classList.remove('is-valid');
        feedback.textContent = message;
    }}
    
    function showSuccess(field, feedback) {{
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        feedback.textContent = '';
    }}
    
    function isValidEmail(email) {{
        return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email);
    }}
}});
</script>'''
        
        return f'''<form id="{self.form_id}" class="advanced-form {self.css_class}" style="{self.style}" novalidate>
    {fields_html}
</form>
{validation_js}'''


class MicroInteraction(ComponentBase):
    """Micro-interactions and animations component"""
    
    def __init__(self, element, interaction_type='hover', animation='pulse', **kwargs):
        super().__init__(**kwargs)
        self.element = element
        self.interaction_type = interaction_type
        self.animation = animation
        
    def render(self):
        interaction_id = f"interaction_{id(self)}"
        
        # Animation CSS
        animation_css = f'''
<style>
.micro-interaction-{interaction_id} {{
    transition: all 0.3s ease;
    cursor: pointer;
}}

.micro-interaction-{interaction_id}.pulse {{
    animation: pulse-{interaction_id} 0.6s ease-in-out;
}}

.micro-interaction-{interaction_id}.bounce {{
    animation: bounce-{interaction_id} 0.6s ease-in-out;
}}

.micro-interaction-{interaction_id}.shake {{
    animation: shake-{interaction_id} 0.5s ease-in-out;
}}

.micro-interaction-{interaction_id}.glow {{
    box-shadow: 0 0 20px rgba(0, 123, 255, 0.5);
    transform: scale(1.05);
}}

@keyframes pulse-{interaction_id} {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.1); }}
    100% {{ transform: scale(1); }}
}}

@keyframes bounce-{interaction_id} {{
    0%, 20%, 60%, 100% {{ transform: translateY(0); }}
    40% {{ transform: translateY(-20px); }}
    80% {{ transform: translateY(-10px); }}
}}

@keyframes shake-{interaction_id} {{
    0%, 100% {{ transform: translateX(0); }}
    10%, 30%, 50%, 70%, 90% {{ transform: translateX(-5px); }}
    20%, 40%, 60%, 80% {{ transform: translateX(5px); }}
}}
</style>'''

        # JavaScript for interactions
        interaction_js = f'''
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const element = document.getElementById('{interaction_id}');
    
    if ('{self.interaction_type}' === 'hover') {{
        element.addEventListener('mouseenter', function() {{
            this.classList.add('{self.animation}');
        }});
        
        element.addEventListener('mouseleave', function() {{
            this.classList.remove('{self.animation}');
        }});
    }} else if ('{self.interaction_type}' === 'click') {{
        element.addEventListener('click', function() {{
            this.classList.add('{self.animation}');
            setTimeout(() => {{
                this.classList.remove('{self.animation}');
            }}, 600);
        }});
    }}
}});
</script>'''

        element_html = self.element.render() if hasattr(self.element, 'render') else str(self.element)
        
        return f'''{animation_css}
<div id="{interaction_id}" class="micro-interaction-{interaction_id} {self.css_class}" style="{self.style}">
    {element_html}
</div>
{interaction_js}'''


class AccessibilityChecker(ComponentBase):
    """Accessibility compliance checker component"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        checker_id = f"a11y_checker_{id(self)}"
        
        return f'''<div id="{checker_id}" class="accessibility-checker {self.css_class}" style="{self.style}">
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <i class="fas fa-universal-access me-2"></i>
                Accessibility Checker
            </h5>
        </div>
        <div class="card-body">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <span>Accessibility Score</span>
                <div id="a11y-score" class="badge bg-secondary">Checking...</div>
            </div>
            
            <div class="progress mb-3">
                <div id="a11y-progress" class="progress-bar" role="progressbar" style="width: 0%"></div>
            </div>
            
            <div id="a11y-results" class="accordion">
                <!-- Results will be populated here -->
            </div>
            
            <button type="button" class="btn btn-primary" onclick="runA11yCheck()">
                <i class="fas fa-search me-2"></i>Run Accessibility Check
            </button>
        </div>
    </div>
</div>

<script>
function runA11yCheck() {{
    const scoreElement = document.getElementById('a11y-score');
    const progressElement = document.getElementById('a11y-progress');
    const resultsElement = document.getElementById('a11y-results');
    
    scoreElement.textContent = 'Checking...';
    scoreElement.className = 'badge bg-warning';
    progressElement.style.width = '0%';
    
    // Simulate checking process
    let progress = 0;
    const interval = setInterval(() => {{
        progress += 10;
        progressElement.style.width = progress + '%';
        
        if (progress >= 100) {{
            clearInterval(interval);
            displayA11yResults();
        }}
    }}, 200);
}}

function displayA11yResults() {{
    const scoreElement = document.getElementById('a11y-score');
    const resultsElement = document.getElementById('a11y-results');
    
    // Mock accessibility checks
    const checks = [
        {{ name: 'Alt Text for Images', status: 'pass', description: 'All images have appropriate alt text' }},
        {{ name: 'Color Contrast', status: 'warning', description: 'Some text may not meet WCAG contrast ratios' }},
        {{ name: 'Keyboard Navigation', status: 'pass', description: 'All interactive elements are keyboard accessible' }},
        {{ name: 'Semantic HTML', status: 'pass', description: 'Proper heading structure and semantic elements used' }},
        {{ name: 'Focus Indicators', status: 'fail', description: 'Some elements lack visible focus indicators' }},
        {{ name: 'ARIA Labels', status: 'pass', description: 'Interactive elements have appropriate ARIA labels' }}
    ];
    
    const passCount = checks.filter(c => c.status === 'pass').length;
    const score = Math.round((passCount / checks.length) * 100);
    
    scoreElement.textContent = score + '%';
    scoreElement.className = score >= 80 ? 'badge bg-success' : score >= 60 ? 'badge bg-warning' : 'badge bg-danger';
    
    resultsElement.innerHTML = checks.map((check, index) => {{
        const statusIcon = check.status === 'pass' ? 'check-circle text-success' : 
                          check.status === 'warning' ? 'exclamation-triangle text-warning' : 
                          'times-circle text-danger';
        
        return `
        <div class="accordion-item">
            <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${{index}}">
                    <i class="fas fa-${{statusIcon}} me-2"></i>
                    ${{check.name}}
                </button>
            </h2>
            <div id="collapse${{index}}" class="accordion-collapse collapse">
                <div class="accordion-body">
                    ${{check.description}}
                </div>
            </div>
        </div>`;
    }}).join('');
}}
</script>'''