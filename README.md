# 📈 Marketing Automation for a Small-Scale Business

This project (2023–2024) was developed for a **startup** with **no marketing budget** and **no existing customer database**.  
The goal was to **boost marketing capabilities** by building an **end-to-end automated lead extraction and outreach system**.

---

## 🚀 Project Overview

The client, a small startup, needed a way to:
- **Find potential customers** without buying expensive marketing lists.
- **Organize unstructured contact data** into a usable database.
- **Send targeted marketing emails at scale** with minimal manual effort.

I implemented a three-step solution:

---

### 1️⃣ Data Extraction – Web Crawler
- Identified a public source: [fastcashconsulting.com](https://fastcashconsulting.com), which contained tens of thousands of potential customer records (email, company name, etc.).
- Built a **Python web scraper** to extract semi-structured text data from the site.
- **Code:** [`text_extraction.py`](https://github.com/charmrain/marketing_overkill/blob/main/webscrapy/text_extraction.py)

---

### 2️⃣ Data Structuring – CSV Database
- Converted extracted **semi-structured data** into a **clean, structured format**.
- Organized customer names, emails, and business areas into a CSV database for easy querying.
- **Code:** [`hyperlink_parser.py`](https://github.com/charmrain/marketing_overkill/blob/main/data%20parse/hyperlink_parser.py)

---

### 3️⃣ Automated Outreach – Mass Email Sending
- Used the structured database to select targeted potential customers.
- Developed a **mass email automation script** to send personalized marketing emails.
- Fully automated the sending process for efficiency and scalability.
- **Code:** [`massive_mails.py`](https://github.com/charmrain/marketing_overkill/blob/main/mail/massive_mails.py)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Requests**, **BeautifulSoup4** – Web scraping
- **pandas** – Data structuring & CSV export
- **smtplib**, **email.mime** – Email automation
- CSV as the lightweight database

---

## 📊 Workflow

1. **Data Source**
   - Public website containing semi-structured customer information.

2. **Web Crawling**
   - Scrape text data using Python and BeautifulSoup4.

3. **Data Parsing & Structuring**
   - Convert semi-structured text into a structured CSV database.

4. **Automated Outreach**
   - Use the CSV database to send targeted marketing emails at scale.

---

## 📌 Use Cases

- **Lead Generation** – Build a customer database from public sources.
- **Small-Business Marketing** – Affordable outreach without buying expensive lists.
- **Automated Email Campaigns** – Save hours of manual work.

---

## 📜 License

This project is for **educational and demonstration purposes only**.  
The use of scraped data must comply with relevant laws and the source website’s terms of service.

---

## 🙌 Acknowledgments

- Inspiration from real-world startup challenges.
- Open-source Python libraries for making automation possible.
