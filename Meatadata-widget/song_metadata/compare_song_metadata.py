#!/usr/bin/python
# -*- coding:utf-8 -*-

from fuzzywuzzy import fuzz


def __parse_duration(duration_text: str):
    d_list = duration_text.split(":")
    time = int(d_list[0]) * 60 + int(d_list[1])
    return time


def compare_song_info(song_info_1: dict, song_info_2: dict) -> int:
    print(song_info_1)
    print(song_info_2)
    if not song_info_1 or not song_info_2:
        return 0
    duration_1 = __parse_duration(song_info_1["duration"])
    duration_2 = __parse_duration(song_info_2["duration"])
    score_list = []
    if duration_1 and duration_2:
        if abs(duration_1 - duration_2) <= 1:
            score_list.append(100)
        elif abs(duration_1 - duration_2) <= 3:
            score_list.append(80)
        else:
            score_list.append(0)
    singer_score = fuzz.partial_ratio(song_info_1["singer"], song_info_2["singer"])
    name_score = fuzz.partial_ratio(song_info_1["songName"], song_info_2["songName"])
    score_list.extend([singer_score, name_score])
    if song_info_1["album"] and song_info_2["album"]:
        album_score = fuzz.partial_ratio(song_info_1["album"], song_info_2["album"])
        score_list.append(album_score)
    return sum(score_list) / len(score_list)




