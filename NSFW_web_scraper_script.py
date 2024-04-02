import os
import requests
from tqdm import tqdm

def download_image(url, output_filename):
  """Downloads an image from the given URL and saves it with the specified filename."""
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for failed requests
    file_size = int(response.headers.get('content-length', 0))  # Get file size if available

    with open(output_filename, 'wb') as f:
      with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc=f"Downloading {url}") as pbar:
        for chunk in response.iter_content(1024):
          f.write(chunk)
          pbar.update(len(chunk))
    print(f"Downloaded image: {url}")
  except requests.exceptions.RequestException as e:
    print(f"Error downloading image: {url} - {e}")

def main():
  """Reads image URLs from a text file, starting from the bottom, and downloads up to 3000 images."""
  image_file_path = input("Enter the path to the image URL file: ")
  download_folder_path = input("Enter the path to the download folder: ")

  # Create download folder if it doesn't exist
  os.makedirs(download_folder_path, exist_ok=True)  # Safe folder creation

  download_count = 0

  try:
    with open(image_file_path, 'r') as f:
      lines = f.readlines()
      lines.reverse()  # Reverse the list to start from the bottom

      for line in lines:
        url = line.strip()  # Remove trailing newline character
        if url:
          output_filename = os.path.join(download_folder_path, f"image_{download_count:04d}.jpg")  # Join paths for filename
          download_image(url, output_filename)
          download_count += 1
          if download_count >= 3000:
            print(f"Downloaded {download_count} images (limit reached)")
            break
  except FileNotFoundError:
    print(f"Error: File not found - {image_file_path}")

if __name__ == "__main__":
  main()
