# YoutubeToSpotifyPlaylistConversion
This application converts a chosen youtube playlist into a spotify playlist

So far, only the following functions are fleshed out and fully functional in the main program file (CreatePlaylist.py):

   * get_youtube_videos()
   * create_spotify_playlist()
   * get_song_in_spotify()
    
All functions listed have been individually tested and work correctly.  

## Local Setup

Run:

       pip install -r requirements.txt

To install all dependancies.

-------------------------------------------------------------------------------------

Before being able to run the program you will need to populate the secrets in the the 2 given secret files

* client_secret_template (Secrets file containing google/youtubes credentials)
* spotify_secrets_template (Secrest file containing spotify secrets)

###Follow the guides below for indepth instructions as to how to get Spotify and Youtube Credentials:

1. Spotify Only needs Username & Bearer Token - [Oauth Portal](https://developer.spotify.com/console/post-playlists/)

2. Youtube Data API V3 [Setting Up API & Client Credentials](https://developers.google.com/youtube/v3/getting-started/)









    


