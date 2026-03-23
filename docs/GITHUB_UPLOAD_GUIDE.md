# 🚀 Step-by-Step Guide: Upload This Project to GitHub
### Written for Beginners — Every Step Explained

---

## What You Need Before Starting
- A computer (Mac or Windows)
- An internet connection
- 15–20 minutes

---

## PART 1: Create a GitHub Account (Skip if you already have one)

1. Open your browser and go to: **https://github.com**
2. Click the green **"Sign up"** button
3. Enter your email, create a password, and choose a username
   - Suggested username: `rajwinderkaur-qa` or `rkaur-qa`
4. Complete the verification and click **"Create account"**
5. Check your email and verify your account

---

## PART 2: Create a New Repository on GitHub

> A "repository" (repo) is like a folder on GitHub that stores your project.

1. After logging in, click the **"+"** icon in the top-right corner
2. Click **"New repository"**
3. Fill in the form:
   - **Repository name:** `speechify-ios-qa`
   - **Description:** `iOS test automation framework for Speechify app using Appium + Python`
   - **Visibility:** Select **Public** ✅ (so Speechify can see it)
   - **DO NOT** check "Add a README file" (we already have one)
   - **DO NOT** check "Add .gitignore" (we already have one)
4. Click the green **"Create repository"** button
5. ✅ You'll see a page with setup instructions — **keep this page open**

---

## PART 3: Install Git on Your Computer

> Git is the tool that sends your files to GitHub.

### On Mac:
1. Open **Terminal** (press `Cmd + Space`, type "Terminal", press Enter)
2. Type this command and press Enter:
   ```
   git --version
   ```
3. If you see something like `git version 2.39.0` — Git is already installed! Skip to Part 4.
4. If not, a popup will appear asking to install Xcode Command Line Tools — click **Install**
5. Wait for it to finish, then run `git --version` again to confirm

### On Windows:
1. Go to: **https://git-scm.com/download/win**
2. Download and run the installer
3. Click "Next" through all steps (default options are fine)
4. After installing, open **Git Bash** (search for it in the Start menu)

---

## PART 4: Set Up Git With Your Name & Email (One-Time Setup)

In Terminal (Mac) or Git Bash (Windows), run these two commands.
Replace the name and email with YOUR details:

```bash
git config --global user.name "Rajwinder Kaur"
git config --global user.email "kaurjheeta1984@gmail.com"
```

Press Enter after each line. No output means it worked. ✅

---

## PART 5: Download the Project Files

The project files are in a ZIP file you downloaded. Here's how to place them correctly:

1. **Unzip the file** — double-click the ZIP file you downloaded
2. You should see a folder called `speechify-ios-qa`
3. **Move this folder** to a location you'll remember, for example:
   - Mac: your **Desktop** or **Documents** folder
   - Windows: your **Desktop** or **Documents** folder

---

## PART 6: Open Terminal in the Project Folder

### On Mac:
1. Open **Terminal**
2. Type `cd ` (with a space after cd), then **drag and drop** the `speechify-ios-qa` folder into the Terminal window
3. Press **Enter**
4. You should see the folder path appear, like: `cd /Users/yourname/Desktop/speechify-ios-qa`

**OR** use this command (replace the path with where YOUR folder is):
```bash
cd ~/Desktop/speechify-ios-qa
```

### On Windows (Git Bash):
```bash
cd ~/Desktop/speechify-ios-qa
```

### Confirm you're in the right folder:
```bash
ls
```
You should see files like `README.md`, `conftest.py`, `requirements.txt` listed. ✅

---

## PART 7: Initialize Git and Upload to GitHub

Run these commands **one by one** in Terminal. Press Enter after each one.

### Step 1 — Initialize git in your project folder
```bash
git init
```
Expected output: `Initialized empty Git repository in .../speechify-ios-qa/.git/`

### Step 2 — Stage all files (tell git what to include)
```bash
git add .
```
No output = success ✅

### Step 3 — Create your first commit (save a snapshot with a message)
```bash
git commit -m "Initial commit: Speechify iOS QA automation framework"
```
Expected output: You'll see a list of files being added.

### Step 4 — Rename the default branch to 'main'
```bash
git branch -M main
```
No output = success ✅

### Step 5 — Connect your local folder to GitHub
> ⚠️ Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username!
```bash
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/speechify-ios-qa.git
```
Example: `git remote add origin https://github.com/rajwinderkaur-qa/speechify-ios-qa.git`

### Step 6 — Push (upload) your files to GitHub
```bash
git push -u origin main
```

You'll be asked for your GitHub **username** and **password**.

> ⚠️ **Important:** GitHub no longer accepts your regular password here.
> You need a **Personal Access Token** instead. See Part 8 below.

---

## PART 8: Create a GitHub Personal Access Token (PAT)

> This is GitHub's secure way to verify it's really you uploading files.

1. On GitHub.com, click your **profile picture** (top-right) → **Settings**
2. Scroll down the left sidebar and click **"Developer settings"**
3. Click **"Personal access tokens"** → **"Tokens (classic)"**
4. Click **"Generate new token"** → **"Generate new token (classic)"**
5. Fill in:
   - **Note:** `speechify-ios-qa upload`
   - **Expiration:** 90 days
   - **Scopes:** Check the box next to **"repo"** (this gives access to repositories)
6. Scroll down and click **"Generate token"**
7. ✅ You'll see a long string of letters and numbers — **COPY IT NOW**
   - ⚠️ You can only see this token ONCE. If you close the page, you'll need to create a new one.
8. Save it somewhere temporarily (like a Notes app)

### Now go back to Terminal and run the push command again:
```bash
git push -u origin main
```
- When asked for **Username**: type your GitHub username, press Enter
- When asked for **Password**: paste your **Personal Access Token** (not your GitHub password)

Expected output:
```
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
Writing objects: 100% (25/25), done.
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## PART 9: Verify Everything Uploaded Correctly

1. Go to: `https://github.com/YOUR_GITHUB_USERNAME/speechify-ios-qa`
2. You should see your project with all folders:
   ```
   📁 .github/workflows/
   📁 docs/
   📁 page_objects/
   📁 scripts/
   📁 test_data/
   📁 tests/
   📄 README.md        ← This should display beautifully on the page
   📄 conftest.py
   📄 requirements.txt
   ```
3. Click on **README.md** — it should show a formatted page with headers, tables, and code blocks ✅

---

## PART 10: Make Your Profile Look Professional

### Add a description to your repository:
1. On your repo page, click the ⚙️ gear icon next to "About" (top right of the page)
2. Add:
   - **Description:** `iOS QA automation framework for Speechify app — Appium, XCUITest, Python, pytest, CI/CD`
   - **Website:** your LinkedIn URL
   - **Topics:** type and add: `appium`, `ios-testing`, `pytest`, `qa-automation`, `xcuitest`, `python`
3. Click **Save changes**

### Pin this repo to your GitHub profile:
1. Go to your GitHub profile: `https://github.com/YOUR_USERNAME`
2. Click **"Customize your profile"**
3. Under "Pinned", click **"+ Add"** and select `speechify-ios-qa`

---

## PART 11: How to Update the Project in the Future

Every time you make changes to files, run these 3 commands to save and upload:

```bash
# 1. Stage your changes
git add .

# 2. Save a snapshot with a description of what changed
git commit -m "Add test for voice selection feature"

# 3. Upload to GitHub
git push
```

---

## 🎉 You're Done!

Your project is now live on GitHub. Share this link with Speechify:
```
https://github.com/YOUR_GITHUB_USERNAME/speechify-ios-qa
```

---

## Troubleshooting

**Problem:** `git push` says "repository not found"
**Fix:** Double-check the URL in Step 5 of Part 7. Make sure your GitHub username is correct.

**Problem:** `fatal: not a git repository`
**Fix:** Make sure you ran `git init` while INSIDE the project folder. Run `cd speechify-ios-qa` first.

**Problem:** Authentication failed
**Fix:** Make sure you're using your Personal Access Token (from Part 8), NOT your GitHub password.

**Problem:** Files uploaded but README looks like plain text
**Fix:** The file must be named exactly `README.md` (capital README, lowercase .md).
