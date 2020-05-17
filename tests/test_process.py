import cv2
from src import process


def test_encode():
    # arrange
    img = 'testoriginal.png'
    FILE = 'testhello_world.py'
    actual = str(process.encode(img, FILE, 5))
    expected = str(cv2.imread('testencoded.png'))
    print('ACTUAL = ', actual)
    print('EXPECTED = ', expected)

    # assert
    assert actual == expected


def test_decode():
    # arrange
    img = 'testencoded.png'
    text_file = open('testhello_world.py', 'r')
    text = text_file.read()
    expected = str(text)

    actual = str(process.decode(img, 5))

    print('ACTUAL|', actual)
    print('EXPECTED|', expected)

    # assert
    assert actual == expected
