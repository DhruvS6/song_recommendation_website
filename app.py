import pickle

import spotipy
import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity

from spotipy import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="8f45ca9c640543a6b212b40054b7e591",
        client_secret="6ec4a6cc077a422f89d8ecee4e69c288"
    )
)
def recommend_songs(song_indx,df,audio_matrix,top_n=10):
    song = df.iloc[song_indx]

    target_genre = song['playlist_genre']
    target_artists = set(song['track_artist'])

    candidates = df[(df['playlist_genre']==target_genre) | (df['track_artist'].apply(lambda x: bool(target_artists & set(x))))]

    candidates = candidates.drop(index = song_indx,errors='ignore')

    if candidates.empty:
        return pd.DataFrame()

    candidate_idx = candidates.index.tolist()

    similarities = cosine_similarity(audio_matrix[song_indx].reshape(1,-1),
                                   audio_matrix[candidate_idx])[0]

    candidates = candidates.copy()
    candidates['similarity'] = similarities

    candidates["artist_boost"] = candidates["track_artist"].apply(
        lambda x: 1 if target_artists & set(x) else 0
    )
    candidates["genre_boost"] = (candidates["playlist_genre"] == target_genre).astype(int)

    candidates['final_score'] = (
        1 * candidates['similarity']
        + 0.9 * candidates['artist_boost']
        + 0.5 * candidates['genre_boost']
    )


    recommended_tracks = (
        candidates
        .sort_values("final_score", ascending=False)
        .head(top_n)["track_name"]
        .tolist()
    )
    return recommended_tracks


songs = pickle.load(open('songs.pkl','rb'))
song_names =songs['track_name'].values
audio_matrix = pickle.load(open('audio_mat.pkl','rb'))



st.title('Song Recommender System')

selected_song_name =st.selectbox(
    "Select your Song",
    song_names,
)
selected_song_index = songs.index[songs['track_name']==selected_song_name][0]
if st.button('Recommend'):
    names= recommend_songs(selected_song_index,songs,audio_matrix)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns([2,2,2,2,2,2,2,2,2,2])
    with col1:
        track_id = songs.loc[songs['track_name'] == names[0], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[0])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col2:
        track_id = songs.loc[songs['track_name'] == names[1], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[1])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col3:
        track_id = songs.loc[songs['track_name'] == names[2], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[2])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col4:
        track_id = songs.loc[songs['track_name'] == names[3], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[3])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col5:
        track_id = songs.loc[songs['track_name'] == names[4], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[4])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col6:
        track_id = songs.loc[songs['track_name'] == names[5], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[5])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col7:
        track_id = songs.loc[songs['track_name'] == names[6], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[6])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col8:
        track_id = songs.loc[songs['track_name'] == names[7], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[7])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col9:
        track_id = songs.loc[songs['track_name'] == names[8], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url,use_container_width=True)
        st.text(names[8])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")
    with col10:
        track_id = songs.loc[songs['track_name'] == names[9], "track_id"].iloc[0]
        track = sp.track(track_id)
        album_images = track["album"]["images"]
        album_cover_url = album_images[0]["url"]
        spotify_url = track["external_urls"]["spotify"]
        st.image(album_cover_url)
        st.text(names[9])
        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")