
import smtplib
import os
from email.message import EmailMessage
from pathlib import Path
import getpass

# Email configuration
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Use your personal email for testing first
TEST_MODE = False

TEST_EMAIL = "deepunmt01@gmail.com"
HR_EMAIL = "hr@ignitershub.com"


# Student details
NAME = "Devender Mathela"
SEMESTER = "7th Semester"
BRANCH = "Computer Science and Engineering"
ROLL_NUMBER = "230180101017"

# Image attachment
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "Professional.jpeg"


def send_email():
    global SENDER_EMAIL, SENDER_PASSWORD
    # Fallback to interactive input if environment variables are not set
    if not SENDER_EMAIL:
        SENDER_EMAIL = input("Enter your Sender Email (Gmail): ").strip()
    if not SENDER_PASSWORD:
        SENDER_PASSWORD = getpass.getpass("Enter your 16-digit Gmail App Password: ").strip()
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: Sender email and password are required.")
        return
    # Select recipient
    receiver_email = TEST_EMAIL if TEST_MODE else HR_EMAIL
    # Validate image attachment
    if not IMAGE_PATH.is_file():
        print(f"Error: Image attachment not found at '{IMAGE_PATH}'!")
        return
    extension = IMAGE_PATH.suffix.lower()
    if extension not in [".png", ".jpg", ".jpeg"]:
        print("Error: Only PNG, JPG, and JPEG images are allowed.")
        return
    # Create email message
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = "Challenge 3 Completed"
    body = f"""Hello HR Team,
I have successfully completed Challenge 3.
Student Details:
Name: {NAME}
Semester: {SEMESTER}
Branch: {BRANCH}
Roll Number: {ROLL_NUMBER}
Please find the attached image.
Regards,
{NAME}
"""
    msg.set_content(body)
    # Attach image
    subtype = "jpeg" if extension in [".jpg", ".jpeg"] else "png"
    with open(IMAGE_PATH, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="image",
            subtype=subtype,
            filename=IMAGE_PATH.name
        )
    try:
        print(f"Connecting to SMTP server... (Sending to: {receiver_email})")
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
        print("Recipient:", receiver_email)
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed! Please make sure you are using a 16-digit Google App Password, not your standard Gmail password.")
    except Exception as error:
        print("Email sending failed:", error)
if __name__ == "__main__":
    send_email()