# 🚀 SETUP INSTRUCTIONS - Event Registration Portal

## ⚡ Quick Setup (3 Steps)

### Step 1: Open Terminal in VS Code
- Open VS Code
- Navigate to the project folder: `event_registration_portal`
- Open integrated terminal (Terminal → New Terminal)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note for Linux/Mac users**: If you get an error, use:
```bash
pip install -r requirements.txt --break-system-packages
```

### Step 3: Run the Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 4: Open in Browser
Open your web browser and go to:
```
http://127.0.0.1:5000/
```

---

## 📋 What You'll See

### 1. Registration Page (Home)
- Fill in student details
- Select one or more IT events
- Submit registration
- Get instant confirmation

### 2. Success Page
- View registration details
- Download PDF certificate
- Return to home or view all registrations

### 3. Registered Students Page
- See all registered students
- View their selected events
- Download their certificates

### 4. Admin Portal
- Login: `admin` / `admin123`
- View dashboard with statistics
- See complete table of all registrations
- Download any certificate

---

## 🎯 Test the Application

### Test Data for Quick Registration:
```
Name: John Doe
Phone: 9876543210
Register Number: 2021CS001
Department: Computer Science
Year: III
College: ABC Engineering College
Events: Select any (e.g., Web Development Workshop, AI & ML Seminar)
Date: Select today's date or any future date
```

---

## 📂 Project Files

```
event_registration_portal/
│
├── app.py                      ← Main Flask application
├── requirements.txt            ← Python dependencies
├── README.md                   ← Full documentation
├── QUICKSTART.md              ← Quick reference
├── PROJECT_OVERVIEW.md        ← Detailed feature list
├── test_system.py             ← Test script
│
├── templates/                  ← HTML templates
│   ├── index.html             ← Registration form
│   ├── success.html           ← Success page
│   ├── registered_students.html
│   ├── admin_login.html
│   └── admin_dashboard.html
│
└── static/                     ← Static files
    ├── css/
    │   └── style.css          ← All styles
    └── js/
        └── script.js          ← JavaScript code
```

---

## 🔧 Troubleshooting

### Problem: "Module not found"
**Solution**: 
```bash
pip install Flask reportlab Werkzeug
```

### Problem: "Port already in use"
**Solution**: Change port in `app.py` line 159:
```python
app.run(debug=True, port=5001)  # Change from 5000 to 5001
```

### Problem: "Template not found"
**Solution**: Make sure you're running from the `event_registration_portal` directory:
```bash
cd event_registration_portal
python app.py
```

### Problem: Certificate not downloading
**Solution**: Check if ReportLab is installed:
```bash
pip install reportlab
```

---

## 🎓 Features Included

✅ **10 IT Events** with timing (9:30 AM - 10:30 AM format)
✅ **Multiple Event Selection** - Students can register for many events
✅ **Professional PDF Certificates** - Auto-generated for each student
✅ **Admin Dashboard** - Secure login with complete data view
✅ **Responsive Design** - Works on desktop, tablet, and mobile
✅ **Colorful UI** - Modern gradient backgrounds and animations
✅ **Form Validation** - Phone number, date, required fields
✅ **Session Management** - Secure admin authentication

---

## 📱 All Routes

| URL | Description | Access |
|-----|-------------|--------|
| http://127.0.0.1:5000/ | Registration Form | Public |
| http://127.0.0.1:5000/registered-students | All Registrations | Public |
| http://127.0.0.1:5000/admin-login | Admin Login | Public |
| http://127.0.0.1:5000/admin-dashboard | Admin Dashboard | Admin Only |

---

## 🎯 Testing Checklist

- [ ] Open home page - registration form loads
- [ ] Fill form and select events
- [ ] Submit registration - redirects to success page
- [ ] Download certificate - PDF downloads
- [ ] View registered students page - student appears
- [ ] Login to admin (admin/admin123)
- [ ] View admin dashboard - see statistics and table
- [ ] Download certificate from admin panel
- [ ] Logout from admin
- [ ] Test responsive design (resize browser)

---

## 📧 Support

If you encounter any issues:
1. Check this SETUP file
2. Read README.md for detailed documentation
3. Run test_system.py to verify installation
4. Check PROJECT_OVERVIEW.md for feature details

---

## 🎉 You're Ready!

Everything is set up and ready to use. Just run:
```bash
python app.py
```

And start registering students for events!

**Enjoy your Event Registration Portal! 🚀**
