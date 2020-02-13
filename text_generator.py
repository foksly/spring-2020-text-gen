from load_save import save_pkl, load_pkl


class TextGenerator():
    def __init__():
        raise NotImplementedError()

    def prepare_data(self, data_path=None):
        raise NotImplementedError()

    def build_model(data, ngram_size=3, save_path=None):
        raise NotImplementedError()

    def generate(length, model=None, saved_model_path=None):
        raise NotImplementedError()
