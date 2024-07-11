PRINT RED
The bytes b'\x1b\x34' and b'\x1b\x35' are ESC/POS commands used to change the print color on certain Star printers.

Explanation of Values
b'\x1b\x34': This is an ESC/POS command to select the red print color.

\x1b is the hexadecimal representation of the ESC (Escape) character, which is commonly used in control sequences for printers.
\x34 is the hexadecimal representation of the digit 4. Together with ESC, this sequence (ESC 4 or \x1b\x34) is used to switch the printer to red color mode.
b'\x1b\x35': This is an ESC/POS command to reset the printer back to the default black print color.

\x1b is the ESC character.
\x35 is the hexadecimal representation of the digit 5. Together with ESC, this sequence (ESC 5 or \x1b\x35) is used to switch the printer back to black color mode.

> Switch Back/Red ink while printing
![image001](https://github.com/Danimlisto16/SP700_PRINT_RED/assets/50421224/d240adf0-ab06-465d-8b05-77cc7e9909a4)


#PRINT LARGE FONT
to print x6 times bigger width and height , you need to send the next command:
x6_heigth = b'\x1B\x68\x36'  # Example custom command 
x6_width= b'\x1B\x57\x36' # Example custom command 

after send this commands is possible send any text,

to reset the size send :

reset_heigth = b'\x1B\x68\x30'  # Example custom command 
reset_width= b'\x1B\x57\x30' # Example custom command 
> Font Size Docs
![fontSize](https://github.com/Danimlisto16/SP700_PRINT_RED/assets/50421224/ed991431-b44b-4764-ba1b-57d4b7babfa0)
