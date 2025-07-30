Here’s a **detailed, placement-ready `README.md`** for your **WhatsApp Chat Analyzer** project using **Streamlit**:

---

# 📊 WhatsApp Chat Analyzer

An interactive web app built using **Streamlit** that analyzes WhatsApp group or personal chats from `.txt` export files. It provides detailed insights including message frequency, emoji usage, active users, and much more using data visualization techniques.

---

### 📌 Features

- ✅ Upload and parse WhatsApp `.txt` chat files  
- ✅ View top-level statistics (messages, words, media, links)  
- ✅ Monthly and daily timeline analysis  
- ✅ Day-wise and month-wise activity map  
- ✅ Weekly heatmap of chat activity (Hour vs Day)  
- ✅ Identify most active users (if analyzing group chats)  
- ✅ Generate a word cloud of most used words  
- ✅ Visualize top 20 most common words  
- ✅ Emoji usage breakdown with pie chart and rankings


---

## 📷 Sample Visualizations


<img width="897" height="241" alt="image" src="https://github.com/user-attachments/assets/5eee5fa0-d10a-4d4b-918b-755da7a5d220" />

* 📈 Monthly / Daily Activity Graphs

  <img width="997" height="873" alt="Screenshot 2025-07-30 100143" src="https://github.com/user-attachments/assets/ef73036b-b0e5-48e8-bb77-a025a92042ae" />

  
  <img width="990" height="858" alt="image" src="https://github.com/user-attachments/assets/46aabb58-f66a-47aa-9f4e-fc980f61e078" />
  
* 📅 Activity Heatmap (Day vs Hour)

  
  <img width="993" height="661" alt="Screenshot 2025-07-30 100235" src="https://github.com/user-attachments/assets/1b739618-6179-4759-8040-a8f9499df50d" />

* ☁️ WordCloud

  
  <img width="936" height="818" alt="Screenshot 2025-07-30 100307" src="https://github.com/user-attachments/assets/4d6f54a8-ce49-4a2c-9a28-8db30a5059e2" />

* 😀 Emoji Pie Chart

  
  <img width="951" height="698" alt="image" src="https://github.com/user-attachments/assets/d7f9cb8a-1ba0-4228-887c-c6be427b394c" />

* 📊 Bar Charts for most common words and active days

  
  <img width="970" height="756" alt="image" src="https://github.com/user-attachments/assets/9658ff78-077a-4889-abb2-a499137ee402" />


---

## 🔧 Tech Stack

| Technology     | Description                |
| -------------- | -------------------------- |
| **Python**     | Core programming language  |
| **Streamlit**  | Web app framework          |
| **Matplotlib** | Plotting charts            |
| **Seaborn**    | Advanced visualizations    |
| **Pandas**     | Data manipulation          |
| **WordCloud**  | Generate word clouds       |
| **urlextract** | Extract URLs from text     |
| **emoji**      | Extract and analyze emojis |

---

## 📂 Folder Structure

```plaintext
whatsapp-chat-analyzer/
│
├── main.py               # Streamlit app main file
├── helper.py             # Helper functions for stats & visualizations
├── preprocessor.py       # Chat parsing and preprocessing logic
├── stop_hinglish.txt     # Custom stop words list (Hinglish)
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
```
---

## 📁 How to Export WhatsApp Chat

1. Open WhatsApp and go to the chat you want to export.
2. Tap on the three-dot menu (top-right).
3. Select **More > Export Chat**.
4. Choose **WITHOUT MEDIA**.
5. Send it to your email or save it as a `.txt` file.
6. Upload it into the app via the **sidebar**.

---
### 🧩 Detailed Functionality

| Section | Description |
|---------|-------------|
| **📁 File Upload** | Upload a WhatsApp chat `.txt` file (exported from WhatsApp) using the sidebar. The file is parsed and cleaned for further analysis. |
| **👤 User Selection** | Choose either a specific user from the chat or analyze the chat as a whole (`Overall`). |
| **📊 Top Statistics** | Displays total messages, word count, number of media files, and links shared by the selected user or group. |
| **📈 Monthly Timeline** | A line graph showing the number of messages sent per month over time to visualize chat consistency or activity spikes. |
| **📅 Daily Timeline** | Shows daily message count to detect high-activity days. Useful for identifying dates with key conversations. |
| **📆 Activity Map** | Two bar charts:<br>• **Busy Days**: Messages sent per day of the week (e.g., Monday, Tuesday).<br>• **Busy Months**: Total messages sent per month. Helps detect peak chat periods. |
| **🧭 Weekly Activity Heatmap** | Heatmap showing the distribution of messages by weekday and hourly time slots, helping to understand chat behavior (e.g., active late at night on weekends). |
| **🙋 Most Active Users** *(Only in Overall mode)* | Displays top contributors in a group chat using a bar chart and a table with percentage share and message count. |
| **☁️ Word Cloud** | A visual representation of the most frequently used words, ignoring common Hinglish stopwords. |
| **🔤 Most Common Words** | A horizontal bar chart listing the top 20 words used, excluding stopwords. |
| **😀 Emoji Analysis** | Table and pie chart showing the most frequently used emojis and their percentage distribution. |


## 📌 Example Stats You’ll Get

* **Total Messages**: 17,532
* **Total Words**: 89,470
* **Media Shared**: 132
* **Links Shared**: 98
* **Top 5 Active Users**
* **Top 20 Words**
* **Most Used Emojis**: 😂 ❤️ 🙏 🤣

---

## ✅ To-Do / Future Improvements

* 📱 Mobile responsive UI
* 📁 Multi-chat comparison
* 🔍 Sentiment analysis using NLP
* 🧠 Chat summarization
* 📥 Export graphs/reports as PDF

---



## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify it.

---

## 🔗 Acknowledgments

* Streamlit team for an amazing web framework
* Python open-source community
* GitHub Copilot, Stack Overflow & my own curiosity 😄

---

Let me know if you’d like me to add a `requirements.txt` or deploy this to **Streamlit Cloud** with a public URL.
