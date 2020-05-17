# Stegano-saurus: A Steganography Project
### Sam Martorana — Fundamentals of Software Dev. Python — SEIS 603-01

A simple python app that allows a user to encode a secret python program in a photo as well as decode and run a secret python program that has already been encoded.

## Summary
STEGANOGRAPHY is the process by which one hides a secret file or message within another file. This app uses steganograp2hy to hide a python program within an image.

### Options
You can choose to ENCODE an image with a program, or DECODE an program from an image. If you choose to DECODE, you can decide whether or not you want to run the program.

Please only choose to run embedded programs from trusted sources. We do not currently have any safety precautions in place to protect you if you choose to run a damaging program. 

### Pattern
For both ENCODING and DECODING, you need a PATTERN. The pattern is used to determine the spacing between encoded pixels. For example, if, during ENCODING, you choose 7, every seventh pixel will be encoded with a character from your python program. During DECODING, you need to supply the decoder with the correct pattern with which the file was 
originally encoded.

## Running the Project

### Dependencies
```pip3 install opencv-python numpy```

## Running the tests

``` python -m pytest```


## Sources

[*Let's Hide a Secret Message in an Image with Python and Opencv*](https://dev.to/erikwhiting88/let-s-hide-a-secret-message-in-an-image-with-python-and-opencv-1jf5) (Erik Whiting)

[*How To Hide Data in Images Using Python*](https://medium.com/better-programming/image-steganography-using-python-2250896e48b9) (Ashwin Goel)

[Pytest Documentation](https://docs.pytest.org/en/latest/)