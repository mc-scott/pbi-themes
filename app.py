"""
Streamlit UI to generate a PBI theme based on user inputs.
In terminal of working directory: python -m streamlit run app.py
"""

import streamlit as st
import utils

with st.sidebar:
    st.header("Power BI Theme Generator App")
    with st.expander("Choose Colour Palette"):
        background = st.color_picker(label="Background", value="#FFFFF1", help="Dashborad background")

st.markdown("""
Choose a pre-formatted theme or change the inputs on the left to create a custom theme.
The preview image below changes as inputs change.
Download a Power BI theme using the button in the right.
""")

# save svg as string object
img = utils.modify_svg(scale=0.6, background=background)
# render svg string as html
utils.render_svg(img)

st.download_button(label="Download Theme", data=img, help="Download JSON theme that can be uploaded to Power BI")

