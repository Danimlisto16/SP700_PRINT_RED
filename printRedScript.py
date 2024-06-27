import socket

def send_escpos_command(printer_ip, printer_port, command):
    """
    Sends an ESC/POS command to a printer via socket.

    :param printer_ip: IP address of the printer.
    :param printer_port: Port number of the printer.
    :param command: The ESC/POS command to send.
    """
    try:
        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((printer_ip, printer_port))
            s.sendall(command)
            print("Command sent successfully")
    except Exception as e:
        print(f"Failed to send command: {e}")

def print_in_red_and_black(printer_ip, printer_port, red_data, black_data):
    """
    Sends data to the printer to be printed in red followed by data in black.

    :param printer_ip: IP address of the printer.
    :param printer_port: Port number of the printer.
    :param red_data: Data to be printed in red.
    :param black_data: Data to be printed in black.
    """
    # ESC/POS command to select red color (for Star printers)
    select_red_command = b'\x1b\x34'


    # ESC/POS command to reset to black color (default)
    reset_color_command = b'\x1b\x35'


    # Data to be printed in red
    red_print_data = red_data.encode('utf-8')


    # Data to be printed in black
    black_print_data = black_data.encode('utf-8')

    
    # Newline command
    new_line = b'\x0A'

    # Combine commands
    red_command = select_red_command + red_print_data + new_line + reset_color_command
    black_command = black_print_data + new_line

    # Send the red command to the printer
    send_escpos_command(printer_ip, printer_port, red_command)
    # Send the black command to the printer
    send_escpos_command(printer_ip, printer_port, black_command)

# Example usage
printer_ip = "10.0.0.13"  # Replace with your printer's IP address
printer_port = 9100           # Replace with your printer's port number
red_data = "This text will be printed in red."
black_data = "This text will be printed in black."

print_in_red_and_black(printer_ip, printer_port, red_data, black_data)
