The bytes b'\x1b\x34' and b'\x1b\x35' are ESC/POS commands used to change the print color on certain Star printers.

Explanation of Values
b'\x1b\x34': This is an ESC/POS command to select the red print color.

\x1b is the hexadecimal representation of the ESC (Escape) character, which is commonly used in control sequences for printers.
\x34 is the hexadecimal representation of the digit 4. Together with ESC, this sequence (ESC 4 or \x1b\x34) is used to switch the printer to red color mode.
b'\x1b\x35': This is an ESC/POS command to reset the printer back to the default black print color.

\x1b is the ESC character.
\x35 is the hexadecimal representation of the digit 5. Together with ESC, this sequence (ESC 5 or \x1b\x35) is used to switch the printer back to black color mode.
