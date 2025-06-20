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
    st.image("https://i.ibb.co/WN4f7FDV/commingsoon-looplyfe.png", width = 120)
    st.markdown("##Comming Soon...")











    