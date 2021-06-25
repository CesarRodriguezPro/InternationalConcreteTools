import cv2
from pylibdmtx.pylibdmtx import decode
from ..models import Tool


def get_barcode_info(stream_pic):
    try:
        name_of = data[0][0].decode('UTF-8')
        return name_of
    except IndexError:
        return None
