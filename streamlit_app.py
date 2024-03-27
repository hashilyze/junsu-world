import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+a^1+a r^2+a r ^3''')

st.markdown("## random image")
st.image("https://picsum.photos/200")

st.markdown("## 기본적인 데이터 형식 입력")
st.checkbox("yes")
st.button("click")
gender = st.radio("Pick your gender", ["Male", "Female"])
st.selectbox("Pick your gender", ["Male", "Female"])
planet = st.multiselect("choose a planet", ["Jupiter", "Mars", "Neptune"])
st.select_slider("Pick a mark", ["Bad", "Good", "Excellent"])
st.slider("Pick a number", 0.50)

st.write("성별:", gender)
st.write("행성:", planet)

st.markdown("## 다양한 데이터 형식 입력")
st.number_input("Pick a number", 0.10)
st.text_input("Email address")
st.date_input("Travelling date")
st.time_input("School time")
st.text_area("Description")
st.file_uploader("Upload a photo")
st.color_picker("Choose your favorite color")

st.markdown("## Visualization")

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.line_chart(df)