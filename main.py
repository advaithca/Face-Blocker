import streamlit as st
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
import io

st.write("""
# Face Blocker
##### Detects and blocks faces from your image
***
""")

image = st.file_uploader("Upload the image file",type=['jpg','jpeg'],accept_multiple_files=False)
if image:
    fig = plt.figure()
    data =  plt.imread(image)
    with st.spinner("Detecting faces..."):
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
    st.success("Detected faces and blocked the faces that were detected!")
    
    placeholder = st.empty()
    with placeholder.container():
        name = st.text_input("Name of output file: ")
        clickme = st.button("Continue")
    if name and clickme:
        placeholder.empty()
        img = io.BytesIO()
        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        plt.savefig(img, format='jpg',bbox_inches=extent)

        btn = st.download_button(
            label="Download image",
            data=img,
            file_name=f'{name}.jpg',
            mime="image/jpg"
        )