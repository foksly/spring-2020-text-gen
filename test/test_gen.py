from ..text_generator import TextGenerator


def test_minimal_requirements():
    gen = TextGenerator()

    preprocessed_data = gen.prepare_data('text.txt')
    model = gen.build_model(preprocessed_data)
    assert len(gen.generate(20, model=model)) == 20
