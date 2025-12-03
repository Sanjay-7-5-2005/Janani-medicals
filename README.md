# Janani Medicals Pharmacy App

A simple Flask-based web application for Janani Medicals, allowing users to browse services, place orders by uploading prescriptions, and contact the pharmacy.

## Features

- **Home Page:** Overview of services and welcome message.
- **Order Now:** Users can upload a prescription image to place an order.
- **Contact Us:** Information on how to reach the pharmacy.
- **Email Notifications:** Automatically sends an email with the order details and prescription attachment to the pharmacy admin.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Email:** Flask-Mail
- **Styling:** Custom CSS with a responsive design

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Sanjay-7-5-2005/Janani-medicals.git
    cd Janani-medicals
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your email credentials:
    ```env
    MAIL_SERVER=smtp.gmail.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME=your_email@gmail.com
    MAIL_PASSWORD=your_app_password
    MAIL_DEFAULT_SENDER=your_email@gmail.com
    RECIPIENT_EMAIL=recipient_email@gmail.com
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```

6.  **Access the app:**
    Open your browser and go to `http://127.0.0.1:5000`

## Project Structure

```
Janani-medicals/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
├── .gitignore          # Git ignore file
├── templates/          # HTML templates
│   ├── layout.html
│   ├── home.html
│   ├── order.html
│   └── contact.html
└── uploads/            # Directory for uploaded prescriptions
```
