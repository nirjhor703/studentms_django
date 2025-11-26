import io
from django.shortcuts import render
from django.http import StreamingHttpResponse, Http404
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import os

# --- Google Drive API setup ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'videos', 'service-account.json')
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build('drive', 'v3', credentials=credentials)

# --- Views ---

def video_list(request):
    """
    List all videos from Google Drive.
    """
    try:
        results = service.files().list(
            pageSize=50,
            fields="files(id, name, mimeType, createdTime)"
        ).execute()
        videos = results.get('files', [])
    except Exception as e:
        print(f"Error fetching videos: {e}")
        videos = []

    return render(request, 'videos/video_list.html', {'videos': videos})


def watch_video(request, file_id):
    """
    Watch video embedded from Google Drive.
    """
    try:
        file = service.files().get(fileId=file_id, fields="name, mimeType").execute()
        embed_url = f"https://drive.google.com/file/d/{file_id}/preview"
        return render(request, 'videos/watch_video.html', {
            "embed_url": embed_url,
            "file_name": file['name']
        })
    except Exception as e:
        print(f"Error fetching file: {e}")
        raise Http404("Video not found")


def download_video(request, file_id):
    """
    Stream download from Google Drive with correct filename.
    """
    try:
        file = service.files().get(fileId=file_id, fields="name, mimeType").execute()
        request_file = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request_file)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        fh.seek(0)

        response = StreamingHttpResponse(fh, content_type=file['mimeType'])
        response['Content-Disposition'] = f'attachment; filename="{file["name"]}"'
        return response
    except Exception as e:
        print(f"Error downloading file: {e}")
        raise Http404("Video not found")
