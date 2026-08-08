Step 1: Open the project in Antigravity
Open Antigravity
File → Open Folder
Select: D:\Projects ML\heart-disease-risk-prediction
Step 2: Open a terminal
Click the Terminal panel at the bottom of Antigravity (or Terminal → New Terminal)
It should already be sitting in your project folder
Step 3: Activate your virtual environment (DO THIS EVERY TIME)

This is the step you keep forgetting — venv does NOT stay active automatically when you close and reopen the IDE. You must run this every single time you open a new terminal:

venv\Scripts\activate

How to know it worked: your terminal line will change to show (venv) at the very start, like this:

(venv) PS D:\Projects ML\heart-disease-risk-prediction>

If you don't see (venv) at the start, none of your commands (streamlit, uvicorn, python) will work correctly — this is almost always the fix when something says "not recognized."

Step 4: Run the app

Option A — Just the web app (most common, use this one):

streamlit run app/streamlit_app.py

This opens your interactive prediction form in a browser tab automatically.

Option B — Just the API (only if testing /predict directly):

uvicorn app.main:app

Then open http://127.0.0.1:8000/docs in your browser manually.

Step 5: Stop the app when done

Click into the terminal and press:

Ctrl + C
Quick Reference (copy-paste block)

Every time you reopen this project, run these two lines in order:

venv\Scripts\activate
streamlit run app/streamlit_app.py

That's it. Two commands. Nothing else needed for a normal demo run.

If something breaks
Problem	Fix
"streamlit not recognized"	You forgot Step 3 — run venv\Scripts\activate first
"uvicorn not recognized"	Same — activate venv first
Terminal doesn't show (venv)	Run venv\Scripts\activate again
"Execution policy" error when activating	Run once: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser, type Y, then try activating again