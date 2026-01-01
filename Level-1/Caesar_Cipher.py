print("🔐 Caesar Cipher")

choice = input("Type 'E' to Encode or 'D' to Decode: ").upper()
message = input("Enter your message: ")
shift = int(input("Enter shift number: "))

result = ""

for char in message:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')

        if choice == "E":
            new_char = chr((ord(char) - start + shift) % 26 + start)
        elif choice == "D":
            new_char = chr((ord(char) - start - shift) % 26 + start)
        else:
            print("Invalid choice")
            break

        result += new_char
    else:
        result += char   # keeps space and symbols

print("Result:", result)
