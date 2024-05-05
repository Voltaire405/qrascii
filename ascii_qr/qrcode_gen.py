import qrcode
from PIL import Image

def generate_qr_ascii(text_to_encode, filename):
  # Generate QR code
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data(text_to_encode)
  qr.make(fit=True)

  img = qr.make_image(fill='black', back_color='white')

  scale_factor = 10 # 1, 10 for size variety
  img_width, img_height = img.size

  # Convert QR code image to ASCII
  ascii_art = ""
  for x in range(0, img_width, scale_factor ):
    for y in range(0, img_height, scale_factor):
      if img.getpixel((y, x)) == 0:
        ascii_art += "██"
      else:
        ascii_art += "  "
    ascii_art += "\n"

  # Write ASCII art to file
  with open(f"./outputs/{filename}", 'w') as file:
    file.write(ascii_art)