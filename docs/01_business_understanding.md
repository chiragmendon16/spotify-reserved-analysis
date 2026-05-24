# Phase 1 — Business Understanding
### Spotify Reserved: Superfan Ticketing Analysis

**Project:** Spotify Reserved — Superfan Identification & Business Impact Analysis  
**Analyst:** Chirag A Mendon  
**Date:** May 2026  
**Status:** In Progress  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Business Context](#3-business-context)
4. [Stakeholder Map](#4-stakeholder-map)
5. [Research Questions](#5-research-questions)
6. [KPI Framework](#6-kpi-framework)
7. [Project Scope](#7-project-scope)
8. [Data Availability Assessment](#8-data-availability-assessment)
9. [Assumptions Log](#9-assumptions-log)
10. [Fictional Stakeholder Briefing Email](#10-stakeholder-briefing-email)

---

## 1. Executive Summary

Spotify launched **Reserved** on May 21, 2026 at its annual Investor Day — a feature that uses streaming behaviour data to identify an artist's most dedicated fans (superfans) and hold two concert tickets for each of them, giving them a private purchase window before tickets go on sale to the general public.

This project builds a **data-driven superfan scoring model**, simulates ticket conversion and Premium subscriber retention outcomes across artist segments, and produces a **recommended KPI dashboard** that Spotify's product and live events teams could use to measure Reserved's performance and guide future rollout decisions.

**Why this matters:** Spotify has 293 million Premium subscribers and a stated target of 1 billion subscribers by 2030. Reserved is Spotify's strongest-ever Premium value proposition — and also its most data-intensive product. Understanding how to define, score, and reward superfans using real behavioural signals is the analytical foundation the entire feature depends on.

---

## 2. Problem Statement

### CRPI Format

| Component | Detail |
|---|---|
| **C — Context** | Spotify launched Reserved in May 2026, a feature that uses streaming data (plays, saves, shares) to identify superfans and hold concert tickets for them before general sale, in exclusive partnership with Live Nation. |
| **R — Research gap** | No public model exists for how Spotify scores superfan eligibility, what the expected ticket conversion rate is among notified fans, or whether Reserved meaningfully reduces Premium subscriber churn. |
| **P — Purpose** | This project builds a transparent superfan scoring model using publicly available Spotify data, simulates ticket conversion and Premium retention outcomes across artist segments, and stress-tests the model's fairness across artist scales (indie to stadium). |
| **I — Impact** | Findings will inform how Spotify's product and live events teams should define Reserved success, prioritise artist partnerships for rollout, and iterate on the feature's eligibility logic. |

### Full Problem Statement

> *"Spotify's Reserved feature rewards superfans with exclusive ticket access based on streaming behaviour. This project analyses what listening signals most strongly define a true superfan, how effectively Reserved can drive Premium subscriber retention, what fairness risks exist in the current model, and what KPIs Spotify should track to measure the feature's success across artists of different scales — from developing indie acts to A-list stadium headliners."*

---

## 3. Business Context

### What is Spotify Reserved?

- Launched: **May 21, 2026** at Spotify Investor Day (New York)
- Feature: Identifies artist's most dedicated fans → holds 2 concert tickets → grants private purchase window (~24 hours) before general sale
- Eligibility: Spotify Premium subscribers, age 18+, starting in the US
- Partner: **Live Nation** (multi-year exclusive launch partner)
- No additional fees from Spotify; fans pay face value on ticketing partner platform
- Identification signals: streams, shares, playlist saves, and other Spotify activity

### Key Business Numbers (Q1 2026)

| Metric | Value |
|---|---|
| Total Monthly Active Users (MAU) | 761 million |
| Premium Subscribers | 293 million |
| Ticket sales driven by Spotify to date | $1.5 billion+ |
| Ticketing partners integrated | 40+ |
| Target subscribers by 2030 | 1 billion |
| Spotify stock movement on Investor Day | +15% |

### Why Reserved is strategically important

Reserved is not just a feature — it is a **strategic pivot**. Spotify is transitioning from an audio streaming platform into a data-powered music ecosystem. Reserved represents:

1. **Premium retention lever** — a reason to stay on Premium that has nothing to do with audio quality or catalogue size
2. **Premium upgrade driver** — a compelling upsell to free-tier users who want access
3. **Data monetisation** — Spotify's engagement data becoming a direct commercial asset
4. **Live music market entry** — competing with ticketing platforms using superior fan data
5. **Anti-scalper positioning** — verified fan data as a tool to fight bots and secondary market inflation

---

## 4. Stakeholder Map

### Primary Stakeholders (High Influence)

| Stakeholder | Role | Primary Goal | Key Question They Need Answered |
|---|---|---|---|
| Spotify Product Team | Internal — decision maker | Drive Premium retention and growth | Does Reserved reduce churn? Which artists should be prioritised first? |
| Spotify Live Events Team | Internal — feature owner | Scale Reserved to more artists and markets | How do we score eligibility fairly across small and large artists? |
| Live Nation / Ticketers | Partner — revenue stakeholder | Fill venues with high-spending genuine fans | Does Reserved reduce scalper inventory on secondary markets? |

### Secondary Stakeholders (Medium Influence)

| Stakeholder | Role | Primary Goal | Key Question They Need Answered |
|---|---|---|---|
| Artists & Managers | External — beneficiary | Ensure real fans attend shows | Will Reserved work for mid-size and indie artists, not just stadium acts? |
| Spotify Premium Subscribers | End user — the fan | Get tickets to see their favourite artists | Am I actually eligible? How do I improve my chances? |
| Music Labels (e.g. UMG, Sony) | External — content partner | Maximise artist revenue and fan engagement | Does Reserved increase overall tour revenue for their roster? |

### Tertiary Stakeholders (Lower Influence)

| Stakeholder | Role | Primary Goal | Key Question They Need Answered |
|---|---|---|---|
| Spotify Investors | Financial — growth focus | Revenue growth and margin improvement | Does Reserved accelerate path to 1B subscribers by 2030? |
| Venues (arenas, theatres) | Commercial — operational | Higher fill rates, lower no-shows | Do Reserved fans show up and spend more in-venue? |
| Independent Artists | External — underserved | Access to Reserved for smaller tours | Is Reserved only for major label / major management acts? |

---

## 5. Research Questions

These are the 7 core business questions this analysis answers. Every chart, model, and dashboard deliverable maps back to one of these questions.

---

**Q1 — Eligibility model**
> *What listening behaviours most strongly predict superfan status, and how should Spotify weight each signal in its scoring model?*

This drives feature selection for the scoring model — streams, saves, shares, playlist adds, repeat listens, discography breadth, follow date. Understanding which signals matter most (and how to combine them into a composite score) is the analytical foundation of Reserved.

---

**Q2 — Experience gap**
> *Beyond guaranteed ticket access, how could Spotify deepen the Reserved experience to create genuine superfan moments before, during, and after the concert?*

Reserved currently ends at ticket purchase. This question identifies product enhancements — exclusive content, priority entry, post-show memory capsules — that would strengthen the feature's Premium retention value.

---

**Q3 — Fairness & bias risks**
> *What structural unfairnesses exist in a streaming-signal-based eligibility model, and how might real fans be excluded despite genuine fandom?*

Six risk dimensions are analysed: bot streaming farms, algorithm opacity, geographic inequity, recency bias, supply-demand gap at scale, and off-platform fandom blindspots.

---

**Q4 — Data architecture**
> *How does Spotify collect, aggregate, and score the behavioural signals that define a superfan, and what are the data quality risks in each signal category?*

This maps the data engineering behind the feature: play events, engagement events, social events, location data, and bot detection signals — and how each one can be approximated using public Spotify API data.

---

**Q5 — A-list scale stress test**
> *How does the Reserved model perform when fan population exceeds seat capacity by 100x or more, as it does for artists like BTS, The Weeknd, or Beyoncé?*

For a 60,000-seat stadium act with 20 million+ monthly listeners, Reserved allocation becomes a 300:1 competition. This question analyses whether the scoring model remains fair and meaningful at extreme scale, and proposes mechanisms (regional quotas, loyalty rotation) to address the gap.

---

**Q6 — App usage and retention impact**
> *Does receiving a Reserved offer correlate with increased Spotify engagement and improved 90-day Premium subscriber retention compared to a control group?*

The retention hypothesis — simulated as an A/B test framework. If Reserved drives even a 3–5% improvement in 90-day retention among eligible fans, the business case for continued investment is strong.

---

**Q7 — Ticket and venue economics**
> *What is the projected revenue uplift for artists, venues, and Spotify if Reserved improves venue fill rates and reduces secondary market ticket inflation?*

Financial impact modelling: combining venue fill rates, in-venue spend per fan, secondary market displacement, and Premium conversion uplift into a single revenue model across a simulated 50-date world tour.

---

## 6. KPI Framework

### Category 1 — Eligibility & Reach KPIs

| KPI | Definition | Formula | Target Benchmark |
|---|---|---|---|
| Superfan identification rate | % of an artist's Premium listeners who qualify as superfans under the scoring model | `superfans identified / total Premium listeners per artist × 100` | 3–8% per artist |
| Reserved offer volume | Total number of Reserved offers sent per artist per tour date | `eligible superfans × allocation rate per show` | Varies by venue size |
| Geographic coverage rate | % of tour markets where at least 500 superfans are identifiable | `tour markets with 500+ superfans / total tour markets × 100` | >80% |

### Category 2 — Conversion & Engagement KPIs

| KPI | Definition | Formula | Target Benchmark |
|---|---|---|---|
| Reserved offer acceptance rate | % of fans who receive a Reserved notification and complete a purchase in the window | `tickets purchased / Reserved offers sent × 100` | 35–55% |
| Window utilisation rate | % of reserved tickets purchased before window closes | `tickets sold in window / total reserved tickets allocated × 100` | >70% |
| Post-offer engagement delta | Change in Spotify engagement score for fans who received an offer vs 30 days prior | `avg engagement score (post-offer, 30d) − avg engagement score (pre-offer, 30d)` | Positive uplift |

### Category 3 — Retention & Premium KPIs

| KPI | Definition | Formula | Target Benchmark |
|---|---|---|---|
| 90-day Premium retention (offer group vs control) | Retention rate difference between Reserved offer recipients vs matched non-recipients | `retention rate (offer group, 90d) / retention rate (control group, 90d)` | Offer group ≥5% higher |
| Premium upgrade rate (Reserved-driven) | Free-to-Premium conversions attributed to Reserved awareness or marketing | `new Premium subs citing Reserved / total new Premium subs in period × 100` | Tracked quarterly |
| Superfan engagement score delta | Change in engagement score for fans after concert attendance vs before | `avg score (post-concert, 60d) − avg score (pre-concert, 60d)` | Positive uplift expected |

### Category 4 — Revenue & Business Impact KPIs

| KPI | Definition | Formula | Target Benchmark |
|---|---|---|---|
| Ticket revenue attributable to Reserved | Total face-value revenue from Reserved window purchases | `tickets sold via Reserved × avg ticket face value` | Tracked per tour |
| In-venue spend uplift (superfan vs general) | Average spend per head at venue (merch, food, upgrades) for Reserved vs general fans | `avg spend (Reserved fan) / avg spend (general admission fan)` | Hypothesis: Reserved fans spend 20–30% more |
| Secondary market displacement rate | % reduction in resale listings for Reserved tours vs comparable non-Reserved tours | `% resale listings (Reserved tour) vs % resale listings (control tour)` | Target: meaningful reduction |
| Revenue impact of retention uplift | Estimated incremental ARR from improved retention driven by Reserved | `293M subs × $10.99/month × retention uplift % × 12` | Even 1% = ~$386M ARR |

---

## 7. Project Scope

### In Scope

- Superfan scoring model using public Spotify API and Kaggle datasets
- Artist segmentation across mainstream, indie, and legacy categories
- Ticket conversion rate simulation (based on modelled assumptions)
- Premium retention impact hypothesis (A/B test framework simulation)
- Fairness and bias analysis of the scoring model
- Financial impact model (revenue uplift simulation)
- Executive dashboard with KPI recommendations
- Product enhancement recommendations for Reserved v2.0

### Out of Scope

- Spotify internal clickstream data (not publicly accessible)
- Real user-level behavioural data (privacy restriction)
- Artist royalty implications of Reserved
- International market regulatory analysis (GDPR, data privacy)
- Real-time Reserved ticket allocation system design
- Live Nation's internal ticketing economics

### Constraints

- All analysis uses **publicly available proxy data** — Spotify Charts, Kaggle datasets, Spotify Web API
- The superfan scoring model is a **simulation**, not Spotify's actual proprietary algorithm
- Financial projections are **modelled estimates** based on published Spotify figures and industry benchmarks
- No access to actual Reserved offer or conversion data (feature launched May 2026)

---

## 8. Data Availability Assessment

| Data needed | Source | Availability | Quality | Proxy used if unavailable |
|---|---|---|---|---|
| Track-level stream counts | Spotify Charts (charts.spotify.com) | Public, weekly CSV | Good | Weekly Top 200 by country |
| Artist-level audio features | Spotify Web API (`/audio-features`) | Free API access | High | Direct API pull |
| Artist popularity score (0–100) | Spotify Web API (`/artists/{id}`) | Free API access | High | Direct API pull |
| Artist follower counts | Spotify Web API (`/artists/{id}`) | Free API access | High | Direct API pull |
| Track-level engagement (saves, shares) | Internal Spotify data only | Not public | N/A | Playlist count from API as proxy |
| User-level listening history | Internal Spotify data only | Not public | N/A | Aggregate engagement score constructed from API signals |
| Premium subscriber demographics | Spotify quarterly reports | Public (aggregate only) | Medium | Published investor relations data |
| Ticket resale market prices | Viagogo / StubHub public listings | Partially public | Medium | Manual sample collection |
| Venue capacity data | Setlist.fm, Wikipedia | Public | Good | Direct lookup |
| Concert tour dates | Songkick / Bandsintown public API | Free API access | High | Direct API pull |

**Data gap strategy:** Where internal Spotify data is unavailable, composite proxy scores are constructed from available API signals and clearly documented in the assumptions log. All proxy constructions are transparent, reproducible, and explicitly flagged in the analysis.

---

## 9. Assumptions Log

Every assumption made in this project is documented here. This is standard practice in professional data analysis — it ensures reproducibility, intellectual honesty, and makes the analysis defensible in a stakeholder review.

| # | Assumption | Justification | Risk if wrong | Impact level |
|---|---|---|---|---|
| A1 | Spotify Charts weekly stream counts are a proportional proxy for total listener engagement per track | Charts are published directly by Spotify; represent the highest-engagement tracks | May underweight casual listeners who stream outside the Top 200 | Medium |
| A2 | Artist popularity score (0–100 from API) correlates positively with total fan base size | Spotify defines this score based on play counts and recency across all tracks | High popularity ≠ deep loyalty; a viral track inflates score temporarily | Medium |
| A3 | The top 5% of listeners by composite engagement score represents the superfan tier | Based on Pareto principle — in most engagement distributions, top 5% drive disproportionate activity | True superfan threshold may vary significantly by genre and artist type | High |
| A4 | A 35–55% Reserved offer acceptance rate is a reasonable baseline | Based on analogous pre-sale acceptance rates from Verified Fan programmes (Ticketmaster data, 2019–2023) | Actual rate could be higher (superfan motivation) or lower (friction in purchase flow) | High |
| A5 | Superfan fans spend approximately 20–30% more per head at venues than general admission fans | Based on concert industry research on fan engagement vs in-venue spend correlation | Spending patterns vary significantly by genre, venue type, and market | Medium |
| A6 | Bot streaming farms represent <5% of total streams for most artists, rising to ~15% for commercially targeted A-list acts | Based on published reports from Spotify and music industry analysts on streaming fraud rates | Could be higher for Reserved-targeted artists given the new financial incentive | High |
| A7 | A Reserved offer improves 90-day Premium retention by approximately 5–8% vs control group | Modelled from analogous loyalty programme research (credit card, subscription services) | Actual effect could be much smaller if fans cancel after the concert | High |
| A8 | 3–8% of a given artist's Premium listeners qualify as superfans under a reasonable scoring model | Constructed from fan engagement distribution patterns in public music industry research | Percentage varies widely — smaller artists may have higher superfan ratios; larger artists lower | Medium |
| A9 | Geographic proximity is defined as within 150km of a tour date venue | Standard industry definition for "local market" in concert discovery features | Fans routinely travel further for major artists; this threshold is conservative | Low |
| A10 | Spotify's scoring algorithm weights full-song plays and playlist saves most heavily | Stated in Spotify's public Reserved announcement; specific weights are proprietary | Actual weighting could prioritise different signals — share activity, search queries, etc. | Medium |

---

## 10. Stakeholder Briefing Email

*This fictional email demonstrates the ability to communicate analysis plans to non-technical business stakeholders — a critical skill for business analysts.*

---

**To:** Rene Volker, Head of Live Events, Spotify  
**From:** [Your Name], Data Analyst  
**Subject:** Reserved Feature — Analytical Framework & Proposed KPI Dashboard  
**Date:** May 23, 2026

---

Hi Rene,

Following the Reserved announcement at Investor Day on Thursday, I wanted to share the analytical framework I'm building to help measure and improve the feature's performance as it scales this summer.

**What I'm analysing:**

Over the next four weeks, I'll be building three connected pieces of work:

1. A **superfan scoring model** — a transparent, data-driven model that maps the listening signals (streams, saves, shares, playlist adds, discography breadth) that predict superfan eligibility. This will help your team understand what the algorithm is rewarding and identify any gaps.

2. An **artist segmentation analysis** — grouping artists into tiers (developing, mid-size, mainstream, A-list stadium) and stress-testing how the scoring model performs at each scale. The A-list stress test is particularly important: for an artist with 20M+ monthly listeners touring 60,000-seat venues, Reserved allocation becomes a 300:1 competition even among eligible superfans.

3. A **Reserved KPI dashboard** — an executive-level dashboard tracking the six metrics that matter most for reporting Reserved's impact to leadership: offer acceptance rate, 90-day Premium retention uplift, revenue attributable to Reserved, secondary market displacement, superfan identification rate, and post-concert engagement delta.

**One finding I want to flag early:**

The current Reserved experience ends at ticket purchase. Based on my initial research, there is a significant opportunity to extend the value — pre-show exclusive content, priority entry lanes, post-concert memory features — that would strengthen the Premium retention case and give your team a clear product roadmap for Reserved v2.0.

I'll have a full draft of findings and the dashboard ready for review in four weeks. Happy to sync before then if it would be useful.

Best,  
[Your Name]

---

## Document History

| Version | Date | Author | Changes |
|---|---|---|---|
| v1.0 | May 2026 | [Your Name] | Initial draft — all 7 sections complete |

---

*This document is part of the Spotify Reserved Analysis portfolio project. All data used is publicly available. This project is not affiliated with or endorsed by Spotify AB.*
