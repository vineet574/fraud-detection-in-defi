from twilio.rest import Client

# Twilio credentials
account_sid = "ACcbeb9a6bea6cfe2a97da661195f02870"
auth_token = "daf07be9228a6672bda9ce32184239e2"  # Replace with new token if regenerated

# Twilio phone number
twilio_number = "+13616007456"

# Alert recipient (Replace with your phone number)
recipient_number = "+919360656493"

# Message content
message_body = "🚨 Fraud Alert! Suspicious transaction detected in DeFi monitoring system."

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS alert
message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to=recipient_number
)

print(f"✅ Alert sent! Message SID: {message.sid}")
