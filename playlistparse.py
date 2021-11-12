#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="This is playlist parser for extrating ranked maps.")
# this is playlist_path
parser.add_argument('input_path', help='input playlist_path')
# this is extracted_ranked_playlist_output
parser.add_argument('output_path', help='output extracted playlist_path')

import json
import jsbeautfiier

def get_file(path):
    with open(path, 'rb') as f:
        data = f.read()
        return data

def get_playlist(path):
    playlist_data = get_file(path)
    playlist_json_data = json.loads(paylist_data)

def main():
    

if __name__ == '__main__':
    main()