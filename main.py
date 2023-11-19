import openai
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

openai.api_type = ""
openai.api_base = ""
openai.api_version = ""
openai.api_key = ""


def get_summary_from_lex_rank(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    luhn_summarizer = LuhnSummarizer()
    lex_summary = lex_summarizer(parser.document, 1)
    luhn_summary = luhn_summarizer(parser.document, 1)
    return lex_summary, luhn_summary


def gpt_model_text(text):
    text_modified = str(text) + """\n\nTl;dr"""
    response = openai.Completion.create(
        engine="OpenAI-DaVinci-text-003",
        prompt=text_modified,
        temperature=1,
        max_tokens=1000,
    )
    gpt_output_text = response.to_dict()["choices"][0].to_dict()["text"]
    return gpt_output_text

