"""
Data visualization components using Chart.js and modern charting
"""
from typing import Optional, List, Dict, Any, Union
from .elements import Element
from .components import ComponentBase

class Chart(ComponentBase):
    """Interactive chart component using Chart.js"""
    
    def __init__(self, chart_type: str, data: Dict[str, Any], 
                 options: Optional[Dict[str, Any]] = None,
                 width: str = "400px", height: str = "300px",
                 css_class: Optional[str] = None):
        chart_class = "chart-container"
        if css_class:
            chart_class += f" {css_class}"
        
        super().__init__(css_class=chart_class)
        
        # Generate unique ID
        import uuid
        self.chart_id = f"chart-{str(uuid.uuid4())[:8]}"
        
        self.chart_type = chart_type
        self.data = data
        self.options = options or {}
        self.width = width
        self.height = height
        
        # Canvas element
        canvas_html = f'''
        <canvas id="{self.chart_id}" width="{width}" height="{height}"></canvas>
        '''
        
        self.content = canvas_html
    
    def render(self):
        attrs = self.render_attributes()
        
        # Chart.js library and configuration
        chart_html = f'''
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const ctx = document.getElementById('{self.chart_id}').getContext('2d');
            new Chart(ctx, {{
                type: '{self.chart_type}',
                data: {self._dict_to_js(self.data)},
                options: {self._dict_to_js(self.options)}
            }});
        }});
        </script>
        '''
        
        return f"<{self.tag}{attrs}>{self.content}</{self.tag}>{chart_html}"
    
    def _dict_to_js(self, obj):
        """Convert Python dict to JavaScript object string"""
        import json
        return json.dumps(obj)

class BarChart(Chart):
    """Bar chart component"""
    
    def __init__(self, labels: List[str], datasets: List[Dict[str, Any]],
                 title: Optional[str] = None, **kwargs):
        data = {
            'labels': labels,
            'datasets': datasets
        }
        
        options = {
            'responsive': True,
            'plugins': {
                'title': {
                    'display': bool(title),
                    'text': title or ''
                }
            }
        }
        
        super().__init__('bar', data, options, **kwargs)

class LineChart(Chart):
    """Line chart component"""
    
    def __init__(self, labels: List[str], datasets: List[Dict[str, Any]],
                 title: Optional[str] = None, **kwargs):
        data = {
            'labels': labels,
            'datasets': datasets
        }
        
        options = {
            'responsive': True,
            'plugins': {
                'title': {
                    'display': bool(title),
                    'text': title or ''
                }
            },
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
        
        super().__init__('line', data, options, **kwargs)

class PieChart(Chart):
    """Pie chart component"""
    
    def __init__(self, labels: List[str], data_values: List[float],
                 colors: Optional[List[str]] = None, title: Optional[str] = None, **kwargs):
        
        # Default colors
        if not colors:
            colors = [
                '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
            ]
        
        data = {
            'labels': labels,
            'datasets': [{
                'data': data_values,
                'backgroundColor': colors[:len(labels)],
                'borderWidth': 1
            }]
        }
        
        options = {
            'responsive': True,
            'plugins': {
                'title': {
                    'display': bool(title),
                    'text': title or ''
                },
                'legend': {
                    'position': 'bottom'
                }
            }
        }
        
        super().__init__('pie', data, options, **kwargs)

class DoughnutChart(Chart):
    """Doughnut chart component"""
    
    def __init__(self, labels: List[str], data_values: List[float],
                 colors: Optional[List[str]] = None, title: Optional[str] = None, **kwargs):
        
        # Default colors
        if not colors:
            colors = [
                '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
                '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
            ]
        
        data = {
            'labels': labels,
            'datasets': [{
                'data': data_values,
                'backgroundColor': colors[:len(labels)],
                'borderWidth': 1
            }]
        }
        
        options = {
            'responsive': True,
            'plugins': {
                'title': {
                    'display': bool(title),
                    'text': title or ''
                },
                'legend': {
                    'position': 'bottom'
                }
            },
            'cutout': '60%'  # Creates the doughnut hole
        }
        
        super().__init__('doughnut', data, options, **kwargs)

class Dashboard(ComponentBase):
    """Dashboard layout with metrics and charts"""
    
    def __init__(self, title: str, metrics: List[Dict[str, Any]],
                 charts: List[Chart], css_class: Optional[str] = None):
        dashboard_class = "dashboard-container"
        if css_class:
            dashboard_class += f" {css_class}"
        
        super().__init__(css_class=dashboard_class)
        
        # Build dashboard HTML
        dashboard_html = f'<div class="dashboard-header"><h2>{title}</h2></div>'
        
        # Metrics row
        if metrics:
            dashboard_html += '<div class="dashboard-metrics row">'
            for metric in metrics:
                metric_html = f'''
                <div class="col-md-3">
                    <div class="metric-card card">
                        <div class="card-body text-center">
                            <h3 class="metric-value">{metric.get('value', '0')}</h3>
                            <p class="metric-label">{metric.get('label', 'Metric')}</p>
                            {f'<small class="metric-change text-{metric.get("change_type", "muted")}">{metric.get("change", "")}</small>' if metric.get('change') else ''}
                        </div>
                    </div>
                </div>
                '''
                dashboard_html += metric_html
            dashboard_html += '</div>'
        
        # Charts row
        if charts:
            dashboard_html += '<div class="dashboard-charts row mt-4">'
            chart_width = 12 // min(len(charts), 3)  # Max 3 charts per row
            
            for i, chart in enumerate(charts):
                if i % 3 == 0 and i > 0:
                    dashboard_html += '</div><div class="dashboard-charts row mt-4">'
                
                dashboard_html += f'<div class="col-md-{chart_width}">'
                dashboard_html += chart.render()
                dashboard_html += '</div>'
            
            dashboard_html += '</div>'
        
        self.content = dashboard_html
    
    def render(self):
        attrs = self.render_attributes()
        
        dashboard_css = '''
        <style>
        .dashboard-container {
            padding: 2rem;
        }
        
        .dashboard-header {
            margin-bottom: 2rem;
            border-bottom: 1px solid #dee2e6;
            padding-bottom: 1rem;
        }
        
        .dashboard-metrics .metric-card {
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        
        .dashboard-metrics .metric-card:hover {
            transform: translateY(-2px);
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            color: #6c757d;
            margin-bottom: 0.5rem;
        }
        
        .metric-change {
            font-weight: bold;
        }
        
        .dashboard-charts .chart-container {
            background: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        '''
        
        return f"{dashboard_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class SparklineChart(ComponentBase):
    """Compact sparkline chart for trends"""
    
    def __init__(self, data_points: List[float], color: str = "#007bff",
                 width: str = "100px", height: str = "30px",
                 css_class: Optional[str] = None):
        sparkline_class = "sparkline-chart"
        if css_class:
            sparkline_class += f" {css_class}"
        
        super().__init__(css_class=sparkline_class)
        
        # Generate unique ID
        import uuid
        self.sparkline_id = f"sparkline-{str(uuid.uuid4())[:8]}"
        
        # Create SVG sparkline
        if not data_points:
            data_points = [0]
        
        min_val = min(data_points)
        max_val = max(data_points)
        range_val = max_val - min_val if max_val != min_val else 1
        
        # Calculate points for SVG path
        points = []
        svg_width = 100
        svg_height = 30
        
        for i, value in enumerate(data_points):
            x = (i / (len(data_points) - 1)) * svg_width if len(data_points) > 1 else 0
            y = svg_height - ((value - min_val) / range_val) * svg_height
            points.append(f"{x},{y}")
        
        path_data = "M " + " L ".join(points)
        
        sparkline_html = f'''
        <svg width="{width}" height="{height}" viewBox="0 0 {svg_width} {svg_height}" 
             class="sparkline-svg" id="{self.sparkline_id}">
            <path d="{path_data}" fill="none" stroke="{color}" stroke-width="2"/>
        </svg>
        '''
        
        self.content = sparkline_html
    
    def render(self):
        attrs = self.render_attributes()
        
        sparkline_css = '''
        <style>
        .sparkline-chart {
            display: inline-block;
            vertical-align: middle;
        }
        
        .sparkline-svg {
            display: block;
        }
        </style>
        '''
        
        return f"{sparkline_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"

class KPICard(ComponentBase):
    """Key Performance Indicator card with trend"""
    
    def __init__(self, title: str, value: str, trend_data: List[float],
                 change: Optional[str] = None, change_type: str = "neutral",
                 icon: Optional[str] = None, css_class: Optional[str] = None):
        kpi_class = "kpi-card card"
        if css_class:
            kpi_class += f" {css_class}"
        
        super().__init__(css_class=kpi_class)
        
        # Create sparkline for trend
        sparkline = SparklineChart(trend_data, width="80px", height="40px")
        
        kpi_html = f'''
        <div class="card-body">
            <div class="d-flex justify-content-between align-items-start">
                <div class="kpi-content">
                    <h6 class="kpi-title text-muted">{title}</h6>
                    <h3 class="kpi-value">{value}</h3>
                    {f'<small class="kpi-change text-{change_type}">{change}</small>' if change else ''}
                </div>
                <div class="kpi-visual">
                    {f'<i class="{icon} kpi-icon"></i>' if icon else ''}
                    {sparkline.render()}
                </div>
            </div>
        </div>
        '''
        
        self.content = kpi_html
    
    def render(self):
        attrs = self.render_attributes()
        
        kpi_css = '''
        <style>
        .kpi-card {
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        
        .kpi-card:hover {
            transform: translateY(-2px);
        }
        
        .kpi-title {
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        
        .kpi-value {
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 0.25rem;
        }
        
        .kpi-change {
            font-weight: bold;
        }
        
        .kpi-icon {
            font-size: 1.5rem;
            color: #6c757d;
            margin-bottom: 0.5rem;
        }
        
        .kpi-visual {
            text-align: center;
        }
        </style>
        '''
        
        return f"{kpi_css}<{self.tag}{attrs}>{self.content}</{self.tag}>"