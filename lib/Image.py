# !/usr/bin/python  
# -*- coding: utf-8 -*-  

import sys  
import PythonMagick  
  
  
class ManImage:  
    """ 
    Manipulate Image Object 
    """  
    def __init__(self, i_file, o_dire):  
        """ 
        init args 
        :param i_file: (str) input image file (eg: "/home/img.jpg") 
        :param o_dire: (str) output image directory (eg: "/home/") 
        """  
        self.i_file = i_file  
        self.o_dire = o_dire  
  
    def __str__(self):  
        traceback = "Executing under {0.argv[0]} of {1.i_file} into {2.o_dire}......".format(sys, self, self)  
        return traceback  
  
    def playimage(self, rs):  
        """ 
        resize image file 
        :param rs: (int) set rs = 400 ~= 100KB output under my test 
        :return: resized PNG image file 
        """  
        image = PythonMagick.Image(self.i_file)  
        try:  
            image.resize(str(rs))  
            image.monochrome(True)  
            image.magick("PNG")  
            image.write(self.o_dire + self.i_file.split('/')[-1].split('.')[0] + '.png')  
            print('"{0.i_file}" play OK......'.format(self))  
        except Exception, e:  
             print(str(e))  


if __name__ == "__main__":

    import os  
    import sys  
    import class_image  
    
    i_dire = sys.argv[1]  
    o_dire = sys.argv[2]  
    rs = sys.argv[3]  
    
    
    for i_file in os.listdir(i_dire):  
        ManImage(i_file=i_dire + i_file, o_dire=o_dire).playimage(rs=rs)  

    