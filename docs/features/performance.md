# Performance Optimization

HTML Generator v3.0 includes comprehensive performance optimization tools to help you build fast, efficient web applications. This guide covers all the performance features and best practices.

## Hot Reload for Development

### HotReloadManager Component

Enable hot reload for instant development feedback:

```python
from html_generator import HotReloadManager

# Enable hot reload in development
if page.is_development():
    hot_reload = HotReloadManager(enabled=True)
    page.add_content(hot_reload)
```

### Features
- **CSS Hot Reload**: Instant CSS updates without page refresh
- **JavaScript Reload**: Automatic page reload for JS changes
- **File Watching**: Monitors file changes every second
- **Visual Indicators**: Shows reload status in the corner
- **Smart Reloading**: Only reloads necessary resources

### Configuration

```python
# Custom configuration
hot_reload = HotReloadManager(
    enabled=True,
    check_interval=500,  # Check every 500ms
    auto_reload_css=True,
    auto_reload_js=False  # Manual reload for JS
)
```

## Performance Profiling

### PerformanceProfiler Component

Monitor and analyze your application's performance:

```python
from html_generator import PerformanceProfiler

# Add performance profiler to your page
profiler = PerformanceProfiler()
page.add_content(profiler)
```

### Metrics Tracked

1. **Load Time**: Total page load time in milliseconds
2. **DOM Nodes**: Number of DOM elements
3. **Memory Usage**: JavaScript heap size
4. **Resource Count**: Number of loaded resources
5. **Render Performance**: Frame rate and rendering metrics

### Performance Recommendations

The profiler automatically generates recommendations:

- **Load Time > 3s**: Suggests image optimization and bundle reduction
- **High DOM Complexity**: Recommends reducing element count
- **Memory Issues**: Identifies potential memory leaks
- **Resource Optimization**: Suggests bundling and minification

### Custom Performance Monitoring

```python
# Add custom performance tracking
class CustomProfiler(PerformanceProfiler):
    def collect_custom_metrics(self):
        # Track custom metrics
        api_response_time = self.measure_api_calls()
        database_query_time = self.measure_database()
        
        return {
            'api_response_time': api_response_time,
            'database_query_time': database_query_time
        }

profiler = CustomProfiler()
page.add_content(profiler)
```

## WebAssembly Integration

### WebAssemblyRenderer Component

Leverage WebAssembly for high-performance rendering:

```python
from html_generator import WebAssemblyRenderer

# Enable WebAssembly rendering
wasm_renderer = WebAssemblyRenderer(enabled=True)
page.add_content(wasm_renderer)

# Use for performance-critical components
large_table = Table(data=large_dataset)
optimized_table = wasm_renderer.fast_render(large_table)
page.add_content(optimized_table)
```

### Performance Benefits

- **5x Faster Rendering**: WebAssembly provides near-native performance
- **Memory Efficiency**: Optimized memory management
- **CPU Optimization**: Efficient use of multiple cores
- **Fallback Support**: Automatic JavaScript fallback

### WebAssembly Features

```python
# Memory pooling for frequent operations
wasm_renderer.enable_memory_pooling()

# Batch DOM operations
wasm_renderer.enable_batch_processing()

# Performance monitoring
wasm_renderer.enable_performance_tracking()
```

## Image Optimization

### ImageOptimizer Component

Automatic image optimization and lazy loading:

```python
from html_generator import ImageOptimizer

# Enable image optimization
optimizer = ImageOptimizer()
page.add_content(optimizer)
```

### Optimization Features

1. **WebP Conversion**: Automatic WebP format conversion
2. **Lazy Loading**: Load images only when visible
3. **Responsive Images**: Generate multiple sizes
4. **Progressive Loading**: Low-res placeholder first
5. **Error Handling**: Graceful fallback for failed loads

### Manual Image Optimization

```python
# Optimize specific images
image = Image("large-photo.jpg", "Description")

# Enable lazy loading
image.add_class("img-lazy")
image.set_attribute("data-src", "large-photo.jpg")

# Add responsive sizes
image.set_attribute("srcset", "small.jpg 480w, medium.jpg 768w, large.jpg 1200w")
image.set_attribute("sizes", "(max-width: 768px) 100vw, 50vw")

# Progressive loading
optimizer.setup_progressive_loading(image)
```

## Critical CSS Extraction

### CriticalCSSExtractor Component

Extract and inline critical CSS for faster initial loads:

```python
from html_generator import CriticalCSSExtractor

# Extract critical CSS
extractor = CriticalCSSExtractor()
page.add_content(extractor)

# In production
if page.is_production():
    critical_css = extractor.extract()
    page.add_critical_css(critical_css)
```

### Critical CSS Benefits

- **Faster First Paint**: Inline critical styles
- **Reduced Render Blocking**: Defer non-critical CSS
- **Better Performance Scores**: Improved Lighthouse scores
- **Automatic Extraction**: Identifies above-the-fold styles

### Custom Critical CSS

```python
# Manual critical CSS definition
critical_styles = """
.hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    height: 100vh;
    display: flex;
    align-items: center;
}
"""

page.add_critical_css(critical_styles)
```

## Code Splitting and Lazy Loading

### CodeSplitter Component

Implement code splitting for better performance:

```python
from html_generator import CodeSplitter

# Enable code splitting
code_splitter = CodeSplitter()
page.add_content(code_splitter)
```

### Lazy Loading Components

```python
# Mark components for lazy loading
heavy_component = DataVisualization(large_dataset)
heavy_component.set_attribute("data-lazy-load", "data-viz")

# Preload critical components
code_splitter.preload_module("critical-charts")
```

### Dynamic Imports

```javascript
// Client-side dynamic imports
async function loadComponent(componentName) {
    try {
        const module = await import(`/components/${componentName}.js`);
        return module.default;
    } catch (error) {
        console.error(`Failed to load ${componentName}:`, error);
        return null;
    }
}
```

## SEO Optimization

### SEOOptimizer Component

Built-in SEO analysis and optimization:

```python
from html_generator import SEOOptimizer

# Add SEO optimizer
seo = SEOOptimizer()
page.add_content(seo)
```

### SEO Checks

1. **Title Tag**: Length and presence validation
2. **Meta Description**: Optimal length checking
3. **Heading Structure**: Proper H1-H6 hierarchy
4. **Alt Text**: Image accessibility
5. **Internal Links**: Link structure analysis
6. **Schema Markup**: Structured data validation
7. **Mobile Optimization**: Viewport and responsiveness

### SEO Best Practices

```python
# Optimize page metadata
page.set_title("HTML Generator - Python Web Development Tool")
page.set_meta_description("Create responsive web pages with Python using our advanced HTML generator library.")
page.set_meta_keywords(["HTML", "Python", "web development", "generator"])

# Add structured data
page.add_schema_markup({
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "HTML Generator",
    "applicationCategory": "DeveloperApplication",
    "operatingSystem": "Web Browser"
})

# Optimize images for SEO
image = Image("product.jpg", "HTML Generator interface showing code editor")
image.set_attribute("title", "HTML Generator Code Editor")
```

## Performance Best Practices

### Page Optimization

```python
# Enable all performance features
def create_optimized_page(title, description):
    page = Page(title, description)
    
    # Enable WebAssembly
    page.add_content(WebAssemblyRenderer())
    
    # Add image optimization
    page.add_content(ImageOptimizer())
    
    # Extract critical CSS
    page.add_content(CriticalCSSExtractor())
    
    # Enable code splitting
    page.add_content(CodeSplitter())
    
    # Add performance monitoring
    page.add_content(PerformanceProfiler())
    
    # SEO optimization
    page.add_content(SEOOptimizer())
    
    return page
```

### Component Optimization

```python
# Optimize heavy components
class OptimizedDataTable(Table):
    def __init__(self, data, **kwargs):
        super().__init__(data, **kwargs)
        
        # Enable virtual scrolling for large datasets
        if len(data) > 100:
            self.enable_virtual_scrolling()
        
        # Lazy load non-visible rows
        self.enable_lazy_rows()
        
        # Use WebAssembly for sorting
        self.enable_wasm_sorting()
    
    def enable_virtual_scrolling(self):
        self.add_class("virtual-scroll")
        self.set_attribute("data-virtual", "true")
    
    def enable_lazy_rows(self):
        self.add_class("lazy-rows")
        
    def enable_wasm_sorting(self):
        self.set_attribute("data-wasm-sort", "true")
```

### Resource Optimization

```python
# Optimize CSS delivery
page.add_css_link("/css/critical.css", critical=True)
page.add_css_link("/css/non-critical.css", preload=True)

# Optimize JavaScript loading
page.add_js_script("/js/critical.js", defer=False)
page.add_js_script("/js/features.js", async=True)

# Preload important resources
page.add_preload("/fonts/inter.woff2", "font", "font/woff2")
page.add_preload("/images/hero.webp", "image")
```

## Performance Monitoring

### Real-time Monitoring

```python
# Enable continuous performance monitoring
page.enable_performance_monitoring(interval=5000)  # Every 5 seconds

# Set performance budgets
page.set_performance_budget({
    'load_time': 3000,  # 3 seconds max
    'memory_usage': 50,  # 50MB max
    'dom_nodes': 1500   # 1500 elements max
})

# Alert on budget violations
page.on_budget_violation(lambda metric, value: 
    print(f"Performance budget exceeded: {metric} = {value}")
)
```

### Performance Analytics

```python
# Track performance metrics
page.track_performance_metric('custom_metric', value)

# Export performance data
performance_data = page.get_performance_data()
page.export_performance_report('performance-report.json')
```

## Testing Performance

### Performance Testing

```python
# Performance test suite
class PerformanceTests:
    def test_page_load_time(self):
        page = create_optimized_page("Test", "Performance test")
        
        start_time = time.time()
        html = page.generate_html()
        end_time = time.time()
        
        generation_time = (end_time - start_time) * 1000
        assert generation_time < 100, f"Page generation took {generation_time}ms"
    
    def test_memory_usage(self):
        page = create_large_page()
        initial_memory = get_memory_usage()
        
        html = page.generate_html()
        
        final_memory = get_memory_usage()
        memory_increase = final_memory - initial_memory
        
        assert memory_increase < 10, f"Memory increased by {memory_increase}MB"
```

### Benchmarking

```python
# Benchmark different approaches
def benchmark_rendering():
    data = generate_test_data(1000)
    
    # Test regular rendering
    start = time.time()
    regular_table = Table(data)
    regular_html = regular_table.render()
    regular_time = time.time() - start
    
    # Test WebAssembly rendering
    start = time.time()
    wasm_table = WebAssemblyRenderer().fast_render(Table(data))
    wasm_time = time.time() - start
    
    print(f"Regular rendering: {regular_time:.3f}s")
    print(f"WebAssembly rendering: {wasm_time:.3f}s")
    print(f"Speedup: {regular_time / wasm_time:.1f}x")
```

## Next Steps

- Learn about [WebAssembly Integration](./webassembly.md) for maximum performance
- Explore [Modern UI Components](./modern-ui.md) with performance in mind
- Check [Advanced Examples](../examples/advanced.md) for real-world optimization
- Review [Accessibility Guidelines](./accessibility.md) for inclusive performance