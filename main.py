import streamlit as st
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
import io

st.write("""
# Face Eraser
##### Detects and erases faces from your image
***
""")

image = st.file_uploader("Upload the image file",type=['png','jpg','jpeg'],accept_multiple_files=False)
if image:
    fig = plt.figure()
    data =  plt.imread(image)
    detector = MTCNN()
    result_list = detector.detect_faces(data)
    plt.axis('off')
    plt.imshow(data)
    ax = plt.gca()
    for result in result_list:
        x, y, width, height = result['box']
        rect = Rectangle((x, y), width, height, fill=True, color='white')
        ax.add_patch(rect)
    st.pyplot(fig)
    name = st.text_input("Name of output file: ")
    if name:
        img = io.BytesIO()
        plt.savefig(img, format='jpg')

        btn = st.download_button(
            label="Download image",
            data=img,
            file_name=f'{name}.jpg',
            mime="image/jpg"
        )