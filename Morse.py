""" Simple Morse code translator.

    Note: OK, not really an algorithm, but something I saw and wanted to try"""

from textwrap import fill

MORSE_DCODE = {'..-.': 'F', '-..-': 'X',
               '.--.': 'P', '-': 'T', '..---': '2',
               '....-': '4', '-----': '0', '--...': '7',
               '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
               '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
               '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
               '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
               '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
               '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1',
               '--..--': ',', '.-.-.-': '.', '.----.': "'"
              }

MORSE_NCODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
               'D': '-..', 'E': '.', 'F': '..-.',
               'G': '--.', 'H': '....', 'I': '..',
               'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---',
               'P': '.--.', 'Q': '--.-', 'R': '.-.',
               'S': '...', 'T': '-', 'U': '..-',
               'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..',

               '0': '-----', '1': '.----', '2': '..---',
               '3': '...--', '4': '....-', '5': '.....',
               '6': '-....', '7': '--...', '8': '---..',
               '9': '----.',

               ',': '--..--', '.': '.-.-.-', "'": '.----.'
              }


def decode_morse_old(morsecode):
    """Returns decoded text string for input series of dots, dashes, and spaces
       NOTE: this version works fine, but I wanted to try a 'one liner' using join()
    """

    words = morsecode.split("   ")
    output = ""
    for word in words:
        chars = word.split()
        for char in chars:
            output += MORSE_DCODE[char]
        output += ' '

    return output.strip()


def decode_morse(morsecode):
    """ Returns decoded text string for input series of dots, dashes, and spaces """

    # As a side effect of the inner split() with no argument,
    # Leading and trailing spaces are ignored and no use of strip() is needed
    return ' '.join([''.join([MORSE_DCODE[letter] for letter in word.split()])
                     for word in morsecode.split('   ')])


def encode_morse(txtstr):
    """ Returns encoded string of dots, dashes, and spaces for the input text string"""

    return '   '.join([' '.join([MORSE_NCODE[letter] for letter in word])
                       for word in txtstr.split()])


def main():
    """ Test harness for the morse code translator"""

    print(decode_morse(".... . -.--   .--- ..- -.. ."))
    print(decode_morse(""))
    print(decode_morse("..."))
    print(decode_morse("  -. --- .--   .. ...   - .... .   - .. -- .     "))

    print(decode_morse(encode_morse("HELLO WORLD")))
    print(decode_morse(encode_morse(" Once upon a time in a very dark place     ".upper())))

    # One more test round-tripping a long, multi-line string
    print(fill(decode_morse(encode_morse(
        """
        As a man gets ready for work, we see that he is tense and sweating.
        His wife kisses him goodbye and wishes him good luck. The man throws
        her an uneasy look and picks up his briefcase. We don't even know
        what is about to take place yet, but we are certainly looking forward
        to finding out how it turns out.
        """.upper()
    ))))


main()
