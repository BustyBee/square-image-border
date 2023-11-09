# square-image-border

This script will add a white square border arround your images. It lets you choose the size of the frame in pixels.

- This script relies on Pillow to work. Install it with `pip install Pillow`

1. Create an `input` and an `output` folder in the same directory as the index.py file.

2. Place the images you would like to add borders to in the `input` folder.

3. Open `index.py` with a code- or texteditor and change `border_size`* and `imgquality`** to your desired values. (*size of the border in pixels, **quality from 1 to 100, 100 is best quality and biggest filesize).

    Example (recommended):
    ```python
    border_size = 300
    imgquality = 95
    ```

4. Run `index.py`

5. Images will be output in the `output` folder in the same directory.