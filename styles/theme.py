from styles.custom_css import get_custom_css

def apply_theme(st_instance):
    custom_css = get_custom_css()
    st_instance.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)
