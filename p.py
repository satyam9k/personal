import streamlit as st

def main():
    st.set_page_config(
        page_title="Heyyy Priyansha!!!",
        page_icon="❤️"
    )

    st.markdown(
        "<h1 style='text-align: center; color: Salmon; font-family: Lobster;'>My Sweet Love🥰</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center; color: #A5F1F7; font-family: Lobster;'>Here's some flowers for you 🌹🌻💐🌼</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center; color: #A5F1F7; font-family: Lobster;'>Click ❤️ to reveal a message </h3>",
        unsafe_allow_html=True
    )

    if st.button("❤️"):
        st.markdown(
            "<p style='color: #ffcccc; font-size: 24px; font-family: Comic Sans MS; text-align: center;'>"
            "I Love You My Gorgeous, My Precious I am so Grateful for you :)<br><br>"
            "Cause all of the small things that you do<br>"
            "Are what remind me why I fell for you<br>"
            "And when we're apart, and I'm missing you<br>"
            "I close my eyes and all I see is you<br>"
            "And the small things you do"
            "</p>",
            unsafe_allow_html=True
        )
        st.audio("song.mp3", format="audio/mp3", start_time=0)
        st.success("Enjoy the playlist!   I Love You SO SO SO Much!!!!!")

   

if __name__ == "__main__":
    main()
