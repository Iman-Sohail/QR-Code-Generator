# QR Code Generator

## Overview

This project is a Python-based QR code generator that allows users to create QR codes for different types of data, including email addresses, phone numbers, URLs, and text.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed before using the QR code generator:

- Python 3.12.1
- Pillow library: `pip install pillow`
- qrcode library: `pip install qrcode`

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Iman-Sohail/QR-Code-Generator.git
cd QR-Code-Generator
```

### Usage

To generate a QR code, run the following command:

```bash
python main.py
```

Follow the prompts to choose the type of QR code and provide the required information.

1. **Email QR Code:**

   Enter '1' when prompted for the type of QR code, then enter your email address.

2. **Phone QR Code:**

   Enter '2' when prompted for the type of QR code, then enter your phone number.

3. **URL QR Code:**

   Enter '3' when prompted for the type of QR code, then enter the website URL.

4. **Text QR Code:**

   Enter '4' when prompted for the type of QR code, then enter your custom text.

### Configuration (Optional)

Customize the appearance of the generated QR codes by following the prompts for color and size options.

## Customization

Adjust QR code colors and appearance by following the prompts during the customization step.

## Validation

Ensure the accuracy of input data with basic validation checks for email, phone, and URL formats.

## Troubleshooting

If you encounter any issues, refer to the following troubleshooting tips:

- **Problem:** Invalid input format.
  - **Solution:** Check the input format for email, phone, or URL and correct any errors.

- **Problem:** Exceeded maximum attempts.
  - **Solution:** Restart the process and ensure valid input within the allowed attempts.

## Contributing

Contributions to this project are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project utilizes the qrcode and Pillow libraries for QR code generation.
