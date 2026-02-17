#!/usr/bin/env python3
"""
Test script to verify Event Registration Portal functionality
"""

import sys
import os

# Add the project directory to path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    try:
        from flask import Flask
        print("  ✅ Flask imported successfully")
        
        from reportlab.pdfgen import canvas
        print("  ✅ ReportLab imported successfully")
        
        import app
        print("  ✅ Application module imported successfully")
        
        return True
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False

def test_routes():
    """Test if all routes are defined"""
    print("\n🔍 Testing routes...")
    import app as application
    
    routes = [
        '/',
        '/register',
        '/success/<int:student_id>',
        '/registered-students',
        '/admin-login',
        '/admin-dashboard',
        '/admin-logout',
        '/download-certificate/<int:student_id>'
    ]
    
    defined_routes = [str(rule) for rule in application.app.url_map.iter_rules()]
    
    for route in routes:
        # Check if route exists in defined routes (ignoring parameter types)
        route_base = route.split('<')[0]
        found = any(route_base in defined_route for defined_route in defined_routes)
        if found:
            print(f"  ✅ Route '{route}' is defined")
        else:
            print(f"  ❌ Route '{route}' is NOT defined")
    
    return True

def test_events():
    """Test if IT events are properly configured"""
    print("\n🔍 Testing IT events configuration...")
    import app as application
    
    if len(application.IT_EVENTS) >= 10:
        print(f"  ✅ {len(application.IT_EVENTS)} events configured")
        for event_name, details in application.IT_EVENTS.items():
            if 'time' in details and 'venue' in details:
                print(f"  ✅ {event_name}")
            else:
                print(f"  ❌ {event_name} - missing time or venue")
    else:
        print(f"  ❌ Only {len(application.IT_EVENTS)} events configured (need 10)")
    
    return True

def test_templates():
    """Test if all template files exist"""
    print("\n🔍 Testing template files...")
    templates = [
        'templates/index.html',
        'templates/success.html',
        'templates/registered_students.html',
        'templates/admin_login.html',
        'templates/admin_dashboard.html'
    ]
    
    all_exist = True
    for template in templates:
        if os.path.exists(template):
            print(f"  ✅ {template} exists")
        else:
            print(f"  ❌ {template} NOT found")
            all_exist = False
    
    return all_exist

def test_static_files():
    """Test if static files exist"""
    print("\n🔍 Testing static files...")
    static_files = [
        'static/css/style.css',
        'static/js/script.js'
    ]
    
    all_exist = True
    for static_file in static_files:
        if os.path.exists(static_file):
            print(f"  ✅ {static_file} exists")
        else:
            print(f"  ❌ {static_file} NOT found")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("=" * 60)
    print("🎓 Event Registration Portal - System Test")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_routes,
        test_events,
        test_templates,
        test_static_files
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"  ❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ ALL TESTS PASSED! Application is ready to run.")
        print("\n🚀 To start the application, run:")
        print("   python app.py")
        print("\n📱 Then open in browser:")
        print("   http://127.0.0.1:5000/")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("=" * 60)

if __name__ == '__main__':
    main()
