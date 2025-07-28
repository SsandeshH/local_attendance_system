# 📝 Local_Attendance_System
Local_Attendance_System is a lightweight, offline-ready attendance system designed to run on a local network (e.g., personal hotspot or LAN). It provides a simple interface for students to mark attendance and an admin panel for data management.

## Highlights
- 🌐 Offline Local Network Use — Runs on a private hotspot or LAN, no internet needed.
- 📱 QR Code for Easy Access — Admin can generate and display a QR code of the app’s URL.
- 🧑‍🎓 Student Interface — Students connect to the network, fill in their details, and submit attendance.
- 📊 Exportable Data — All submissions are compiled and exported as .xlsx Excel sheets.

## 📁 Project Structure

```text
Local_Attendance_System/
├── app/                          # Application package
│   ├── static/                   # Static files (e.g., images, CSS)
│   │   └── images/               # Image assets
│   │
│   ├── templates/                # HTML templates for Flask
│   │   ├── index.html            # Landing page for users
│   │   └── admin.html            # Admin panel for export/config
│   │
│   ├── app.py                    # Main Flask application runner
│   ├── data_export.py            # XLSX export logic
│   └── data_handle.py            # In-memory data dictionary handler
│
├── data/                         # Folder to store exported XLSX files
│
├── requirements.txt              # List of required Python packages
├── README.md                     # Project documentation
└── .gitignore                    # Git ignored files/folders
```
# Installation Guide
1. Git clone this repository.
2. Create a vitual environment (Recommended)
    - For Linux/MacOS:
   ```text 
   python3 -m venv env
   source env/bin/activate
   ```
   - For Windows:
   ```text
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install requirements
    - ```text
        pip install -r requirements.txt
        ```
4. Run the app(In terminal)
    ```text 
    python app.py
    ```

## For Admin
To generate the QR code, You will need to know the ip address of your hosting computer. To know the IP:
- For Windows/MacOS in CMD/bash:
    ```text
    ifconfig
    ```
    example: Look for inet 192.168.1.x


- For Linux(Debian,Ubuntu) in Terminal:
    ```text
    hostname -I
    ```
    example: 192.168.1.73 172.17.0.1  ....
    your ip is 192.168.1.73

From this , You can determine your Application Url be:

http://PC-IP-Address:8000/

http://192.168.1.73:8000/

Paste this to generate the QR code

## 📤 Exporting Attendance
1. Navigate to /admin in your browser.

2. Click the Export button.

3. Exported .xlsx files will be saved in the data/ directory.