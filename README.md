# 🔗 URL Shortener (Flask + SQLite + Docker)

A simple URL shortener that converts long URLs into short links and redirects users.

---

## 🧭 Minimap (Architecture Overview)

```
+-------------+        +-------------------+        +-------------+
|   Browser   | -----> |   Flask App       | -----> |  SQLite DB  |
| (User Input)|        | (app.py)          |        | (urls.db)   |
+-------------+        +-------------------+        +-------------+
       |                         |
       |                         |
       |<------ Short URL -------|
```

---

## 🔄 Request Flow (Step-by-Step)

```
1. User enters URL in browser
        ↓
2. Flask receives POST request (/)
        ↓
3. Generate short_id (shortuuid)
        ↓
4. Store (original_url + short_id) in SQLite
        ↓
5. Return short URL to user
        ↓
6. User opens short URL (/abc123)
        ↓
7. Flask queries DB
        ↓
8. Redirect to original URL
```

---

## 🐳 Docker Flow

```
+-------------------+
| Docker Container  |
|-------------------|
|  Flask App        |
|  SQLite DB File   |
+-------------------+
         |
         ↓
  Port 5000 exposed
         ↓
http://<EC2-IP>:5000
```

---

## 📁 Project Structure

```
url-shortener/
│
├── app.py              # Main Flask app
├── models.py           # Database model
├── requirements.txt    # Dependencies
├── Dockerfile          # Container setup
│
├── templates/
│   └── index.html      # UI
│
├── static/
│   └── style.css       # Styling
│
└── urls.db             # SQLite database (auto-created)
```

---

## 🚀 Features

* URL shortening
* Redirection
* Clean UI
* SQLite database
* Docker support

---

## ▶️ Run (Python)

```
python app.py
```

---

## 🐳 Run (Docker)

```
docker build -t url-shortener .
docker run -p 5000:5000 url-shortener
```

---

## 🌐 Access

```
http://localhost:5000
```

or (EC2)

```
http://<your-public-ip>:5000
```

---

## 💡 Example

```
Input:
https://google.com

Output:
http://localhost:5000/abc123
```

---

## 🚀 Future Enhancements

* Custom URLs
* Click tracking
* Expiry links
* Authentication
* Domain integration

```
```
