import streamlit as st
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
import os

st.write("""
# Face Eraser
##### Detects and erases faces from your image
***
""")

image = st.file_uploader("Upload the image file",type=['png','jpg','jpeg'],accept_multiple_files=False)
if image:
    data =  plt.imread(image)
    detector = MTCNN()
    result_list = detector.detect_faces(data)
    plt.imshow(data)
    ax = plt.gca()
    for result in result_list:
        x, y, width, height = result['box']
        rect = Rectangle((x, y), width, height, fill=True, color='white')
        ax.add_patch(rect)
   
    name = st.text_input("Name of output file: ")
    if name:
        plt.savefig(f'{name}.jpg',dpi=90,bbox_inches='tight')
        image2 = plt.imread(f'{name}.jpg')

        st.image(image2)
        with open(f'{name}.jpg', "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name=f'{name}.jpg',
                    mime="image/png"
                )