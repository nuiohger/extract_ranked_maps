# 説明
既存のマップリストから、ランク用マップだけを抽出してプレイリストを作るやつ

# 使い方
```
usage: playlistparse.py [-h] [--input_beatmap_path INPUT_BEATMAP_PATH] [--input_ranked_path INPUT_RANKED_PATH]
                        output_path

This is playlist parser for extrating ranked maps.

positional arguments:
  output_path           output extracted playlist path

optional arguments:
  -h, --help            show this help message and exit
  --input_beatmap_path INPUT_BEATMAP_PATH
                        input beatmap folder path
  --input_ranked_path INPUT_RANKED_PATH
                        input current ranked playlist path
```

rankedのプレイリストは　ここから取ってくる https://www.beatsavior.io/
か
ここから ranked_allを取ってくる　https://github.com/aplulu/bs-ranked-playlist/releases
またはここから　https://scoresaber.balibalo.xyz/playlist-maker