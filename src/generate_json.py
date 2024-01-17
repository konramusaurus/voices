import json
import urllib.parse
from pathlib import Path

def main():
    dir_assets = Path(__file__).parents[1] / Path('assets')
    repository_url = 'https://raw.githubusercontent.com/konramusaurus/voices/main/'

    data = dict()
    formed_data = dict()

    for voice in sorted(dir_assets.glob('**/*.mp3')):
        voice_path = str(voice).replace('/workspaces/voices/', '')
        voice_file = voice_path.split('/')[-1]
        voice_dir = voice_path.split('/')[-2]

        voice_file_tokens = voice_file.split('_')
        voice_dir_tokens = voice_dir.split('_')

        title = voice_dir_tokens[1]

        if title not in data:
            data[title] = {
                "title": title,
                "publish_date": voice_dir_tokens[0],
                "video_url": f'https://www.youtube.com/watch?v={voice_dir_tokens[-1]}',
                "voices": [],
            }
        
        voice_slug_and_tags = "_".join(voice_file_tokens[1:])
        
        data[title]["voices"].append(
            {
                "slug": ''.join(voice_slug_and_tags.split(']')[1:]).replace('.mp3', ''),
                "voice_url": repository_url + urllib.parse.quote(voice_path.encode()),
                "tags": voice_slug_and_tags.replace('[', '').split(']')[0].split(','),
            }
        )
    
    formed_data = [value for _, value in data.items()]
    with Path(dir_assets.parent / Path('index.json')).open('w') as f:
        json.dump(formed_data, f, indent=2)


if __name__ == '__main__':
    main()