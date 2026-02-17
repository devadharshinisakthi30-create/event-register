from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

registered_students = []

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

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/')
def index():
    return render_template('index.html', events=IT_EVENTS)

@app.route('/register', methods=['POST'])
def register():
    registration_id = f"HME{str(len(registered_students) + 1).zfill(3)}"
    student_data = {
        'id': len(registered_students) + 1,
        'registration_id': registration_id,
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'register_number': request.form.get('register_number'),
        'department': request.form.get('department'),
        'year': request.form.get('year'),
        'college': request.form.get('college'),
        'events': request.form.getlist('events'),
        'date': request.form.get('date'),
        'registration_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
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
    student = next((s for s in registered_students if s['id'] == student_id), None)
    return render_template('success.html', student=student)

@app.route('/registered-students')
def registered_students_page():
    return render_template('registered_students.html', students=registered_students)

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
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
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html', students=registered_students)

@app.route('/admin-logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))

@app.route('/get-server-url')
def get_server_url():
    server_url = f"{request.scheme}://{request.host}"
    return jsonify({'url': server_url, 'type': 'public', 'message': 'Accessible from anywhere!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)