import cv2
import os
import glob

# === Config ===
image_folder = r"E:\\college\\Sem_VI\\Project\\Image_control\\resources"  # Put your images in this folder
zoom_step = 0.001
min_zoom = 0.1
max_zoom = 5.0

# === Init ===
image_paths = glob.glob(os.path.join(image_folder, '*.*'))
supported_ext = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
image_paths = [p for p in image_paths if os.path.splitext(p)[1].lower() in supported_ext]

if not image_paths:
    print("⚠️ No images found in the folder.")
    exit()

index = 0
zoom_factor = 0.1

def display_image(img_path, zoom):
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ Failed to load: {img_path}")
        return
    h, w = img.shape[:2]
    resized = cv2.resize(img, (int(w * zoom), int(h * zoom)))
    cv2.imshow("Image Viewer", resized)

while True:
    current_image_path = image_paths[index]
    display_image(current_image_path, zoom_factor)

    key = cv2.waitKey(0)

    # === Navigation ===
    if key == ord('j'):
        index = (index + 1) % len(image_paths)
        zoom_factor = 0.1
        print("➡️ Next image")
    elif key == ord('f'):
        index = (index - 1) % len(image_paths)
        zoom_factor = 0.1
        print("⬅️ Previous image")

    # === Zooming ===
    elif key == ord('+') or key == ord('='):
        zoom_factor = min(max_zoom, zoom_factor + zoom_step)
        print(f"🔍 Zooming in: {zoom_factor:.3f}")
    elif key == ord('-') or key == ord('_'):
        zoom_factor = max(min_zoom, zoom_factor - zoom_step)
        print(f"🔍 Zooming out: {zoom_factor:.3f}")

    # === Delete ===
    elif key == ord('d'):
        print("❓ Press 'd' again to confirm deletion.")
        key = cv2.waitKey(2000)  # Wait for up to 2 seconds for the second 'd'
        if key == ord('d'):
            print(f"🗑️ Deleted current file: {current_image_path}")
            os.remove(current_image_path)
            del image_paths[index]
            if not image_paths:
                print("🧼 All images deleted. Exiting.")
                break
            index = index % len(image_paths)
            zoom_factor = 0.1
        else:
            print("❌ Deletion canceled.")

    # === Exit ===
    elif key == 27:  # Esc key
        print("👋 Exiting.")
        break

cv2.destroyAllWindows()
