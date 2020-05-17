import cv2


# generator to convert the text into unicode
def convert_message(message):
    for c in message:
        yield ord(c)


# convert image into numpy array
def convert_image(image):
    img = cv2.imread(image)
    return img


def encode(image, message, pattern):
    text_file = open(message, 'r')
    text = text_file.read()
    string_message = str(text)

    img = convert_image(image)
    msg = convert_message(string_message)

    for width in range(len(img)):
        for height in range(len(img[0])):
            if (width + 1 * height +1) % pattern == 0:
                try:
                    img[width - 1][height - 1][0] = next(msg)
                except StopIteration:
                    img[width - 1][height - 1][0] = 0
                    return img


def decode(image, pattern):
    img = convert_image(image)
    message = ''
    for width in range(len(img)):
        for height in range(len(img[0])):
            if (width - 1 * height - 1) % pattern == 0:
                if img[width - 1][width - 1][0] != 0:
                    message = message + chr(img[width - 1][width - 1][0])
                else:
                    return str(message)


def save_img(image, name):
    name = name + '.png'
    cv2.imwrite(name, image)


def save_file(program, name):
    decoded_file = open(name, 'w+')
    decoded_file.write(program)
    decoded_file.close()


def run_program(program):
    exec(open(program).read())