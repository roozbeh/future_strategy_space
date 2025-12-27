import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# ============================================================================
# CONFIGURATION - Update these with your email settings
# ============================================================================



SMTP_SERVER = "smtp.porkbun.com"
SMTP_PORT = 587  # Use 465 for SSL, 587 for TLS
SENDER_EMAIL = "info@futurestrategy.space"
SENDER_PASSWORD = "PASSWORD"  # Your email password or app password
SENDER_NAME = "FutureStrategy"  # Name to display in emails

# Email subject (can include template variables)
EMAIL_SUBJECT = "Hello {{first_name}} - how can we help?"

# Email template with personalization placeholders
EMAIL_TEMPLATE = """
Hi {{first_name}},

Thanks for responding to our campaign.

At our core, we work with small and mid-sized businesses to make AI practical, affordable, and genuinely useful, not complicated or overwhelming. Our mission is simple: we help you use tools like AI-powered chatbots and automation to save time and scale operations without adding extra staff or complexity.

Because no two businesses are the same, we’d love to learn more about your current setup. This allows us to identify the specific areas where AI can drive measurable cost reduction and increase revenue for your company.

Are you open to a 30-minute conversation to explore your goals?

You can choose a time that works best for you on our calendar here: https://calendly.com/futurestrategy-info/30min

Best
FutureStrategy Team
"""

# ============================================================================
# RECIPIENT LIST - Add your recipients here
# ============================================================================

RECIPIENTS = [
    # {
    # "first_name": "Rafael",
    # "email": "rafa4114@hotmail.com",
    # },
    # {
    # "first_name": "Lilly",
    # "email": "lilly_sps@yahoo.com",
    # },
    # {
    # "first_name": "Jeffery",
    # "email": "jeffreyrattiliff1@gmail.com",
    # },
    # {
    # "first_name": "Brathwaite",
    # "email": "francisco@allhandsupinc.org",
    # },
    # {
    # "first_name": "Allen",
    # "email": "allendavis2712bn@gmail.com",
    # },
    # {
    # "first_name": "Tommy",
    # "email": "tommyleegriffinjr88@gmail.com",
    # },
    # {
    # "first_name": "Mark",
    # "email": "markhargrove61@yahoo.com",
    # },
    # {
    # "first_name": "Robby",
    # "email": "robbydurdin68@gmail.com",
    # },
    # {
    # "first_name": "Rolando",
    # "email": "culebrarolando756@gmail.com",
    # },
    # {
    # "first_name": "Emma",
    # "email": "isseke11@gmail.com",
    # },
    {
    "first_name": "Joseph",
    "email": "josephjeanpaul23@gmail.com",
    },
    {
    "first_name": "mkeeewww",
    "email": "mikekral80@gmail.com",
    },
    # {
    # "first_name": "Jose",
    # "email": "joseandrescruz1753@gmail.com",
    # },
    # {
    # "first_name": "Cesar",
    # "email": "Cesarsold@yahoo.com",
    # },
    # {
    # "first_name": "Michael",
    # "email": "austell.a.engineering@gmail.com",
    # },
    # {
    # "first_name": "Tim",
    # "email": "darkvader4timothy@gmail.com",
    # },
]
# ============================================================================
# FUNCTIONS
# ============================================================================

def personalize_text(text, recipient):
    """
    Replace template variables in text with recipient's data.
    Variables are in the format {{variable_name}}
    """
    personalized = text
    
    # Add sender information to available variables
    recipient_data = {
        **recipient,
        "sender_email": SENDER_EMAIL,
        "sender_name": SENDER_NAME
    }
    
    # Replace all {{variable}} with recipient's data
    for key, value in recipient_data.items():
        placeholder = f"{{{{{key}}}}}"
        personalized = personalized.replace(placeholder, str(value))
    
    return personalized


def send_email(recipient):
    """Send personalized email to a single recipient"""
    try:
        # Personalize subject and body
        subject = personalize_text(EMAIL_SUBJECT, recipient)
        body = personalize_text(EMAIL_TEMPLATE, recipient)
        
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        message["To"] = recipient["email"]
        
        # Attach body as plain text
        message.attach(MIMEText(body, "plain"))
        
        # Connect to SMTP server and send
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient["email"], message.as_string())
        
        print(f"✓ Email sent to {recipient['first_name']} ({recipient['email']})")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send email to {recipient['email']}: {str(e)}")
        return False


def send_bulk_emails():
    """Send emails to all recipients"""
    print(f"\n{'=' * 60}")
    print(f"Sending {len(RECIPIENTS)} emails...")
    print(f"{'=' * 60}\n")
    
    successful = 0
    failed = 0
    
    for recipient in RECIPIENTS:
        if send_email(recipient):
            successful += 1
        else:
            failed += 1
        
        # Add a small delay between emails to avoid rate limiting
        time.sleep(1)
    
    # Print summary
    print(f"\n{'=' * 60}")
    print(f"Email Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(RECIPIENTS)}")
    print(f"{'=' * 60}\n")


# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    send_bulk_emails()
