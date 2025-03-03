from twilio.rest import Client

# Twilio credentials
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxx"  # Replace with new token if regenerated

# Twilio phone number
twilio_number = "xxxxxxxxxxxxxxx"

# Alert recipient (Replace with your phone number)
recipient_number = "xxxxxxxxxxx"

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
