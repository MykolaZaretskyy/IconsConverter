# IconsConverter

Scripts for images conversion to all Android and iOS resolutions.

## script.py

This script converts a single specified image into all existing Android and iOS resolutions, creates folders structure in current folder and inserts converted image into corresponding folders.

Command-line arguments:
- "-i", "--icon" - an image to convert(required argument);
- "-c", "--color" - color to convert to(required argument);
- "-w", "--width" - resizing image's width(set to 25 by default);
- "-h", "--height" - resizing image's width(set to 25 by default);

Example:
python script.py -i /Users/Nickolay/image_to_convert.png -c #787878 -w 30 -h 30

Folders with images created:
- MagickIcons
  - Android
    - drawable-mdpi
      * image_to_convert.png
    - drawable-hdpi
      * image_to_convert.png
    - drawable-xhdpi
      * image_to_convert.png
    - drawable-xxhdpi
      * image_to_convert.png
    - drawable-xxxhdpi
      * image_to_convert.png
  - iOS
    * image_to_convert.png
    * image_to_convert@2x.png
    * image_to_convert@3x.png

## convert_all_images_in_directory.py

This script converts all images in specified folder by image extension using scripts.py. By default image extensions list contains: .png, .jpeg, .jpg , however, it could be specified as a command-line argument.

Command-line arguments:
- "-d" - directory to convert images from(required argument)
- "-c", "--color" - color to convert to(required argument);
- "-e", "--extension" - filter images to coverts by extension(images extension to coverts by default: .png, .jpeg, .jpg)
- "-w", "--width" - resizing image's width(set to 25 by default);
- "-h", "--height" - resizing image's width(set to 25 by default);


