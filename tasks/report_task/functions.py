from tools.img import customImg


def get_status(fundo):
    vals = {
        "fundo bacana": {
            "msg": "Olha esse fundo, que bacana!",
            "img": customImg("media\\image.gif"),
            "if_error": "",
        },
        "fundo ruim": {
            "msg": "Olha esse fundo, que ruim.",
            "img": None,
            "if_error": "Era, de fato, ruim",
        }
    }
    return vals[fundo]