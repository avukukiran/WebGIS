import streamlit as st
import leafmap.foliumap as leafmap

# Set up the Streamlit app
st.set_page_config(page_title="Web GIS App", layout="wide",page_icon="🦈")

st.title("Web GIS Application")
st.write("Explore interactive maps with this simple Web GIS tool!")

# Add custom CSS for padding and height
custom_css = """  <style>
    /* Set padding for the main content */
    .main {
        padding: 10px 10px 10px 10px; /* Top-Bottom, Left-Right */
        # gap:10px;
    }
    .st-emotion-cache-fn1920 {
        gap:1px;
    }
    /* Adjust the height of the Streamlit app container */
    .css-1y0tads {
        min-height: 100vh; /* Full viewport height */
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header("Map Settings")
lat = st.sidebar.number_input("Enter latitude:", value=0.0, step=0.1)
lon = st.sidebar.number_input("Enter longitude:", value=0.0, step=0.1)
zoom = st.sidebar.slider("Zoom level:", min_value=1, max_value=18, value=3)

# Create a map using leafmap
m = leafmap.Map(center=[lat, lon], zoom=zoom)
# m.add_basemap
# print(type(leafmap.Map))

# Add basemap options
m.add_vector_tile_layer("http://localhost:8088/geoserver/spatial/wms?version=1.3.0&layers=spatial:states",None,"States")
basemap = st.sidebar.selectbox("Choose a basemap:", leafmap.basemaps)
m.add_basemap(basemap='HYBRID')
# Display the map
m.to_streamlit(height=500)
