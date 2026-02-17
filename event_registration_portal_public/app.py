from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os
import socket
import threading
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# Global variable to store public URL
public_url = None
use_ngrok = False  # Set to True to enable ngrok tunneling

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def start_ngrok():
    """Start ngrok tunnel (optional - requires pyngrok)"""
    global public_url, use_ngrok
    
    try:
        from pyngrok import ngrok
        
        # Kill any existing ngrok processes
        ngrok.kill()
        
        # Start ngrok tunnel
        public_tunnel = ngrok.connect(5000, bind_tls=True)
        public_url = public_tunnel.public_url
        use_ngrok = True
        
        print("\n" + "="*70)
        print("🌐 NGROK TUNNEL ACTIVE - ACCESSIBLE FROM ANYWHERE!")
        print("="*70)
        print(f"📱 Public URL (works on mobile data): {public_url}")
        print("="*70)
        print("✅ Anyone can access this URL - even on mobile data/different WiFi")
        print("="*70 + "\n")
        
    except ImportError:
        print("\n" + "="*70)
        print("⚠️  NGROK NOT INSTALLED - Using local network only")
        print("="*70)
        print("To enable public access (mobile data users):")
        print("1. Install: pip install pyngrok")
        print("2. Restart the application")
        print("="*70 + "\n")
        use_ngrok = False
    except Exception as e:
        print(f"\n⚠️  Ngrok error: {e}")
        print("Using local network only\n")
        use_ngrok = False

# In-memory storage for registered students (in production, use a database)
registered_students = []

# IT Events with predefined timings
IT_EVENTS = {
    'Web Development Workshop': {'time': '9:30 AM - 10:30 AM', 'venue': 'Computer Lab 1'},
    'AI & Machine Learning Seminar': {'time': '11:00 AM - 12:00 PM', 'venue': 'Seminar Hall A'},
    'Cybersecurity Awareness': {'time': '1:00 PM - 2:00 PM', 'venue': 'Auditorium'},
    'Cloud Computing Basics': {'time': '2:30 PM - 3:30 PM', 'venue': 'Computer Lab 2'},
    'Data Science Bootcamp': {'time': '9:00 AM - 11:00 AM', 'venue': 'Conference Room'},
    'Mobile App Development': {'time': '10:00 AM - 11:30 AM', 'venue': 'IT Block - Room 301'},
    'Blockchain Technology': {'time': '12:00 PM - 1:00 PM', 'venue': 'Seminar Hall B'},
    'IoT Innovations': {'time': '3:00 PM - 4:00 PM', 'venue': 'Innovation Lab'},
    'Python Programming Contest': {'time': '9:30 AM - 12:30 PM', 'venue': 'Computer Lab 3'},
    'UI/UX Design Workshop': {'time': '2:00 PM - 3:30 PM', 'venue': 'Design Studio'}
}

# Admin credentials (in production, use hashed passwords and database)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

@app.route('/test')
def test():
    """Test page to verify server is working"""
    return render_template('test.html')

@app.route('/')
def index():
    """Home page with registration form"""
    return render_template('index.html', events=IT_EVENTS)

@app.route('/register', methods=['POST'])
def register():
    """Handle student registration"""
    # Generate registration ID in format HME001, HME002, etc.
    registration_id = f"HME{str(len(registered_students) + 1).zfill(3)}"
    
    student_data = {
        'id': len(registered_students) + 1,
        'registration_id': registration_id,  # New registration ID field
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'register_number': request.form.get('register_number'),
        'department': request.form.get('department'),
        'year': request.form.get('year'),
        'college': request.form.get('college'),
        'events': request.form.getlist('events'),  # Multiple events selection
        'date': request.form.get('date'),
        'registration_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add event details for each selected event
    student_data['event_details'] = []
    for event_name in student_data['events']:
        if event_name in IT_EVENTS:
            student_data['event_details'].append({
                'name': event_name,
                'time': IT_EVENTS[event_name]['time'],
                'venue': IT_EVENTS[event_name]['venue']
            })
    
    registered_students.append(student_data)
    
    return redirect(url_for('success', student_id=student_data['id']))

@app.route('/success/<int:student_id>')
def success(student_id):
    """Registration success page"""
    student = next((s for s in registered_students if s['id'] == student_id), None)
    return render_template('success.html', student=student)

@app.route('/registered-students')
def registered_students_page():
    """Display all registered students"""
    return render_template('registered_students.html', students=registered_students)

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    
    return render_template('admin_login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    """Admin dashboard - requires login"""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    return render_template('admin_dashboard.html', students=registered_students)

@app.route('/admin-logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

# Certificate functionality removed as per user request
# @app.route('/download-certificate/<int:student_id>')
# def download_certificate(student_id):
#     """Generate and download participation certificate"""
#     ... (removed)

@app.route('/get-server-url')
def get_server_url():
    """Get server URL for QR code - returns public URL if available"""
    global public_url, use_ngrok
    
    if use_ngrok and public_url:
        # Use public ngrok URL (accessible from anywhere)
        return jsonify({
            'url': public_url,
            'type': 'public',
            'message': 'Works on mobile data & any network!'
        })
    else:
        # Use local network IP (same WiFi only)
        local_ip = get_local_ip()
        port = request.host.split(':')[1] if ':' in request.host else '5000'
        server_url = f"http://{local_ip}:{port}"
        return jsonify({
            'url': server_url,
            'type': 'local',
            'message': 'Same WiFi network only'
        })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    local_ip = get_local_ip()
    
    print("\n" + "="*70)
    print("🎓 Event Registration Portal Starting...")
    print("="*70)
    
    # Try to start ngrok for public access
    start_ngrok()
    
    if use_ngrok and public_url:
        print("✅ SERVER READY - TWO WAYS TO ACCESS:")
        print("="*70)
        print(f"📱 PUBLIC URL (mobile data): {public_url}")
        print(f"🏠 LOCAL URL (same WiFi):    http://{local_ip}:5000/")
        print("="*70)
        print("QR Code will use PUBLIC URL - works on mobile data! 📱")
    else:
        print("✅ SERVER READY - LOCAL NETWORK ONLY:")
        print("="*70)
        print(f"🏠 Local Access:  http://127.0.0.1:5000/")
        print(f"📱 Network Access: http://{local_ip}:5000/")
        print("="*70)
        print("⚠️  QR Code works on same WiFi only")
        print("💡 Install pyngrok for mobile data access: pip install pyngrok")
    
    print("="*70)
    print("📲 Scan QR code on website to access from mobile!")
    print("="*70 + "\n")
    
    # Start Flask server
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
