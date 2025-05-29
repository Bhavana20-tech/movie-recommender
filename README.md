# movie-recommender
🎬 Movie Recommender System This is a web-based application that recommends similar movies based on the one you input. It uses content-based filtering with movie overview vectors to find and display recommendations. The app is built using Streamlit for an interactive front-end and integrates with the OMDB API to fetch movie posters and details.
# 🎬 Movie Recommender System

Welcome to my Movie Recommender System built with Python and Streamlit! 🚀 This project suggests movies based on your input and displays their posters using data fetched from the OMDB API.

---

## 📌 Project Description

This web app helps users discover movies similar to the one they enter. It uses content-based filtering (cosine similarity) and shows movie posters and clickable titles that redirect users to Google search for more details.

---

## 🔧 Features

* 🔍 Input a movie name to get 5 recommended similar movies.
* 🖼️ Posters for each recommended movie are shown.
* 🖱️ Click on a movie title to open a Google search about that movie.
* 🧱 Poster layout in a clean 4x2 grid.
* ☁️ Hosted online via Streamlit Cloud (easy to share).

---

## 🧠 Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn** (for cosine similarity)
* **Streamlit** (for UI)
* **OMDB API** (for movie posters)

---

## 🛠️ How to Run Locally

1. Clone the repo or download the source files.
2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```
4. Open the local URL displayed in your terminal.

---

## 🔗 Deployment

The app is deployed using [Streamlit Cloud](https://streamlit.io/cloud). You can share your app via a public URL provided by Streamlit.

---

## 📎 OMDB API

We use the OMDB API to fetch movie posters.

* Sign up at [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)
* Use your free API key in the code:

  ```python
  def fetch_poster(movie_name, api_key='YOUR_API_KEY'):
      ...
  ```

---

## 🙋‍♂️ Author

**Developed by:** Bhavana 💻

Let's connect on [https://www.linkedin.com/in/bhavana-peddaboina-123231308/) and share ideas! ✨

---

```

---

## 📢 Show Some Love

If you like this project, give it a ⭐ on GitHub or share it with your friends! 🥳

---

## 📬 Contact

Have questions? Reach out via LinkedIn or email me!
https://www.linkedin.com/in/bhavana-peddaboina-123231308/

---

Thank you for checking out my project! 🎉
