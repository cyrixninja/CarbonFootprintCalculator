import streamlit as st
import equations
import base64

st.title(' ')
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.png')


st.title("Carbon Footprint Calculator")
option = st.selectbox(
    'Choose Which type of Carbon Footprint do you wanna calculate',
    ('Choose an Option', 'Household Carbon Footprint','Public Transport Carbon Footprint','Car Carbon Footprint','Food Carbon Footprint'))

if option=="Household Carbon Footprint":
        equations.household()
elif option=="Public Transport Carbon Footprint":
        equations.publictransport()
elif option=="Car Carbon Footprint":
        equations.carcarbonfootprint()
elif option=="Food Carbon Footprint":
        equations.food()