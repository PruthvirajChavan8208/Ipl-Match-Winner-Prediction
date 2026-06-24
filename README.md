# IPL Match Winner Predictor 🏏

An end-to-end Machine Learning web application deployed using Streamlit that predicts the winning probability of an Indian Premier League (IPL)
match based on pre-match variables. By analyzing historical trends, the app provides data-driven insights into match outcomes before a single ball is bowled.


Check this link:-https://ipl-match-winner-prediction-dryyzk5urae7ojposdxs4g.streamlit.app/

## 🚀 Features
- Match Outcome Classification: Uses machine learning to calculate exact win/loss probabilities for both teams.
- Match Setup inputs: Computes predictions instantly based on:
  - Batting Team & Bowling Team selection.
  - Toss Winner.
  - Toss Decision (Bat or Field).
  - Match Venue (Stadium).
- Interactive UI: A clean, user-friendly Streamlit dashboard deployed for seamless interaction.
- Historical Insights: Leverages years of match data to account for crucial real-world variables like venue bias and toss advantages
(e.g., chasing success in night matches).

## 📊 Architecture & Algorithmic Workflow

The project utilizes a classification pipeline optimized for categorical match features:

1. Data Preprocessing & Feature Engineering:
   - Consolidating historical match metrics to map head-to-head records and ground-specific trends.
   - Processing critical high-level features: team1,team2, toss_winner, toss_decision, and venue.
2. Model Selection:
   - Evaluated multiple models including Logistic Regression, Random Forest Classifier, and XGBoost.
   - Random Forest was implemented to output well-calibrated, robust probability distributions for the two competing squads.
3. Pipeline Optimization:
   - Implemented via a Scikit-Learn Pipeline utilizing OneHotEncoder to smoothly transform categorical selections into numerical inputs for the trained model.

## 🛠️ Tech Stack
- Language: Python 3.x
- Libraries: Pandas, NumPy, Scikit-Learn
- Web Framework & Deployment: Streamlit
- Model Serialization: Pickle

## ⚙️ Installation & Usage

1. Clone the Repository:
`bash
   git clone :-(https://github.com/PruthvirajChavan8208/Ipl-Match-Winner-Prediction.git)
   cd Ipl-Match-Winner-Prediction
2.Check sample Usage on Streamlit
	Check this link:-https://ipl-match-winner-prediction-dryyzk5urae7ojposdxs4g.streamlit.app/