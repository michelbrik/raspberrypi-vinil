import spotipy
from spotipy.oauth2 import SpotifyOAuth
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def create_spotify_api_client():
    """
    Create spotify API client.

    :return: spotipy.Spotify.
    """
    api_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=getenv("CLIENT_ID"),
                                                           client_secret=getenv("CLIENT_SECRET"),
                                                           redirect_uri="http://localhost:8888/callback",
                                                           scope="user-read-playback-state,user-modify-playback-state"))
    return api_client


def transfer_to_device(client):
    """
    Transfer data to specific device.

    :param client: spotipy.Spotify.
    :return:
    """
    client.transfer_playback(device_id=getenv("DEVICE_ID"), force_play=True)


def play_song(client, song_ids):
    """
    Play song using spotify API client.

    :param client: spotipy.Spotify.
    :param song_ids: str.
    :return:
    """
    list_of_songs = [f'spotify:track:{song_id}' for song_id in song_ids]
    client.start_playback(device_id=getenv("DEVICE_ID"), uris=list_of_songs)


def main(song_id):
    """
    Main API caller function.

    :param song_id: list.
    :return:
    """
    client = create_spotify_api_client()
    transfer_to_device(client)
    play_song(client, song_id=song_id)
