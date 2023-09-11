The SubI machine works with a string that contains 0s, 1s, newlines and other space(whivh are simply ignored).
It converts 0s and 1s into a word (complex number in base i-1 with specified in config.py length).
Newlines makes code(data) to shift to (number of lines + 1)i. Yes, code and data are the same and two-dimensional.
Negative position is allowed.

You can manipulate with data using commands:

1111111111111(-38+13i) - ends the program
0000001110111(3j) - prints at the position of the first argument the chracter of the code, that is the real value of the first argument, with curses atributes of the imag value.
0110111001100(42) - goto.
0000110011110(5-7i) - if the value under the argument is 0, then go up by i, else skip.
0001100001111(2+17i) - adds secons argument to the value under the first argument.
0000100011111(14+i) - copies the value under the second argument to the cell under the first.
0001101110111(19i) - shifts by the value under the second argument value under the first.
0110110110110(39-13i) - getch() to the argument.
0000000011101(-1) - negates the argument.
0000001100000(4+4i) - performs subIwise and.
1111110011111(-42+9j) - performs subIwise or.

Also, there is a tool called basesubi.py, which helps you convert to and from base i-1.
