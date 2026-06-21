import streamlit as st

from api import generate_image
from prompts import build_prompt


st.title("🎨 AI Image Generator")


st.write("Generate beautiful AI images using Hugging Face")


prompt = st.text_input("Enter image prompt")



style = st.radio(

"Select Style",

["Anime","Cyberpunk","Realistic","Fantasy"]

)




if "history" not in st.session_state:

    st.session_state.history=[]



final_prompt = build_prompt(

        prompt,

        style

    )

if st.button("Generate"):
    response = generate_image(final_prompt) 
    
if response.status_code == 200:
      st.image(response.content)

else:
    st.error(f"Status code: {response.status_code}")
    st.code(response.text)


    # image = generate_image(

    #     final_prompt 

    # )



    # st.image(

    #     image,

    #     caption=final_prompt

    # )



    st.session_state.history.append(

        final_prompt

    )




st.subheader("Prompt History")


for p in st.session_state.history:

    st.write("•",p)
