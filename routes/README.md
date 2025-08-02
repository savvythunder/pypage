# Flask Routes Directory

This directory contains the Flask route handlers for the HTML Generator web application, organized into logical modules for maintainability and scalability.

## Route Structure

### Core Route Modules

- `main.py` - Primary web interface routes (pages, editor, gallery)
- `api.py` - RESTful API endpoints for programmatic access
- `config.py` - Configuration and visual tool routes
- `docs.py` - Documentation and help system routes

## Route Organization

### Main Routes (`main.py`)
- `/` - Home page with overview and quick start
- `/editor` - Interactive code editor with live preview
- `/gallery` - Generated page gallery and management
- `/examples` - Code examples and templates
- `/preview/<page_id>` - Preview generated pages

### API Routes (`api.py`)
- `/api/pages` - CRUD operations for generated pages
- `/api/generate` - HTML generation from Python code
- `/api/validate` - Code validation and syntax checking
- `/api/export` - Export functionality (PDF, JSON)
- `/api/hot-reload` - Hot reload support for development

### Configuration Routes (`config.py`)
- `/navbar-builder` - Visual navbar configuration tool
- `/css-builder` - Interactive CSS rule builder
- `/theme-selector` - Theme switching interface
- `/performance` - Performance monitoring dashboard

### Documentation Routes (`docs.py`)
- `/docs` - Documentation home page
- `/docs/<path>` - Dynamic documentation serving
- `/docs/api` - API reference and examples
- `/docs/search` - Documentation search functionality

## Route Features

### Modern Web Standards
- **RESTful Design**: Consistent API patterns
- **JSON API**: Structured data exchange
- **Error Handling**: Comprehensive error responses
- **Validation**: Input sanitization and validation
- **Security**: CSRF protection and input validation

### Performance Optimizations
- **Caching**: Route-level caching for static content
- **Compression**: Gzip compression for responses
- **CDN Integration**: Static asset optimization
- **Database Optimization**: Efficient query patterns

### User Experience
- **Progressive Enhancement**: JavaScript enhancement over HTML
- **Mobile Responsive**: Touch-friendly interfaces
- **Accessibility**: WCAG compliant routes
- **Internationalization**: Multi-language support ready

## Route Implementation Examples

### Basic Route Pattern

```python
@main_bp.route('/example')
def example_route():
    """Example route with error handling and logging"""
    try:
        # Route logic here
        return render_template('example.html', data=data)
    except Exception as e:
        logger.error(f"Error in example route: {str(e)}")
        return render_template('error.html', error=str(e)), 500
```

### API Route Pattern

```python
@api_bp.route('/api/resource', methods=['GET', 'POST'])
def api_resource():
    """RESTful API endpoint with JSON responses"""
    if request.method == 'GET':
        # Handle GET request
        return jsonify({'status': 'success', 'data': data})
    
    elif request.method == 'POST':
        # Handle POST request
        try:
            data = request.get_json()
            # Process data
            return jsonify({'status': 'success', 'message': 'Created'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 400
```

### Configuration Route Pattern

```python
@config_bp.route('/config/tool')
def config_tool():
    """Configuration interface with form handling"""
    form = ConfigForm()
    
    if form.validate_on_submit():
        # Save configuration
        flash('Configuration saved successfully', 'success')
        return redirect(url_for('config.config_tool'))
    
    return render_template('config/tool.html', form=form)
```

## Security Considerations

### Input Validation
- Sanitize all user inputs
- Validate file uploads
- Check request size limits
- Prevent code injection

### Authentication & Authorization
- Session management
- CSRF protection
- Rate limiting
- Permission checking

### Data Protection
- SQL injection prevention
- XSS protection
- Secure headers
- Environment variable protection

## Error Handling

### Consistent Error Responses

```python
def handle_api_error(error):
    """Standardized API error handling"""
    return jsonify({
        'status': 'error',
        'message': str(error),
        'code': getattr(error, 'code', 500),
        'timestamp': datetime.utcnow().isoformat()
    }), getattr(error, 'code', 500)

# Register error handlers
@api_bp.errorhandler(400)
def bad_request(error):
    return handle_api_error(error)

@api_bp.errorhandler(404)
def not_found(error):
    return handle_api_error(error)

@api_bp.errorhandler(500)
def internal_error(error):
    return handle_api_error(error)
```

## Testing Routes

### Unit Testing

```python
def test_main_routes(client):
    """Test main application routes"""
    
    # Test home page
    response = client.get('/')
    assert response.status_code == 200
    assert b'HTML Generator' in response.data
    
    # Test editor page
    response = client.get('/editor')
    assert response.status_code == 200
    
    # Test gallery page
    response = client.get('/gallery')
    assert response.status_code == 200

def test_api_routes(client):
    """Test API endpoints"""
    
    # Test page creation
    response = client.post('/api/pages', 
        json={'title': 'Test', 'code': 'page = Page("Test")'})
    assert response.status_code == 201
    
    # Test page retrieval
    response = client.get('/api/pages')
    assert response.status_code == 200
    assert 'data' in response.get_json()
```

### Integration Testing

```python
def test_full_workflow(client):
    """Test complete user workflow"""
    
    # Create page via editor
    response = client.post('/editor/generate', data={
        'title': 'Test Page',
        'code': 'page = Page("Test", "Description")\npage.add_content(Heading("Hello"))'
    })
    assert response.status_code == 200
    
    # Check gallery includes new page
    response = client.get('/gallery')
    assert b'Test Page' in response.data
    
    # Preview the page
    page_id = extract_page_id(response.data)
    response = client.get(f'/preview/{page_id}')
    assert response.status_code == 200
    assert b'Hello' in response.data
```

## Performance Monitoring

### Route Performance Tracking

```python
@main_bp.before_request
def before_request():
    """Track request start time"""
    g.start_time = time.time()

@main_bp.after_request
def after_request(response):
    """Log request performance"""
    if hasattr(g, 'start_time'):
        duration = time.time() - g.start_time
        logger.info(f"Route {request.endpoint} took {duration:.3f}s")
    return response
```

### Caching Implementation

```python
from flask_caching import Cache

cache = Cache()

@main_bp.route('/cached-content')
@cache.cached(timeout=300)  # 5 minutes
def cached_content():
    """Cached route for static content"""
    # Expensive operation here
    return render_template('static_content.html', data=data)
```

## Development Guidelines

### Code Organization
1. Keep routes focused and single-purpose
2. Use blueprints for logical grouping
3. Implement consistent error handling
4. Add comprehensive logging
5. Write tests for all routes

### Documentation
1. Document all route parameters
2. Provide example requests/responses
3. Explain business logic
4. Include error conditions
5. Maintain API documentation

### Deployment
1. Use environment-specific configurations
2. Implement health check endpoints
3. Set up monitoring and alerting
4. Use reverse proxy for production
5. Enable SSL/TLS

## Next Steps

- Review individual route files for specific implementations
- Check [API Documentation](../docs/web-app/api-reference.md) for endpoint details
- Study [Architecture Guide](../docs/development/architecture.md) for system design
- Explore [Testing Guide](../docs/development/testing.md) for testing strategies