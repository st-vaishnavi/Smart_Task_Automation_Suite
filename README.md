# 🚀 Smart Task Automation Suite

A Python-based automation application that combines multiple productivity tools into one modern desktop application with a graphical user interface built using **CustomTkinter**.

---

## 📌 Project Overview

Smart Task Automation Suite is an all-in-one desktop application that helps users automate common tasks such as:

* Extracting email addresses from text files
* Organizing files into categories automatically
* Scraping website titles and statistics
* Generating reports and logs
* Managing settings through an interactive GUI

The project demonstrates concepts of **Python automation, file handling, web scraping, GUI development, and software packaging**.

---

## ✨ Features

### 📧 Email Extractor

* Extracts email addresses from text files.
* Removes duplicate email addresses.
* Saves results in `.txt` and `.csv` formats.
* Generates extraction reports.

### 📂 File Organizer

* Automatically categorizes files into:

  * Images
  * Documents
  * Videos
  * Audio
  * Archives
  * Others
* Displays file statistics.
* Supports Undo functionality.

### 🌐 Website Title Scraper

* Extracts website titles.
* Displays:

  * Website Title
  * Status Code
  * Response Time
* Stores results in text and CSV files.

### 🌍 Batch Website Scraper

* Processes multiple URLs from a file.
* Calculates:

  * Success Rate
  * Average Response Time
  * Fastest Website
  * Slowest Website
* Generates detailed reports.

### 📊 Reports System

* View generated reports directly in the application.
* Clear reports when required.

### ⚙️ Settings Page

* Change appearance mode:

  * Dark Mode
  * Light Mode
  * System Mode
* Clear logs.
* Clear reports.

### 🖥️ Modern GUI

* Built using CustomTkinter.
* User-friendly navigation sidebar.
* Multiple pages and interactive interface.

---

## 🛠️ Technologies Used

* Python 3
* CustomTkinter
* Requests
* BeautifulSoup4
* CSV
* JSON
* Pathlib
* Tkinter
* PyInstaller

---

## 📁 Project Structure

```text
Smart_Task_Automation_Suite/
│
├── gui/
│   ├── app.py
│   ├── dashboard_page.py
│   ├── email_page.py
│   ├── organizer_page.py
│   ├── scraper_page.py
│   ├── reports_page.py
│   ├── settings_page.py
│   └── about_page.py
│
├── modules/
│   ├── email_extractor.py
│   ├── file_organizer.py
│   ├── undo_manager.py
│   ├── web_scraper.py
│   ├── batch_scraper.py
│   ├── logger.py
│   └── report_generator.py
│
├── input/
├── output/
├── assets/
├── screenshots/
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Smart_Task_Automation_Suite.git
cd Smart_Task_Automation_Suite
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python gui/app.py
```

---

## 📦 Create Executable

```bash
python -m PyInstaller --onefile --windowed gui/app.py
```

The executable will be generated inside:

```text
dist/app.exe
```

---

## 📸 Screenshots

Add screenshots here:

* Dashboard
* Email Extractor
* File Organizer
* Website Scraper
* Reports Page
* Settings Page
* About Page

---

## 🔮 Future Enhancements

* Cloud deployment
* Database integration
* User authentication
* Email sending functionality
* Data visualization dashboard
* Multi-threading for faster processing
* Cross-platform installer

---

## 👩‍💻 Developer

**Vaishnavi Bagal**

Computer Science Engineering Student

Passionate about:

* Python Development
* Automation
* Data Science
* Artificial Intelligence
* Software Development

---

## 📄 License

This project is developed for educational and learning purposes.
