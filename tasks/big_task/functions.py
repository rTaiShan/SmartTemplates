from tools.img import customImg


def get_title_str(start_date):
    return f"Dia D-{start_date}"

def get_imgs(img_paths):
    imgs = []
    for path in img_paths:
        imgs.append(customImg(path))
    return imgs

def get_observacao(codigo):
    observacoes = {
        "2": "<b>Forte!</b>",
        "1": "Codigo inicial",
        "0": "Codigo vazio",
    }
    return observacoes.get(codigo)