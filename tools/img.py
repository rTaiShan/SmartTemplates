import base64
import pathlib


def encode_img(path):
    '''
    Gets utf-8 of B64 encoding of file in path
    '''
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode('utf-8')
    return encoded_string


class customImg:
    '''
    Holds src string and html img tag
    '''
    def __init__(self, path) -> None:
        self.path = path
        self.src = f"data:image/{(pathlib.Path(path).suffix)[1::]};base64,{encode_img(path)}"
        self.html_encoded = f"<img src={self.src}>"
