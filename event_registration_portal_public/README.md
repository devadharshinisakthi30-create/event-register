# 🎓 Event Registration Portal

A comprehensive web-based Event Registration Portal built with Flask that allows students to register for IT events, view registered participants, and download participation certificates.

## ✨ Features

### 🎯 Student Features
- **Interactive Registration Form** - Students can register with their details
- **Multiple Event Selection** - Select one or more IT events simultaneously
- **10 IT Events** with predefined timings (9:30-10:30, etc.)
- **Automatic Certificate Generation** - Download PDF certificates immediately after registration
- **View All Registrations** - See all registered students publicly
- **📱 QR Code Access** - Scan QR code with mobile to access portal instantly

### 🔐 Admin Features
- **Secure Login System** - Protected admin dashboard with session management
- **Complete Dashboard** - View all registered students in a table format
- **Statistics Overview** - See total registrations, events, and departments
- **Certificate Download** - Download certificates for any registered student

### 📱 Mobile Features
- **QR Code on Every Page** - Automatically generated for mobile access
- **Network Auto-Detection** - Server detects and displays network IP
- **Mobile-Responsive Design** - Beautiful on all screen sizes
- **Camera-Ready QR** - Scan with any mobile camera app

### 📋 Available IT Events
1. **Web Development Workshop** (9:30 AM - 10:30 AM)
2. **AI & Machine Learning Seminar** (11:00 AM - 12:00 PM)
3. **Cybersecurity Awareness** (1:00 PM - 2:00 PM)
4. **Cloud Computing Basics** (2:30 PM - 3:30 PM)
5. **Data Science Bootcamp** (9:00 AM - 11:00 AM)
6. **Mobile App Development** (10:00 AM - 11:30 AM)
7. **Blockchain Technology** (12:00 PM - 1:00 PM)
8. **IoT Innovations** (3:00 PM - 4:00 PM)
9. **Python Programming Contest** (9:30 AM - 12:30 PM)
10. **UI/UX Design Workshop** (2:00 PM - 3:30 PM)

## 📁 Project Structure

```
event_registration_portal/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── templates/                      # HTML templates
│   ├── index.html                 # Registration form page
│   ├── success.html               # Registration success page
│   ├── registered_students.html   # View all registered students
│   ├── admin_login.html           # Admin login page
│   └── admin_dashboard.html       # Admin dashboard
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css              # Main stylesheet
│   └── js/
│       └── script.js              # JavaScript functionality
│
└── certificates/                   # Directory for certificate storage
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- VS Code (recommended)

### Step 1: Install Dependencies

Open terminal in VS Code and run:

```bash
cd event_registration_portal
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

### Step 3: Access the Portal

Open your web browser and navigate to:
- **Home/Registration**: http://127.0.0.1:5000/
- **Registered Students**: http://127.0.0.1:5000/registered-students
- **Admin Login**: http://127.0.0.1:5000/admin-login

## 🔐 Admin Credentials

```
Username: admin
Password: admin123
```

**⚠️ Important**: Change these credentials in production by modifying `app.py`

## 📝 How to Use

### For Students

1. **Navigate to Home Page**
   - Fill in personal information (Name, Phone, Register Number)
   - Select academic details (Department, Year, College)
   
2. **Select Events**
   - Choose one or more events from the available IT events
   - Each event shows timing and venue
   - Multiple selections allowed
   
3. **Submit Registration**
   - Click "Register Now" button
   - View confirmation page with all details
   
4. **Download Certificate**
   - Click "Download Certificate" button
   - PDF certificate will be generated and downloaded

### For Administrators

1. **Login**
   - Go to Admin Login page
   - Enter credentials (admin/admin123)
   
2. **View Dashboard**
   - See statistics (total registrations, events, departments)
   - View complete list of registered students in table format
   
3. **Download Certificates**
   - Click the 📄 icon in the Actions column
   - Certificate for any student can be downloaded

## 🎨 Features Implementation

### Frontend
- **HTML5** - Semantic markup and structure
- **CSS3** - Modern, responsive, and colorful design
- **JavaScript** - Form validation and interactivity
- **Gradient Backgrounds** - Eye-catching color schemes
- **Responsive Design** - Works on all device sizes

### Backend
- **Flask Routing** - Multiple routes for different pages
- **Form Handling** - POST and GET request processing
- **Session Management** - Secure admin authentication
- **PDF Generation** - ReportLab for certificate creation
- **In-Memory Storage** - Student data storage (use database in production)

### Special Features
- ✅ Multiple event selection with checkboxes
- ✅ Event timing displayed for each event (9:30-10:30 format)
- ✅ Professional PDF certificate generation
- ✅ Colorful and modern UI design
- ✅ Form validation (phone number, date, required fields)
- ✅ Admin session management
- ✅ Responsive design for mobile devices

## 🎓 Certificate Features

Certificates include:
- Student name (prominently displayed)
- Register number and academic details
- All registered events with timings and venues
- Event date
- Professional border and design
- Digital signatures (Event Coordinator & Principal)

## 📱 QR Code Features

**NEW**: QR code displayed at the bottom of every page!

- **Auto-Generated**: Creates QR code automatically
- **Network Detection**: Detects your computer's IP address
- **Mobile Access**: Scan with phone camera to access portal
- **Professional Design**: Blue QR code matching site theme
- **Easy Scanning**: Large 200x200px code
- **Instructions Included**: Clear how-to-scan guide
- **Works Offline**: Uses local WiFi network

### How to Use QR Code:
1. Start server: `python app.py`
2. Server shows network URL in terminal
3. Scroll to bottom of any page
4. Scan QR code with mobile camera
5. Portal opens on mobile browser!

**Requirements**: Computer and mobile on same WiFi network

For detailed QR code documentation, see `QR_CODE_GUIDE.md`

## 🔧 Customization

### Add More Events
Edit the `IT_EVENTS` dictionary in `app.py`:

```python
IT_EVENTS = {
    'Your Event Name': {
        'time': '10:00 AM - 11:00 AM',
        'venue': 'Your Venue'
    },
    # Add more events...
}
```

### Change Admin Credentials
Modify in `app.py`:

```python
ADMIN_USERNAME = 'your_username'
ADMIN_PASSWORD = 'your_password'
```

### Customize Colors
Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #3b82f6;
    --secondary-color: #8b5cf6;
    /* Modify other colors... */
}
```

## 📱 Responsive Design

The portal is fully responsive and works on:
- 💻 Desktop computers
- 📱 Tablets
- 📱 Mobile phones

## ⚠️ Important Notes

1. **Data Storage**: Currently uses in-memory storage. For production, implement a database (SQLite, PostgreSQL, MySQL)
2. **Security**: Change admin credentials and secret key in production
3. **PDF Storage**: Certificates are generated dynamically and not stored
4. **Session Management**: Uses Flask sessions for admin authentication

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

### Module Not Found Error
```bash
pip install -r requirements.txt --upgrade
```

### Template Not Found
Ensure you're running from the correct directory:
```bash
cd event_registration_portal
python app.py
```

## 🚀 Future Enhancements

- Database integration (SQLite/PostgreSQL)
- Email notifications for registrations
- QR code on certificates
- Event capacity limits
- Student login system
- Payment integration
- Export to Excel functionality
- Advanced analytics dashboard

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

Event Registration Portal - Python Flask Project

---

**Enjoy using the Event Registration Portal! 🎉**
