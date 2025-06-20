import streamlit as st

st.set_page_config(page_title = "Loop Lyfe", layout = "centered")

st.title("💥 WELCOME TO LOOP LYFE 💥")

st.caption('''Loop Lyfe is a portal that showcases my own handmade fun & dumbass programs.
It acts as a door to my silly-smart creations 💻❤️''')

st.divider()

st.subheader("My Projects 💡🧪")

col1, col2 = st.columns(2)

with col1:
    st.image("https://i.ibb.co/SwvBW0xK/lovecalc-looplyfe.png", width = 120)
    st.markdown("## 💘love Calculator")
    st.caption("Check your love fate")
    st.link_button("💘Try now", "https://love-calculator-cffrt6jqlhwxnespueq7zs.streamlit.app/")

with st.expander("💡 How does it work?"):
    st.write("""This calculator checks for common letters in both names,
        adds a bit of playful math, and gives you a love % score.
        Don't take it too seriously... unless it says 100% 😉 [AI GENERATED OFC]""")



with col2:
    st.image("https://i.ibb.co/M3GNzBg/fate-flip.png", width = 120)
    st.markdown("## 🪙Fate Flip")
    st.caption("Not just a normal coin toss...")
    st.link_button("🪙Try now", "https://fate-flip-kqfqirehbkpj2ocmturhwa.streamlit.app/")

with st.expander("💡 How does it work?"):
    st.write("""" Fate Flip is a playful web app 
        built with Python and Streamlit that lets users flip a coin... but not just any coin.
        You can customize what "Heads" and "Tails" mean — whether it's "I eat pizza" vs. 
        "I study tonight", or "Quit my job" vs. "Keep grinding".""")    

    











    