import streamlit as st 
import pandas as pd 
import altair as alt 
import seaborn as sns 

st.title("Palmer's Penguins")
st.markdown('Use the streamlit app to make your own scatterplot about penguins!')

selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
penguin_file = st.file_uploader("Select your Local Penguins CSV (default provided)")
if penguin_file is not None:
    penguins_df = pd.read_cvs(penguin_file)
else: 
    st.stop()




sns.set_style('darkgrid')
markers = {"Adelie": "x", "Gentoo": "s", "Chinstrap": "o"}

alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of Palmer's Penguins")
        .mark_circle()
        .encode(
            x=selected_x_var, 
            y=selected_y_var,
            color="species",
        )
        .interactive()
)

st.altair_chart(alt_chart, use_container_width=True)