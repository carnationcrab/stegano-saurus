import cv2

# convert the text into unicode
def convert_message(message):
    for c in message:
        yield(ord(c))


# convert image into numpy array
def get_image(image):
  img = cv2.imread(image)
  return img

# uses the greatest common denominator to determine which pixels to grab
def gcd(x, y):
  while(y):
    x, y = y, x % y

  return x


def encode(image, message):
    img = get_image(image)
    msg = convert_message(message)
    pattern = gcd(len(img), len(img[0]))

    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i + 1 * j + 1) % pattern == 0:
                try:
                    img[i - 1][j - 1][0] = next(msg)
                except StopIteration:
                    img[i - 1][j - 1][0] = 0
                    return img


def decode(image):
  img = get_image(image)
  pattern = gcd(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          return message


def run_program(program):
    exec(open(program).read())


def main():
    IMG = 'shot.png'

    FILE = 'hello_world.py'
    text_file = open(FILE, 'r')
    text = text_file.read()
    MSG = str(text)

    text_file.close()

    encoded = encode(IMG, MSG)
    cv2.imwrite("EncodedImage.png", encoded)

    decoded = str(decode('EncodedImage.png'))

    decoded_file = open('decoded.py', 'w+')
    decoded_file.write(decoded)
    decoded_file.close()

    run_program('decoded.py')


main()
