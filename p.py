import streamlit as st

def main():
    st.set_page_config(
        page_title="Heyyy Priyansha!!!",
        page_icon="❤️"
    )

    st.markdown(
        "<h1 style='text-align: center; color: white;'>Pixel Art Surprise</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center; color: white;'>Click the heart to reveal a message ❤️</h3>",
        unsafe_allow_html=True
    )

    if st.button("❤️"):
        st.markdown(
            "<p style='color: #ffcccc; font-size: 24px; font-family: Lobster; text-align: center;'>"
            "I Love You My Gorgeous, My Precious I am so Grateful for you<br><br>"
            "Cause all of the small things that you do<br>"
            "Are what remind me why I fell for you<br>"
            "And when we're apart, and I'm missing you<br>"
            "I close my eyes and all I see is you<br>"
            "And the small things you do"
            "</p>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
