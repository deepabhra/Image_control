# Image Viewer with Keyboard Controls

This project is a Python-based image viewer that allows users to navigate through images in a folder, zoom in/out, and delete images using keyboard controls. It uses OpenCV for image display and manipulation.

---

## Features

- **Image Navigation**:
  - Press `j` to view the next image.
  - Press `f` to view the previous image.

- **Zooming**:
  - Press `+` or `=` to zoom in.
  - Press `-` or `_` to zoom out.

- **Delete with Confirmation**:
  - Press `d` twice to delete the current image (confirmation required).

- **Exit**:
  - Press `Esc` to exit the viewer.

---

## Requirements

- Python 3.6 or higher
- Libraries:
  - `opencv-python`
  - `os`
  - `glob`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/deepabhra/Image_control.git
   cd image-viewer
   ```

2. Install the required Python libraries:
   ```bash
   pip install opencv-python
   ```

3. Place your images in the `resources` folder (or update the `image_folder` path in the script).

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Use the keyboard controls to navigate, zoom, or delete images.

---

## Keyboard Controls

| Key         | Action                          |
|-------------|---------------------------------|
| `j`         | Next image                     |
| `f`         | Previous image                 |
| `+` or `=`  | Zoom in                        |
| `-` or `_`  | Zoom out                       |
| `d` + `d`   | Delete the current image       |
| `Esc`       | Exit the viewer                |

---

## Folder Structure

```
Image_control/
├── main.py          # Main script
├── resources/       # Folder containing images
└── README.md        # Project documentation
```

---

## How It Works

1. **Image Loading**:
   - The script scans the `resources` folder for supported image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`).
   - Images are displayed one at a time in an OpenCV window.

2. **Keyboard Interaction**:
   - The script listens for key presses using OpenCV's `cv2.waitKey()` function.
   - Based on the key pressed, the script performs actions like navigating, zooming, or deleting images.

3. **Zooming**:
   - The zoom factor is adjusted dynamically, and the image is resized accordingly.

4. **Deletion**:
   - When `d` is pressed twice, the current image is deleted from the folder and removed from the list of images.

5. **Exit**:
   - Pressing `Esc` closes the OpenCV window and exits the program.

---

## Supported Image Formats

The following image formats are supported:
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.gif`

---

## Troubleshooting

1. **No Images Found**:
   - Ensure the `resources` folder contains images with supported formats.
   - Verify the `image_folder` path in the script.

2. **Image Viewer Not Responding**:
   - Ensure you have installed the required libraries using `pip install opencv-python`.
   - Check if your Python version is 3.6 or higher.

3. **Keyboard Controls Not Working**:
   - Ensure the OpenCV window is active when pressing keys.

---

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request.


---

## Author

- **Abhradeep Guin**  
  [GitHub Profile](https://github.com/deepabhra)

---

## Future Enhancements

- Add support for additional image formats.
- Implement a graphical user interface (GUI) for better usability.
- Add functionality to rotate images.
- Allow users to save zoomed or edited images.