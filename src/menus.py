from src import process


def main():
    choice = int(input('Hello! \n'
                       'This is a simple steganography app. \n'
                       'Please click below and type your choice: \n'
                       '    1. ENCODE a python program into an image\n'
                       '    2. DECODE a python program from an image\n'
                       '    3. ...I am confused. \n'))

    if choice == 1:
        pattern = int(input('What pattern? '))
        image = input('What image? Include file extension. ')
        message = input('What program would you like to encode? Include file extension. ')
        name = input('What would you like to call your encoded image? No need to add the file extension. ')

        encoded = process.encode(image, message, pattern)
        process.save_img(encoded, name)

    elif choice == 2:
        image = input('What image would you like to decode? Include file extension.')
        pattern = int(input('What pattern was this image encoded with? '))
        name = input('What should we call the file when done processing? (no need to add the file extension. ')
        run = int(input(('Would you like to run this code after decoding it, or simply rebuild the file? \n'
                         '    1. Yes (Please only do this with images you trust. '
                         'No precautions are taken to prevent malicious code from running. \n'
                         '    2. No \n')))

        extended_name = name + '.py'
        if run == 1:
            decoded = process.decode(image, pattern)
            process.save_file(decoded, extended_name)
            process.run_program(extended_name)
        if run == 2:
            decoded = process.decode(image, pattern)

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
        raise Exception("Please select an available option.")


main()