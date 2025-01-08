import streamlit as st


class VerbTest:
    def __init__(self, verbs):

        # Streamlit app layout
        st.title("Test Your Knowledge")

        # Create input fields for each pronoun
        for pronoun, (answer, sentence, translation) in verbs.items():
            st.write(translation)  # Show English translation

            user_answer = st.text_input(sentence, key=pronoun, autocomplete="off")
            if user_answer:
                if user_answer.strip().lower() == answer.lower():
                    st.success(f"Correct! The answer is '{answer}'.")
                else:
                    st.error(f"Incorrect! The correct answer is '{answer}'.")
