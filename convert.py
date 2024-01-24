from PIL import Image
import os

def convert_to_webp(input_path, output_path, quality=80):
    try:
        with Image.open(input_path) as img:
            # Automatically append ".webp" to the output file path
            if not output_path.lower().endswith(".webp"):
                output_path += ".webp"
            
            img.save(output_path, 'WEBP', quality=quality)
        print(f"Conversion successful! Image saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    input_image_path = input("Enter the path of the input image: ")

    if not os.path.isfile(input_image_path):
        print("Error: Invalid file path.")
        return

    output_image_path = input("Enter the path for the output WebP image (without extension): ")

    quality = int(input("Enter the compression quality (0-100): "))
    quality = max(0, min(quality, 100))  # Ensure quality is between 0 and 100

    convert_to_webp(input_image_path, output_image_path, quality)

if __name__ == "__main__":
    main()
