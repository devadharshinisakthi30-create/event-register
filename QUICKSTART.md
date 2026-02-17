# 🚀 Quick Start Guide

## Installation Steps (5 Minutes)

### Step 1: Install Python Dependencies
```bash
cd event_registration_portal
pip install Flask==3.0.0 reportlab==4.0.7 Werkzeug==3.0.1
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
```
http://127.0.0.1:5000/
```

## Quick Test

### Test Student Registration
1. Go to http://127.0.0.1:5000/
2. Fill the form:
   - Name: "John Doe"
   - Phone: "9876543210"
   - Register No: "2021CS001"
   - Department: "Computer Science"
   - Year: "III"
   - College: "ABC Engineering College"
   - Select any events
   - Pick a date
3. Click "Register Now"
4. Download certificate

### Test Admin Dashboard
1. Go to http://127.0.0.1:5000/admin-login
2. Username: `admin`
3. Password: `admin123`
4. View dashboard with registered students

## All Routes

| Route | Description |
|-------|-------------|
| `/` | Home - Registration Form |
| `/register` | Process registration (POST) |
| `/success/<id>` | Registration success page |
| `/registered-students` | View all students |
| `/admin-login` | Admin login page |
| `/admin-dashboard` | Admin dashboard (requires login) |
| `/admin-logout` | Logout admin |
| `/download-certificate/<id>` | Download PDF certificate |

## IT Events Included

1. Web Development Workshop (9:30 AM - 10:30 AM)
2. AI & Machine Learning Seminar (11:00 AM - 12:00 PM)
3. Cybersecurity Awareness (1:00 PM - 2:00 PM)
4. Cloud Computing Basics (2:30 PM - 3:30 PM)
5. Data Science Bootcamp (9:00 AM - 11:00 AM)
6. Mobile App Development (10:00 AM - 11:30 AM)
7. Blockchain Technology (12:00 PM - 1:00 PM)
8. IoT Innovations (3:00 PM - 4:00 PM)
9. Python Programming Contest (9:30 AM - 12:30 PM)
10. UI/UX Design Workshop (2:00 PM - 3:30 PM)

## Troubleshooting

**Problem**: Cannot access the site
**Solution**: Make sure Flask is running and check the port

**Problem**: Module not found
**Solution**: Run `pip install -r requirements.txt`

**Problem**: Certificate not downloading
**Solution**: Check if reportlab is installed: `pip install reportlab`

## Features Checklist

✅ Student registration form with all fields
✅ 10 IT events with timing and venue
✅ Multiple event selection
✅ Registered students page
✅ Admin login with session management
✅ Admin dashboard with statistics
✅ PDF certificate generation
✅ Colorful and responsive UI
✅ Form validation
✅ Professional design

---

**Ready to go! Start the server and open in browser! 🎉**
