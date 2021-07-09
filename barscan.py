"""import os
import tempfile
open("/tmp/hhh.txt","w").write("hellow")
#os.system("/tmp/hhh.txt")
print(input("Scan a barcode right now:"))   """
"""
import time
from escpos.printer import Usb
from escpos.connections import getUSBPrinter
#from escpos.printer import Usb
import sys
import os

from usb.core import find as finddev
import usb
dev = finddev(idVendor=0x0519, idProduct=0x0001)
print(dev)

printer = getUSBPrinter()(idVendor=0x0519, idProduct=0x0001) # Create the printer object with the connection params
printer.cr()
printer.disable()
printer.enable()
printer.horizontalPosition(100)
printer.initialize()
printer.feedPaper()
for i in range(10):

    printer.align('center')
    printer.lineSpacing(0)
    printer.text("                                                   000010"+str(i))
    #printer.underline()
    #printer.lf()
    #time.sleep(1)
printer.initialize()

printer.cutPaper("partial",feed=True)
"""
"""
import os
import tempfile
open("/tmp/hhh.txt","w").write("hellow")
#os.system("/tmp/hhh.txt")
print(input("Scan a barcode right now:"))
f=tempfile.mktemp(".doc")
open(f,"w").write("    hhouw")
os.startfile(f,"print")



"""
"""
import usb.core
import usb.util
import sys
import time
def hid2ascii(lst):
    assert len(lst) == 8, 'Invalid data length (needs 8 bytes)'
    conv_table = {
        0:['', ''],
        4:['a', 'A'],
        5:['b', 'B'],
        6:['c', 'C'],
        7:['d', 'D'],
        8:['e', 'E'],
        9:['f', 'F'],
        10:['g', 'G'],
        11:['h', 'H'],
        12:['i', 'I'],
        13:['j', 'J'],
        14:['k', 'K'],
        15:['l', 'L'],
        16:['m', 'M'],
        17:['n', 'N'],
        18:['o', 'O'],
        19:['p', 'P'],
        20:['q', 'Q'],
        21:['r', 'R'],
        22:['s', 'S'],
        23:['t', 'T'],
        24:['u', 'U'],
        25:['v', 'V'],
        26:['w', 'W'],
        27:['x', 'X'],
        28:['y', 'Y'],
        29:['z', 'Z'],
        30:['1', '!'],
        31:['2', '@'],
        32:['3', '#'],
        33:['4', '$'],
        34:['5', '%'],
        35:['6', '^'],
        36:['7' ,'&'],
        37:['8', '*'],
        38:['9', '('],
        39:['0', ')'],
        40:['\n', '\n'],
        41:['\x1b', '\x1b'],
        42:['\b', '\b'],
        43:['\t', '\t'],
        44:[' ', ' '],
        45:['_', '_'],
        46:['=', '+'],
        47:['[', '{'],
        48:[']', '}'],
        49:['\\', '|'],
        50:['#', '~'],
        51:[';', ':'],
        52:["'", '"'],
        53:['`', '~'],
        54:[',', '<'],
        55:['.', '>'],
        56:['/', '?'],
        100:['\\', '|'],
        103:['=', '='],
        }
    # A 2 in first byte seems to indicate to shift the key. For example
    # a code for ';' but with 2 in first byte really means ':'.
    if lst[0] == 2:
        shift = 1
    else:
        shift = 0
    # The character to convert is in the third byte
    ch = lst[2]
    if ch not in conv_table:
        print("Warning: data not in conversion table")
        return ''
    return conv_table[ch][shift]

def barcode_fetch_usb():
    # Scanner A: Vendor=0xffff and Product=0x0035 | Scanner B: Vendor=0x0483 and Product=0x0011
    dev = usb.core.find(idVendor=0x05e0, idProduct=0x1701)  
    if dev is None:
        raise ValueError('USB device not found')

    # Disconnect it from kernel
    needs_reattach = False
    if dev.is_kernel_driver_active(0):
        needs_reattach = True
        dev.detach_kernel_driver(0)
        print("Detached USB device from kernel driver")

    # set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()
   
    # get an endpoint instance
    cfg = dev.get_active_configuration()
    intf = cfg[(0,0)]
    ep = usb.util.find_descriptor(
        intf,
        # match the first IN endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_IN)
    
    assert ep is not None, "Endpoint for USB device not found. Something is wrong."
    # Loop through a series of 8-byte transactions and convert each to an
    # ASCII character. Print output after 0.5 seconds of no data.
    line = ''
    inicio = time.perf_counter()
    
    while True:
        try:
            # Wait up to 0.5 seconds for data. 500 = 0.5 second timeout.
            data = ep.read(1000, 500)
            
            ch = hid2ascii(data)
            line += ch
            
        except KeyboardInterrupt:
            print("Stopping program")
            dev.reset()
            if needs_reattach:
                dev.attach_kernel_driver(0)
                print("Reattached USB device to kernel driver")
            break
        
        except usb.core.USBError as e:
            # Timed out. End of the data stream. Print the scan line.
            print(e)
            if len(line) > 0:
                print(line)
                f=open("barcode_lido.txt", "w")
                f.write(line)
                f.close()
                line = ''
                return line
            
        except Exception as e:
            print(e)

barcode_fetch_usb()
print("finished barcode")
"""

"""

import time
from escpos.printer import Usb
from escpos.connections import getUSBPrinter
#from escpos.printer import Usb
import sys
import os

from usb.core import find as finddev
import usb
dev = finddev(idVendor=0x0519, idProduct=0x0001)
print(dev)

printer = getUSBPrinter()(idVendor=0x0519, idProduct=0x0001) # Create the printer object with the connection params
printer.cr()
printer.horizontalPosition(0)
printer.initialize()
for i in range(10):

    printer.align('center')
    printer.lineSpacing(0)
    printer.text("                                                   000010"+str(i))
    #printer.underline()
    #printer.lf()
    #time.sleep(1)
printer.initialize()

printer.cutPaper("partial",feed=False)

"""
"""
import StarTSPImage
from PIL import Image, ImageDraw

image = Image.new('RGB', (500, 500), color='White')
draw = ImageDraw.Draw(image)
draw.ellipse((0, 0, 500, 500), fill='Black')

raster = StarTSPImage.imageToRaster(image)

printer = open('/dev/usb/lp0', "wb")
printer.write(raster)
"""






"""
import barcode
barcode.PROVIDED_BARCODES
EAN = barcode.get_barcode_class('ean13')

ean = EAN('5901234123458')

fullname = ean.save('ean13_barcode')

# Example with PNG
from barcode.writer import ImageWriter
ean = EAN('5901234123458', writer=ImageWriter())
fullname = ean.save('ean13_barcode3.jpg')

from io import BytesIO
# Pillow (ImageWriter) produces RAW format here
from barcode import generate
name = generate('EAN13', '5901234123458', output='barcode_svg2')

# with file like object
fp = BytesIO()
generate('EAN13', '5901234123458', writer=ImageWriter(), output=fp)


"""


"""

from escpos import printer


p = printer.Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.text("Hello World!\n")
p.text("Stay at home!\n")
p.image("your_image_file.jpg")
p.cut()


p.ktt();
"""
"""

from escpos.printer import Usb

p = Usb(0x0519,0x0001,0)
#p.image12('ean13_barcode2.png')
#p.barcode66(text="shantanu", textPosition='below', font='b', height=50, width=2, system='CODE93')
p.image('ean13_barcode2.png', impl="graphics")
# Print text
p.print_and_feed()


"""

"""
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF,barcode



barcode_value = "1234567891232"

from escpos.printer import Usb
import tempfile
import barcode,cairo

p = Usb(0x0519, 0x0001)
#p.qr("houssine", size=3,native=False, center=False, impl="bitImageRaster")

#p.barcode("1234567891234", 'EAN13', height=64, width=3, pos="BELOW", font="A", align_ct=True, function_type="A")
#p.barcode("1234567891234", 'EAN13',  64, 3, "BELOW", "A")
barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)

p._image_send_graphics_data(20,20,[2,2,2,2])
p._image_send_graphics_data(barcode_eanbc13, high_density_vertical=False, high_density_horizontal=False, impl="graphics",fragment_height=960, center=False)
#print(p.paper_status())
#print(p.check_barcode( 'EAN13','5901234123458'))
#p.barcode('5901234123458', 'EAN13', function_type="B")
#p.image('barcod33.gif', impl="bitImageRaster", fragment_height=1)
#p.barcode('1324354657687','EAN13', height=64, width=2, pos="BELOW", font="B",
#                align_ct=True, function_type=None, check=True)



#p.barcode("1234567891234", "EAN13", function_type="B")
#p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
#p.cut()
#p.set(align='left', font='a', bold=True, underline=0, width=2,height=1, density=9, invert=False, smooth=False, flip=False,double_width=False, double_height=False, custom_size=False)
#p.set(align='left', font='a', text_type='normal', width=1, height=1, density=9, invert=False, smooth=False,flip=False)
p.text("                                         Nassim         Anis\n")
#p.text("                                          C08           C13\n")
##print(generate_barcode("5901234123458",64,3))
p.print_and_feed()
"""


"""
from escpos.printer import Usb


# Adapt to your needs
p = Usb(0x0519, 0x0001)

# Print software and then hardware barcode with the same content
#p.soft_barcode('code39', '123456',64,3)
#p.soft_barcode('code39', '123456', impl='bitImageColumn',
#                     module_height=5, module_width=0.2, text_distance=1,
#                     center=True)
p.text('\n')
p.text('\n')
#p.barcode('123456', 'CODE39',64,3,2,"a")
p.barcode('123456', 'CODE39',height=64, width=3, pos="BELOW", font="A",align_ct=True, function_type="B", check=True)
p.print_and_feed()
"""
"""

from escpos.connections import getUSBPrinter
from escpos.image import EscposImage
im=EscposImage('ean13_barcode2.png')
printer = getUSBPrinter(commandSet='Generic')(idVendor=0x0519, idProduct=0x0001)
#printer.barcode(text='Shantanu', textPosition='below', font='A', height=100, width=6, system='CODE93')

from escpos import *
from escpos.printer import Usb
Epson = Usb(0x0519,0x0001,0)
Epson.image(im)
#Epson.text("Hello World")
#Epson.barcode('1324354657687','EAN13',64,2,'a','B')


#Epson.print_and_feed()

"""
"""
from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x0519,
                          idProduct=0x0001,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01) # Create the printer object with the connection params

# Print a image
printer.image("barcod33.gif")

printer.text("Hello World")
printer.lf()

printer.align('center')
printer.text('This text is center aligned')

# Print a barcode
printer.barcode(text='Shantanu', textPosition='below', font='b', height=100, width=2, system='CODE93')
printer.lf()

import barcode
from barcode.writer import ImageWriter

bar_class = barcode.get_barcode_class('code128')
barcode = '1234567890'
writer=ImageWriter()
code128 = bar_class(barcode, writer)
code128.save('filename')
"""
"""
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF,barcode

def createBarCodes():

    c = canvas.Canvas("barcodes.pdf", pagesize=letter)

    barcode_value = "1234567891232"
    # draw the eanbc13 code
    barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
    d = Drawing(50, 10)
    d.add(barcode_eanbc13)
    print(type(barcode_eanbc13))
    renderPDF.draw(d, c, 15, 700)



    c.save()

if __name__ == "__main__":
    createBarCodes()
"""





import StarTSPImage

raster = StarTSPImage.imageFileToRaster('ean13_barcode5566666666.png')

from escpos.connections import getUSBPrinter


from escpos.printer import Usb
printer = getUSBPrinter()(idVendor=0x0519,
                          idProduct=0x0001,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01) # Create the printer object with the connection params

# Adapt to your needs
#printer = Usb(0x0519, 0x0001)
#printer.text_img(raster)

printer.text(raster)
#printer.print_and_feed()

"""



import barcode
barcode.PROVIDED_BARCODES
EAN = barcode.get_barcode_class('ean13')



# Example with PNG
from barcode.writer import ImageWriter
ean = EAN('2107091010109', writer=ImageWriter())
fullname = ean.save('ean13_barcode5566666666',options={"module_width":0.35, "module_height":7,"font_size": 10, "text_distance": 2, "quiet_zone": 3,"write_text": True, "center_text":True},text="akkkkkkkkkkkkkkkkkkkkkk \n fbbbbbbbb \n ncccccccccccc\n jddddd")

"""




