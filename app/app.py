import streamlit as st
from streamlit_drawable_canvas import st_canvas
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
from PIL import Image

class VideoTransformer(VideoTransformerBase):
        def transform(self, frame):
        # add image processing code here if needed
            return frame
def facial_expression_page():

    # Initialize the camera with a transformer
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

        st.write("Capture your facial expression using the camera above.")


#CSS stylinf
st.markdown(
    """
    <style>
    h1 {
        font-family: 'Arial';
        font-size: 50px;
    }
    h3 {
        font-family: 'Courier New';
        font-size: 30px;
    } 
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stRadio {
        font-size: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#initializing the pages
if "page" not in st.session_state:
     st.session_state.page = "Home"



#Navigation bars styling
st.markdown(
  """
    <style>                                                                 
    .stApp {
        background-color: #ADD8E6;  /* Light blue */
    }

    .title {
        text-align: center;
        font-size: 50px;
        color: green;
    }

    .subtitle {
        text-align: center;
        font-size: 25px;
        color: #6abd45;
    }

    # .nav {
    #     display: flex;
    #     justify-content: space-around;
    #     padding: 10px;
    #     backgrounf-color: #f4f4f4;
    #     border-radius: 10px
    #     margin-bottom: 30px;
    # }
    # .nav div {
    #     padding: 10px 20px
    #     background-color: #ffe98a;
    #     border-radius: 10px;
    #     text-align: center;
    #     font-size: 18px;
    #     color: black;
    # }
    # .nav-item {
    #     font-soze: 18px;
    #     font-weight: bold;
    #     padding: 10px;
    #     text-align: center;
    #     color: white;
    #     background-color: #2980b9;
    #     border-radius: 5px;
    #     cursor: pointer;
    #     transition: background-color 0.3s;
    # }
    # .nav-item:hover {
    #     background-color: #3498db;
    # }
    # .emoji-container {
    #     text-align: left;
    #     position: absolute;
    #     bottom: 50px;
    #     left: 50px;
    # }

    .stRadio > div {
        display: flex;
        justify-content: center;
        padding: 10px 0;
        position: fixed;
        width: 100%;
        top: 0;
        left: 0;
        z-index: 100;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: #f2f2f2;
       
         #border-radius: 10px;
    }
    .stRadio > div label {
        padding: 10px 20px;
        margin: 0 10px;
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
    }
    .stRadio > div label:hover {
        background-color: #0056b3;
        color: black;
    }
    .stRadio > div label.selected {
        background-color: #ffb3b3;
        color: white;
    }

    </style>
    <div class="nav">
        <div class="nav-item" onCLick="window.location.reload()">Home</div>
        <div class="nav-item" onCLick="window.location.reload()">Text to Emoji</div>
        <div class="nav-item" onCLick="window.location.reload()">Sketch to Emoji</div>
        <div class="nav-item" onCLick="window.location.reload()">Facial expression to Emoji</div>
    </div>
    """,
    unsafe_allow_html=True  
)




nav_options = ["Home", "Text to Emoji", "Sketch to Emoji", "Facial Expression to Emoji"]
nav_selection = st.sidebar.selectbox("", nav_options, index=0)
# page = st.radio(
#     "nav",
#     ["Home", "Text to Emoji", "Sketch to Emoji", "Facial Expression to Emoji"],
#     index=0 #this sets the default page to "Home"
# )

#this updates the session state based on the page selected
#st.session_state.page = page;

#defining the layout of the pages
if nav_selection == "Home":
    st.markdown("<h1 style='text-align: center; color: blue;'>Emoji Generator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00ab41;'>Welcome to the Emoji  Generator! Navigate to a page to create emojis from text, sketches, or facial expressions</h3>", unsafe_allow_html=True)

elif nav_selection == "Text to Emoji":
    st.markdown("<h1 style='text-align: center; color: blue;'>Text to Emoji</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: green;'Create Emoji with words!</h3>", unsafe_allow_html=True)
   # st.write("Create Emoji with text!")
    user_input = st.text_input("Create Emoji with text!", placeholder="Ex: A cat wearing a hat")

    if st.button("Generate Emoji"):
         emoji = "😊"

         st.markdown(f"### Your Emoji: {emoji}")

elif nav_selection == "Sketch to Emoji":
    st.markdown("<h1 style='text-align: center; color: blue;'>Sketch to Emoji</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: green;'>Sketch your text to Emoji!</h3>", unsafe_allow_html=True)
    
   
    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     drawing_mode = st.radio(
    #         "Drawing tool:",
    #         ("freedraw", "rect", "circle", "transform", "line", "eraser")
    #     )

    # with col2:
    #     stroke_width = st.slider("Stroke width:", 1, 25, 5)
        
    # with col3:
    #     stroke_color = st.color_picker("Stroke color:", "#000000")

    
   

    canvas_height = 400
    canvas_width = 400

#

   # canvas for sketching
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Set a transparent background color
        stroke_width=5,                      # Set pen width
        stroke_color="#000000",               # Set pen color (black)
        background_color="#ffffff",           # Set background color (white)
        height=400,                           # Canvas height
        width=400,                            # Canvas width
        drawing_mode="freedraw",              # Allow free drawing
        key="canvas"
    )

    if st.button("Generate Emoji"):

        emoji = "😊"  # Replace this with actual emoji generation 

    # Display the generated emoji instead of the sketch
        st.markdown(f"### Your Emoji: {emoji}")

    # reset canvas
        canvas_result.image_data = None

elif nav_selection == "Facial Expression to Emoji":
    st.markdown("<h1 style='text-align: center; color: blue;'>Facial expression to Emoji</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: green;'>Create emoji with your expression!</h3>", unsafe_allow_html=True)
    facial_expression_page()

    if st.button("Generate Emoji"):

        emoji = "😊"  # Replace this with actual emoji generation 

    # Display the generated emoji instead of the sketch
        st.markdown(f"### Your Emoji: {emoji}")
    

# st.markdown("<h1 style='text-align: center; color: blue;'>Emoji Generator</h1>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align: center; color: green;'>Create emojis from text, sketches, or facial expressions</h3>", unsafe_allow_html=True)
# st.markdown('<div class="title">Emoji Generator</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Unleash Your Emoji Creativity!</div>', unsafe_allow_html=True)
# st.markdown("""
#     <div class="emoji-container">
#         <img src="https://53.fs1.hubspotusercontent-na1.net/hubfs/53/00-Blog_Thinkstock_Images/emoji-marketing.png" widht="60/>
#     </div>
    # """, unsafe_allow_html=True)

#buttons to change the page
# st.sidebar.button("Home", on_click=switch_page, args=("Home",))
# st.sidebar.button("Text to Emoji", on_click=switch_page, args=("Text to Emoji",))
# st.sidebar.button("Sketch to Emoji", on_click=switch_page, args=("Sketch to Emoji",))
# st.sidebar.button("Facial expression to Emoji", on_click=switch_page, args=("Facial expression to Emoji",))



# Top navigation using radio buttons
# option = st.radio(
#     "Select Input Method:",
#     ("Facial Expression", "Text to Emoji", "Sketch to Emoji"),
#     index=0
# )

# # Display content based on selection
# if option == "Facial Expression":
#     st.subheader("Facial Expression to Emoji")
#     st.write("Upload a photo or use your webcam to capture your expression.")

# elif option == "Text to Emoji":
#     st.subheader("Text to Emoji")
#     text_input = st.text_input("Enter your text:")
#     if st.button("Generate Emoji"):
#         st.write("Generated emoji based on text!")

# elif option == "Sketch to Emoji":
#     st.subheader("Sketch to Emoji")
#     st.write("Upload your sketch or draw it on the canvas.")






# st.title("Emoji Generator") 
# st.sidebar.title("Features")
# feature_type = st.sidebar.selectbox("Select a feature!", ["Text-to-Emoji", "Skecth to Emoji", "Facial Expression to Emoji"])
