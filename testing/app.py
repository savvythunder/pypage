"""
Testing Application for PyPage Library Documentation

This application demonstrates all the features of the PyPage library
and serves as both a testing environment and documentation generator.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pypage import *
from flask import Flask, render_template_string, request, jsonify, send_file
import tempfile
import webbrowser
from datetime import datetime

app = Flask(__name__)
app.secret_key = "testing-key"

class PyPageTester:
    """Main testing class for PyPage library features"""
    
    def __init__(self):
        self.test_results = []
        self.generated_pages = []
    
    def test_basic_components(self):
        """Test basic PyPage components"""
        page = Page("Basic Components Test", "Testing Core Features")
        
        # Test basic elements
        page.add_content(Heading("Basic Elements Test", 1))
        page.add_content(Paragraph("This paragraph tests basic text rendering."))
        
        # Test lists
        test_list = HtmlList([
            "First item",
            "Second item", 
            "Third item"
        ], list_type="ul")
        page.add_content(test_list)
        
        # Test containers
        container = Container([
            Heading("Container Test", 2),
            Paragraph("This content is inside a container.")
        ])
        page.add_content(container)
        
        # Test cards
        card = Card([
            Heading("Card Test", 3),
            Paragraph("This is a test card component.")
        ])
        page.add_content(card)
        
        # Test images
        image = Image("https://via.placeholder.com/300x200", "Test Image")
        page.add_content(image)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "Basic Components",
            "status": "passed" if len(html) > 1000 else "failed",
            "html": html
        })
        
        return html
    
    def test_advanced_components(self):
        """Test advanced PyPage components"""
        page = Page("Advanced Components Test", "Testing Enhanced Features")
        
        # Test navigation
        nav_links = [
            {"url": "/", "text": "Home"},
            {"url": "/about", "text": "About"},
            {"url": "/contact", "text": "Contact"}
        ]
        page.add_navbar(nav_links)
        
        # Test forms
        form = Form(action="/test", method="POST")
        form.add_field(Input("text", "name", label="Name", required=True))
        form.add_field(Input("email", "email", label="Email"))
        form.add_field(TextArea("message", label="Message", rows=4))
        form.add_field(Select("category", [
            {"value": "web", "text": "Web Development"},
            {"value": "mobile", "text": "Mobile Development"}
        ], label="Category"))
        form.add_field(Button("Submit", "submit"))
        page.add_content(form)
        
        # Test layout system
        row = Row()
        col1 = Column(width="md-6")
        col1.add_content(Heading("Column 1", 3))
        col1.add_content(Paragraph("This is the first column."))
        
        col2 = Column(width="md-6") 
        col2.add_content(Heading("Column 2", 3))
        col2.add_content(Paragraph("This is the second column."))
        
        row.add_column(col1)
        row.add_column(col2)
        page.add_content(row)
        
        # Test alerts and badges
        alert = Alert("This is a test alert!", "info")
        page.add_content(alert)
        
        badge_container = Div([
            Badge("New", "primary"),
            " ",
            Badge("Featured", "success"),
            " ", 
            Badge("Popular", "warning")
        ])
        page.add_content(badge_container)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "Advanced Components",
            "status": "passed" if "form" in html and "row" in html else "failed",
            "html": html
        })
        
        return html
    
    def test_css_builder(self):
        """Test CSS builder functionality"""
        page = Page("CSS Builder Test", "Testing Custom Styling")
        
        # Create custom CSS
        css_builder = CSSBuilder()
        css_builder.add_rule(".custom-header", {
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "color": "white",
            "padding": "2rem",
            "border-radius": "10px",
            "text-align": "center"
        })
        
        css_builder.add_rule(".custom-card", {
            "border": "2px solid #007bff",
            "border-radius": "15px",
            "padding": "1.5rem",
            "margin": "1rem 0",
            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)"
        })
        
        # Add responsive breakpoints
        css_builder.responsive_breakpoints(".custom-header",
            sm={"font-size": "1.2rem"},
            md={"font-size": "1.5rem"}, 
            lg={"font-size": "2rem"}
        )
        
        page.custom_css = css_builder.render()
        
        # Add styled content
        page.add_content(Heading("Custom Styled Header", 1, css_class="custom-header"))
        
        styled_card = Card([
            Heading("Styled Card", 3),
            Paragraph("This card has custom styling applied.")
        ], css_class="custom-card")
        page.add_content(styled_card)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "CSS Builder",
            "status": "passed" if "custom-header" in html and "custom-card" in html else "failed",
            "html": html
        })
        
        return html
    
    def test_data_visualization(self):
        """Test data visualization components"""
        page = Page("Data Visualization Test", "Testing Charts and Graphs")
        
        # Test chart data
        chart_data = {
            "labels": ["January", "February", "March", "April", "May"],
            "datasets": [{
                "label": "Sales",
                "data": [10, 19, 3, 5, 2],
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)"
            }]
        }
        
        # Test bar chart
        bar_chart = BarChart("sales-chart", chart_data, width=400, height=200)
        page.add_content(Heading("Bar Chart Test", 2))
        page.add_content(bar_chart)
        
        # Test KPI cards
        kpi_row = Row()
        kpi1 = KPICard("Total Sales", "1,234", "↑ 12%", "success")
        kpi2 = KPICard("Revenue", "$45,678", "↓ 3%", "danger")
        kpi3 = KPICard("Users", "5,432", "↑ 8%", "success")
        
        kpi_row.add_column(Column([kpi1], width="md-4"))
        kpi_row.add_column(Column([kpi2], width="md-4"))
        kpi_row.add_column(Column([kpi3], width="md-4"))
        page.add_content(kpi_row)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "Data Visualization",
            "status": "passed" if "chart" in html.lower() and "kpi" in html.lower() else "failed",
            "html": html
        })
        
        return html
    
    def test_animations(self):
        """Test animation components"""
        page = Page("Animation Test", "Testing Animations and Transitions")
        
        # Test fade in animation
        fade_content = FadeIn(
            Container([
                Heading("Fade In Animation", 2),
                Paragraph("This content fades in when the page loads.")
            ])
        )
        page.add_content(fade_content)
        
        # Test slide up animation
        slide_content = SlideUp(
            Card([
                Heading("Slide Up Animation", 3),
                Paragraph("This card slides up from the bottom.")
            ])
        )
        page.add_content(slide_content)
        
        # Test animate on scroll
        scroll_content = AnimateOnScroll(
            Container([
                Heading("Scroll Animation", 2),
                Paragraph("This content animates when scrolled into view.")
            ]),
            animation_type="fadeInUp"
        )
        page.add_content(scroll_content)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "Animations",
            "status": "passed" if "animation" in html.lower() or "fade" in html.lower() else "failed",
            "html": html
        })
        
        return html
    
    def test_dark_mode(self):
        """Test dark mode functionality"""
        page = Page("Dark Mode Test", "Testing Dark Mode Toggle")
        
        # Add dark mode toggle
        dark_toggle = DarkModeToggle(position="top-right")
        page.add_content(dark_toggle)
        
        # Add theme provider
        theme_provider = ThemeProvider()
        page.add_content(theme_provider)
        
        # Add content that works well with dark mode
        page.add_content(Heading("Dark Mode Demo", 1))
        page.add_content(Paragraph("Toggle the dark mode switch to see the theme change."))
        
        # Test cards in dark mode
        card = Card([
            Heading("Dark Mode Card", 3),
            Paragraph("This card adapts to dark and light themes.")
        ])
        page.add_content(card)
        
        html = page.generate_html()
        self.test_results.append({
            "test": "Dark Mode",
            "status": "passed" if "dark" in html.lower() and "theme" in html.lower() else "failed",
            "html": html
        })
        
        return html
    
    def run_all_tests(self):
        """Run all tests and generate a comprehensive report"""
        print("Running PyPage Library Tests...")
        
        tests = [
            self.test_basic_components,
            self.test_advanced_components, 
            self.test_css_builder,
            self.test_data_visualization,
            self.test_animations,
            self.test_dark_mode
        ]
        
        for test in tests:
            try:
                html = test()
                self.generated_pages.append({
                    "name": test.__name__,
                    "html": html,
                    "timestamp": datetime.now().isoformat()
                })
                print(f"✓ {test.__name__} completed")
            except Exception as e:
                print(f"✗ {test.__name__} failed: {str(e)}")
                self.test_results.append({
                    "test": test.__name__,
                    "status": "failed",
                    "error": str(e)
                })
        
        return self.test_results

# Flask routes for the testing application
@app.route('/')
def index():
    """Main testing interface"""
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PyPage Testing Application</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center mb-4">PyPage Library Testing Application</h1>
            <p class="text-center lead">Test and document all PyPage library features</p>
            
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">Available Tests</h5>
                            <div class="d-grid gap-2">
                                <button class="btn btn-primary" onclick="runTest('basic')">Test Basic Components</button>
                                <button class="btn btn-primary" onclick="runTest('advanced')">Test Advanced Components</button>
                                <button class="btn btn-primary" onclick="runTest('css')">Test CSS Builder</button>
                                <button class="btn btn-primary" onclick="runTest('data-viz')">Test Data Visualization</button>
                                <button class="btn btn-primary" onclick="runTest('animations')">Test Animations</button>
                                <button class="btn btn-primary" onclick="runTest('dark-mode')">Test Dark Mode</button>
                                <button class="btn btn-success" onclick="runAllTests()">Run All Tests</button>
                            </div>
                        </div>
                    </div>
                    
                    <div id="results" class="mt-4"></div>
                </div>
            </div>
        </div>
        
        <script>
            function runTest(testType) {
                fetch('/test/' + testType)
                    .then(response => response.json())
                    .then(data => {
                        displayResult(data);
                    });
            }
            
            function runAllTests() {
                fetch('/test/all')
                    .then(response => response.json())
                    .then(data => {
                        displayResults(data);
                    });
            }
            
            function displayResult(result) {
                const resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = `
                    <div class="card">
                        <div class="card-body">
                            <h5>Test Result: ${result.test}</h5>
                            <span class="badge ${result.status === 'passed' ? 'bg-success' : 'bg-danger'}">${result.status}</span>
                            <div class="mt-3">
                                <button class="btn btn-sm btn-outline-primary" onclick="previewHTML('${btoa(result.html)}')">Preview HTML</button>
                            </div>
                        </div>
                    </div>
                `;
            }
            
            function displayResults(results) {
                const resultsDiv = document.getElementById('results');
                let html = '<div class="card"><div class="card-body"><h5>All Test Results</h5>';
                
                results.forEach(result => {
                    html += `
                        <div class="d-flex justify-content-between align-items-center border-bottom py-2">
                            <span>${result.test}</span>
                            <span class="badge ${result.status === 'passed' ? 'bg-success' : 'bg-danger'}">${result.status}</span>
                        </div>
                    `;
                });
                
                html += '</div></div>';
                resultsDiv.innerHTML = html;
            }
            
            function previewHTML(encodedHTML) {
                const html = atob(encodedHTML);
                const newWindow = window.open();
                newWindow.document.write(html);
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/test/<test_type>')
def run_test(test_type):
    """Run a specific test"""
    tester = PyPageTester()
    
    if test_type == 'basic':
        html = tester.test_basic_components()
    elif test_type == 'advanced':
        html = tester.test_advanced_components()
    elif test_type == 'css':
        html = tester.test_css_builder()
    elif test_type == 'data-viz':
        html = tester.test_data_visualization()
    elif test_type == 'animations':
        html = tester.test_animations()
    elif test_type == 'dark-mode':
        html = tester.test_dark_mode()
    elif test_type == 'all':
        results = tester.run_all_tests()
        return jsonify(results)
    else:
        return jsonify({"error": "Unknown test type"}), 400
    
    # Return the last test result
    return jsonify(tester.test_results[-1])

if __name__ == '__main__':
    print("Starting PyPage Testing Application...")
    print("Visit http://localhost:5001 to run tests")
    app.run(host='0.0.0.0', port=5001, debug=True)