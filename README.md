# 💻 Flipkart Laptop Scraper 🛍️

This project is a web scraping script that extracts **laptop titles** and **prices** from the **Flipkart Laptop Section**, stores the scraped HTML, parses the data using **BeautifulSoup**, and finally saves it into a structured **CSV file** using **Pandas**.

## 📌 Features

- ✅ Scrapes laptop product titles and prices from Flipkart.
- ✅ Stores raw HTML for backup and offline parsing.
- ✅ Parses data using `BeautifulSoup` from stored HTML.
- ✅ Saves clean data into `data.csv`.
- ✅ Lightweight and modular code.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| 🐍 Python | Programming Language |
| 🌐 Selenium | For live scraping of the webpage |
| 🧼 BeautifulSoup (bs4) | For parsing saved HTML |
| 📊 Pandas | For converting data into a DataFrame and saving to CSV |
| 🧪 ChromeDriver | WebDriver for automating browser |

---

## 🔄 Workflow

1. **Step 1 – Scraping with Selenium**  
   Uses Selenium to open the Flipkart laptop section and scrape:
   - Laptop **Title**
   - Laptop **Price**

2. **Step 2 – Saving HTML**  
   Saves the complete HTML of the page into a file called `laptops.html`.

3. **Step 3 – Parsing with BeautifulSoup**  
   Loads the `laptops.html` file and extracts titles and prices.

4. **Step 4 – Exporting to CSV**  
   Stores the extracted data into a structured `data.csv` file.

---

## 📁 File Structure

