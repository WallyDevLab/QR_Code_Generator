import qrcode
from tkinter import Tk, Label, Entry, Button, PhotoImage, messagebox
from PIL import Image, ImageTk

def generate_qr_code(url):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Return the image
    return img

def generate_qr_code_from_input():
    # Get URL input from entry widget
    url = url_entry.get()

    # Generate QR code
    qr_code = generate_qr_code(url)

    # Convert PIL image to PhotoImage
    img = ImageTk.PhotoImage(qr_code)

    # Update label with QR code image
    qr_label.config(image=img)
    qr_label.image = img

def main():
    # Create main window
    root = Tk()
    root.title("QR Code Generator")

    # URL entry widget
    global url_entry
    url_entry = Entry(root, width=40)
    url_entry.pack(pady=10)

    # Button to generate QR code
    generate_button = Button(root, text="Generate QR Code", command=generate_qr_code_from_input)
    generate_button.pack()

    # Label to display QR code
    global qr_label
    qr_label = Label(root)
    qr_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
