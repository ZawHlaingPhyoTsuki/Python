import qrcode
from PIL import Image
import os

# Function that ensures a unique filename is genearted, even if the user specifies a name that already exists.
def get_unique_filename(base_filename):
    """Generates a unique filename by appending a number if necessary."""
    count = 1
    filename = base_filename
    while os.path.exists(filename + ".jpg"):
        filename = f"{base_filename}_{count}"
        count += 1
    return filename + ".jpg"

# Get user input for the QR code value and desired filename
value = input("Enter the value (URL or Text) for the QR code: ")
filename = input("Enter the desired filename (without extension): ")

# Create a QR code instance
qr_code = qrcode.QRCode(version=2, box_size=15, border=5)

# Add Data to the QR Code
qr_code.add_data(value)
qr_code.make(fit=True) #Generate the QR code 

# Generate the QR code image
qr_image = qr_code.make_image(fill="black", back_color="white")

# Get the unique filename and save the QR code image
unique_filename = get_unique_filename(filename)
qr_image.save(unique_filename, format="JPEG")

print(f"QR code saved as {unique_filename}")
