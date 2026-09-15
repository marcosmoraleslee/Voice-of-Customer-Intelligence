"""
Custom CSS styles injected into the Streamlit app.
"""

def get_custom_css():
    return """
/* =========================================================
   FONTS
   ========================================================= */

@import url(
    'https://fonts.googleapis.com/css2?family=Lexend:wght@100..900'
    '&family=Mulish:ital,wght@0,200..1000;1,200..1000'
    '&family=Urbanist:ital,wght@0,100..900;1,100..900'
    '&display=swap'
);

/* =========================================================
   GLOBAL
   ========================================================= */

html,
body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {
    background-color: #EAF4EE !important;
    color: #1A1A1A !important;
    color-scheme: light !important;
}

html,
body {
    font-family: "Mulish", sans-serif !important;
    -webkit-font-smoothing: antialiased !important;
}

[data-testid="stAppViewContainer"] > div:first-child {
    padding: 0 !important;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 2.5rem !important;
    padding-bottom: 4rem !important;
}

/* =========================================================
   TYPOGRAPHY
   ========================================================= */

h1, h2, h3, h4, h5, h6 {
    font-family: "Lexend", sans-serif !important;
    color: #1A1A1A !important;
    font-weight: 600 !important;
    letter-spacing: -0.02em !important;
}

h1 { font-size: 2.6rem !important; line-height: 1.15 !important; }
h2 { font-size: 1.8rem !important; line-height: 1.25 !important; }
h3 { font-size: 1.35rem !important; line-height: 1.3 !important; }
h4 { font-size: 1.05rem !important; line-height: 1.35 !important; }

p, li, label, {
    font-family: "Mulish", sans-serif !important;
}

p {
    color: #4F5A54 !important;
    line-height: 1.6 !important;
}

[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color: #68736D !important;
}

/* =========================================================
   GENERAL BUTTONS (General app action buttons)
   ========================================================= */

.stButton > button {
    background-color: #9B4DFF !important;
    color: #FFFFFF !important;
    border: 1px solid #9B4DFF !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.25rem !important;
    font-family: "Mulish", sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}

.stButton > button:hover {
    background-color: #B06CFF !important;
    color: #FFFFFF !important;
    border-color: #B06CFF !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 10px rgba(155, 77, 255, 0.18) !important;
}

.stButton > button:active {
    background-color: #7F3BDB !important;
    border-color: #7F3BDB !important;
}

/* Forzar que cualquier texto interno en los botones generales sea blanco */
.stButton > button *, 
.stButton > button span, 
.stButton > button div, 
.stButton > button p {
    color: #FFFFFF !important;
}

/* =========================================================
   FEEDBACK SIGNALS BUTTONS (Corrección definitiva de UX)
   ========================================================= */

div[data-testid="column"] .stButton > button {
    background-color: #FFFFFF !important;
    background-image: none !important;
    color: #1A1A1A !important;
    border: 1px solid rgba(26, 26, 26, 0.12) !important;
    border-left: 6px solid #70C04B !important;
    border-radius: 10px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 0.75rem 1rem !important;
    box-shadow: 0 2px 6px rgba(31, 55, 43, 0.04) !important;
    transition: all 0.2s ease-in-out !important;
}

div[data-testid="column"] .stButton > button * {
    color: #1A1A1A !important;
}

div[data-testid="column"] .stButton > button:hover {
    background-color: #FAFAFA !important;
    border-color: #70C04B !important;
    border-left-color: #70C04B !important;
    transform: translateX(3px) !important;
    box-shadow: 0 4px 12px rgba(112, 192, 75, 0.12) !important;
}

div[data-testid="column"] .stButton > button:hover div,
div[data-testid="column"] .stButton > button:hover p,
div[data-testid="column"] .stButton > button:hover span {
    color: #70C04B !important;
}

/* =========================================================
   FILE UPLOADER
   ========================================================= */

/* Dropzone */
[data-testid="stFileUploaderDropzone"] {
    background-color: #4F5A54 !important;
    border: 2px dashed rgba(155, 77, 255, 0.4) !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
}

/* Native Upload button */
[data-testid="stFileUploaderDropzone"] button {
    background-color: #9B4DFF !important;
    border: 1px solid #9B4DFF !important;
    border-radius: 10px !important;
    box-shadow: none !important;
    font-weight: 700 !important;
}

/* Upload button text */
[data-testid="stFileUploaderDropzone"] button [data-testid="stMarkdownContainer"] {
    color: #FFFFFF !important;
}

[data-testid="stFileUploaderDropzone"] button [data-testid="stMarkdownContainer"] p {
    color: #FFFFFF !important;
}

/* Button hover */
[data-testid="stFileUploaderDropzone"] button:hover {
    background-color: #B06CFF !important;
    border-color: #B06CFF !important;
}

/* File size and allowed type text */
[data-testid="stFileUploaderDropzone"] small {
    color: #4F5A54 !important;
    font-family: "Mulish", sans-serif !important;
}

/* Uploaded file information */
[data-testid="stUploadedFile"] span,
[data-testid="stUploadedFile"] p {
    color: #1A1A1A !important;
}


/* =========================================================
   INPUTS & SELECTBOX
   ========================================================= */

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: #FFFFFF !important;
    color: #1A1A1A !important;
    border: 1px solid rgba(26, 26, 26, 0.10) !important;
    border-radius: 12px !important;
    padding: 0.65rem 0.9rem !important;
}

.stSelectbox label {
    color: #1A1A1A !important;
    font-weight: 700 !important;
}

.stSelectbox [data-baseweb="select"] {
    background-color: #FFFFFF !important;
    border: 1px solid rgba(26, 26, 26, 0.10) !important;
    border-radius: 12px !important;
}

.stSelectbox [data-baseweb="select"] [role="combobox"],
.stSelectbox [data-baseweb="select"] span,
.stSelectbox [data-baseweb="select"] div {
    color: #1A1A1A !important;
    background-color: #FFFFFF !important;
}

[data-baseweb="popover"], [data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] [role="option"] {
    background-color: #FFFFFF !important;
    color: #1A1A1A !important;
}

[data-baseweb="menu"] [role="option"]:hover {
    background-color: #F4F7F5 !important;
    color: #70C04B !important;
}

/* =========================================================
   METRICS & CARDS
   ========================================================= */

[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border-radius: 18px !important;
    padding: 1.25rem 1.4rem !important;
    box-shadow: 0 4px 14px rgba(31, 55, 43, 0.07) !important;
}

[data-testid="stMetricLabel"] {
    color: #68736D !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #1A1A1A !important;
    font-family: "Lexend", sans-serif !important;
}

/* =========================================================
   DATAFRAME & EXPANDERS
   ========================================================= */

[data-testid="stDataFrame"], [data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border-radius: 16px !important;
    border: 1px solid rgba(26, 26, 26, 0.08) !important;
}

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #EAF4EE; }
::-webkit-scrollbar-thumb { background: rgba(79, 90, 84, 0.25); border-radius: 10px; }
"""