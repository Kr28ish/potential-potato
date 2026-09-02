import cv2
import easyocr

# 1. Load the original image
image = cv2.imread(r"C:\Users\krish\OneDrive\Desktop\New folder\0063e41b53567829.jpg")

# 2. YOLO detection
x = 242
y = 210
width = 62
height = 18
confidence = 0.794

# 3. Convert YOLO center coordinates to corners
x1 = int(x - width / 2)
y1 = int(y - height / 2)
x2 = int(x + width / 2)
y2 = int(y + height / 2)

print("Plate box:", x1, y1, x2, y2)

# 4. Crop the number plate
plate = image[y1:y2, x1:x2]

# 5. Enlarge the tiny plate
plate = cv2.resize(
    plate,
    None,
    fx=5,
    fy=5,
    interpolation=cv2.INTER_CUBIC
)

# 6. Convert to grayscale
gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

# 7. OCR
reader = easyocr.Reader(['en'])

results = reader.readtext(gray)

# 8. Print detected number
for result in results:
    text = result[1]
    ocr_confidence = result[2]

    print("Plate Number:", text)
    print("OCR Confidence:", ocr_confidence)

# 9. Save crop for checking
cv2.imwrite(r"C:\Users\krish\OneDrive\Desktop\New folder\plate_crop.png", gray)