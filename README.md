# 🔗 URL Shortener (Flask + Docker Implementation)

A lightweight and efficient web application that converts long URLs into short, shareable links.  
It also supports basic analytics like click tracking and is fully containerized using Docker for easy deployment.

---

## 🚀 Features

- 🔗 URL shortening  
- 🔁 Redirection to original URL  
- 📊 Click tracking (analytics)  
- ♻️ Duplicate URL handling  
- 💾 Persistent storage using SQLite  
- 🐳 Docker support  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Flask  
- **Database:** SQLite (Flask-SQLAlchemy)  
- **Frontend:** HTML, CSS  
- **Containerization:** Docker  

---

## 💡 How It Works

When a user enters a long URL, the application creates a shorter version of it that is easier to share.

First, the user submits a long URL through the website.
The Flask backend receives this request and generates a unique short code (for example, abc123).

This short code is then stored in the database along with the original URL and a click count (starting from 0).

After that, the application returns a short link like:

http://localhost:5000/abc123

When someone opens this short link, the application checks the database, finds the original URL, and redirects the user to it. At the same time, it increases the click count to track how many times the link was used.


🔄 Workflow
User submits a long URL
Backend generates a unique short code
URL mapping is stored in SQLite
Short URL is returned
Accessing it redirects to original URL
Click count is updated

🔧 Components
1. Flask Application (app.py)


Handles HTTP requests


Generates short URLs


Redirects users


Tracks click counts


2. Database (SQLite)


Stores:


Short Code


Original URL


Click Count




3. Frontend (templates/index.html)


Simple UI for user input


Displays shortened URLs


4. Docker


Containerized environment


Ensures consistent deployment



📁 Project Structure
url-shortener/│├── app.py├── models.py├── requirements.txt├── Dockerfile├── urls.db│├── templates/│   └── index.html│├── static/│   └── style.css

🔌 API Endpoints
Home Page
GET /
Create Short URL
POST /
Body:
url=<long_url>
Redirect
GET /<short_code>
Stats (Optional)
GET /stats

⚙️ Installation (Local Setup)
1. Clone Repository
git clone https://github.com/your-username/url-shortener.gitcd url-shortener
2. Create Virtual Environment
python3 -m venv venvsource venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
python app.py
5. Open in Browser
http://localhost:5000

🐳 Run with Docker
Build Image
docker build -t url-shortener .
Run Container
docker run -d -p 5000:5000 url-shortener
Access Application
http://localhost:5000

📊 Data Model
Table: urls- id        INTEGER (Primary Key)- short     TEXT (Unique)- original  TEXT- clicks    INTEGER

🧪 Example
Input:
https://www.example.com/very/long/url
Output:
http://localhost:5000/Ab12Xy

🌍 Deployment Options


AWS EC2


Docker Hub


Render / Railway



💥 Future Improvements


👤 User authentication


📊 Advanced analytics dashboard


⏳ Expiring URLs


🌐 Custom short URLs


📱 QR code generation



📌 Key Learnings


Flask web development


REST API design


Database integration


Docker containerization


URL routing and redirection



👩‍💻 Author
Nandu

⭐ Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

📄 License
This project is licensed under the MIT License.
---This version is:- Clean for GitHub  - Looks like a real production project  - Strong enough for resume + portfolio  ---Next step (optional but powerful):- Add **project screenshot**- Add **live demo link**- Push to GitHub with proper repo nameSend your next project — I’ll format it the same way 👍
