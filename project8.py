import streamlit as st

with st.sidebar:
    image = 'denvau.jpg'
    st.image(image, caption='Đen Vâu')
    st.write('**Họ và tên:** Nguyễn Đức Cường')
    st.write('**Nghệ danh:** Đen Vâu')
    st.write(
        'Nguyễn Đức Cường, thường được biết đến với nghệ danh Đen Vâu hay Đen, '
        'là một nam rapper và nhạc sĩ người Việt Nam. Đen Vâu từng giành được giải Cống hiến '
        'và là "một trong số ít nghệ sĩ thành công từ làn sóng underground và âm nhạc indie" của Việt Nam.'
    )

st.title('🎵 Bài hát yêu thích')
st.subheader('Cho tôi lang thang')
audio_file = open('denvaunhac.mp3', 'rb')  
st.audio(audio_file, format='audio/mp3')

st.title('🎬 MV yêu thích')
st.subheader('Đưa nhau đi trốn')
video_url = 'https://www.youtube.com/watch?v=5e7e_KZINA4'
st.video(video_url)