morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def encode_morse_code(message):
    encoded_message = []
    for char in message.upper():
        if char in morse_code_dict:
            encoded_message.append(morse_code_dict[char])
    return ' '.join(encoded_message)

def decode_morse_code(encoded_message):
    decoded_message = []
    encoded_words = encoded_message.split(' / ')
    for word in encoded_words:
        encoded_chars = word.split()
        decoded_chars = []
        for char in encoded_chars:
            for key, value in morse_code_dict.items():
                if value == char:
                    decoded_chars.append(key)
                    break
        decoded_message.append(''.join(decoded_chars))
    return ' '.join(decoded_message)

def main():
    while True:
        print("Morse Code Application")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            message = input("Enter the message to encode: ")
            encoded_message = encode_morse_code(message)
            print("Encoded message:", encoded_message)
            print()
        elif choice == '2':
            encoded_message = input("Enter the message to decode: ")
            decoded_message = decode_morse_code(encoded_message)
            print("Decoded message:", decoded_message)
            print()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == '__main__':
    main()
