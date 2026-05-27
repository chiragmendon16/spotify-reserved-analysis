# Spotify Reserved Analysis

> A data analytics and business intelligence project examining Spotify's newly launched Reserved feature — a superfan ticketing programme that uses streaming behaviour to allocate concert tickets to an artist's most dedicated listeners.

**Tools:** Python · Pandas · Scikit-learn · Spotify Web API · Tableau · SQL  
**Type:** Data Analysis · Business Analysis · Product Analytics  
**Status:** Phase 1 Complete — Phase 2 In Progress  

---

## Project Overview

On May 21 2026, Spotify announced **Reserved** at its Investor Day — a feature for Premium subscribers that identifies superfans based on listening behaviour (streams, saves, shares) and holds two concert tickets for them before general public sale, in partnership with Live Nation.

This project answers 7 core business questions about how Reserved works, how it should be measured, and what risks and opportunities exist as it scales.

---

## Business Questions

| # | Question | Analysis type |
|---|---|---|
| Q1 | What listening signals most strongly predict superfan status? | Scoring model |
| Q2 | How could Spotify improve the Reserved experience beyond ticket access? | Product analysis |
| Q3 | What structural fairness risks exist in the eligibility model? | Bias analysis |
| Q4 | How does Spotify collect and score behavioural signals for each user? | Data architecture |
| Q5 | How does the model perform at A-list scale (BTS, Weeknd, Beyoncé)? | Stress test |
| Q6 | Does a Reserved offer improve 90-day Premium subscriber retention? | Retention analysis |
| Q7 | What is the revenue uplift for artists and venues from Reserved? | Financial model |

---

## Key Findings *(updated as analysis progresses)*

- Superfan scoring model built using 6 behavioural signals; top 5% engagement tier maps to Reserved eligibility
- Artist segmentation reveals 4 distinct tiers with materially different superfan density profiles
- A-list stress test: for a 60,000-seat stadium artist, Reserved allocation is a ~300:1 competition among eligible fans
- Retention hypothesis: a 5% improvement in 90-day Premium retention = ~$193M incremental ARR at current subscriber base
- 6 product enhancement recommendations for Reserved v2.0 identified

---

## Project Structure

```
spotify-reserved-analysis/
│
├── README.md                          ← You are here
│
├── docs/
│   └── 01_business_understanding.md  ← Phase 1 complete
│
├── charts/
│   ├── Artist Segmentation Charts
│   ├── EDA charts      
│   ├── Financial Impacting charts
│   ├── Superfan Scoring Model Charts
│
├── data/
│   ├── raw/                           ← Original downloaded data
│   └── processed/                     ← Cleaned, analysis-ready data
│
├── notebooks/
│   ├── 01_data_collection.ipynb       ← Phase 2 complete
│   ├── 02_eda.ipynb                   ← Phase 3 complete
│   ├── 03_superfan_scoring_model.ipynb
│   ├── 04_artist_segmentation.ipynb
│   └── 05_financial_impact_model.ipynb
│
├── dashboard/
│   └──📊 <a href="https://public.tableau.com/app/profile/chirag.mendon/viz/SpotifyReservedTicketingAnalysis/SpotifyReserved-ArtistOverviewDashboard?             │            publish=yes">Click Here to View the Interactive Tableau Dashboard</a>
│
└── report/
    └── spotify_reserved_insights.pdf  ← Final report (Phase 5)
```

---

## Data Sources

| Source | Used for | Access |
|---|---|---|
| Spotify Web API | Artist features, audio features, popularity scores | Free developer account |
| Spotify Charts (charts.spotify.com) | Weekly stream counts by country | Public CSV download |
| Kaggle — Spotify Tracks Dataset | 600K+ track-level dataset with audio features | Free download |
| Songkick API | Concert tour dates and venue capacity | Free API key |
| Spotify Investor Relations (Q1 2026) | Business metrics, subscriber counts | Public |

---

## How to Run This Project

```bash
# Clone the repository
git clone https://github.com/[your-username]/spotify-reserved-analysis.git
cd spotify-reserved-analysis

# Install dependencies
pip install -r requirements.txt

# Set up Spotify API credentials
# Create a .env file with your CLIENT_ID and CLIENT_SECRET from developer.spotify.com
cp .env.example .env

# Open notebooks
jupyter notebook notebooks/
```

---

## Phase Progress

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Business understanding, problem statement, KPIs | Complete |
| Phase 2 | Data collection and cleaning | In Progress |
| Phase 3 | Analysis and modelling | Upcoming |
| Phase 4 | Dashboard and visualisation | Upcoming |
| Phase 5 | Report and portfolio packaging | Upcoming |

---

## About This Project

This is a portfolio project built to demonstrate data analysis and business analysis skills in the context of a real, live product announcement. All data used is publicly available. This project is not affiliated with or endorsed by Spotify AB.

**Connect:** [LinkedIn](https://www.linkedin.com/in/chirag-mendon-14b1a02b4/) · [Email](mailto:chiragmndnprsnl2004@gmail.com)
