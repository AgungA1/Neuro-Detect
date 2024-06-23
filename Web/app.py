import streamlit as st
import streamlit_antd_components as sac
from scanner.vgg16 import app as scan_vgg
from description.glioma import app as glioma
from description.meningioma import app as meningioma
from description.pituitary import app as pituitary

class MultiApp:
    def run():
        with st.sidebar:
            app = sac.menu([
                sac.MenuItem('Home', icon='house-fill'),
                sac.MenuItem('Tumor', icon='info-circle-fill', children=[
                    sac.MenuItem('Glioma'),
                    sac.MenuItem('Meningioma'),
                    sac.MenuItem('Pituitary'),
                ]),
                sac.MenuItem('Scan', icon='upc-scan')
            ], size='xs', variant='right-bar', open_all=True)

        if app == "Home":
            st.header("NeuroDetect")
            st.write("NeuroDetect adalah aplikasi web yang dikembangkan untuk mendeteksi dan mengenali tumor otak menggunakan teknologi deep learning. Aplikasi ini menyediakan informasi tentang jenis-jenis tumor otak, gejala yang mungkin muncul, serta metode diagnosis dan pengobatan yang umum digunakan.")
            st.write("Pilih menu di sebelah kiri untuk memulai.")
        elif app == "Glioma":
            glioma()
        elif app == "Meningioma":
            meningioma()
        elif app == "Pituitary":
            pituitary()
        elif app == "Scan":
            scan_vgg()
    run()