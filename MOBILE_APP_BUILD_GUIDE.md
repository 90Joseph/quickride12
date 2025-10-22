# QuickBite Mobile App Build & Deployment Guide

## 🎯 Overview
This guide will help you build and deploy native mobile apps (iOS & Android) for QuickBite.

---

## Prerequisites

### 1. Create Expo Account (Free)
- Go to: https://expo.dev/signup
- Sign up with email or GitHub
- Verify your email

### 2. Install EAS CLI on Your Computer
Open Terminal/Command Prompt and run:
```bash
npm install -g eas-cli
```

### 3. Login to Expo
```bash
eas login
```
Enter your Expo credentials.

---

## 📱 Building Your Mobile Apps

### Step 1: Export Your Code from Emergent

1. Click **"Save to GitHub"** button in Emergent
2. Connect your GitHub account
3. Choose repository name: `quickbite-mobile`
4. Your code will be exported

### Step 2: Clone to Your Computer

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/quickbite-mobile.git
cd quickbite-mobile/frontend
```

### Step 3: Update Backend URL

Edit `frontend/.env` file:
```env
# Replace preview URL with your deployed backend URL
EXPO_PUBLIC_BACKEND_URL=https://your-deployed-backend-url.com
```

### Step 4: Configure EAS Build

```bash
# In the frontend folder
eas build:configure
```

This creates `eas.json` file. Update it:

```json
{
  "cli": {
    "version": ">= 5.9.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "android": {
        "buildType": "apk"
      }
    },
    "production": {
      "android": {
        "buildType": "app-bundle"
      }
    }
  },
  "submit": {
    "production": {}
  }
}
```

### Step 5: Update app.json

Edit `frontend/app.json`:

```json
{
  "expo": {
    "name": "QuickBite",
    "slug": "quickbite-ph",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "light",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#FF6B6B"
    },
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.quickbite.ph"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FF6B6B"
      },
      "package": "com.quickbite.ph",
      "permissions": [
        "ACCESS_FINE_LOCATION",
        "ACCESS_COARSE_LOCATION"
      ]
    },
    "web": {
      "favicon": "./assets/favicon.png"
    }
  }
}
```

---

## 🏗️ Building the Apps

### Build for Android (APK for Testing)

```bash
eas build --platform android --profile preview
```

This creates an APK file you can install on Android phones directly.

**Wait Time:** 10-15 minutes

**Download:** After build completes, you'll get a download link for the APK.

### Build for iOS (TestFlight)

```bash
eas build --platform ios --profile production
```

**Requirements:**
- Apple Developer Account ($99/year)
- You'll be asked to login with Apple ID during build

**Wait Time:** 15-20 minutes

### Build for Both at Once

```bash
eas build --platform all
```

---

## 📦 Testing Your Apps

### Android Testing (Easy!)

1. Download the APK from the build link
2. Transfer to your Android phone
3. Install it (enable "Install from Unknown Sources" if needed)
4. Open QuickBite app
5. Test all features!

### iOS Testing (via TestFlight)

1. After build completes, submit to TestFlight:
```bash
eas submit --platform ios
```

2. Wait for Apple review (1-2 days)
3. Install TestFlight app on iPhone
4. Add testers via App Store Connect
5. Test the app!

---

## 🚀 Publishing to App Stores

### Google Play Store (Android)

#### 1. Build Production Version
```bash
eas build --platform android --profile production
```

#### 2. Create Google Play Developer Account
- Go to: https://play.google.com/console
- Pay $25 one-time fee
- Complete registration

#### 3. Create App Listing
- App name: QuickBite
- Category: Food & Drink
- Add screenshots (take from app)
- Add description
- Upload app bundle

#### 4. Submit for Review
- Review takes 1-3 days
- App goes live after approval!

### Apple App Store (iOS)

#### 1. Create Apple Developer Account
- Go to: https://developer.apple.com
- Pay $99/year
- Complete registration

#### 2. Build Production Version
```bash
eas build --platform ios --profile production
```

#### 3. Submit to App Store
```bash
eas submit --platform ios
```

#### 4. Create App Store Listing
- Go to: https://appstoreconnect.apple.com
- Create new app
- Add screenshots
- Add description
- Set pricing (Free)
- Submit for review

#### 5. Wait for Review
- Review takes 1-3 days
- App goes live after approval!

---

## 🎨 App Assets You Need

Before building, create these images:

### Icon (1024x1024 PNG)
- App icon with QuickBite logo
- No transparency
- Save as: `frontend/assets/icon.png`

### Splash Screen (1242x2436 PNG)
- Loading screen when app opens
- QuickBite logo centered
- Background: #FF6B6B (red)
- Save as: `frontend/assets/splash.png`

### Adaptive Icon (1024x1024 PNG)
- Android adaptive icon
- Logo in center 600x600 area
- Save as: `frontend/assets/adaptive-icon.png`

---

## 🔧 Common Issues & Solutions

### Issue: Build Fails with "Invalid Bundle Identifier"
**Solution:** Change bundle ID in app.json to unique name:
```json
"bundleIdentifier": "com.yourname.quickbite"
```

### Issue: "Metro bundler not found"
**Solution:** Run in frontend folder:
```bash
npm install
```

### Issue: Can't login on built app
**Solution:** Make sure EXPO_PUBLIC_BACKEND_URL is set to deployed backend URL, not localhost.

### Issue: App crashes on startup
**Solution:** Check if all dependencies are compatible:
```bash
npx expo install --fix
```

---

## 📊 Build Status Tracking

Monitor your builds:
```bash
eas build:list
```

Or visit: https://expo.dev/accounts/YOUR_USERNAME/projects/quickbite-ph/builds

---

## 💡 Pro Tips

1. **Test APK First:** Always build Android APK first - it's faster and easier to test
2. **Use Different Profiles:** Use `preview` for testing, `production` for app stores
3. **Update Regularly:** When you fix bugs, rebuild and resubmit
4. **Version Numbers:** Increment version in app.json for each update
5. **Screenshots Matter:** Good screenshots increase downloads by 30%!

---

## 📞 Need Help?

- **Expo Docs:** https://docs.expo.dev
- **EAS Build Docs:** https://docs.expo.dev/build/introduction/
- **Discord:** https://discord.gg/expo

---

## ✅ Checklist

Before submitting to app stores:

- [ ] Tested on real devices (Android & iOS)
- [ ] All features working
- [ ] Backend API is deployed and accessible
- [ ] App icons and splash screens added
- [ ] Screenshots prepared (5-6 per platform)
- [ ] App description written
- [ ] Privacy policy created
- [ ] Terms of service created
- [ ] Contact email set up
- [ ] Developer accounts created (Apple & Google)

---

## 🎉 You're Done!

Your QuickBite app is now:
- ✅ Live as web app
- ✅ Built as native mobile app
- ✅ Ready for app stores!

**Next Steps:**
1. Test thoroughly
2. Gather feedback
3. Fix any issues
4. Submit to app stores
5. Market your app!

Good luck! 🚀
