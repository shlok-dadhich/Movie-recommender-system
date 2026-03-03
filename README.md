# 🎬 Movie Recommender System

A content-based movie recommender system built with **Python** and **Streamlit** that suggests similar movies based on your selection, complete with movie posters fetched from the TMDB API.

---

## 🚀 Demo

Select a movie from the dropdown and click **Recommend** to get 19 similar movie suggestions with posters!

---

## 📁 Project Structure

```
Movie-recommender-system/
│
├── app.py                  # Main Streamlit application
├── movies.pkl              # Movie dataset (pickled DataFrame)
├── similarity.pkl          # Similarity matrix (download separately)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-recommender-system.git
cd Movie-recommender-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Similarity Model

The `similarity.pkl` file is too large for GitHub. Download it from Google Drive and place it in the root of the project folder:

📥 **[Download similarity.pkl from Google Drive](https://drive.google.com/file/d/1mMllk3kHBtp8UIE7-yDFqw1VSr2njy7y/view?usp=sharing)**

After downloading, your folder should look like:
```
Movie-recommender-system/
├── similarity.pkl   ✅  ← place here
├── movies.pkl       ✅  ← already in repo
├── app.py
...
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **Movies Dataset** (`movies.pkl`) — Contains movie titles and IDs.
2. **Similarity Matrix** (`similarity.pkl`) — A precomputed cosine similarity matrix between movies based on their features (genres, keywords, cast, crew, etc.).
3. When a movie is selected, the app finds the top 19 most similar movies using the similarity matrix.
4. Movie posters are fetched in real-time from the **[TMDB API](https://www.themoviedb.org/documentation/api)**.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Requests](https://requests.readthedocs.io/)
- [TMDB API](https://www.themoviedb.org/documentation/api)

---

## 📌 Notes

- Make sure both `movies.pkl` and `similarity.pkl` are in the **same directory** as `app.py` before running.
- The TMDB API key is embedded in the app. If it stops working, generate a free key at [themoviedb.org](https://www.themoviedb.org/) and replace it in `app.py`.
