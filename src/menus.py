from src import process

def main():
    choice = int(input('Hello! \n'
                       'This is a simple steganography app. \n'
                       'Please click below and type your choice: \n'
                       '    1. Encode a python program into an image\n'
                       '    2. SAFE MODE: Decode a python program from an image\n'
                       '    3. I am confused. \n'))

    if choice == 1:
        pattern = input('What pattern? ')
        image = input('What image? ')
        program = input('What program would you like to encode? ')
        process.encode(image, program, pattern)
    elif choice == 2:
        image = input('What image would you like to decode? (include the file extension, like this: file.py) ')
        pattern = input('What pattern was this image encoded with? ')
        run = input(('Would you like to run this code after decoding it, or simply rebuild the file? \n'
                     '    1. Yes (Please only do this with images you trust. '
                     'No precautions are taken to prevent malicious code from running \n'
                     '    2. No \n'))
        decoded = process.decode(image)
    elif choice == 3:
        print('Hey, we get it! This can be confusing. \n'
              'STEGANOGRAPHY is the process by which one hides a secret file or message within another file. \n'
              ' \n'
              'This app uses steganography to hide a python program within an image. \n'
              ' \n'
              '* OPTIONS * \n'
              ' \n'
              '    You can choose to ENCODE an image with a program, or DECODE an program from an image. \n'
              'If you choose to DECODE, you can decide whether or not you want to run the program. \n'
              'Please only choose to run embedded programs from trusted sources. We do not currently have any \n '
              'safety precautions in place to protect you if you choose to run a damaging program. \n'
              ' \n'
              ' \n'
              '* WHAT IS THE PATTERN FOR? * \n'
              ' \n'
              'For both ENCODING and DECODING, you need a PATTERN. The pattern is used to determine the spacing \n '
              'between encoded pixels. For example, if, during ENCODING, you choose 7, every seventh pixel will be \n '
              'encoded with a character from your python program. \n'
              'During DECODING, you need to supply the decoder with the correct pattern with which the file was \n '
              'originally encoded. \n')
    else:
        raise Exception("Enter correct input")


main()