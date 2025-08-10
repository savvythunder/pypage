# PyPage Testing Application

This testing application provides a comprehensive testing environment for the PyPage library. It demonstrates all features and serves as both a testing tool and documentation generator.

## Features

- **Basic Components Testing**: Tests core elements like Page, Heading, Paragraph, Lists, Images, etc.
- **Advanced Components Testing**: Tests forms, navigation, layout system, alerts, badges
- **CSS Builder Testing**: Tests custom CSS generation and responsive design
- **Data Visualization Testing**: Tests charts, graphs, and KPI cards
- **Animation Testing**: Tests fade in, slide up, and scroll animations
- **Dark Mode Testing**: Tests dark mode toggle and theme switching

## Running the Tests

1. Start the testing application:
```bash
cd testing
python app.py
```

2. Open your browser to `http://localhost:5001`

3. Use the interface to run individual tests or all tests at once

## Test Results

Each test generates:
- HTML output demonstrating the feature
- Pass/fail status
- Error details if any issues occur
- Preview capability to see the generated HTML

## Adding New Tests

To add a new test:

1. Create a new method in the `PyPageTester` class
2. Follow the naming convention `test_feature_name`
3. Add the test to the `run_all_tests` method
4. Add a button to the web interface

## Documentation Generation

The testing application can be used to generate documentation by:
- Running all tests to capture feature examples
- Exporting the generated HTML for documentation
- Creating screenshots of the rendered components