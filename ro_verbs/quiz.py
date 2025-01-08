import streamlit as st
import pandas as pd


EDITING = "editing"


class VerbQuiz:
    def __init__(self, verbs):
        self.verbs = verbs
        audio_html = f"""
<style>
.stAudio {{
    height: 30px;
}}
</style>
"""
        st.markdown(audio_html, unsafe_allow_html=True)

        # Loop through the pronouns to create inputs
        for person, forms in verbs.items():
            col1, col2 = st.columns(2)

            with col1:
                num = "singular"
                key = f"{num}_{person}"
                with st.form(key):
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        singular_answer = st.text_input(
                            f"{person} Singular", key=key+"_input", autocomplete="off")
                    with col_b:
                        submitted = st.form_submit_button("Check")
                    if submitted:
                        if singular_answer:
                            correct_singular = forms["Singular"]["answer"]
                            if singular_answer.strip().lower() == correct_singular.lower():
                                st.success("✅ Correct")
                            else:
                                st.error(
                                    f"❌ Incorrect (Correct: {correct_singular})")
                        if forms["Singular"]["audio"]:
                            st.audio(forms["Singular"]["audio"])

            with col2:
                num = "plural"
                key = f"{num}_{person}"
                with st.form(key):
                    col_a, col_b = st.columns([3, 1])
                    with col_a:
                        plural_answer = st.text_input(
                            f"{person} Plural", key=key+"_input", autocomplete="off")
                    with col_b:
                        submitted = st.form_submit_button("Check")
                    if submitted:
                        correct_plural = forms["Plural"]["answer"]
                        if plural_answer.strip().lower() == correct_plural.lower():
                            st.success("✅ Correct")
                        else:
                            st.error(
                                f"❌ Incorrect (Correct: {correct_plural})")

                # Play audio for plural
                if forms["Plural"]["audio"]:
                    st.audio(forms["Plural"]["audio"])

        st.button("Clear", on_click=self.clear_inputs)

    def clear_inputs(self):
        for person, _ in self.verbs.items():
            st.session_state[f"singular_{person}_input"] = ""
            st.session_state[f"plural_{person}_input"] = ""
