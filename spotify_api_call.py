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


def play_song(client, song_id, id_kind):
    """
    Play song using spotify API client.

    :param client: spotipy.Spotify.
    :param song_id: str.
    :param id_kind: str.
    :return:
    """
    client.start_playback(device_id=getenv("DEVICE_ID"), uris=[f'spotify:{id_kind}:{song_id}'])


def main(id_kind, song_id):
    """
    Main API caller function.

    :param id_kind: str.
    :param song_id: str.
    :return:
    """
    client = create_spotify_api_client()
    transfer_to_device(client)
    play_song(client, song_id=song_id, id_kind=id_kind)

main("album", "4sb0eMpDn3upAFfyi4q2rw")
