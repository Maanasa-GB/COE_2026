import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Image to PDF Converter")

st.title("📄 Image to PDF Converter")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to RGB
    if image.mode == "RGBA":
        image = image.convert("RGB")

    pdf_path = "converted.pdf"

    # Save as PDF
    image.save(pdf_path, "PDF", resolution=100.0)

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="⬇ Download PDF",
            data=pdf_file,
            file_name="converted.pdf",
            mime="application/pdf"
        )
