import streamlit as st
import matplotlib
import common
from common import (
    create_data,
    plot_linear_trend,
    plot_linear_trend2
)


def get_fig2(x, y):
    return plot_linear_trend2(x, y)


def main():
    # matplotlib.use('TkAgg')
    num_point = st.slider('num_points', 100, 1000)
    create_data = st.cache_resource(common.create_data)
    x, y = create_data(num_points=num_point)
    color = st.selectbox('color', ['red', 'green', 'orange'])
    fig1 = plot_linear_trend(x, y, oren='the best', color=color)
    st.pyplot(fig1)
    fig2 = get_fig2(x, y)
    st.pyplot(fig2)
    with st.sidebar:
        st.slider('How many tea spoons of sugar?', 0, 10)


if __name__ == "__main__":
    main()