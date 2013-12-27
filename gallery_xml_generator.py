from glob import glob
import os
from os import rename


class Picture:
    __name=""
    __tech=""
    __dim=""
    __year=""
    __filename=""
    
    def __init__(self, filename):
        self.__filename = filename
        
        # remove extension
        filename = filename[:-4]
        
        tokens = filename.split("_")
        self.__name = tokens[0]
        self.__tech = tokens[1]
        self.__dim = tokens[2]
        self.__year = tokens[3]
        
    def big_pic_str(self):
        big_str = "<photo image=\"images/big/%s\">\n" % (self.__filename)
        big_str += "<![CDATA[<head>%s</head><br><body>%s, %s, %s</body>]]></photo>\n" % (self.__name, self.__dim, self.__tech, self.__year)
        return big_str
    
    def thumbs_pic_str(self):
        thumbs_str = "<photo image=\"images/thumbs/%s\">\n" % (self.__filename)
        thumbs_str += "<![CDATA[<head>%s</head><br><body>%s, %s, %s</body>]]></photo>\n" % (self.__name, self.__dim, self.__tech, self.__year)
        return thumbs_str
        
    def __str__(self):
        return "[Picture name:%s tech:%s dim:%s, year:%s]" % (self.__name, self.__tech, self.__dim, self.__year)

def rename_jpegs():
    for filename in glob('*.JPG'):
        new_filename = filename[:-4]
        rename(filename, new_filename)
        rename(new_filename, new_filename + ".jpg")
        
def build_filenames():
    filenames = []
    for filename in glob('*.jpg'):
        filenames.append(filename)
    return filenames
        
def build_pictures(filenames):
    pictures = []
    for file in filenames:
        picture = Picture(file)
        pictures.append(picture)
    
    return pictures

def generate_big_xml(file, pictures):
    f = open(file, "w")
    f.write("<images>\n")
    for pic in pictures:
        f.write(pic.big_pic_str())
    f.write("</images>\n")
    f.close()

def generate_thumbs_xml(file, pictures):
    f = open(file, "w")
    f.write("<images>\n")
    for pic in pictures:
        f.write(pic.thumbs_pic_str())
    f.write("</images>\n")
    f.close()
    
    
PATH="C:\\Users\\iulia\\Pictures\\galerie_maria"
BIG_FILE="big2.xml"
THUMBS_FILE="thumbs2.xml"

os.chdir(PATH)

rename_jpegs()

filenames = build_filenames()
pictures = build_pictures(filenames)

generate_big_xml(BIG_FILE, pictures)
generate_thumbs_xml(THUMBS_FILE, pictures)


