import streamlit as st 
import pandas as pd 
import altair as alt 
import seaborn as sns 

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplt about penguins!')
selected_species = st.selectbox('What species would you like to visualize?',
                                ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])



# import our data 
penguins_df = pd.read_csv("penguins.csv")
penguins_df = penguins_df[penguins_df['species'] == selected_species]
alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of {selected_species} Penguins")
        .mark_circle()
        .encode(
            x=selected_x_var, 
            y=selected_y_var,
        )
        .interactive()
)

st.altair_chart(alt_chart, use_container_width=True)