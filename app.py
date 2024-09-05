import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    st.title("Samay AI Assistant 🤖")
    user_input = st.text_input("Ask me anything:", placeholder="Type something...")

    
    if st.button("Enter/ Speak"):
            if user_input:
                st.session_state.user_input = user_input
                print(user_input)
            if not user_input:
                with st.spinner("Listening..."):
                    text = voice_input()
                    print(text)
                    
                    if not text:
                        st.error("No input detected. Please try again.")
                        
                        return
            else:
                  text =user_input
            response = llm_model_object(text)
            st.text_area(label="Response:", value=response, height=350)
            print(response)
            with st.spinner("loading audio"):
                text_to_speech(response)

                
            audio_output = text_to_speech(response)
            
            st.audio(audio_output, format='audio/mp3')
            st.download_button(label="Download Speech",
                               data=audio_output,
                               file_name="speech.mp3",
                               mime="audio/mp3")    
            # audio_file = open("speech.mp3", "rb")
            # audio_bytes = audio_file.read()
                
            # st.audio(audio_bytes)
            # st.download_button(label="Download Speech",
            #                    data=audio_bytes,
            #                    file_name="speech.mp3",
            #                    mime="audio/mp3")
            
if __name__ == '__main__':
    main()
