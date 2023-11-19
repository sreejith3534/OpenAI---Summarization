import streamlit as st
from main import get_summary_from_lex_rank, gpt_model_text


def prepare_ui():
    st.title("Text Summarization")
    get_text = st.text_area("Input Text")
    if get_text:
        st.write("Input text: ")
        st.text("")
        st.markdown(get_text)
        lex_summary_text, luhn_summary_text = get_summary_from_lex_rank(str(get_text))
        complete_str_lex = ""
        complete_str_luhn = ""
        for details in lex_summary_text:
            complete_str_lex += str(details)
            complete_str_luhn += "\n"
        for details in luhn_summary_text:
            complete_str_luhn += str(details)
            complete_str_luhn += "\n"
        gpt_text = gpt_model_text(str(get_text))
        st.text("")
        st.write("Summary text Lex Rank:")
        st.text("")
        st.markdown(complete_str_lex)
        st.write("Summary text Luhn Rank:")
        st.text("")
        st.markdown(complete_str_luhn)
        st.write("Summary text GPT:")
        st.text("")
        st.markdown(gpt_text)


if __name__ == "__main__":
    try:
        st.set_page_config(layout="wide")
        prepare_ui()
    except Exception as e:
        st.write("issue identified as :", e)