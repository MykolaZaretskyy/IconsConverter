from __future__ import print_function
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import os, sys, getopt
from os.path import isfile, join

root = 'MagickIcons'
androin_folder = 'MagickIcons/Android'
ios_folder = 'MagickIcons/iOS/'
mdpi_android_folder = 'MagickIcons/Android/drawable-mdpi/'
hdpi_android_folder = 'MagickIcons/Android/drawable-hdpi/'
xhdpi_android_folder = 'MagickIcons/Android/drawable-xhdpi/'
xxhdpi_android_folder = 'MagickIcons/Android/drawable-xxhdpi/'
xxxhdpi_android_folder = 'MagickIcons/Android/drawable-xxxhdpi/'

dimension_scales = {
    mdpi_android_folder: 1,
    hdpi_android_folder: 1.5,
    xhdpi_android_folder: 2,
    xxhdpi_android_folder: 3,
    xxxhdpi_android_folder: 4
}

folders_paths = {root, androin_folder, ios_folder, mdpi_android_folder, hdpi_android_folder, xhdpi_android_folder,
                 xxhdpi_android_folder, xxxhdpi_android_folder}


def convert_image(image_to_convert_path, destination_path, color, width, height, scale):
    with Image(filename=image_to_convert_path) as icon_to_convert:
        with Drawing() as draw:
            with icon_to_convert.clone() as clone:
                draw.fill_color = color
                draw.color(0, 0, 'reset')
                draw.draw(clone)
                icon_to_convert.composite_channel('default_channels', clone, 'atop')

                with Image(width=120, height=120) as output_image:
                    if icon_to_convert.height >= icon_to_convert.width:
                        scale_factor = output_image.height / float(icon_to_convert.height)
                    else:
                        scale_factor = output_image.width / float(icon_to_convert.width)

                    with icon_to_convert.clone() as badge:
                        scaled_width = int(scale_factor * icon_to_convert.width)
                        scaled_height = int(scale_factor * icon_to_convert.height)
                        badge.resize(width=scaled_width, height=scaled_height)

                        output_image.composite(badge, left=(output_image.width - badge.width) / 2,
                                               top=(output_image.height - badge.height) / 2)

                        output_image.resize(width=int(width*scale), height=int(height*scale))
                        output_image.save(filename=destination_path)


def create_files_structure():
    for path in folders_paths:
        if not os.path.exists(path):
            os.makedirs(path)

if __name__ == "__main__":
    image_to_convert = ''
    color = ''
    width = 25
    height = 25
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:a:c:w:hh:d", ["iconvert=", "all", "color=", "width=", "height=", "directory="])
    except getopt.GetoptError:
        print('script.py -i <image_to_convert> -c <color(for example: blue, red, #787878)>, -w <width(25 by default)>, '
              '--height <height(25 by default)>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -i <image_to_convert> -c <color(for example: blue, red, #787878)>, -w <width(25 by default)>, '
                  '--height <height(25 by default)>')
            sys.exit()
        elif opt in ("-i", "--iconvert"):
            image_to_convert = arg
        elif opt in ("-c", "--color"):
            color = Color(arg)
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-hh", "--height"):
            height = int(arg)
        elif opt in ("-a", "--all"):
            convert_all = True
        elif opt in ("-d", "--directory"):
            directory = arg

    if image_to_convert == '':
        print('Choose image to convert')
        sys.exit()
    elif color == '':
        print('Choose destination color')
        sys.exit()

    create_files_structure()
    for path, scale in dimension_scales.items():
        convert_image(image_to_convert, path + image_to_convert, color, width, height, scale)
        if scale == 1 or scale == 2 or scale == 3:
            img_name = image_to_convert.split('.')[0]
            img_extension = image_to_convert.split('.')[1]
            convert_image(image_to_convert, ios_folder + "{0}@{1}.{2}".format(img_name, scale, img_extension),
                          color, width, height, scale)