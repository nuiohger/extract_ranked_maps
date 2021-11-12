#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="This is playlist parser for extrating ranked maps.")

parser.add_argument('input_beatmap_path', help='input beatmap folder path')
parser.add_argument('input_ranked_path', help='input current ranked playlist path')
parser.add_argument('output_path', help='output extracted playlist path')

default_playlist = 'default_playlist.json'

import json
import jsbeautfiier

def get_file_data(path):
    with open(path, 'rb') as f:
        data = f.read()
        return data

def get_playlist(path):
    playlist_data = get_file_data(path)
    playlist_json_data = json.loads(paylist_data)

def main():
    

if __name__ == '__main__':
    main()