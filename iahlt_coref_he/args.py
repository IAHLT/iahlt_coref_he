import argparse

MODEL_TYPES = ['longformer', 'roberta', 'dictabert']

DEFAULT_LONGFORMER = "allenai/longformer-base-4096"
DEFAULT_DICTA_BERT = "dicta-il/dictabert" #"onlplab/alephbert-base"#
DEFAULT_MODEL = DEFAULT_DICTA_BERT
DEFAULT_STR = MODEL_TYPES[2]

if DEFAULT_MODEL == DEFAULT_DICTA_BERT:
    max_seq_len = 512
elif DEFAULT_MODEL == DEFAULT_LONGFORMER:
    max_seq_len = 3500

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--learning_rate", default=1e-5, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--head_learning_rate", default=3e-4, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--dropout_prob", default=0.3, type=float)
    parser.add_argument("--weight_decay", default=0.01, type=float, help="Weight deay if we apply some.")
    parser.add_argument("--adam_beta1", default=0.9, type=float, help="Epsilon for Adam optimizer.")
    parser.add_argument("--adam_beta2", default=0.98, type=float, help="Epsilon for Adam optimizer.")
    parser.add_argument("--adam_epsilon", default=1e-6, type=float, help="Epsilon for Adam optimizer.")
    parser.add_argument("--train_epochs", default=3.0, type=float, help="Total number of training epochs to perform.")
    parser.add_argument("--ffnn_size", type=int, default=2048)

    parser.add_argument("--logging_steps", type=int, default=500, help="Log every X updates steps.")
    parser.add_argument("--eval_steps", type=int, default=500, help="Eval every X updates steps.")

    parser.add_argument("--device", type=str, default='cpu')

    parser.add_argument("--seed", type=int, default=42, help="random seed for initialization")

    parser.add_argument("--max_span_length", type=int, default=30)
    parser.add_argument("--top_lambda", type=float, default=0.4)

    parser.add_argument("--experiment_name", type=str, default=None)
    parser.add_argument("--cache_dir", type=str, default='cache')

    parser.add_argument("--max_segment_len", type=int, default=512)
    parser.add_argument("--max_tokens_in_batch", type=int, default=5000)

    # parser.add_argument("--conll_path_for_eval", type=str, default=None)

    args = parser.parse_args()
    return args