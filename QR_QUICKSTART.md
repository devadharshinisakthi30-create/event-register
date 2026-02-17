# 🚀 QR CODE - QUICK START

## What's New?
Your Event Registration Portal now has **QR CODE** at the bottom of every page!

## How It Works:
1. **Start server**: `python app.py`
2. **Scroll down** on website to see QR code
3. **Scan with mobile** camera
4. **Portal opens** on mobile browser!

## Requirements:
✅ Computer and mobile on **same WiFi network**
✅ Flask server running
✅ Mobile camera app (built-in on all phones)

## Quick Test:

### Step 1: Start Server
```bash
cd event_registration_portal
python app.py
```

You'll see:
```
📱 Network Access: http://192.168.1.100:5000/
📱 Scan QR Code on the website to access from mobile!
```

### Step 2: Open on Desktop
Go to: `http://127.0.0.1:5000/`

### Step 3: Scroll to Bottom
You'll see a white card with QR code

### Step 4: Scan with Mobile
- **iPhone**: Open Camera → Point at QR → Tap notification
- **Android**: Open Camera → Point at QR → Tap URL

### Step 5: It Works!
Portal opens on your mobile phone! 🎉

## Where QR Code Appears:
- ✅ Home page (registration form)
- ✅ Registered students page
- ✅ Success page (after registration)

## Troubleshooting:

**Problem**: QR code doesn't appear
**Fix**: Hard refresh browser (Ctrl+Shift+R)

**Problem**: Scan doesn't work
**Fix**: Ensure mobile is on same WiFi as computer

**Problem**: Shows "Loading..." 
**Fix**: Restart Flask server

## Network Setup:

### Home WiFi:
1. Connect computer to WiFi
2. Connect mobile to **same** WiFi
3. Start server
4. Scan QR code ✓

### Using Hotspot:
1. Create hotspot on mobile
2. Connect computer to mobile hotspot
3. Start server
4. Scan QR code ✓

## Features:

📱 **Auto-generated** - QR code creates itself
🎨 **Styled** - Blue QR code matches website theme
📲 **Easy to scan** - Large, clear QR code
🔗 **Shows URL** - Displays the link below QR
💡 **Instructions** - Tells users how to scan
📱 **Mobile optimized** - Looks great on all devices

## The QR Code Contains:
```
http://your-network-ip:5000/
```
Example: `http://192.168.1.100:5000/`

This IP changes based on your network.

## Benefits:

✅ No need to type URL
✅ Instant mobile access
✅ Share with friends easily
✅ Professional appearance
✅ Works offline (local network)
✅ No internet needed (uses WiFi)

---

**That's it! Start the server and try scanning the QR code!** 📱✨

For detailed documentation, see: `QR_CODE_GUIDE.md`
