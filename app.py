import streamlit as st
from openai import OpenAI

# ----------------------------
# Load API Key
# ----------------------------
api_key = st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found in secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# ----------------------------
# Language Selector
# ----------------------------
language = st.selectbox(
    "🌍 Choose language / Choisissez la langue / Safidio ny fiteny",
    ["English", "French", "Malagasy"]
)

# ----------------------------
# UI Text by Language
# ----------------------------
if language == "English":
    title = "🎨 AI Image Generator"
    desc = "Describe an image and let AI create it for you."
    prompt_label = "Your prompt"
    btn_text = "Generate Image"
    size_label = "Image size"
    tips_title = "Prompt Examples & Tips"
    footer = "AI Image Generator | Powered by OpenAI"
elif language == "French":
    title = "🎨 Générateur d’Images IA"
    desc = "Décrivez une image et l’IA la créera pour vous."
    prompt_label = "Votre description"
    btn_text = "Générer l’image"
    size_label = "Taille de l’image"
    tips_title = "Exemples de prompts & conseils"
    footer = "Générateur d’Images IA | Propulsé par OpenAI"
else:
    title = "🎨 Mpamorona Sary AI"
    desc = "Farito ny sary tianao, dia foronin'ny AI."
    prompt_label = "Fanazavana soratana"
    btn_text = "Hamorona sary"
    size_label = "Haben’ny sary"
    tips_title = "Ohatra sy torohevitra"
    footer = "Mpamorona Sary AI | Mampiasa OpenAI"

# ----------------------------
# Header
# ----------------------------
st.markdown(f"<h1 style='text-align:center;color:#4B0082'>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:#555'>{desc}</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Prompt Input
# ----------------------------
prompt = st.text_area(
    prompt_label,
    placeholder="e.g. A romantic portrait in the rain, cinematic lighting..."
)

size = st.selectbox(
    size_label,
    ["256x256", "512x512", "1024x1024"]
)

# ----------------------------
# Example Prompts (Collapsible)
# ----------------------------
with st.expander(tips_title):
    st.write("• A romantic portrait of a girl in the rain, soft cinematic lighting")
    st.write("• A futuristic city at sunset, neon lights, cyberpunk style")
    st.write("• A watercolor painting of a forest in autumn")
    st.write("• A fantasy castle floating in the clouds")
    st.write("• A cute robot studying in a classroom")
    st.markdown("""
    **Tips:**
    - Add style: photorealistic, watercolor, digital art, anime  
    - Add mood: romantic, dark, dreamy, bright  
    - Add lighting: cinematic, soft, neon, golden  
    """)

# ----------------------------
# Generate Button
# ----------------------------
if st.button(btn_text) and prompt:
    with st.spinner("Generating image..."):
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size,
            n=1
        )
        image_url = result.data[0].url

    st.image(image_url, caption="Generated Image", use_column_width=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown(f"<p style='text-align:center;color:#888'>{footer}</p>", unsafe_allow_html=True)
