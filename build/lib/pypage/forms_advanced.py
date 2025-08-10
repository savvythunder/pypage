"""
Advanced form components with enhanced validation and UX
"""
from typing import Optional, List, Dict, Any, Union
from .elements import Element
from .components import ComponentBase

class FileUpload(ComponentBase):
    """Advanced file upload component with drag & drop"""
    
    def __init__(self, name: str, accept: Optional[str] = None,
                 multiple: bool = False, max_size: Optional[str] = None,
                 preview: bool = True, drag_drop: bool = True,
                 css_class: Optional[str] = None):
        upload_class = "file-upload-container"
        if css_class:
            upload_class += f" {css_class}"
        
        super().__init__(css_class=upload_class)
        
        # Generate unique ID
        import uuid
        self.upload_id = f"upload-{str(uuid.uuid4())[:8]}"
        
        # Build upload area HTML
        upload_html = f'''
        <div class="file-upload-area" id="{self.upload_id}">
            <input type="file" id="{self.upload_id}-input" name="{name}" 
                   class="file-upload-input" 
                   {f'accept="{accept}"' if accept else ''}
                   {'multiple' if multiple else ''}>
            
            <div class="file-upload-label">
                <div class="upload-icon">📁</div>
                <div class="upload-text">
                    <strong>Click to upload</strong> or drag and drop
                </div>
                <div class="upload-hint">
                    {f'Accepted: {accept}' if accept else 'Any file type'}
                    {f' • Max size: {max_size}' if max_size else ''}
                </div>
            </div>
            
            <div class="file-upload-preview" id="{self.upload_id}-preview"></div>
        </div>
        '''
        
        self.content = upload_html
        self.preview = preview
        self.drag_drop = drag_drop
    
    def render(self):
        attrs = self.render_attributes()
        
        upload_css = '''
        <style>
        .file-upload-container {
            margin-bottom: 1rem;
        }
        
        .file-upload-area {
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s;
            cursor: pointer;
            position: relative;
        }
        
        .file-upload-area:hover {
            border-color: #007bff;
            background-color: #f8f9fa;
        }
        
        .file-upload-area.dragover {
            border-color: #007bff;
            background-color: #e3f2fd;
        }
        
        .file-upload-input {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            cursor: pointer;
        }
        
        .upload-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .upload-text {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        
        .upload-hint {
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        .file-upload-preview {
            margin-top: 1rem;
            display: none;
        }
        
        .preview-item {
            display: flex;
            align-items: center;
            padding: 0.5rem;
            border: 1px solid #dee2e6;
            border-radius: 4px;
            margin-bottom: 0.5rem;
            background: white;
        }
        
        .preview-icon {
            margin-right: 0.5rem;
            font-size: 1.2rem;
        }
        
        .preview-info {
            flex: 1;
        }
        
        .preview-name {
            font-weight: bold;
        }
        
        .preview-size {
            color: #6c757d;
            font-size: 0.8rem;
        }
        </style>
        '''
        
        upload_js = f'''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const uploadArea = document.getElementById('{self.upload_id}');
            const fileInput = document.getElementById('{self.upload_id}-input');
            const preview = document.getElementById('{self.upload_id}-preview');
            
            // Click to upload
            uploadArea.addEventListener('click', function() {{
                fileInput.click();
            }});
            
            // Drag and drop
            uploadArea.addEventListener('dragover', function(e) {{
                e.preventDefault();
                this.classList.add('dragover');
            }});
            
            uploadArea.addEventListener('dragleave', function(e) {{
                e.preventDefault();
                this.classList.remove('dragover');
            }});
            
            uploadArea.addEventListener('drop', function(e) {{
                e.preventDefault();
                this.classList.remove('dragover');
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {{
                    fileInput.files = files;
                    showPreview(files);
                }}
            }});
            
            // File selection
            fileInput.addEventListener('change', function() {{
                if (this.files.length > 0) {{
                    showPreview(this.files);
                }}
            }});
            
            function showPreview(files) {{
                if (!{str(self.preview).lower()}) return;
                
                preview.innerHTML = '';
                preview.style.display = 'block';
                
                Array.from(files).forEach(file => {{
                    const item = document.createElement('div');
                    item.className = 'preview-item';
                    
                    const icon = getFileIcon(file.type);
                    const size = formatFileSize(file.size);
                    
                    item.innerHTML = `
                        <div class="preview-icon">${{icon}}</div>
                        <div class="preview-info">
                            <div class="preview-name">${{file.name}}</div>
                            <div class="preview-size">${{size}}</div>
                        </div>
                    `;
                    
                    preview.appendChild(item);
                }});
            }}
            
            function getFileIcon(type) {{
                if (type.startsWith('image/')) return '🖼️';
                if (type.startsWith('video/')) return '🎥';
                if (type.startsWith('audio/')) return '🎵';
                if (type.includes('pdf')) return '📄';
                if (type.includes('text')) return '📝';
                return '📎';
            }}
            
            function formatFileSize(bytes) {{
                if (bytes === 0) return '0 Bytes';
                const k = 1024;
                const sizes = ['Bytes', 'KB', 'MB', 'GB'];
                const i = Math.floor(Math.log(bytes) / Math.log(k));
                return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
            }}
        }});
        </script>
        '''
        
        return f"{upload_css}{upload_js}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class DateTimePicker(ComponentBase):
    """Advanced date/time picker component"""
    
    def __init__(self, name: str, picker_type: str = "datetime",
                 value: Optional[str] = None, min_date: Optional[str] = None,
                 max_date: Optional[str] = None, format_str: Optional[str] = None,
                 css_class: Optional[str] = None):
        picker_class = "datetime-picker-container"
        if css_class:
            picker_class += f" {css_class}"
        
        super().__init__(css_class=picker_class)
        
        # Generate unique ID
        import uuid
        self.picker_id = f"picker-{str(uuid.uuid4())[:8]}"
        
        # Determine input type and attributes
        input_type = {
            'date': 'date',
            'time': 'time',
            'datetime': 'datetime-local',
            'month': 'month',
            'week': 'week'
        }.get(picker_type, 'datetime-local')
        
        picker_html = f'''
        <div class="input-group">
            <input type="{input_type}" 
                   id="{self.picker_id}" 
                   name="{name}" 
                   class="form-control datetime-input"
                   {f'value="{value}"' if value else ''}
                   {f'min="{min_date}"' if min_date else ''}
                   {f'max="{max_date}"' if max_date else ''}>
            <span class="input-group-text">
                <i class="fas fa-calendar-alt"></i>
            </span>
        </div>
        '''
        
        self.content = picker_html

class FormWizard(ComponentBase):
    """Multi-step form wizard component"""
    
    def __init__(self, steps: List[Dict[str, Any]], css_class: Optional[str] = None):
        wizard_class = "form-wizard-container"
        if css_class:
            wizard_class += f" {css_class}"
        
        super().__init__(css_class=wizard_class)
        
        # Generate unique ID
        import uuid
        self.wizard_id = f"wizard-{str(uuid.uuid4())[:8]}"
        
        # Build wizard HTML
        wizard_html = f'<div class="wizard-wrapper" id="{self.wizard_id}">'
        
        # Step indicator
        wizard_html += '<div class="wizard-steps">'
        for i, step in enumerate(steps):
            step_class = "wizard-step"
            if i == 0:
                step_class += " active"
            
            wizard_html += f'''
            <div class="{step_class}" data-step="{i}">
                <div class="step-number">{i + 1}</div>
                <div class="step-title">{step.get('title', f'Step {i + 1}')}</div>
            </div>
            '''
        wizard_html += '</div>'
        
        # Step content
        wizard_html += '<div class="wizard-content">'
        for i, step in enumerate(steps):
            step_class = "wizard-panel"
            if i == 0:
                step_class += " active"
            
            content = step.get('content', '')
            if hasattr(content, 'render'):
                content = content.render()
            elif isinstance(content, list):
                content = ''.join([item.render() if hasattr(item, 'render') else str(item) for item in content])
            
            wizard_html += f'''
            <div class="{step_class}" data-panel="{i}">
                <h4>{step.get('title', f'Step {i + 1}')}</h4>
                {content}
            </div>
            '''
        wizard_html += '</div>'
        
        # Navigation buttons
        wizard_html += '''
        <div class="wizard-navigation">
            <button type="button" class="btn btn-secondary wizard-prev" disabled>Previous</button>
            <button type="button" class="btn btn-primary wizard-next">Next</button>
            <button type="submit" class="btn btn-success wizard-submit" style="display: none;">Submit</button>
        </div>
        '''
        
        wizard_html += '</div>'
        self.content = wizard_html
    
    def render(self):
        attrs = self.render_attributes()
        
        wizard_css = '''
        <style>
        .form-wizard-container {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .wizard-steps {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
            position: relative;
        }
        
        .wizard-steps::before {
            content: '';
            position: absolute;
            top: 20px;
            left: 0;
            right: 0;
            height: 2px;
            background: #dee2e6;
            z-index: 1;
        }
        
        .wizard-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 2;
            background: white;
            padding: 0 1rem;
        }
        
        .step-number {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #dee2e6;
            color: #6c757d;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-bottom: 0.5rem;
            transition: all 0.3s;
        }
        
        .wizard-step.active .step-number,
        .wizard-step.completed .step-number {
            background: #007bff;
            color: white;
        }
        
        .step-title {
            font-size: 0.9rem;
            text-align: center;
            color: #6c757d;
        }
        
        .wizard-step.active .step-title {
            color: #007bff;
            font-weight: bold;
        }
        
        .wizard-content {
            min-height: 300px;
            margin-bottom: 2rem;
        }
        
        .wizard-panel {
            display: none;
        }
        
        .wizard-panel.active {
            display: block;
        }
        
        .wizard-navigation {
            text-align: center;
            border-top: 1px solid #dee2e6;
            padding-top: 1rem;
        }
        
        .wizard-navigation .btn {
            margin: 0 0.5rem;
        }
        </style>
        '''
        
        wizard_js = f'''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const wizard = document.getElementById('{self.wizard_id}');
            const steps = wizard.querySelectorAll('.wizard-step');
            const panels = wizard.querySelectorAll('.wizard-panel');
            const prevBtn = wizard.querySelector('.wizard-prev');
            const nextBtn = wizard.querySelector('.wizard-next');
            const submitBtn = wizard.querySelector('.wizard-submit');
            
            let currentStep = 0;
            
            function updateWizard() {{
                // Update steps
                steps.forEach((step, index) => {{
                    step.classList.remove('active', 'completed');
                    if (index === currentStep) {{
                        step.classList.add('active');
                    }} else if (index < currentStep) {{
                        step.classList.add('completed');
                    }}
                }});
                
                // Update panels
                panels.forEach((panel, index) => {{
                    panel.classList.toggle('active', index === currentStep);
                }});
                
                // Update buttons
                prevBtn.disabled = currentStep === 0;
                
                if (currentStep === steps.length - 1) {{
                    nextBtn.style.display = 'none';
                    submitBtn.style.display = 'inline-block';
                }} else {{
                    nextBtn.style.display = 'inline-block';
                    submitBtn.style.display = 'none';
                }}
            }}
            
            nextBtn.addEventListener('click', function() {{
                if (currentStep < steps.length - 1) {{
                    currentStep++;
                    updateWizard();
                }}
            }});
            
            prevBtn.addEventListener('click', function() {{
                if (currentStep > 0) {{
                    currentStep--;
                    updateWizard();
                }}
            }});
            
            // Initialize
            updateWizard();
        }});
        </script>
        '''
        
        return f"{wizard_css}{wizard_js}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class FormValidation(ComponentBase):
    """Advanced form validation component"""
    
    def __init__(self, form_id: str, rules: Dict[str, Dict[str, Any]], 
                 css_class: Optional[str] = None):
        validation_class = "form-validation"
        if css_class:
            validation_class += f" {css_class}"
        
        super().__init__(css_class=validation_class)
        self.form_id = form_id
        self.rules = rules
        
        # This component only provides JavaScript validation
        self.content = ""
    
    def render(self):
        validation_js = f'''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const form = document.getElementById('{self.form_id}');
            if (!form) return;
            
            const rules = {self._dict_to_js(self.rules)};
            
            // Add validation styles
            const style = document.createElement('style');
            style.textContent = `
                .form-control.is-valid {{
                    border-color: #28a745;
                }}
                .form-control.is-invalid {{
                    border-color: #dc3545;
                }}
                .invalid-feedback {{
                    display: block;
                    width: 100%;
                    margin-top: 0.25rem;
                    font-size: 0.875rem;
                    color: #dc3545;
                }}
                .valid-feedback {{
                    display: block;
                    width: 100%;
                    margin-top: 0.25rem;
                    font-size: 0.875rem;
                    color: #28a745;
                }}
            `;
            document.head.appendChild(style);
            
            function validateField(field, rule) {{
                const value = field.value.trim();
                const errors = [];
                
                // Required validation
                if (rule.required && !value) {{
                    errors.push(rule.required_message || 'This field is required');
                }}
                
                if (value) {{
                    // Min length
                    if (rule.min_length && value.length < rule.min_length) {{
                        errors.push(`Minimum length is ${{rule.min_length}} characters`);
                    }}
                    
                    // Max length
                    if (rule.max_length && value.length > rule.max_length) {{
                        errors.push(`Maximum length is ${{rule.max_length}} characters`);
                    }}
                    
                    // Pattern validation
                    if (rule.pattern) {{
                        const regex = new RegExp(rule.pattern);
                        if (!regex.test(value)) {{
                            errors.push(rule.pattern_message || 'Invalid format');
                        }}
                    }}
                    
                    // Email validation
                    if (rule.email) {{
                        const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
                        if (!emailRegex.test(value)) {{
                            errors.push('Please enter a valid email address');
                        }}
                    }}
                    
                    // Number validation
                    if (rule.number) {{
                        if (isNaN(value)) {{
                            errors.push('Please enter a valid number');
                        }} else {{
                            const num = parseFloat(value);
                            if (rule.min && num < rule.min) {{
                                errors.push(`Minimum value is ${{rule.min}}`);
                            }}
                            if (rule.max && num > rule.max) {{
                                errors.push(`Maximum value is ${{rule.max}}`);
                            }}
                        }}
                    }}
                }}
                
                return errors;
            }}
            
            function showFieldValidation(field, errors) {{
                // Remove existing feedback
                const existingFeedback = field.parentNode.querySelector('.invalid-feedback, .valid-feedback');
                if (existingFeedback) {{
                    existingFeedback.remove();
                }}
                
                if (errors.length > 0) {{
                    field.classList.remove('is-valid');
                    field.classList.add('is-invalid');
                    
                    const feedback = document.createElement('div');
                    feedback.className = 'invalid-feedback';
                    feedback.textContent = errors[0];
                    field.parentNode.appendChild(feedback);
                }} else {{
                    field.classList.remove('is-invalid');
                    field.classList.add('is-valid');
                    
                    const feedback = document.createElement('div');
                    feedback.className = 'valid-feedback';
                    feedback.textContent = 'Looks good!';
                    field.parentNode.appendChild(feedback);
                }}
            }}
            
            // Add event listeners
            Object.keys(rules).forEach(fieldName => {{
                const field = form.querySelector(`[name="${{fieldName}}"]`);
                if (field) {{
                    field.addEventListener('blur', function() {{
                        const errors = validateField(field, rules[fieldName]);
                        showFieldValidation(field, errors);
                    }});
                    
                    field.addEventListener('input', function() {{
                        if (field.classList.contains('is-invalid')) {{
                            const errors = validateField(field, rules[fieldName]);
                            if (errors.length === 0) {{
                                showFieldValidation(field, errors);
                            }}
                        }}
                    }});
                }}
            }});
            
            // Form submission validation
            form.addEventListener('submit', function(e) {{
                let hasErrors = false;
                
                Object.keys(rules).forEach(fieldName => {{
                    const field = form.querySelector(`[name="${{fieldName}}"]`);
                    if (field) {{
                        const errors = validateField(field, rules[fieldName]);
                        showFieldValidation(field, errors);
                        if (errors.length > 0) {{
                            hasErrors = true;
                        }}
                    }}
                }});
                
                if (hasErrors) {{
                    e.preventDefault();
                    // Scroll to first error
                    const firstError = form.querySelector('.is-invalid');
                    if (firstError) {{
                        firstError.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                        firstError.focus();
                    }}
                }}
            }});
        }});
        </script>
        '''
        
        return validation_js
    
    def _dict_to_js(self, obj):
        """Convert Python dict to JavaScript object string"""
        import json
        return json.dumps(obj)

class SearchableSelect(ComponentBase):
    """Searchable select dropdown with filtering"""
    
    def __init__(self, name: str, options: List[Dict[str, str]],
                 placeholder: str = "Search and select...",
                 multiple: bool = False, css_class: Optional[str] = None):
        select_class = "searchable-select-container"
        if css_class:
            select_class += f" {css_class}"
        
        super().__init__(css_class=select_class)
        
        # Generate unique ID
        import uuid
        self.select_id = f"select-{str(uuid.uuid4())[:8]}"
        
        # Build searchable select HTML
        select_html = f'''
        <div class="searchable-select" id="{self.select_id}">
            <input type="text" class="form-control search-input" 
                   placeholder="{placeholder}" autocomplete="off">
            <div class="select-dropdown">
                <div class="select-options">
                    {self._render_options(options, multiple)}
                </div>
            </div>
            <select name="{name}" {'multiple' if multiple else ''} style="display: none;" 
                    class="hidden-select">
                {self._render_select_options(options)}
            </select>
        </div>
        '''
        
        self.content = select_html
        self.options = options
        self.multiple = multiple
    
    def _render_options(self, options, multiple):
        options_html = ""
        for option in options:
            value = option.get('value', '')
            text = option.get('text', value)
            
            options_html += f'''
            <div class="select-option" data-value="{value}">
                {f'<input type="checkbox" class="option-checkbox">' if multiple else ''}
                <span class="option-text">{text}</span>
            </div>
            '''
        return options_html
    
    def _render_select_options(self, options):
        options_html = ""
        for option in options:
            value = option.get('value', '')
            text = option.get('text', value)
            options_html += f'<option value="{value}">{text}</option>'
        return options_html
    
    def render(self):
        attrs = self.render_attributes()
        
        select_css = '''
        <style>
        .searchable-select-container {
            position: relative;
            margin-bottom: 1rem;
        }
        
        .searchable-select {
            position: relative;
        }
        
        .search-input {
            cursor: pointer;
        }
        
        .select-dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ced4da;
            border-top: none;
            border-radius: 0 0 4px 4px;
            max-height: 200px;
            overflow-y: auto;
            z-index: 1000;
            display: none;
        }
        
        .select-dropdown.show {
            display: block;
        }
        
        .select-option {
            padding: 0.5rem 0.75rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .select-option:hover {
            background-color: #f8f9fa;
        }
        
        .select-option.selected {
            background-color: #007bff;
            color: white;
        }
        
        .option-checkbox {
            margin: 0;
        }
        
        .option-text {
            flex: 1;
        }
        </style>
        '''
        
        select_js = f'''
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const container = document.getElementById('{self.select_id}');
            const searchInput = container.querySelector('.search-input');
            const dropdown = container.querySelector('.select-dropdown');
            const options = container.querySelectorAll('.select-option');
            const hiddenSelect = container.querySelector('.hidden-select');
            const isMultiple = {str(self.multiple).lower()};
            
            let selectedValues = [];
            
            // Show/hide dropdown
            searchInput.addEventListener('focus', function() {{
                dropdown.classList.add('show');
                this.select();
            }});
            
            document.addEventListener('click', function(e) {{
                if (!container.contains(e.target)) {{
                    dropdown.classList.remove('show');
                }}
            }});
            
            // Filter options
            searchInput.addEventListener('input', function() {{
                const filter = this.value.toLowerCase();
                
                options.forEach(option => {{
                    const text = option.querySelector('.option-text').textContent.toLowerCase();
                    option.style.display = text.includes(filter) ? 'flex' : 'none';
                }});
            }});
            
            // Option selection
            options.forEach(option => {{
                option.addEventListener('click', function(e) {{
                    e.preventDefault();
                    const value = this.dataset.value;
                    const text = this.querySelector('.option-text').textContent;
                    
                    if (isMultiple) {{
                        const checkbox = this.querySelector('.option-checkbox');
                        if (selectedValues.includes(value)) {{
                            selectedValues = selectedValues.filter(v => v !== value);
                            this.classList.remove('selected');
                            checkbox.checked = false;
                        }} else {{
                            selectedValues.push(value);
                            this.classList.add('selected');
                            checkbox.checked = true;
                        }}
                        
                        // Update display
                        searchInput.value = selectedValues.length > 0 ? 
                            `${{selectedValues.length}} item(s) selected` : '';
                    }} else {{
                        selectedValues = [value];
                        searchInput.value = text;
                        dropdown.classList.remove('show');
                        
                        // Update option appearance
                        options.forEach(opt => opt.classList.remove('selected'));
                        this.classList.add('selected');
                    }}
                    
                    // Update hidden select
                    Array.from(hiddenSelect.options).forEach(opt => {{
                        opt.selected = selectedValues.includes(opt.value);
                    }});
                }});
            }});
        }});
        </script>
        '''
        
        return f"{select_css}{select_js}<{self.tag}{attrs}>{self.content}</{self.tag}>"