import qrcode
from tkinter import Tk, Label, Entry, Button, PhotoImage, messagebox
from PIL import Image, ImageTk

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def generate_qr_code_from_input(url_entry, qr_label):
    url = url_entry.get()
    if url:
        qr_code = generate_qr_code(url)
        img = ImageTk.PhotoImage(qr_code)
        qr_label.config(image=img)
        qr_label.image = img
    else:
        messagebox.showerror("Error", "Please enter a URL.")

def main():
    root = Tk()
    root.title("QR Code Generator")

    url_entry = Entry(root, width=40)
    url_entry.pack(pady=10)

    generate_button = Button(root, text="Generate QR Code", command=lambda: generate_qr_code_from_input(url_entry, qr_label))
    generate_button.pack()

    qr_label = Label(root)
    qr_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()