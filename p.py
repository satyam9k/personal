import streamlit as st

def main():
    st.set_page_config(
        page_title="Pixel Art Surprise",
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

    if st.button("Press me"):
        st.write("I Love You My Gorgeous, My Precious I am so Grateful for you")

if __name__ == "__main__":
    main()
