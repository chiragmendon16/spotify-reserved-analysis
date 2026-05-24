import os
import pandas as pd
import numpy as np

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

ARTISTS = [
    {'id': '1Xyo4u8uXC1ZmMpatF05PJ', 'name': 'The Weeknd',       'tier': 'A-List Stadium'},
    {'id': '3TVXtAsR1Inumwj472S9r4', 'name': 'Drake',             'tier': 'A-List Stadium'},
    {'id': '06HL4z0CvFAxyc27GXpf02', 'name': 'Taylor Swift',      'tier': 'A-List Stadium'},
    {'id': '6l3HvQ5sa6mXTsMTB19rO5', 'name': 'J. Cole',           'tier': 'A-List Stadium'},
    {'id': '6eUKZXaKkcviH0Ku9w2n3V', 'name': 'Ed Sheeran',        'tier': 'A-List Stadium'},
    {'id': '246dkjvS1zLTtiykXe5h60', 'name': 'Post Malone',       'tier': 'Mainstream'},
    {'id': '7tYKF4w9nC0nq9CsPZTHyP', 'name': 'SZA',               'tier': 'Mainstream'},
    {'id': '6M2wZ9GZgrQXHCFfjv46we', 'name': 'Doja Cat',           'tier': 'Mainstream'},
    {'id': '4q3ewBCX7sLwd24euuV69X', 'name': 'Bad Bunny',          'tier': 'Mainstream'},
    {'id': '6KImCVD70vtIoJWnq6nGn3', 'name': 'Harry Styles',       'tier': 'Mainstream'},
    {'id': '1McMsnEElThX1knmY4oliG', 'name': 'Olivia Rodrigo',    'tier': 'Mainstream'},
    {'id': '5K4W6rqBFWDnAN6FQUkS6x', 'name': 'Kanye West',        'tier': 'Mainstream'},
    {'id': '4dpARuHxo51G3z768sgnrY', 'name': 'Adele',              'tier': 'Mainstream'},
    {'id': '4LLpKhyESsyAXpc4laK94U', 'name': 'Steve Lacy',        'tier': 'Mid-Size'},
    {'id': '738wLrAtLtCtFqdk3lAkpQ', 'name': 'Omar Apollo',       'tier': 'Mid-Size'},
    {'id': '2FXC3k01G6Gw61bmprjgqS', 'name': 'Arlo Parks',        'tier': 'Mid-Size'},
    {'id': '45eNHdiiAjOwp6L4D4228I', 'name': 'Conan Gray',        'tier': 'Mid-Size'},
    {'id': '5LHRHt1k9lMyONurDHEdrp', 'name': 'Tame Impala',       'tier': 'Mid-Size'},
    {'id': '3WGpXCj9YhhfX11TToZcXP', 'name': 'Remi Wolf',         'tier': 'Mid-Size'},
    {'id': '7Hjbimq43OgxaBRpFXic4x', 'name': 'Phoebe Bridgers',   'tier': 'Mid-Size'},
    {'id': '3nFkdlSjzX9mRTtwJOb70',  'name': 'Rex Orange County', 'tier': 'Mid-Size'},
    {'id': '7sfl4Xt5KmfyDs2T3SVSMK', 'name': 'Lil Uzi Vert',      'tier': 'Mid-Size'},
    {'id': '0Y5tJX1MQlPlqiwlOH1tJY', 'name': 'Travis Scott',      'tier': 'Mid-Size'},
    {'id': '4NZvixzsSefsNiIqXn0NDe', 'name': 'Faye Webster',      'tier': 'Developing'},
    {'id': '0c173mlxpT3ui454x5F8mR', 'name': 'Maude Latour',      'tier': 'Developing'},
    {'id': '3CZqomH6KpJZBqQGzMqDh4', 'name': 'Samia',             'tier': 'Developing'},
    {'id': '1ASIN6bRNMnkSq8J1F9S4r', 'name': 'Mk.gee',            'tier': 'Developing'},
    {'id': '0YrpP0JTNKlbON61fOqI2k', 'name': 'Ethel Cain',        'tier': 'Developing'},
    {'id': '5a2EaR3hamoenG9rDuLzsL', 'name': 'Gracie Abrams',     'tier': 'Developing'},
    {'id': '4NZvixzsSefsNiIqXn0NDe2', 'name': 'Faye Webster',      'tier': 'Developing'},
]

np.random.seed(42)

# Generate Artists Profile
artist_profiles = []
for a in ARTISTS:
    if a['tier'] == 'A-List Stadium':
        followers = np.random.randint(50_000_000, 100_000_000)
        pop = np.random.randint(90, 100)
    elif a['tier'] == 'Mainstream':
        followers = np.random.randint(10_000_000, 50_000_000)
        pop = np.random.randint(80, 90)
    elif a['tier'] == 'Mid-Size':
        followers = np.random.randint(1_000_000, 10_000_000)
        pop = np.random.randint(65, 80)
    else:
        followers = np.random.randint(200_000, 1_000_000)
        pop = np.random.randint(50, 65)
        
    artist_profiles.append({
        'artist_id': a['id'],
        'name': a['name'],
        'tier': a['tier'],
        'followers': followers,
        'popularity': pop,
        'genres': 'pop, indie pop',
        'primary_genre': 'pop',
        'spotify_url': f"https://open.spotify.com/artist/{a['id']}"
    })

df_artists = pd.DataFrame(artist_profiles).drop_duplicates('artist_id')

# Generate Tracks
all_tracks = []
for idx, row in df_artists.iterrows():
    for i in range(10):
        tid = f"track_{row['artist_id']}_{i}"
        all_tracks.append({
            'artist_id': row['artist_id'],
            'artist_name': row['name'],
            'tier': row['tier'],
            'track_id': tid,
            'track_name': f"{row['name']} Hit {i+1}",
            'album_name': f"{row['name']} Album",
            'release_date': f"202{np.random.randint(0,6)}-01-01",
            'popularity': max(0, row['popularity'] - np.random.randint(0, 20)),
            'duration_ms': np.random.randint(180_000, 250_000),
            'explicit': bool(np.random.choice([True, False], p=[0.3, 0.7]))
        })
df_tracks = pd.DataFrame(all_tracks)

# Generate Audio Features
AUDIO_COLS = ['danceability','energy','key','loudness','mode','speechiness',
              'acousticness','instrumentalness','liveness','valence','tempo','time_signature']
audio_raw = []
for tid in df_tracks['track_id']:
    audio_raw.append({
        'track_id': tid,
        'danceability': np.clip(np.random.normal(0.6, 0.15), 0, 1),
        'energy': np.clip(np.random.normal(0.65, 0.2), 0, 1),
        'key': np.random.randint(0, 12),
        'loudness': np.clip(np.random.normal(-6, 2), -60, 0),
        'mode': np.random.choice([0, 1]),
        'speechiness': np.clip(np.random.normal(0.1, 0.05), 0, 1),
        'acousticness': np.clip(np.random.normal(0.3, 0.2), 0, 1),
        'instrumentalness': np.clip(np.random.normal(0.05, 0.1), 0, 1),
        'liveness': np.clip(np.random.normal(0.2, 0.1), 0, 1),
        'valence': np.clip(np.random.normal(0.5, 0.2), 0, 1),
        'tempo': np.clip(np.random.normal(120, 20), 60, 200),
        'time_signature': 4
    })
df_audio = pd.DataFrame(audio_raw)
df_tracks_enriched = df_tracks.merge(df_audio, on='track_id', how='left')

# Generate Listener Pool (exact logic from notebook)
SIGNAL_WEIGHTS = {
    'repeat_play_rate':       0.30,
    'playlist_save_rate':     0.25,
    'share_rate':             0.15,
    'discography_breadth':    0.15,
    'follow_tenure_months':   0.10,
    'concert_page_views':     0.05,
}

N = 1000
def simulate_listeners(artist_row, n=N):
    pop_factor = artist_row['popularity'] / 100
    records = []
    for idx in range(n):
        repeat_play_rate    = np.clip(np.random.beta(2, 3 + pop_factor * 4), 0, 1)
        playlist_save_rate  = np.clip(np.random.beta(1.5, 4), 0, 1)
        share_rate          = np.clip(np.random.beta(1, 8), 0, 1)
        discography_breadth = np.clip(np.random.beta(2, 5), 0, 1)
        follow_tenure_raw   = np.clip(np.random.exponential(18 + pop_factor * 24), 0, 120)
        follow_tenure_norm  = follow_tenure_raw / 120
        concert_views       = np.random.poisson(1.5)
        concert_views_norm  = np.clip(concert_views / 20, 0, 1)

        raw = (
            repeat_play_rate    * SIGNAL_WEIGHTS['repeat_play_rate'] +
            playlist_save_rate  * SIGNAL_WEIGHTS['playlist_save_rate'] +
            share_rate          * SIGNAL_WEIGHTS['share_rate'] +
            discography_breadth * SIGNAL_WEIGHTS['discography_breadth'] +
            follow_tenure_norm  * SIGNAL_WEIGHTS['follow_tenure_months'] +
            concert_views_norm  * SIGNAL_WEIGHTS['concert_page_views']
        )
        records.append({
            'artist_id':            artist_row['artist_id'],
            'artist_name':          artist_row['name'],
            'tier':                 artist_row['tier'],
            'artist_popularity':    artist_row['popularity'],
            'artist_followers':     artist_row['followers'],
            'listener_id':          f"{artist_row['artist_id']}_{idx:04d}",
            'repeat_play_rate':     round(repeat_play_rate, 4),
            'playlist_save_rate':   round(playlist_save_rate, 4),
            'share_rate':           round(share_rate, 4),
            'discography_breadth':  round(discography_breadth, 4),
            'follow_tenure_months': round(follow_tenure_raw, 1),
            'concert_page_views':   concert_views,
            'superfan_score':       round(raw * 100, 2),
        })
    return records

all_listeners = []
for _, row in df_artists.iterrows():
    all_listeners.extend(simulate_listeners(row))

df_listeners = pd.DataFrame(all_listeners)

# Apply Reserved Eligibility
RESERVED_PERCENTILE = 95
thresholds = df_listeners.groupby('artist_id')['superfan_score'].quantile(RESERVED_PERCENTILE/100).reset_index()
thresholds.columns = ['artist_id', 'reserved_threshold']
df_listeners = df_listeners.merge(thresholds, on='artist_id', how='left')
df_listeners['reserved_eligible'] = df_listeners['superfan_score'] >= df_listeners['reserved_threshold']

df_eligible = df_listeners[df_listeners['reserved_eligible']].copy()

# Save everything
df_artists.to_csv('data/raw/artists_raw.csv', index=False)
df_tracks.to_csv('data/raw/top_tracks_raw.csv', index=False)
df_tracks_enriched.to_csv('data/raw/audio_features_raw.csv', index=False)
df_listeners.to_csv('data/raw/listener_pool_raw.csv', index=False)

df_artists.to_csv('data/processed/artists_clean.csv', index=False)
df_tracks_enriched.to_csv('data/processed/tracks_audio_features_clean.csv', index=False)
df_listeners.to_csv('data/processed/listener_pool_clean.csv', index=False)
df_eligible.to_csv('data/processed/reserved_eligible_listeners.csv', index=False)

print("Mock data generated and saved successfully!")
