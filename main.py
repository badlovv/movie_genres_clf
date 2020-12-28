import streamlit as st
from model import GenreClassifier


genres_clf = GenreClassifier()

st.title('Classify your text into movie genre!')
st.markdown('''

''')
text = st.text_area(label='Type in some dialogue from a movie.',
                      value="All these protocols and procedures to make it seem "
                            "like you have it under control. But you're a bunch of boys "
                            "making models out of balsa wood. You don't have anything under control!")


st.write('Genres: {}'.format(', '.join(genres_clf.predict_genre(text)[0])))
