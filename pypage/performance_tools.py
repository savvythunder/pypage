"""
Performance optimization tools and monitoring
Includes hot reload, performance profiling, and optimization features
"""

from .elements import Element
from .components import ComponentBase
import json
import time


class HotReloadManager(ComponentBase):
    """Hot reload functionality for development"""
    
    def __init__(self, enabled=True, **kwargs):
        super().__init__(**kwargs)
        self.enabled = enabled
        
    def render(self):
        if not self.enabled:
            return ''
            
        return '''<script>
// Hot Reload Manager
class HotReloadManager {
    constructor() {
        this.enabled = true;
        this.lastModified = {};
        this.checkInterval = 1000; // Check every second
        this.init();
    }
    
    init() {
        if (!this.enabled) return;
        
        console.log('🔥 Hot Reload enabled');
        this.startWatching();
        this.addIndicator();
    }
    
    startWatching() {
        setInterval(() => {
            this.checkForChanges();
        }, this.checkInterval);
    }
    
    checkForChanges() {
        fetch('/api/hot-reload/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lastModified: this.lastModified
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.changed) {
                this.handleReload(data);
            }
        })
        .catch(error => {
            console.error('Hot reload check failed:', error);
        });
    }
    
    handleReload(data) {
        console.log('🔄 Changes detected, reloading...');
        this.showReloadIndicator();
        
        if (data.type === 'css') {
            this.reloadCSS();
        } else if (data.type === 'js') {
            this.reloadJS();
        } else {
            this.reloadPage();
        }
    }
    
    reloadCSS() {
        const links = document.querySelectorAll('link[rel="stylesheet"]');
        links.forEach(link => {
            const newLink = link.cloneNode();
            newLink.href = link.href + (link.href.includes('?') ? '&' : '?') + 'v=' + Date.now();
            link.parentNode.insertBefore(newLink, link.nextSibling);
            link.remove();
        });
    }
    
    reloadJS() {
        // For JS changes, we need to reload the page
        this.reloadPage();
    }
    
    reloadPage() {
        window.location.reload();
    }
    
    addIndicator() {
        const indicator = document.createElement('div');
        indicator.id = 'hot-reload-indicator';
        indicator.innerHTML = '🔥';
        indicator.style.cssText = `
            position: fixed;
            top: 10px;
            right: 10px;
            background: #28a745;
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 12px;
            z-index: 10000;
            display: none;
        `;
        document.body.appendChild(indicator);
    }
    
    showReloadIndicator() {
        const indicator = document.getElementById('hot-reload-indicator');
        if (indicator) {
            indicator.style.display = 'block';
            indicator.style.background = '#ffc107';
            indicator.innerHTML = '🔄 Reloading...';
            
            setTimeout(() => {
                indicator.style.display = 'none';
            }, 2000);
        }
    }
}

// Initialize hot reload in development
if (window.location.hostname === 'localhost' || window.location.hostname.includes('replit')) {
    new HotReloadManager();
}
</script>'''


class PerformanceProfiler(ComponentBase):
    """Performance profiling and monitoring tools"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        profiler_id = f"perf_profiler_{id(self)}"
        
        return f'''<div id="{profiler_id}" class="performance-profiler {self.css_class}" style="{self.style}">
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <i class="fas fa-tachometer-alt me-2"></i>
                Performance Profiler
            </h5>
        </div>
        <div class="card-body">
            <div class="row mb-4">
                <div class="col-md-3">
                    <div class="text-center">
                        <div class="h4 text-primary" id="load-time">--</div>
                        <small class="text-muted">Load Time (ms)</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <div class="h4 text-success" id="dom-nodes">--</div>
                        <small class="text-muted">DOM Nodes</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <div class="h4 text-warning" id="memory-usage">--</div>
                        <small class="text-muted">Memory (MB)</small>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="text-center">
                        <div class="h4 text-info" id="resource-count">--</div>
                        <small class="text-muted">Resources</small>
                    </div>
                </div>
            </div>
            
            <div class="performance-chart mb-4">
                <canvas id="perf-chart" height="200"></canvas>
            </div>
            
            <div class="performance-recommendations">
                <h6>Performance Recommendations</h6>
                <ul id="perf-recommendations" class="list-group list-group-flush">
                    <!-- Recommendations will be populated here -->
                </ul>
            </div>
            
            <div class="mt-3">
                <button type="button" class="btn btn-primary me-2" onclick="runPerformanceTest()">
                    <i class="fas fa-play me-2"></i>Run Test
                </button>
                <button type="button" class="btn btn-outline-secondary" onclick="exportReport()">
                    <i class="fas fa-download me-2"></i>Export Report
                </button>
            </div>
        </div>
    </div>
</div>

<script>
class PerformanceProfiler {{
    constructor() {{
        this.metrics = {{}};
        this.init();
    }}
    
    init() {{
        this.collectInitialMetrics();
        this.startMonitoring();
    }}
    
    collectInitialMetrics() {{
        // Navigation timing
        if (performance.timing) {{
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            document.getElementById('load-time').textContent = loadTime;
        }}
        
        // DOM nodes count
        const domNodes = document.querySelectorAll('*').length;
        document.getElementById('dom-nodes').textContent = domNodes;
        
        // Memory usage (if available)
        if (performance.memory) {{
            const memoryMB = Math.round(performance.memory.usedJSHeapSize / 1024 / 1024);
            document.getElementById('memory-usage').textContent = memoryMB;
        }}
        
        // Resource count
        if (performance.getEntriesByType) {{
            const resources = performance.getEntriesByType('resource');
            document.getElementById('resource-count').textContent = resources.length;
        }}
    }}
    
    startMonitoring() {{
        // Monitor performance every 5 seconds
        setInterval(() => {{
            this.updateMetrics();
        }}, 5000);
    }}
    
    updateMetrics() {{
        if (performance.memory) {{
            const memoryMB = Math.round(performance.memory.usedJSHeapSize / 1024 / 1024);
            document.getElementById('memory-usage').textContent = memoryMB;
        }}
    }}
    
    generateRecommendations() {{
        const recommendations = [];
        
        // Check load time
        const loadTime = parseInt(document.getElementById('load-time').textContent);
        if (loadTime > 3000) {{
            recommendations.push({{
                type: 'warning',
                message: 'Page load time is over 3 seconds. Consider optimizing images and reducing bundle size.',
                priority: 'high'
            }});
        }}
        
        // Check DOM complexity
        const domNodes = parseInt(document.getElementById('dom-nodes').textContent);
        if (domNodes > 1500) {{
            recommendations.push({{
                type: 'info',
                message: 'High DOM complexity detected. Consider reducing the number of elements.',
                priority: 'medium'
            }});
        }}
        
        // Check memory usage
        const memory = parseInt(document.getElementById('memory-usage').textContent);
        if (memory > 50) {{
            recommendations.push({{
                type: 'warning',
                message: 'High memory usage detected. Check for memory leaks.',
                priority: 'high'
            }});
        }}
        
        // Check resource count
        const resources = parseInt(document.getElementById('resource-count').textContent);
        if (resources > 50) {{
            recommendations.push({{
                type: 'info',
                message: 'Many resources loaded. Consider bundling and minification.',
                priority: 'medium'
            }});
        }}
        
        return recommendations;
    }}
    
    displayRecommendations() {{
        const recommendations = this.generateRecommendations();
        const container = document.getElementById('perf-recommendations');
        
        if (recommendations.length === 0) {{
            container.innerHTML = '<li class="list-group-item text-success"><i class="fas fa-check me-2"></i>No performance issues detected</li>';
            return;
        }}
        
        container.innerHTML = recommendations.map(rec => {{
            const iconClass = rec.type === 'warning' ? 'exclamation-triangle text-warning' : 'info-circle text-info';
            const priorityBadge = rec.priority === 'high' ? 'badge bg-danger' : 'badge bg-secondary';
            
            return `
            <li class="list-group-item d-flex justify-content-between align-items-start">
                <div>
                    <i class="fas fa-${{iconClass}} me-2"></i>
                    ${{rec.message}}
                </div>
                <span class="${{priorityBadge}}">${{rec.priority}}</span>
            </li>`;
        }}).join('');
    }}
}}

function runPerformanceTest() {{
    const profiler = new PerformanceProfiler();
    profiler.displayRecommendations();
    
    // Show loading state
    const button = event.target;
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Running...';
    button.disabled = true;
    
    setTimeout(() => {{
        button.innerHTML = originalText;
        button.disabled = false;
    }}, 2000);
}}

function exportReport() {{
    const metrics = {{
        loadTime: document.getElementById('load-time').textContent,
        domNodes: document.getElementById('dom-nodes').textContent,
        memoryUsage: document.getElementById('memory-usage').textContent,
        resourceCount: document.getElementById('resource-count').textContent,
        timestamp: new Date().toISOString()
    }};
    
    const blob = new Blob([JSON.stringify(metrics, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'performance-report.json';
    a.click();
    URL.revokeObjectURL(url);
}}

// Initialize profiler
document.addEventListener('DOMContentLoaded', function() {{
    const profiler = new PerformanceProfiler();
}});
</script>'''


class SEOOptimizer(ComponentBase):
    """SEO optimization checker and tools"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        seo_id = f"seo_optimizer_{id(self)}"
        
        return f'''<div id="{seo_id}" class="seo-optimizer {self.css_class}" style="{self.style}">
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <i class="fas fa-search me-2"></i>
                SEO Optimizer
            </h5>
        </div>
        <div class="card-body">
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="text-center">
                        <div class="h4" id="seo-score">--</div>
                        <small class="text-muted">SEO Score</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center">
                        <div class="h4 text-success" id="meta-tags">--</div>
                        <small class="text-muted">Meta Tags</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center">
                        <div class="h4 text-info" id="heading-structure">--</div>
                        <small class="text-muted">Heading Structure</small>
                    </div>
                </div>
            </div>
            
            <div class="seo-checklist">
                <h6>SEO Checklist</h6>
                <div id="seo-checklist" class="row">
                    <!-- Checklist items will be populated here -->
                </div>
            </div>
            
            <div class="seo-suggestions mt-4">
                <h6>Optimization Suggestions</h6>
                <div id="seo-suggestions" class="alert alert-info">
                    Click "Analyze Page" to get SEO recommendations
                </div>
            </div>
            
            <div class="mt-3">
                <button type="button" class="btn btn-primary me-2" onclick="analyzeSEO()">
                    <i class="fas fa-search me-2"></i>Analyze Page
                </button>
                <button type="button" class="btn btn-outline-secondary" onclick="exportSEOReport()">
                    <i class="fas fa-file-download me-2"></i>Export Report
                </button>
            </div>
        </div>
    </div>
</div>

<script>
class SEOOptimizer {{
    constructor() {{
        this.checks = [
            {{ name: 'Title Tag', check: () => document.title.length > 0 && document.title.length <= 60 }},
            {{ name: 'Meta Description', check: () => {{
                const meta = document.querySelector('meta[name="description"]');
                return meta && meta.content.length > 0 && meta.content.length <= 160;
            }} }},
            {{ name: 'H1 Tag', check: () => document.querySelectorAll('h1').length === 1 }},
            {{ name: 'Alt Text', check: () => {{
                const images = document.querySelectorAll('img');
                return Array.from(images).every(img => img.alt && img.alt.trim().length > 0);
            }} }},
            {{ name: 'Internal Links', check: () => document.querySelectorAll('a[href^="/"], a[href^="#"]').length > 0 }},
            {{ name: 'Meta Viewport', check: () => document.querySelector('meta[name="viewport"]') !== null }},
            {{ name: 'Schema Markup', check: () => {{
                return document.querySelectorAll('[itemtype], script[type="application/ld+json"]').length > 0;
            }} }},
            {{ name: 'Canonical URL', check: () => document.querySelector('link[rel="canonical"]') !== null }}
        ];
    }}
    
    analyze() {{
        const results = this.checks.map(check => ({{
            name: check.name,
            passed: check.check()
        }}));
        
        const passedChecks = results.filter(r => r.passed).length;
        const score = Math.round((passedChecks / results.length) * 100);
        
        // Update UI
        this.updateScoreDisplay(score);
        this.updateChecklist(results);
        this.generateSuggestions(results);
        
        return {{ score, results }};
    }}
    
    updateScoreDisplay(score) {{
        const scoreElement = document.getElementById('seo-score');
        scoreElement.textContent = score + '%';
        scoreElement.className = 'h4 ' + (score >= 80 ? 'text-success' : score >= 60 ? 'text-warning' : 'text-danger');
        
        // Update meta tags count
        const metaTags = document.querySelectorAll('meta').length;
        document.getElementById('meta-tags').textContent = metaTags;
        
        // Update heading structure
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6').length;
        document.getElementById('heading-structure').textContent = headings;
    }}
    
    updateChecklist(results) {{
        const container = document.getElementById('seo-checklist');
        container.innerHTML = results.map(result => {{
            const iconClass = result.passed ? 'check text-success' : 'times text-danger';
            const statusText = result.passed ? 'Passed' : 'Failed';
            
            return `
            <div class="col-md-6 mb-2">
                <div class="d-flex align-items-center">
                    <i class="fas fa-${{iconClass}} me-2"></i>
                    <span>${{result.name}}</span>
                    <small class="ms-auto text-muted">${{statusText}}</small>
                </div>
            </div>`;
        }}).join('');
    }}
    
    generateSuggestions(results) {{
        const failedChecks = results.filter(r => !r.passed);
        const container = document.getElementById('seo-suggestions');
        
        if (failedChecks.length === 0) {{
            container.innerHTML = '<div class="alert alert-success"><i class="fas fa-check me-2"></i>Great! All SEO checks passed.</div>';
            return;
        }}
        
        const suggestions = {{
            'Title Tag': 'Add a descriptive title tag (1-60 characters) to your page.',
            'Meta Description': 'Add a meta description (120-160 characters) that summarizes your page content.',
            'H1 Tag': 'Use exactly one H1 tag per page for the main heading.',
            'Alt Text': 'Add descriptive alt text to all images for accessibility and SEO.',
            'Internal Links': 'Add internal links to help users navigate and improve SEO.',
            'Meta Viewport': 'Add a viewport meta tag for mobile responsiveness.',
            'Schema Markup': 'Add structured data markup to help search engines understand your content.',
            'Canonical URL': 'Add a canonical URL to prevent duplicate content issues.'
        }};
        
        const suggestionHTML = failedChecks.map(check => {{
            return `<li><strong>${{check.name}}:</strong> ${{suggestions[check.name] || 'Needs improvement'}}</li>`;
        }}).join('');
        
        container.innerHTML = `
        <div class="alert alert-warning">
            <h6><i class="fas fa-exclamation-triangle me-2"></i>Recommendations:</h6>
            <ul class="mb-0">${{suggestionHTML}}</ul>
        </div>`;
    }}
}}

function analyzeSEO() {{
    const optimizer = new SEOOptimizer();
    const results = optimizer.analyze();
    
    console.log('SEO Analysis Results:', results);
}}

function exportSEOReport() {{
    const optimizer = new SEOOptimizer();
    const results = optimizer.analyze();
    
    const report = {{
        url: window.location.href,
        timestamp: new Date().toISOString(),
        score: results.score,
        checks: results.results,
        title: document.title,
        metaDescription: document.querySelector('meta[name="description"]')?.content || 'Not found'
    }};
    
    const blob = new Blob([JSON.stringify(report, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'seo-report.json';
    a.click();
    URL.revokeObjectURL(url);
}}
</script>'''


class CodeSplitter(ComponentBase):
    """Code splitting and lazy loading utilities"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        return '''<script>
// Code Splitting and Lazy Loading Manager
class CodeSplitter {
    constructor() {
        this.loadedModules = new Set();
        this.loadingPromises = new Map();
        this.init();
    }
    
    init() {
        this.setupIntersectionObserver();
        this.setupDynamicImports();
    }
    
    setupIntersectionObserver() {
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        this.loadLazyComponent(entry.target);
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                rootMargin: '50px'
            });
            
            document.querySelectorAll('[data-lazy-load]').forEach(element => {
                observer.observe(element);
            });
        }
    }
    
    async loadLazyComponent(element) {
        const componentName = element.dataset.lazyLoad;
        
        if (this.loadedModules.has(componentName)) {
            return;
        }
        
        try {
            element.innerHTML = '<div class="text-center p-3"><div class="spinner-border" role="status"></div></div>';
            
            // Simulate dynamic import
            await this.dynamicImport(componentName);
            
            this.loadedModules.add(componentName);
            element.innerHTML = `<div class="alert alert-success">Component "${componentName}" loaded!</div>`;
            
        } catch (error) {
            console.error(`Failed to load component ${componentName}:`, error);
            element.innerHTML = `<div class="alert alert-danger">Failed to load component "${componentName}"</div>`;
        }
    }
    
    async dynamicImport(moduleName) {
        if (this.loadingPromises.has(moduleName)) {
            return this.loadingPromises.get(moduleName);
        }
        
        const promise = new Promise((resolve) => {
            // Simulate network delay
            setTimeout(resolve, 1000 + Math.random() * 1000);
        });
        
        this.loadingPromises.set(moduleName, promise);
        return promise;
    }
    
    preloadModule(moduleName) {
        if (!this.loadedModules.has(moduleName) && !this.loadingPromises.has(moduleName)) {
            this.dynamicImport(moduleName);
        }
    }
    
    // Critical CSS extraction
    extractCriticalCSS() {
        const criticalStyles = [];
        const viewportHeight = window.innerHeight;
        
        document.querySelectorAll('*').forEach(element => {
            const rect = element.getBoundingClientRect();
            if (rect.top < viewportHeight) {
                const styles = window.getComputedStyle(element);
                criticalStyles.push({
                    selector: this.generateSelector(element),
                    styles: this.extractImportantStyles(styles)
                });
            }
        });
        
        return criticalStyles;
    }
    
    generateSelector(element) {
        if (element.id) return `#${element.id}`;
        if (element.className) return `.${element.className.split(' ')[0]}`;
        return element.tagName.toLowerCase();
    }
    
    extractImportantStyles(styles) {
        const important = [
            'display', 'position', 'width', 'height', 'margin', 'padding',
            'background', 'color', 'font-size', 'font-family', 'line-height'
        ];
        
        const extracted = {};
        important.forEach(prop => {
            if (styles[prop] && styles[prop] !== 'auto') {
                extracted[prop] = styles[prop];
            }
        });
        
        return extracted;
    }
}

// Initialize code splitter
document.addEventListener('DOMContentLoaded', function() {
    window.codeSplitter = new CodeSplitter();
});

// Image optimization utilities
class ImageOptimizer {
    static createWebPFallback(imgElement) {
        if (!imgElement.src) return;
        
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        const img = new Image();
        img.onload = function() {
            canvas.width = this.width;
            canvas.height = this.height;
            ctx.drawImage(this, 0, 0);
            
            // Try to create WebP
            canvas.toBlob((blob) => {
                if (blob) {
                    const webpUrl = URL.createObjectURL(blob);
                    const picture = document.createElement('picture');
                    
                    const webpSource = document.createElement('source');
                    webpSource.srcset = webpUrl;
                    webpSource.type = 'image/webp';
                    
                    const fallbackImg = imgElement.cloneNode(true);
                    
                    picture.appendChild(webpSource);
                    picture.appendChild(fallbackImg);
                    
                    imgElement.parentNode.replaceChild(picture, imgElement);
                }
            }, 'image/webp', 0.8);
        };
        
        img.src = imgElement.src;
    }
    
    static lazyLoadImages() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });
            
            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }
}

// Initialize image optimization
document.addEventListener('DOMContentLoaded', function() {
    ImageOptimizer.lazyLoadImages();
});
</script>'''