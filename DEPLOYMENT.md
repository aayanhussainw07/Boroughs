# Deploying Boroughs to GitHub Pages

This guide will help you deploy Boroughs to GitHub Pages (frontend) and a backend hosting service.

## Overview

- **Frontend**: Deployed to GitHub Pages (static hosting)
- **Backend**: Deployed to Railway, Render, or Heroku (server hosting)

## Prerequisites

- Git and GitHub account
- Node.js and npm installed
- Python 3.8+ installed

---

## Part 1: Deploy Backend

### Option A: Railway (Recommended)

1. **Sign up at [Railway.app](https://railway.app)**
   - Connect your GitHub account

2. **Create new project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your Boroughs repository

3. **Configure the backend**
   - Railway will auto-detect your Flask app
   - Set root directory to `backend` if needed
   - Add environment variables (if using Claude API):
     ```
     ANTHROPIC_API_KEY=your_key_here
     ```

4. **Deploy**
   - Railway will automatically deploy
   - Copy your backend URL: `https://boroughs-production.up.railway.app`

### Option B: Render

1. **Sign up at [Render.com](https://render.com)**

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Select the `backend` directory

3. **Configure**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3

4. **Add environment variables** (optional)
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

5. **Deploy** and copy your URL

### Option C: Heroku

1. **Install Heroku CLI**
   ```bash
   brew install heroku/brew/heroku  # macOS
   # or download from heroku.com
   ```

2. **Create Procfile** in `backend/` folder:
   ```
   web: python app.py
   ```

3. **Deploy**
   ```bash
   cd backend
   heroku login
   heroku create boroughs-backend
   git push heroku main
   ```

4. **Set environment variables**
   ```bash
   heroku config:set ANTHROPIC_API_KEY=your_key_here
   ```

---

## Part 2: Configure Frontend

### 1. Update Environment Variables

Edit `frontend/.env.production` with your backend URL:

```env
VITE_API_BASE_URL=https://your-backend-url.com/api
```

**Example:**
```env
VITE_API_BASE_URL=https://boroughs-production.up.railway.app/api
```

### 2. Update Vite Config

In `frontend/vite.config.js`, update the `base` to match your GitHub repo name:

```javascript
export default defineConfig({
  base: '/Boroughs/', // Change to your repo name
  // ...
})
```

If your repo is `username/my-housing-app`, use:
```javascript
base: '/my-housing-app/',
```

### 3. Install gh-pages

```bash
cd frontend
npm install --save-dev gh-pages
```

---

## Part 3: Deploy to GitHub Pages

### 1. Initialize Git (if not already done)

```bash
# In the root directory
git init
git add .
git commit -m "Initial commit"
```

### 2. Create GitHub Repository

1. Go to [GitHub.com](https://github.com/new)
2. Create a new repository named `Boroughs` (or your preferred name)
3. **Do NOT** initialize with README

### 3. Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/Boroughs.git
git branch -M main
git push -u origin main
```

### 4. Deploy Frontend

```bash
cd frontend
npm run deploy
```

This will:
- Build your React app (`npm run build`)
- Deploy to the `gh-pages` branch
- Your site will be live at: `https://YOUR_USERNAME.github.io/Boroughs/`

### 5. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select branch: `gh-pages`
4. Click **Save**

Your site should be live in a few minutes!

---

## Part 4: Update Backend CORS

Update your Flask backend to allow requests from your GitHub Pages URL:

In `backend/app.py`, update CORS:

```python
from flask_cors import CORS

CORS(app, origins=[
    'http://localhost:3000',
    'https://YOUR_USERNAME.github.io'
])
```

Redeploy your backend after this change.

---

## Testing Your Deployment

1. Visit your GitHub Pages URL: `https://YOUR_USERNAME.github.io/Boroughs/`
2. Take the quiz and check if the backend API works
3. Open browser DevTools → Network tab to debug any issues

---

## Troubleshooting

### Frontend Issues

**Problem**: Blank page or 404 errors
- **Solution**: Check `base` in `vite.config.js` matches your repo name
- Ensure it starts and ends with `/`: `/Boroughs/`

**Problem**: API calls failing
- **Solution**: Check `.env.production` has correct backend URL
- Verify CORS is configured on backend
- Check browser console for errors

**Problem**: Assets not loading
- **Solution**: Update `base` path in `vite.config.js`
- Rebuild and redeploy: `npm run deploy`

### Backend Issues

**Problem**: Backend not responding
- **Solution**: Check backend logs on Railway/Render/Heroku
- Verify environment variables are set
- Check Flask app is running on correct port

**Problem**: CORS errors
- **Solution**: Update CORS origins in `app.py`
- Redeploy backend

---

## Updating Your Deployment

### Update Frontend

```bash
cd frontend
npm run deploy
```

### Update Backend

**Railway/Render**: Just push to GitHub
```bash
git add .
git commit -m "Update backend"
git push origin main
```

**Heroku**:
```bash
git push heroku main
```

---

## Custom Domain (Optional)

### For Frontend (GitHub Pages)

1. Buy a domain (Namecheap, Google Domains, etc.)
2. Add `CNAME` file in `frontend/public/`:
   ```
   yourdomain.com
   ```
3. Configure DNS:
   - Add A records pointing to GitHub Pages IPs
   - Or add CNAME record: `YOUR_USERNAME.github.io`
4. In GitHub repo settings → Pages, add custom domain

### For Backend

- Railway/Render provide custom domain options in settings
- Point your domain's subdomain (e.g., `api.yourdomain.com`) to backend

---

## Environment Variables Summary

### Frontend (.env.production)
```env
VITE_API_BASE_URL=https://your-backend-url.com/api
```

### Backend (Railway/Render/Heroku)
```env
ANTHROPIC_API_KEY=your_claude_key_here  # Optional
FLASK_ENV=production
```

---

## Quick Deploy Checklist

- [ ] Backend deployed to Railway/Render/Heroku
- [ ] Backend URL copied
- [ ] `.env.production` updated with backend URL
- [ ] `vite.config.js` base path matches repo name
- [ ] `gh-pages` package installed
- [ ] Code pushed to GitHub
- [ ] `npm run deploy` executed
- [ ] GitHub Pages enabled in repo settings
- [ ] Backend CORS updated with GitHub Pages URL
- [ ] Site tested and working

---

## Need Help?

- **GitHub Pages**: https://pages.github.com
- **Railway Docs**: https://docs.railway.app
- **Render Docs**: https://render.com/docs
- **Vite Deployment**: https://vitejs.dev/guide/static-deploy.html

---

**Your Boroughs app is now live!** 🎉

Visit: `https://YOUR_USERNAME.github.io/Boroughs/`
