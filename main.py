from ascii_qr import qrcode_gen

# Usage example, generate a QR code for a YouTube URL
text = "https://www.youtube.com"
filename = "youtube_qr.txt"

qrcode_gen.generate_qr_ascii(text, filename)