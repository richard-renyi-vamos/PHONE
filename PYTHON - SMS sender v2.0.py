import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client

# Function to send SMS
def send_sms():
    account_sid = account_sid_entry.get()
    auth_token = auth_token_entry.get()
    twilio_number = twilio_number_entry.get()
    to_number = to_number_entry.get()
    message_body = message_body_text.get("1.0", tk.END).strip()
    
    if not account_sid or not auth_token or not twilio_number or not to_number or not message_body:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=to_number
        )
        messagebox.showinfo("Success", f"Message sent with SID: {message.sid}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("SMS Sender")

# Create and place the input fields and labels
tk.Label(root, text="Twilio Account SID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
account_sid_entry = tk.Entry(root, width=40)
account_sid_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Twilio Auth Token:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
auth_token_entry = tk.Entry(root, width=40, show="*")
auth_token_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Twilio Phone Number:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
twilio_number_entry = tk.Entry(root, width=40)
twilio_number_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Recipient Phone Number:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
to_number_entry = tk.Entry(root, width=40)
to_number_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Message Body:").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
message_body_text = tk.Text(root, width=30, height=5)
message_body_text.grid(row=4, column=1, padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send SMS", command=send_sms)
send_button.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
