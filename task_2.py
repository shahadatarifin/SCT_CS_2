from PIL import Image
import numpy as np
import argparse

def load_image(image_path):
    """Load an image into a NumPy array."""
    img = Image.open(image_path)
    return np.array(img)

def save_image(pixels, output_path):
    """Save a NumPy array as an image."""
    img = Image.fromarray(pixels)
    img.save(output_path)

def swap_channels(pixels):
    """Swap RGB channels (BGR instead of RGB)."""
    if len(pixels.shape) == 3:  # Only for color images
        return pixels[:, :, [2, 1, 0]]  # BGR instead of RGB
    return pixels

def apply_xor(pixels, key=123):
    """Apply XOR operation on each pixel with a key."""
    return np.bitwise_xor(pixels, key)

def apply_addition(pixels, value=50):
    """Add a value to each pixel (with modulo 256 to prevent overflow)."""
    return (pixels + value) % 256

def shuffle_rows(pixels, seed=None):
    """Randomly shuffle rows (reversible if seed is fixed)."""
    if seed is not None:
        np.random.seed(seed)
    np.random.shuffle(pixels)
    return pixels

def shuffle_columns(pixels, seed=None):
    """Randomly shuffle columns (reversible if seed is fixed)."""
    if seed is not None:
        np.random.seed(seed)
    return np.random.permutation(pixels.T).T

def encrypt_image(image_path, output_path, operations):
    """Apply encryption operations on an image."""
    pixels = load_image(image_path)
    
    for op in operations:
        if op['name'] == 'swap':
            pixels = swap_channels(pixels)
        elif op['name'] == 'xor':
            pixels = apply_xor(pixels, op.get('key', 123))
        elif op['name'] == 'add':
            pixels = apply_addition(pixels, op.get('value', 50))
        elif op['name'] == 'shuffle_rows':
            pixels = shuffle_rows(pixels, op.get('seed', None))
        elif op['name'] == 'shuffle_cols':
            pixels = shuffle_columns(pixels, op.get('seed', None))
    
    save_image(pixels, output_path)
    print(f"Encrypted image saved to: {output_path}")

def decrypt_image(image_path, output_path, operations):
    """Reverse encryption operations to recover the original image."""
    pixels = load_image(image_path)
    
    # Reverse operations in reverse order
    for op in reversed(operations):
        if op['name'] == 'swap':
            pixels = swap_channels(pixels)  # Swap again to reverse
        elif op['name'] == 'xor':
            pixels = apply_xor(pixels, op.get('key', 123))  # XOR is reversible
        elif op['name'] == 'add':
            pixels = apply_addition(pixels, -op.get('value', 50))  # Subtract to reverse
        elif op['name'] == 'shuffle_rows':
            pixels = shuffle_rows(pixels, op.get('seed', None))  # Same shuffle
        elif op['name'] == 'shuffle_cols':
            pixels = shuffle_columns(pixels, op.get('seed', None))
    
    save_image(pixels, output_path)
    print(f"Decrypted image saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output", required=True, help="Output image path")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, help="Encrypt or Decrypt")
    args = parser.parse_args()

    # Define encryption operations (must match for decryption)
    operations = [
        {'name': 'swap'},
        {'name': 'xor', 'key': 42},
        {'name': 'shuffle_rows', 'seed': 1234}
    ]

    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, operations)
    else:
        decrypt_image(args.input, args.output, operations)

if __name__ == "__main__":
    main()
