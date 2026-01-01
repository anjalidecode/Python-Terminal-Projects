morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

reverse_morse = {v: k for k, v in morse_code.items()}

print("🆘 Morse Code Translator")
choice = input("Type 'T' for Text to Morse or 'M' for Morse to Text: ").upper()

if choice == "T":
    text = input("Enter text: ").upper()
    result = ""

    for char in text:
        if char == " ":
            result += "/ "
        else:
            result += morse_code.get(char, "") + " "

    print("Morse Code:", result)

elif choice == "M":
    morse = input("Enter Morse Code (use / for space): ")
    words = morse.split(" / ")
    result = ""

    for word in words:
        letters = word.split()
        for letter in letters:
            result += reverse_morse.get(letter, "")
        result += " "

    print("Text:", result.strip())

else:
    print("Invalid choice")
