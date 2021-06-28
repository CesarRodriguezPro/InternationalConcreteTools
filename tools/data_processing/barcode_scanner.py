from pylibdmtx.pylibdmtx import decode
from PIL import Image
import os


def get_barcode_info(picture_obj):


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    picture_path = BASE_DIR + os.path.normpath(picture_obj.image.url)
    result = decode(Image.open(picture_path))

    try:
        decode_data = str(result[0].data.decode('UTF-8'))
        return decode_data, picture_path

    except IndexError:
        return None, None
