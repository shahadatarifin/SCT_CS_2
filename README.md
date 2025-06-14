# Simple Image Encryption Tool

## Task Objective
The objective of this project is to create a simple yet effective image encryption and decryption tool. The program applies various reversible transformations on an input image to encrypt it, and then reverses those operations to decrypt and restore the original image.

## Approach
The tool processes images as NumPy arrays and applies a sequence of transformations such as:
- Swapping RGB color channels to BGR
- Applying bitwise XOR with a key to each pixel
- Shuffling rows randomly with a fixed seed for reversibility

These transformations are chained together to produce an encrypted image. Decryption applies the inverse operations in reverse order to recover the original image.

## Tools Used
- **Python**: The main programming language
- **Pillow (PIL)**: For loading and saving images
- **NumPy**: For efficient image array manipulation
- **argparse**: For command-line argument parsing

## What I Learned
- How to manipulate images at the pixel level using NumPy arrays.
- Implementing simple reversible encryption operations on images.
- Using fixed random seeds to enable reversible random shuffling.
- Working with command-line arguments to create flexible scripts.
- Understanding how simple cryptographic concepts like XOR can be applied to image data.

---

## Usage

To encrypt an image:
```bash
python your_script.py --input path/to/input_image.png --output path/to/encrypted_image.png --mode encrypt

