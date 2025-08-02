// HTML Generator Editor JavaScript

let editor;
let isModified = false;

// Initialize CodeMirror editor
document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.getElementById('codeEditor');
    if (textarea) {
        editor = CodeMirror.fromTextArea(textarea, {
            mode: 'python',
            theme: 'dracula',
            lineNumbers: true,
            indentUnit: 4,
            tabSize: 4,
            indentWithTabs: false,
            autoCloseBrackets: true,
            matchBrackets: true,
            lineWrapping: true,
            extraKeys: {
                "Ctrl-Space": "autocomplete",
                "Ctrl-S": function(cm) {
                    generatePage();
                },
                "Ctrl-/": "toggleComment"
            }
        });
        
        // Track changes
        editor.on('change', function() {
            isModified = true;
        });
        
        // Auto-save every 30 seconds if modified
        setInterval(function() {
            if (isModified) {
                localStorage.setItem('editorContent', editor.getValue());
                localStorage.setItem('editorTitle', document.getElementById('title').value);
                isModified = false;
            }
        }, 30000);
        
        // Load saved content
        const savedContent = localStorage.getItem('editorContent');
        const savedTitle = localStorage.getItem('editorTitle');
        
        if (savedContent && !textarea.value.trim()) {
            editor.setValue(savedContent);
        }
        
        if (savedTitle && !document.getElementById('title').value) {
            document.getElementById('title').value = savedTitle;
        }
    }
    
    // Load example from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const exampleIndex = urlParams.get('example');
    if (exampleIndex !== null) {
        loadExampleCode(parseInt(exampleIndex));
    }
});

// Example code templates
const examples = {
    basic: `# Create a basic webpage
page = Page("My Website", "Welcome to My Site")
page.add_content(Heading("About Us", 2))
page.add_content(Paragraph("This is a simple webpage created with the HTML generator."))
page.add_content(Paragraph("We create beautiful, functional websites."))`,

    navigation: `# Create a webpage with navigation
page = Page("My Blog", "John's Blog")
page.add_navbar([
    {"url": "/", "text": "Home"},
    {"url": "/about", "text": "About"},
    {"url": "/contact", "text": "Contact"}
])
page.add_content(Heading("Latest Posts", 2))
page.add_content(Paragraph("Welcome to my blog where I share my thoughts and experiences."))`,

    cards: `# Create a webpage with card layout
page = Page("Our Services", "What We Offer")

# Create a container for cards
container = Container()
container.add_content(Heading("Our Services", 2))

# Add service cards
card1 = Card("Web Development", "We create modern, responsive websites using the latest technologies.")
card1.add_class("mb-4")
container.add_content(card1)

card2 = Card("Mobile Apps", "Native and cross-platform mobile applications for iOS and Android.")
card2.add_class("mb-4")
container.add_content(card2)

card3 = Card("Consulting", "Technical consulting and architecture design for your projects.")
card3.add_class("mb-4")
container.add_content(card3)

page.add_content(container)`,

    portfolio: `# Create a portfolio webpage
page = Page("Portfolio", "My Work")

# Add navigation
page.add_navbar([
    {"url": "#home", "text": "Home"},
    {"url": "#portfolio", "text": "Portfolio"},
    {"url": "#contact", "text": "Contact"}
])

# Skills section
page.add_content(Heading("Skills & Expertise", 2))
skills_list = List([
    "Python Programming",
    "Web Development (Flask, Django)",
    "Frontend Development (HTML, CSS, JavaScript)",
    "Database Design (PostgreSQL, MongoDB)",
    "API Development and Integration",
    "Cloud Services (AWS, Google Cloud)"
], ordered=False)
skills_list.add_class("list-group list-group-flush")
page.add_content(skills_list)

# Featured project
page.add_content(Heading("Featured Project", 2))
page.add_content(Image("https://via.placeholder.com/800x400", "Project Screenshot"))
page.add_content(Paragraph("This HTML Generator Library allows developers to create webpages using Python code with an intuitive object-oriented approach."))

# Contact card
contact_card = Card("Get In Touch", "Interested in working together? Let's discuss your project!")
contact_card.add_class("mt-4 bg-primary text-white")
page.add_content(contact_card)`
};

// Load example code
function loadExample() {
    const modal = new bootstrap.Modal(document.getElementById('exampleModal'));
    modal.show();
}

function loadExampleCode(type) {
    let code;
    if (typeof type === 'string') {
        code = examples[type];
    } else {
        // Handle numeric index from examples page
        const exampleCodes = [
            examples.basic,
            examples.navigation,
            examples.cards,
            examples.portfolio
        ];
        code = exampleCodes[type] || examples.basic;
    }
    
    if (editor && code) {
        editor.setValue(code);
        isModified = true;
    }
    
    // Close modal if it's open
    const modal = bootstrap.Modal.getInstance(document.getElementById('exampleModal'));
    if (modal) {
        modal.hide();
    }
}

// Format code
function formatCode() {
    if (editor) {
        const code = editor.getValue();
        // Basic Python formatting (add more sophisticated formatting if needed)
        const formatted = code
            .split('\n')
            .map(line => line.trimRight())
            .join('\n')
            .replace(/\n{3,}/g, '\n\n'); // Remove excessive blank lines
        
        editor.setValue(formatted);
        isModified = true;
        
        // Show feedback
        showTemporaryMessage('Code formatted!', 'success');
    }
}

// Clear code
function clearCode() {
    if (editor && confirm('Are you sure you want to clear all code?')) {
        editor.setValue(examples.basic);
        isModified = true;
    }
}

// Generate page
function generatePage() {
    if (editor) {
        // Update textarea value
        editor.save();
        
        // Add loading state
        const submitBtn = document.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Generating...';
        submitBtn.disabled = true;
        
        // Submit form
        document.getElementById('codeForm').submit();
    }
}

// Show documentation
function showDocs() {
    // Toggle all accordion items
    const accordionItems = document.querySelectorAll('#docsAccordion .accordion-collapse');
    const allExpanded = Array.from(accordionItems).every(item => item.classList.contains('show'));
    
    accordionItems.forEach(item => {
        const bsCollapse = new bootstrap.Collapse(item, {
            toggle: false
        });
        
        if (allExpanded) {
            bsCollapse.hide();
        } else {
            bsCollapse.show();
        }
    });
}

// Utility functions
function showTemporaryMessage(message, type = 'info') {
    // Create and show a temporary alert
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto-remove after 3 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 3000);
}

// Save to localStorage before leaving
window.addEventListener('beforeunload', function() {
    if (editor && isModified) {
        localStorage.setItem('editorContent', editor.getValue());
        localStorage.setItem('editorTitle', document.getElementById('title').value);
    }
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + S to save
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        generatePage();
    }
    
    // Ctrl/Cmd + N for new
    if ((e.ctrlKey || e.metaKey) && e.key === 'n') {
        e.preventDefault();
        if (confirm('Start with a new page? Any unsaved changes will be lost.')) {
            window.location.href = '/editor';
        }
    }
});

// Auto-complete helper
function insertSnippet(snippet) {
    if (editor) {
        const cursor = editor.getCursor();
        editor.replaceRange(snippet, cursor);
        editor.focus();
    }
}

// Common snippets
const snippets = {
    page: 'page = Page("Title", "Header Text")',
    heading: 'Heading("Text", 2)',
    paragraph: 'Paragraph("Your text here")',
    list: 'List(["Item 1", "Item 2", "Item 3"])',
    card: 'Card("Title", "Description")',
    image: 'Image("https://example.com/image.jpg", "Alt text")'
};

// Add snippet buttons (if needed)
function addSnippetButtons() {
    const snippetContainer = document.createElement('div');
    snippetContainer.className = 'mb-3';
    snippetContainer.innerHTML = '<small class="text-muted">Quick Insert:</small><br>';
    
    Object.entries(snippets).forEach(([name, code]) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'btn btn-sm btn-outline-secondary me-1 mb-1';
        btn.textContent = name;
        btn.onclick = () => insertSnippet(code);
        snippetContainer.appendChild(btn);
    });
    
    // Insert before the editor if desired
    // const editorCard = document.querySelector('.card .card-body');
    // editorCard.insertBefore(snippetContainer, editorCard.firstChild);
}

// Initialize tooltips and popovers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});
