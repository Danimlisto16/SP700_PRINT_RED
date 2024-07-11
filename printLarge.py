import socket
import time

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

def send_custom_command_and_text(printer_ip, printer_port, command, text):
    """
    Sends a custom ESC/POS command followed by text to the printer.

    :param printer_ip: IP address of the printer.
    :param printer_port: Port number of the printer.
    :param command: The ESC/POS command to send.
    :param text: The text to send after the command.
    """
    # Encode the text to bytes
    text_data = text.encode('utf-8')

    # Newline command
    new_line = b'\x0A'

    # Combine command and text
    full_command = command + text_data + new_line

    # Send the combined command and text to the printer
    send_escpos_command(printer_ip, printer_port, full_command)

# Example usage
printer_ip = "10.0.0.13"  
printer_port = 9100       
custom_text = "text to test"
custom_command_1 = b'\x1B\x68\x35' #increase HEIGHT  # Example custom command 
custom_command_2= b'\x1B\x57\x35'  #INCREASE WIDTH # Example custom command
custom_command = custom_command_1 + custom_command_2

send_custom_command_and_text(printer_ip, printer_port, custom_command, custom_text)
    
