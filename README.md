
# 📊📧 Conversational-Agent-for-Automated-Daily-Report-Generation

## 🚀 Implementation

1. **Extract Data**: Extract data from the sales spreadsheet.
2. **Generate Report**: Generate a daily sales report in PDF format.
3. **Email Report**: Email the report to the management team.
4. **Scheduling**: Send the report on demand or schedule the mailing at a certain time .

## 📦 Dependencies

This project uses Python for scripting and automation. The following libraries are required:

- **Pandas**: For reading spreadsheet files.
- **reportLab**: For report generation.
- **schedule**: To schedule daily mail.
- **smtplib**: To send mail using SMTP server.
- **NLTK**: To create and manage a conversational agent to perform all user-specified tasks.

## 🛠️ Instructions on How to Run the Scripts

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:
    ```bash
    pip install pandas reportlab schedule smtplib nltk
    ```

3. **Set up email server settings**:
    - Use an app password to send emails as Google Mail server rejects regular account mails to connect.
    - Update the email server settings in the script with your email credentials.

4. **Run the script**:
    ```bash
    python main.py
    ```

## ✉️ Email Server Settings

- Use app password to send mails (Google Mail server rejects regular account mails) 🔒
- SMTP server: 'smtp.gmail.com'
- Port: 587
- Email address: [your_email@example.com](mailto:your_email@example.com)
- App password: your_app_password

  
## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For any questions or suggestions, please contact:

- **Email**: [mail](mailto:santoshkumarnawd@gmail.com)
- **LinkedIn**: Santosh Kumar

---

Feel free to customize this `README.md` file further to suit your project's needs. If you have any other details or sections you'd like to add, let me know! 😊
