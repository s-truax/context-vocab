import csv
import os
import shutil
import sys
import requests

AUDIO_DIRECTORY = './extras/audio'
ANKI_MEDIA_DIR = 'C:/Users/sam/AppData/Roaming/Anki2/User 1/collection.media'

def download_mp3s(audio_ids,
                 audio_url_template='https://tatoeba.org/audio/download/{0}',
                 audio_directory=AUDIO_DIRECTORY):
    
    for a_id in audio_ids:
        request_url = audio_url_template.format(a_id)
        mp3data_request = requests.get(request_url)
        mp3data = mp3data_request.content
        with open(f'{audio_directory}/{a_id}.mp3', 'wb') as mp3file:
            mp3file.write(mp3data)

if __name__ == "__main__":
    
    tsv_filename = sys.argv[1]

    # get the audio files that already exit
    audio_files = os.listdir('./extras/audio')

    old_audio_ids = [os.path.splitext(f)[0] for f in audio_files]

    with open(tsv_filename, newline='', encoding='utf-8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        header = next(reader)
        idx = header.index('tatoeba audio id')
        new_audio_ids = [r[idx] for r in reader if r[idx]]

    to_download = [x for x in new_audio_ids if x not in old_audio_ids]
    if not to_download:
        print("No new audio files to download")

    download_mp3s(to_download)

    if sys.argv[2] == '--update-media':
        new_mp3s = [x + ".mp3" for x in to_download]
        for mp3file in new_mp3s:
            shutil.copy2(f'./extras/audio/{mp3file}', ANKI_MEDIA_DIR)




