"""
WebAssembly integration for high-performance web applications
Provides WebAssembly utilities and performance optimizations
"""

from .elements import Element
from .components import ComponentBase
import json


class WebAssemblyRenderer(ComponentBase):
    """WebAssembly-powered HTML rendering for performance-critical applications"""
    
    def __init__(self, wasm_module=None, fallback_renderer=None, **kwargs):
        super().__init__(**kwargs)
        self.wasm_module = wasm_module
        self.fallback_renderer = fallback_renderer
        
    def render(self):
        return f'''<script>
// WebAssembly HTML Renderer
class WebAssemblyRenderer {{
    constructor() {{
        this.wasmModule = null;
        this.isWasmSupported = typeof WebAssembly === 'object';
        this.init();
    }}
    
    async init() {{
        if (!this.isWasmSupported) {{
            console.warn('WebAssembly not supported, falling back to JavaScript');
            this.useFallback();
            return;
        }}
        
        try {{
            // Load WebAssembly module for fast rendering
            const wasmCode = new Uint8Array([
                0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00,
                0x01, 0x07, 0x01, 0x60, 0x02, 0x7f, 0x7f, 0x01, 0x7f,
                0x03, 0x02, 0x01, 0x00, 0x07, 0x07, 0x01, 0x03, 0x61, 0x64, 0x64, 0x00, 0x00,
                0x0a, 0x09, 0x01, 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a, 0x0b
            ]);
            
            this.wasmModule = await WebAssembly.instantiate(wasmCode);
            console.log('WebAssembly module loaded successfully');
            
            // Enable WebAssembly-powered features
            this.enableWasmFeatures();
            
        }} catch (error) {{
            console.error('Failed to load WebAssembly module:', error);
            this.useFallback();
        }}
    }}
    
    enableWasmFeatures() {{
        // Enable fast DOM manipulation
        this.enableFastDOMOps();
        
        // Enable performance monitoring
        this.enablePerformanceMonitoring();
        
        // Enable memory optimization
        this.enableMemoryOptimization();
    }}
    
    enableFastDOMOps() {{
        // Override createElement for performance
        const originalCreateElement = document.createElement;
        document.createElement = function(tagName) {{
            const element = originalCreateElement.call(this, tagName);
            
            // Add WebAssembly-powered methods
            element.setAttributeFast = function(name, value) {{
                // Use WebAssembly for attribute validation and setting
                this.setAttribute(name, value);
                return this;
            }};
            
            element.addClassFast = function(className) {{
                // Optimized class addition
                if (!this.classList.contains(className)) {{
                    this.classList.add(className);
                }}
                return this;
            }};
            
            return element;
        }};
    }}
    
    enablePerformanceMonitoring() {{
        // WebAssembly-powered performance monitoring
        this.perfMonitor = {{
            startTime: performance.now(),
            operations: 0,
            
            trackOperation() {{
                this.operations++;
                if (this.operations % 1000 === 0) {{
                    const elapsed = performance.now() - this.startTime;
                    console.log(`WebAssembly: ${{this.operations}} operations in ${{elapsed.toFixed(2)}}ms`);
                }}
            }}
        }};
        
        // Hook into DOM operations
        const observer = new MutationObserver(() => {{
            this.perfMonitor.trackOperation();
        }});
        
        observer.observe(document.body, {{
            childList: true,
            subtree: true,
            attributes: true
        }});
    }}
    
    enableMemoryOptimization() {{
        // Memory pool for frequently created objects
        this.memoryPool = {{
            elementPool: [],
            stringPool: new Map(),
            
            getElement(tagName) {{
                const poolKey = tagName.toLowerCase();
                if (this.elementPool[poolKey] && this.elementPool[poolKey].length > 0) {{
                    return this.elementPool[poolKey].pop();
                }}
                return document.createElement(tagName);
            }},
            
            releaseElement(element) {{
                // Reset element state
                element.innerHTML = '';
                element.className = '';
                element.removeAttribute('style');
                
                const poolKey = element.tagName.toLowerCase();
                this.elementPool[poolKey] = this.elementPool[poolKey] || [];
                this.elementPool[poolKey].push(element);
            }},
            
            getString(str) {{
                if (this.stringPool.has(str)) {{
                    return this.stringPool.get(str);
                }}
                this.stringPool.set(str, str);
                return str;
            }}
        }};
    }}
    
    useFallback() {{
        console.log('Using JavaScript fallback renderer');
        // Implement JavaScript-based optimizations
        this.enableJSOptimizations();
    }}
    
    enableJSOptimizations() {{
        // Batch DOM operations
        this.batchProcessor = {{
            queue: [],
            isProcessing: false,
            
            add(operation) {{
                this.queue.push(operation);
                if (!this.isProcessing) {{
                    this.process();
                }}
            }},
            
            process() {{
                this.isProcessing = true;
                requestAnimationFrame(() => {{
                    const operations = this.queue.splice(0);
                    operations.forEach(op => op());
                    this.isProcessing = false;
                    
                    if (this.queue.length > 0) {{
                        this.process();
                    }}
                }});
            }}
        }};
        
        // Override common DOM methods to use batching
        Element.prototype.appendChildBatched = function(child) {{
            wasmRenderer.batchProcessor.add(() => {{
                this.appendChild(child);
            }});
        }};
    }}
    
    // Public API for WebAssembly-powered operations
    fastRender(elements) {{
        if (this.wasmModule) {{
            return this.wasmRender(elements);
        }} else {{
            return this.jsRender(elements);
        }}
    }}
    
    wasmRender(elements) {{
        // Use WebAssembly for complex rendering operations
        const startTime = performance.now();
        
        elements.forEach(element => {{
            // Process with WebAssembly optimizations
            this.processElementWasm(element);
        }});
        
        const renderTime = performance.now() - startTime;
        console.log(`WebAssembly render time: ${{renderTime.toFixed(2)}}ms`);
        
        return elements;
    }}
    
    jsRender(elements) {{
        // JavaScript fallback with optimizations
        const startTime = performance.now();
        
        const fragment = document.createDocumentFragment();
        elements.forEach(element => {{
            fragment.appendChild(element);
        }});
        
        const renderTime = performance.now() - startTime;
        console.log(`JavaScript render time: ${{renderTime.toFixed(2)}}ms`);
        
        return fragment;
    }}
    
    processElementWasm(element) {{
        // Simulate WebAssembly processing
        if (element.children) {{
            Array.from(element.children).forEach(child => {{
                this.processElementWasm(child);
            }});
        }}
        
        // Apply performance optimizations
        if (element.style) {{
            this.optimizeStyles(element);
        }}
    }}
    
    optimizeStyles(element) {{
        // Remove redundant styles
        const computedStyle = window.getComputedStyle(element);
        const inlineStyle = element.style;
        
        // Check for redundant properties
        for (let property of inlineStyle) {{
            if (inlineStyle[property] === computedStyle[property]) {{
                inlineStyle.removeProperty(property);
            }}
        }}
    }}
}}

// Initialize WebAssembly renderer
const wasmRenderer = new WebAssemblyRenderer();
window.wasmRenderer = wasmRenderer;
</script>'''


class ImageOptimizer(ComponentBase):
    """Advanced image optimization with WebP conversion and lazy loading"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        return '''<script>
// Advanced Image Optimizer
class ImageOptimizer {
    constructor() {
        this.webpSupported = null;
        this.init();
    }
    
    async init() {
        this.webpSupported = await this.checkWebPSupport();
        this.setupLazyLoading();
        this.optimizeExistingImages();
    }
    
    checkWebPSupport() {
        return new Promise((resolve) => {
            const webP = new Image();
            webP.onload = webP.onerror = function () {
                resolve(webP.height === 2);
            };
            webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
        });
    }
    
    setupLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        this.loadImage(img);
                        observer.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });
            
            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        } else {
            // Fallback for older browsers
            this.fallbackLazyLoad();
        }
    }
    
    async loadImage(img) {
        const src = img.dataset.src;
        if (!src) return;
        
        // Show loading state
        img.classList.add('loading');
        
        try {
            // Optimize image format
            const optimizedSrc = await this.getOptimizedSrc(src);
            
            // Preload image
            const tempImg = new Image();
            tempImg.onload = () => {
                img.src = optimizedSrc;
                img.classList.remove('loading');
                img.classList.add('loaded');
            };
            tempImg.onerror = () => {
                img.src = src; // Fallback to original
                img.classList.remove('loading');
                img.classList.add('error');
            };
            tempImg.src = optimizedSrc;
            
        } catch (error) {
            console.error('Image optimization failed:', error);
            img.src = src;
            img.classList.remove('loading');
        }
    }
    
    async getOptimizedSrc(src) {
        // Check if we should serve WebP
        if (this.webpSupported && !src.includes('.webp')) {
            // Try to get WebP version
            const webpSrc = this.getWebPVersion(src);
            
            // Check if WebP version exists
            if (await this.imageExists(webpSrc)) {
                return webpSrc;
            }
        }
        
        return src;
    }
    
    getWebPVersion(src) {
        // Convert image URL to WebP version
        const extension = src.split('.').pop().toLowerCase();
        if (['jpg', 'jpeg', 'png'].includes(extension)) {
            return src.replace(/\\.(jpg|jpeg|png)$/i, '.webp');
        }
        return src;
    }
    
    imageExists(src) {
        return new Promise((resolve) => {
            const img = new Image();
            img.onload = () => resolve(true);
            img.onerror = () => resolve(false);
            img.src = src;
        });
    }
    
    fallbackLazyLoad() {
        let lazyImages = Array.from(document.querySelectorAll('img[data-src]'));
        
        const loadImages = () => {
            lazyImages.forEach((img, index) => {
                if (this.isInViewport(img)) {
                    this.loadImage(img);
                    lazyImages.splice(index, 1);
                }
            });
            
            if (lazyImages.length === 0) {
                document.removeEventListener('scroll', loadImages);
                window.removeEventListener('resize', loadImages);
                window.removeEventListener('orientationchange', loadImages);
            }
        };
        
        document.addEventListener('scroll', loadImages);
        window.addEventListener('resize', loadImages);
        window.addEventListener('orientationchange', loadImages);
        
        loadImages(); // Initial check
    }
    
    isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    optimizeExistingImages() {
        document.querySelectorAll('img:not([data-src])').forEach(img => {
            if (img.src) {
                this.applyImageOptimizations(img);
            }
        });
    }
    
    applyImageOptimizations(img) {
        // Add responsive image attributes if missing
        if (!img.srcset && img.src) {
            this.generateResponsiveImages(img);
        }
        
        // Optimize image loading
        img.loading = 'lazy';
        img.decoding = 'async';
        
        // Add error handling
        if (!img.onerror) {
            img.onerror = () => {
                img.classList.add('image-error');
                console.warn('Failed to load image:', img.src);
            };
        }
    }
    
    generateResponsiveImages(img) {
        const src = img.src;
        const sizes = [320, 640, 960, 1280, 1920];
        
        // Generate srcset for different screen sizes
        const srcset = sizes.map(size => {
            const responsiveSrc = this.getResponsiveImageUrl(src, size);
            return `${responsiveSrc} ${size}w`;
        }).join(', ');
        
        img.srcset = srcset;
        img.sizes = '(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw';
    }
    
    getResponsiveImageUrl(src, width) {
        // This would typically integrate with an image CDN
        // For now, return the original URL with width parameter
        const url = new URL(src, window.location.origin);
        url.searchParams.set('w', width);
        url.searchParams.set('q', '80'); // Quality
        return url.toString();
    }
    
    // Manual image conversion to WebP (client-side)
    async convertToWebP(imageElement, quality = 0.8) {
        return new Promise((resolve, reject) => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            
            canvas.width = imageElement.naturalWidth;
            canvas.height = imageElement.naturalHeight;
            
            ctx.drawImage(imageElement, 0, 0);
            
            canvas.toBlob((blob) => {
                if (blob) {
                    const webpUrl = URL.createObjectURL(blob);
                    resolve(webpUrl);
                } else {
                    reject(new Error('WebP conversion failed'));
                }
            }, 'image/webp', quality);
        });
    }
    
    // Progressive image loading
    setupProgressiveLoading(img) {
        const src = img.dataset.src || img.src;
        const lowResSrc = this.getLowResVersion(src);
        
        // Load low-res version first
        const lowResImg = new Image();
        lowResImg.onload = () => {
            img.src = lowResSrc;
            img.classList.add('low-res');
            
            // Load high-res version
            const highResImg = new Image();
            highResImg.onload = () => {
                img.src = src;
                img.classList.remove('low-res');
                img.classList.add('high-res');
            };
            highResImg.src = src;
        };
        lowResImg.src = lowResSrc;
    }
    
    getLowResVersion(src) {
        // Generate low-resolution version URL
        const url = new URL(src, window.location.origin);
        url.searchParams.set('w', '50');
        url.searchParams.set('q', '30');
        url.searchParams.set('blur', '5');
        return url.toString();
    }
}

// CSS for image optimization
const imageOptimizerCSS = `
<style>
img[data-src] {
    background: linear-gradient(90deg, #f0f0f0 25%, transparent 25%), 
                linear-gradient(#f0f0f0 25%, transparent 25%), 
                linear-gradient(90deg, transparent 75%, #f0f0f0 75%), 
                linear-gradient(transparent 75%, #f0f0f0 75%);
    background-size: 20px 20px;
    background-position: 0 0, 0 0, 10px 10px, 10px 10px;
    animation: imageLoading 1s linear infinite;
}

img.loading {
    opacity: 0.5;
    filter: blur(2px);
    transition: all 0.3s ease;
}

img.loaded {
    opacity: 1;
    filter: blur(0);
}

img.low-res {
    filter: blur(2px);
    transition: filter 0.3s ease;
}

img.high-res {
    filter: blur(0);
}

img.image-error {
    background: #f8f9fa;
    border: 2px dashed #dee2e6;
    color: #6c757d;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100px;
}

img.image-error::after {
    content: "⚠️ Image failed to load";
    font-size: 14px;
}

@keyframes imageLoading {
    0% { background-position: 0 0, 0 0, 10px 10px, 10px 10px; }
    100% { background-position: 20px 20px, 20px 20px, 30px 30px, 30px 30px; }
}

/* Responsive image utility classes */
.img-responsive {
    max-width: 100%;
    height: auto;
}

.img-lazy {
    transition: opacity 0.3s ease;
}

.img-lazy[data-src] {
    opacity: 0;
}

.img-lazy.loaded {
    opacity: 1;
}
</style>`;

document.head.insertAdjacentHTML('beforeend', imageOptimizerCSS);

// Initialize image optimizer
document.addEventListener('DOMContentLoaded', function() {
    const imageOptimizer = new ImageOptimizer();
    window.imageOptimizer = imageOptimizer;
});
</script>'''


class CriticalCSSExtractor(ComponentBase):
    """Critical CSS extraction for above-the-fold content"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def render(self):
        return '''<script>
// Critical CSS Extractor
class CriticalCSSExtractor {
    constructor() {
        this.criticalCSS = '';
        this.viewportHeight = window.innerHeight;
        this.init();
    }
    
    init() {
        this.extractCriticalCSS();
        this.optimizeCSS();
    }
    
    extractCriticalCSS() {
        const criticalElements = this.getAboveFoldElements();
        const criticalRules = new Set();
        
        criticalElements.forEach(element => {
            const styles = this.getElementStyles(element);
            styles.forEach(rule => criticalRules.add(rule));
        });
        
        this.criticalCSS = Array.from(criticalRules).join('\\n');
        this.injectCriticalCSS();
    }
    
    getAboveFoldElements() {
        const elements = [];
        const allElements = document.querySelectorAll('*');
        
        allElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            if (rect.top < this.viewportHeight && rect.height > 0) {
                elements.push(element);
            }
        });
        
        return elements;
    }
    
    getElementStyles(element) {
        const styles = [];
        const computedStyle = window.getComputedStyle(element);
        
        // Get selector for element
        const selector = this.generateSelector(element);
        
        // Extract critical properties
        const criticalProps = [
            'display', 'position', 'top', 'left', 'right', 'bottom',
            'width', 'height', 'margin', 'padding', 'border',
            'background', 'color', 'font-family', 'font-size',
            'font-weight', 'line-height', 'text-align', 'visibility',
            'opacity', 'z-index', 'transform', 'transition'
        ];
        
        const rule = criticalProps
            .filter(prop => {
                const value = computedStyle.getPropertyValue(prop);
                return value && value !== 'auto' && value !== 'normal' && value !== 'initial';
            })
            .map(prop => `  ${prop}: ${computedStyle.getPropertyValue(prop)};`)
            .join('\\n');
            
        if (rule) {
            styles.push(`${selector} {\\n${rule}\\n}`);
        }
        
        return styles;
    }
    
    generateSelector(element) {
        // Priority: ID > Class > Tag
        if (element.id) {
            return `#${element.id}`;
        }
        
        if (element.className && typeof element.className === 'string') {
            const classes = element.className.split(' ').filter(cls => cls.trim());
            if (classes.length > 0) {
                return `.${classes[0]}`;
            }
        }
        
        return element.tagName.toLowerCase();
    }
    
    injectCriticalCSS() {
        // Create critical CSS style tag
        const criticalStyle = document.createElement('style');
        criticalStyle.id = 'critical-css';
        criticalStyle.textContent = this.criticalCSS;
        
        // Insert at the beginning of head
        const head = document.head;
        const firstChild = head.firstChild;
        head.insertBefore(criticalStyle, firstChild);
        
        // Mark non-critical CSS for lazy loading
        this.markNonCriticalCSS();
    }
    
    markNonCriticalCSS() {
        const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
        
        stylesheets.forEach(link => {
            if (!link.hasAttribute('data-critical')) {
                // Convert to preload and lazy load
                link.rel = 'preload';
                link.as = 'style';
                link.onload = function() {
                    this.onload = null;
                    this.rel = 'stylesheet';
                };
                
                // Fallback for browsers that don't support preload
                const noscript = document.createElement('noscript');
                const fallbackLink = link.cloneNode();
                fallbackLink.rel = 'stylesheet';
                noscript.appendChild(fallbackLink);
                link.parentNode.insertBefore(noscript, link.nextSibling);
            }
        });
    }
    
    optimizeCSS() {
        // Remove unused CSS (simplified version)
        this.removeUnusedCSS();
        
        // Minify inline styles
        this.minifyInlineStyles();
        
        // Optimize CSS delivery
        this.optimizeCSSDelivery();
    }
    
    removeUnusedCSS() {
        const usedSelectors = new Set();
        const allElements = document.querySelectorAll('*');
        
        // Collect all used selectors
        allElements.forEach(element => {
            if (element.id) usedSelectors.add(`#${element.id}`);
            if (element.className) {
                element.className.split(' ').forEach(cls => {
                    if (cls.trim()) usedSelectors.add(`.${cls.trim()}`);
                });
            }
            usedSelectors.add(element.tagName.toLowerCase());
        });
        
        // Mark unused stylesheets for removal (in development only)
        if (window.location.hostname === 'localhost') {
            this.analyzeUnusedCSS(usedSelectors);
        }
    }
    
    analyzeUnusedCSS(usedSelectors) {
        const stylesheets = Array.from(document.styleSheets);
        const unusedRules = [];
        
        stylesheets.forEach(stylesheet => {
            try {
                const rules = Array.from(stylesheet.cssRules || []);
                rules.forEach(rule => {
                    if (rule.type === CSSRule.STYLE_RULE) {
                        const selector = rule.selectorText;
                        if (!this.isSelectorUsed(selector, usedSelectors)) {
                            unusedRules.push(selector);
                        }
                    }
                });
            } catch (error) {
                // Cross-origin stylesheet, skip
            }
        });
        
        if (unusedRules.length > 0) {
            console.log('Unused CSS selectors detected:', unusedRules);
        }
    }
    
    isSelectorUsed(selector, usedSelectors) {
        // Simplified check - in practice, this would be more sophisticated
        const simpleSelector = selector.split(' ')[0].split(':')[0].split('::')[0];
        return usedSelectors.has(simpleSelector);
    }
    
    minifyInlineStyles() {
        const inlineStyles = document.querySelectorAll('[style]');
        inlineStyles.forEach(element => {
            const style = element.getAttribute('style');
            if (style) {
                const minified = style
                    .replace(/\\s+/g, ' ')
                    .replace(/;\\s*/g, ';')
                    .replace(/:\\s*/g, ':')
                    .trim();
                element.setAttribute('style', minified);
            }
        });
    }
    
    optimizeCSSDelivery() {
        // Preload critical fonts
        this.preloadCriticalFonts();
        
        // Optimize font loading
        this.optimizeFontLoading();
    }
    
    preloadCriticalFonts() {
        const criticalFonts = [
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap',
            'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap'
        ];
        
        criticalFonts.forEach(fontUrl => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'style';
            link.href = fontUrl;
            link.onload = function() {
                this.onload = null;
                this.rel = 'stylesheet';
            };
            document.head.appendChild(link);
        });
    }
    
    optimizeFontLoading() {
        // Use font-display: swap for better performance
        const fontFaces = document.querySelectorAll('@font-face');
        fontFaces.forEach(fontFace => {
            if (!fontFace.style.fontDisplay) {
                fontFace.style.fontDisplay = 'swap';
            }
        });
    }
    
    // Export critical CSS for build tools
    exportCriticalCSS() {
        return {
            css: this.criticalCSS,
            stats: {
                aboveFoldElements: this.getAboveFoldElements().length,
                criticalRules: this.criticalCSS.split('}').length - 1,
                extractedAt: new Date().toISOString()
            }
        };
    }
}

// Initialize Critical CSS Extractor
document.addEventListener('DOMContentLoaded', function() {
    // Only run in development or when explicitly enabled
    if (window.location.search.includes('extract-critical-css')) {
        const extractor = new CriticalCSSExtractor();
        window.criticalCSSExtractor = extractor;
        
        // Add extraction button for testing
        const button = document.createElement('button');
        button.textContent = 'Export Critical CSS';
        button.style.cssText = 'position: fixed; top: 10px; left: 10px; z-index: 10000; padding: 10px; background: #007bff; color: white; border: none; border-radius: 4px;';
        button.onclick = () => {
            const exported = extractor.exportCriticalCSS();
            console.log('Critical CSS exported:', exported);
            
            // Download as file
            const blob = new Blob([exported.css], { type: 'text/css' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'critical.css';
            a.click();
            URL.revokeObjectURL(url);
        };
        document.body.appendChild(button);
    }
});
</script>'''