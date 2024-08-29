from ufal.udpipe import Model, Pipeline, ProcessingError
from conllu import parse

import sys


NO_PARSER_PIPELINE = {'tagger': Pipeline.DEFAULT, 'parser': Pipeline.NONE}


def extract_tokens(data):
    # multi-words are not having an int id.
    tokens = [entry['form'].strip() for entry in data if isinstance(entry['id'], int)]
    return tokens


class Tokenizer:
    def __init__(self, model_path) -> None:
        self.model = Model.load(model_path)

    def tokenize(self, text):
        tokens = []
        result = self._tokenize(text)
        for sub_result in result:
            tokens += extract_tokens(sub_result) 
        return tokens
    
    def _tokenize(self, text: str, pipeline_spec: dict=NO_PARSER_PIPELINE):
        tagger, parser = pipeline_spec['tagger'], pipeline_spec['parser']
        pipeline = Pipeline(self.model, 'tokenize', tagger, parser, 'conllu')
        error = ProcessingError()

        processed = pipeline.process(text, error)
        if error.occurred():
            sys.stderr.write("An error occurred when running run_udpipe: ")
            sys.stderr.write(error.message)
            sys.stderr.write("\n")
            sys.exit(1)
        return parse(processed)
    


if __name__ == '__main__':
    t = Tokenizer('models/model_3_6_24_he.udpipe')
    t.tokenize('שלום כולם. מה נשמע איתכם? הכל בסדר?')
    pass