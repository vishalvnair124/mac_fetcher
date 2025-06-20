# 🖥️ MAC Fetcher – Flask App

A simple **Flask web application** that fetches and displays the **MAC address** of the device accessing the app.

---

## 🚀 Features

- 🔍 Displays the MAC address of the client machine  
- 🌐 Web interface using Flask and HTML templates  
- ⚡ Lightweight and easy to run locally

---

## 🧑‍💻 Built With

- Python  
- Flask  
- HTML (Jinja2 Templates)

---

## 📁 Project Structure

```
mac_fetcher/
├── app.py            # Flask main app
├── templates/
│   └── index.html    # Frontend display
└── README.md
```

---

## ⚙️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/vishalvnair124/mac_fetcher.git
cd mac_fetcher
```

2. Install dependencies:

```bash
pip install flask
```

3. Run the app:

```bash
python app.py
```

4. Open in browser:

```bash
http://localhost:5000
```

---

## 👨‍💻 Developed By

**Vishal V Nair**  
📫 GitHub: [@vishalvnair124](https://github.com/vishalvnair124)

---

> 🔒 *Note: Web apps cannot directly fetch the client's actual MAC address due to browser security restrictions. This app may show the server MAC or require specific setups to fetch from a local network.*
