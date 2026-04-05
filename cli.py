from tkinter import EXCEPTION

from func import QrCodeGenerator as qr

def main():
    data = input("Enter the data to encode in the QR code: ")
    logo = input("Enter the path to the logo image (optional, press Enter to skip): ")
    output = input("Enter the output file name (e.g., 'qrcode.png'): ")

    if not logo:
        logo = None
    if not output:
        output = "Untitled.png"
    if not data:
        print("Error: Data cannot be empty.")
        return

    qr(data, logo, output)
    print(f"QR code generated and saved as '{output}'.")

if __name__ == "__main__":
    main()