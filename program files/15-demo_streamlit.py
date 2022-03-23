import matplotlib.pyplot as plt
import numpy.random as npr
import streamlit as st

st.title("Streamlit Demo")
st.write('Here is some special text that I want you to read')
st.write('# Here is h1')
"""
### Here is a subheading 
* here is a bullet
* here is some *italics*
"""
st.sidebar.title('Parameters')
size = st.sidebar.text_input('Sample size', 100)
bins = st.sidebar.slider("Number of bins", 10, 100)
color = st.sidebar.color_picker('Click to pick')
st.sidebar.write(f"the current color is {color}")
button = st.sidebar.button("Click me!")

st.sidebar.date_input("Start date")


def function_name():
    pass


x = npr.standard_normal(int(size))
fig, ax = plt.subplots(figsize=(4, 2))
ax = plt.hist(x, bins=bins, color=color, edgecolor='w')
st.write(fig)

if button:
    function_name()
