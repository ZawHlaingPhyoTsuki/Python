import qrcode
from PIL import Image
import os

# Define the value for the QR code
value = input("Enter the value (URL or Text) for the QR code: ")


# Create a QR code instance
qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
qr_code.add_data(value)
qr_code.make(fit=True)

# Generate the QR code image
qr_image = qr_code.make_image(fill="black", back_color="white")

# Function to get the next filename
def get_next_filename(base_filename):
    count = 1
    while os.path.exists(f"{base_filename}{count}.png"):
        count += 1
    return f"{base_filename}{count}.png"

# Get the next filename
filename = get_next_filename("qr")
# Save the QR code image
qr_image.save(filename)

print(f"QR code saved as {filename}")

 
