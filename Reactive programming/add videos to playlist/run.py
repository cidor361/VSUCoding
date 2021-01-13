import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


CLIENT_SECRETS_FILE = 'client_secret_410963308212-p0k89bq504vdttevm6mvpp60jiga15jc.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

RATINGS = ('like', 'dislike', 'none')
VIDEO = 'b3OFazOMRC8'


# Authorization request and store authorization object.
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


# Execute like function and print result
def like_youtube_video(youtube, video_id):
    parser = argparse.ArgumentParser()
    parser.add_argument('--videoId', default=video_id,
                        help='ID of video to like.')
    parser.add_argument('--rating', default='like',
                        choices=RATINGS,
                        help='Indicates whether the rating is "like", "dislike", or "none".')
    args = parser.parse_args()

    try:
        youtube.videos().rate(
            id=args.videoId,
            rating=args.rating
        ).execute()
        #like_video(youtube, args)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    else:
        print ('The %s rating has been added for video ID %s.' %
               (args.rating, args.videoId))


def add_video_to_playlist(youtube, video_id, playlist_id):
    q = youtube.playlistItems().insert(
        part = "snippet",
        body = {
            'snippet': {
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
    ).execute()
    print('Video %s added to watch later playlist' %(video_id))


# TODO: create function to get new video from channel


youtube = get_authenticated_service()
like_youtube_video(youtube, VIDEO)
add_video_to_playlist(youtube, VIDEO, "WL")
