# Author Nick Zaretskyy(koljazaretsky@gmail.com)

import os, sys, getopt
from wand.color import Color

image_extension_to_convert = ['.png', '.jpg', '.jpeg']

if __name__ == "__main__":
    # try:
    #     directory_path = sys.argv[1]
    # except IndexError:
    #     print('Input directory path as the first parameter')
    #     sys.exit()

    directory_path = ''
    extension = ''
    color = ''
    width = 25
    height = 25
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:c:w:h:e:", ["color=", "width=", "height=", "extension="])
    except getopt.GetoptError:
        print('script.py <directory_path> -c <color(for example: blue, red, #787878)>, -w <width(25 by default)>, '
              '-h <height(25 by default)>, -e <image_extension_to_convert>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print('script.py <directory_path> -c <color(for example: blue, red, #787878)>, -w <width(25 by default)>, '
                  '-h <height(25 by default)>')
            sys.exit()
        elif opt in ("-c", "--color"):
            color = arg
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-h", "--height"):
            height = int(arg)
        elif opt in ("-h", "--height"):
            extension = arg
        elif opt == "-d":
            directory_path = arg

    if directory_path == '':
        print('Input directory path as the first parameter(-d <path>)')

    files = os.listdir(directory_path)

    if color == '':
        print('Choose conversion color')
        sys.exit()

    if extension != '':
        image_extension_to_convert = [extension]

    for img_file in files:
        for ext in image_extension_to_convert:
            if img_file.endswith(ext):
                full_img_path = directory_path+img_file
                os.system("python script.py -i {0} -c {1} -w {2} -h {3}".format(full_img_path, color, width, height))