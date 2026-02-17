# 🔧 TROUBLESHOOTING - White/Blank Screen Issue

## Problem: White Screen When Opening http://127.0.0.1:5000/

### Quick Diagnosis Steps:

## Step 1: Open Browser Developer Tools
1. Press **F12** on your keyboard
2. Click the **Console** tab
3. Look for RED error messages
4. Take a screenshot if you see errors

## Step 2: Check Network Tab
1. In Developer Tools, click **Network** tab
2. Refresh the page (F5)
3. Look for any files with status **404** (red)
4. Check if `style.css` loaded (should be status 200 in green)

## Step 3: Try Test Page
1. Stop your Flask server (Ctrl+C)
2. Start it again: `python app.py`
3. Go to: **http://127.0.0.1:5000/test**
4. You should see a colorful page saying "Flask Server is Working!"

## Common Causes & Fixes:

### Cause 1: Wrong Directory
**Fix:**
```bash
cd event_registration_portal  # Make sure you're IN this folder
python app.py                  # Then run
```

### Cause 2: Browser Cache
**Fix:**
- Hard refresh: **Ctrl + Shift + R** (Windows/Linux)
- Hard refresh: **Cmd + Shift + R** (Mac)
- Or clear browser cache

### Cause 3: Port Already in Use
**Fix:**
- Change port in `app.py` (last line):
```python
app.run(debug=True, port=5001)  # Change from 5000 to 5001
```
- Then go to: http://127.0.0.1:5001/

### Cause 4: Static Files Not Found
**Fix:**
```bash
# Verify files exist
ls static/css/style.css
ls templates/index.html

# If files missing, copy from backup
cp -r /home/claude/event_registration_portal/* .
```

### Cause 5: Flask Not Running
**Check if you see this in terminal:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

If not, restart:
```bash
python app.py
```

## Step-by-Step Fresh Start:

### 1. Stop Everything
- Close browser
- Stop Flask (Ctrl+C in terminal)

### 2. Clean Start
```bash
cd event_registration_portal
python app.py
```

### 3. Wait for Server
Look for:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 4. Open Browser Fresh
- Open NEW browser tab
- Go to: http://127.0.0.1:5000/
- Hard refresh: Ctrl+Shift+R

## What You Should See:

### On the Registration Page:
- Purple to pink gradient background
- Blue navigation bar at top
- White card in center
- Form fields:
  - Name, Phone, Register Number
  - Department, Year, College
  - 10 event checkboxes (colored cards)
  - Date picker
  - Blue "Register Now" button

## Still Not Working?

### Check Terminal for Errors
Look in your terminal where Flask is running. Any error messages?

### Try Minimal Test:
1. Go to: **http://127.0.0.1:5000/test**
2. If this works but main page doesn't, there's an issue with the main template

### Check File Permissions:
```bash
# Make sure files are readable
ls -la static/css/style.css
ls -la templates/index.html
```

### Reinstall Dependencies:
```bash
pip uninstall Flask reportlab
pip install Flask==3.0.0 reportlab==4.0.7
```

## Get Detailed Error Info:

### Check Flask Debug Output:
In your terminal (where Flask is running), you should see:
```
127.0.0.1 - - [date] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [date] "GET /static/css/style.css HTTP/1.1" 200 -
```

If you see **404** instead of **200**, that file wasn't found.

### Browser Console Should Show:
- No errors (no red text)
- CSS file loaded successfully

## Manual CSS Test:

Try accessing CSS directly in browser:
**http://127.0.0.1:5000/static/css/style.css**

You should see CSS code. If you get 404, the static folder isn't configured correctly.

## Nuclear Option - Fresh Install:

```bash
# Go to parent directory
cd ..

# Remove old folder
rm -rf event_registration_portal

# Copy fresh from backup
cp -r /home/claude/event_registration_portal .

# Go into folder
cd event_registration_portal

# Install
pip install -r requirements.txt

# Run
python app.py
```

## Contact Information:

If none of these work, provide:
1. Screenshot of browser console (F12 → Console tab)
2. Screenshot of Network tab (F12 → Network tab)
3. Terminal output from Flask
4. What you see at http://127.0.0.1:5000/test

---

**Most Common Fix**: Just hard refresh the browser (Ctrl+Shift+R)!
