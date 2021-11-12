#!/usr/bin/env python3

#define
default_playlist = 'default_playlist.json'
default_beatmap = 'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'
default_ranked_playlist = 'ranked_all'

import argparse
parser = argparse.ArgumentParser(description="This is playlist parser for extrating ranked maps.")

parser.add_argument('--input_beatmap_path', help='input beatmap folder path', default=default_beatmap)
parser.add_argument('--input_ranked_path', help='input current ranked playlist path')
parser.add_argument('output_path', help='output extracted playlist path')
args = parser.parse_args()

import json
import jsbeautifier
import hashlib
import os

class playlistHelper():
    def get_file_data(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            return data

    def get_json_data(self, path):
        file_data = self.get_file_data(path)
        file_json_data = json.loads(file_data)
        return file_json_data

class playlistEditor():
    def __init__(self, beatmap_path, ranked_playlist_path, output_path):
        self.ranked_playlist_path = ranked_playlist_path
        self.beatmap_path = beatmap_path
        self.output_path = output_path
        self.helper = playlistHelper()
        self.default_playlist = default_playlist
        self.beatmap_hash_list = self.__get_beatmap_hash_list()
        if(self.ranked_playlist_path):
            self.ranked_hash_list = self.__get_ranked_hash_list()
        else:
            self.default_ranked_playlist = default_ranked_playlist
            self.ranked_hash_list = self.__collect_ranked_hash_list()
        self.filterd_hash_list = self.__filter_beatmap_from_ranked_list()

    def __filter_beatmap_from_ranked_list(self):
        hash_list = []
        for beatmap_hash in self.beatmap_hash_list:
            if(beatmap_hash in self.ranked_hash_list): 
                hash_list.append({'hash' : beatmap_hash})
        return hash_list

    def __get_ranked_hash_list(self):
        hash_list = []
        ranked_playlist_json = self.helper.get_json_data(self.ranked_playlist_path)
        for obj in ranked_playlist_json['songs']:
            hash_list.append(obj['hash'].lower()) # set object
        return hash_list

    def __get_beatmap_hash_list(self):
        hash_list = []
        beatmap_dirs = []
        for beatmap_file in os.listdir(self.beatmap_path):
            if os.path.isdir(os.path.join(self.beatmap_path, beatmap_file)): # dir checker
                beatmap_dirs.append(os.path.join(self.beatmap_path, beatmap_file))
        for beatmap_dir in beatmap_dirs:
            metadata = self.__get_beatmap_hash(beatmap_dir)
            if(metadata):
                hash_list.append(metadata.lower())
        return hash_list

    #https://note.com/denpadokei/n/nf23eb568d4f1
    def __calc_metadata_hash(self, path):
        info_path = os.path.join(path, 'info.dat')
        info_json = self.helper.get_json_data(info_path)
        difficulty_files = [info_path]
        difficultyBeatmapSets_list = info_json['_difficultyBeatmapSets']
        for difficultyBeatmapSets in difficultyBeatmapSets_list:
            difficultyBeatmaps_list = difficultyBeatmapSets['_difficultyBeatmaps']
            for difficultyBeatmaps in difficultyBeatmaps_list:
                difficulty_files.append(os.path.join(path, difficultyBeatmaps['_beatmapFilename']))
        Message = b''
        print(difficulty_files)
        for difficulty_file in difficulty_files:
            Message += self.helper.get_file_data(difficulty_file)
        hash = hashlib.sha1(Message).hexdigest().lower()
        return hash

    def __get_beatmap_hash(self, path):
        metadata_path = os.path.join(path, 'metadata.dat')
        if not(os.path.isfile(metadata_path)):
            hash = self.__calc_metadata_hash(path)
            return hash
        metadata_json = self.helper.get_json_data(metadata_path)
        hash = metadata_json['hash']
        return hash

    def __collect_ranked_hash_list(self):
        hash_list = []
        playlist_files = []
        for playlist_file in os.listdir(self.default_ranked_playlist):
            if os.path.isfile(os.path.join(self.default_ranked_playlist, playlist_file)): # file checker
                playlist_files.append(os.path.join(self.default_ranked_playlist, playlist_file))
        for playlist_file in playlist_files:
            ranked_playlist_json = self.helper.get_json_data(playlist_file)
            for obj in ranked_playlist_json['songs']:
                hash_list.append(obj['hash'].lower()) # set object
        return hash_list

    def create_playlist(self):
        self.default_playlist_json = self.helper.get_json_data(self.default_playlist)
        self.default_playlist_json['songs'] = self.filterd_hash_list
        self.default_playlist_data = jsbeautifier.beautify(json.dumps(self.default_playlist_json))
        with open(self.output_path, 'wb') as f:
            f.write(self.default_playlist_data.encode())

def main():
    editor = playlistEditor(args.input_beatmap_path, args.input_ranked_path, args.output_path)
    editor.create_playlist()

if __name__ == '__main__':
    main()
