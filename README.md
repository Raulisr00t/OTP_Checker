# OTP Email Sender

This project is a Python script that sends an OTP (One-Time Password) via email to a recipient. The script uses an HTML template for the email content and integrates the OTP and activation link dynamically.

## Features

- Generates a random 4-digit OTP.
- Reads and uses an HTML template for the email body.
- Sends email using the Gmail SMTP server.
- Provides both plain text and HTML versions of the email content.

## Prerequisites

- Python 3.x
- Gmail account with "App Password" enabled. [How to generate an App Password](https://support.google.com/accounts/answer/185833?hl=en)

## Installation

1. Clone the repository or download the script file.

2. Install required packages (if not already installed):
    ```bash
    pip install email
    ```

3. Create an `index.html` file in the same directory as the script with the following content:

    ```html
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Verification Code</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f7f9fc;
                margin: 0;
                padding: 0;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            .email-container {
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333333;
            }
            p {
                color: #666666;
            }
            .code {
                display: inline-block;
                margin: 20px 0;
                padding: 10px 20px;
                font-size: 24px;
                color: #ffffff;
                background-color: #4CAF50;
                border-radius: 5px;
                letter-spacing: 2px;
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #999999;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <h1>Email Verification</h1>
            <p>Hello,</p>
            <p>Please use the following code to verify your account:</p>
            <div class="code">{{ activation_code }}</div>
            <p>This code is valid for 5 minutes.</p>
            <p>If you close the site you can click and go to the site: <a href="{{ activation_link }}">here</a></p>
            <div class="footer">
                <p>If you did not request this, please ignore this message.</p>
                <p>&copy; 2024 Esago. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    ```

## Configuration

1. Update the script with your Gmail account details:
    ```python
    owner_email = "your@gmail.com"
    owner_password = "your_app_password"
    ```

## Usage

1. Run the script:
    ```bash
    python otp_sender.py
    ```

2. Enter the recipient's email address when prompted:
    ```plaintext
    Enter the recipient's email address: recipient@example.com
    ```

3. The script will generate an OTP, send the email, and print the OTP to the console.

## Error Handling

- The script checks if the email address is provided and if it is in the correct format.
- Any errors during the email sending process will be caught and printed to the console.

## Example

```plaintext
Enter the recipient's email address: recipient@example.com
OTP sent to recipient@example.com: 1234
```

## License

This README file provides an overview of the project, installation steps, configuration details, usage instructions, error handling, an example, and licensing information.
