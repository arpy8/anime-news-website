import requests, streamlit as st, os
st.set_page_config(page_title="Tech Today", page_icon=":newspaper:")
def news(keyword="technology"): return requests.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey={st.secrets["NEWS_API"]}&language=en&searchIn=title').json()['articles']
st.markdown("""<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> <br><br><br> <hr style='border-top: 3px dotted grey;'><hr style='border-top: 3px dotted grey;'> <br><br><h1 style='text-align: center; color: red;'>🔥Latest trending news in tech🔥</h1><br><br><hr style='border-top: 3px dotted grey;'><hr style='border-top: 3px dotted grey;'><br><br><br><br><br><br><br><br><br>""", unsafe_allow_html=True)
for random_news in list(news()):st.markdown(f"""<h2>{random_news['title']}</h2><h5>{random_news['description']}</h5>Link : <a href="{random_news['url']}">{random_news['url'][:80]}...</a><br>Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i> <hr>""", unsafe_allow_html=True)