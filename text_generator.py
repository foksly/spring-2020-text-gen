from load_save import save_pkl, load_pkl


class TextGenerator():
    def __init__(self):
        raise NotImplementedError()

    def prepare_data(self, data_path=None):
        raise NotImplementedError()

    def build_model(self, data, ngram_size=3, save_path=None):
        raise NotImplementedError()

    def generate(self, length, model=None, saved_model_path=None):
        raise NotImplementedError()
