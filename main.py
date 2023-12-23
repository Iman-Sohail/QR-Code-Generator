import qrcode
from PIL import Image

MAX_TRIES = 5

def generate_qr_code(data, filename="qrcode.png", fill_color="black", back_color="white", box_size=20, border=1):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save QR code image
    qr_code.save('./qr_code_images/'+filename)
    print(f"QR code saved as {filename}")

def qr_code_colors():
    fill_color = input("Please enter fill color (Default: Black): ").strip() or "black"
    back_color = input("Please enter back color (Default: White): ").strip() or "white"
    box_size = input("Please enter box size (Default: 20): ").strip() or 20
    border = input("Please enter border (Default: 1): ").strip() or 1

    try:
        box_size = int(box_size)
        border = int(border)
    except ValueError:
        print("Invalid input for box size or border. Please enter valid numbers.")
        exit()

    return fill_color, back_color, box_size, border

def validate_email(email):
    # Basic email validation
    return '@' in email and '.' in email

def validate_phone(phone):
    # Basic phone number validation
    if not phone.isdigit():
        print("Phone number can't include letters. Please enter a valid phone number.")
        return False

    # Check if the phone number starts with '0' but does not have a country code
    if phone.startswith('0'):
        print("Phone number should include a country code. Please enter a valid phone number.")
        return False

    return True


def validate_url(url):
    # Basic URL validation
    return url.startswith(("http://", "https://"))

qr_type = input("Please enter the type of QR Code (e.g., email=1, phone=2, url=3, text=4): ").lower()

for _ in range(MAX_TRIES):
    if qr_type == "email" or qr_type == "1":
        email_input = input("Enter your email: ")
        if validate_email(email_input):
            generate_qr_code("mailto:" + email_input, "email_qrcode.png", *qr_code_colors())
            break

    elif qr_type == "phone" or qr_type == "2":
        phone_input = input("Enter your phone: ")
        if validate_phone(phone_input):
            generate_qr_code("tel:+" + phone_input, "phone_qrcode.png", *qr_code_colors())
            break

    elif qr_type == "url" or qr_type == "3":
        website_input = input("Enter website URL: ")
        if validate_url(website_input):
            generate_qr_code(website_input, "website_qrcode.png", *qr_code_colors())
            break

    elif qr_type == "text" or qr_type == "4":
        text_input = input("Enter your text: ")
        generate_qr_code(text_input, "text_qrcode.png", *qr_code_colors())
        break

    else:
        print(f"Unsupported QR type: {qr_type}. Please choose from email, phone, url, or text.")
        break

    if _ < MAX_TRIES - 1:
        print(f"Invalid input. Please try again. Attempts left: {MAX_TRIES - (_ + 1)}")
    else:
        print("Exceeded maximum attempts. Exiting.")
        exit()