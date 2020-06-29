import json
import requests
import pdb
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl

from spotify_secrets import SPOTIFY_USER_ID,spotify_token

class CreatePlaylist:
    youtube_playlist_id = "PLk0vAs4YY3u_tlo96dpuVeHb9oex3a1NJ"
    all_youtube_song_info = {}

    def _init_(self):
        pass

    def get_youtube_videos(self, playlist = youtube_playlist_id):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes="https://www.googleapis.com/auth/youtube.readonly")
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId= playlist
        )
        response = request.execute()
        return response

    def get_liked_videos(self):
        pass

    def create_spotify_playlist(self):
        request_body = json.dumps({
            "name": "Youtube To Spotify Conversion",
            "description": "This is a conversion list of all songs from Youtube playlist",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(SPOTIFY_USER_ID)
        post = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = post.json()
        return response_json["id"]##reference newly created playlist id

    def get_song_in_spotify(self,song_name,artist):
        query = 'https://api.spotify.com/v1/search?q=track%3A{}+artist%3A{}&type=track&offset=0&limit=50'.format(song_name, artist)
        get = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = get.json()
        songs = response_json["tracks"]["items"]
        uri = songs[0]["uri"]

        return uri


    def add_songs_to_playlist(self):
        self.get_youtube_videos()



if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_songs_to_playlist()