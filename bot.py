# Author: Laevos :3
# basically what im trying to do here is like
# list all the available anime
# prompt the user for either the dirname or maybe to make it
# easier, the first 8 chars of its md5sum.
import mpv
import re
import hashlib
import os

from fuzzywuzzy import process
from pathlib import Path as P
from pprint import pp

# Minimum Levenshtein distance for matching
MIN_LEV = 75

# right now we're just hardcoding this
# TODO: Let the user provide their anime directory
source_dir = str(P('~/Videos/anime/complete').expanduser())
filetypes = re.compile('.*\.(mkv|mp4|avi)')

# DEBUG
# pp(source_dir)

# Build a list of vids
try:
    titles = [title for title in os.listdir(source_dir) if os.path.isdir(f"{source_dir}/{title}")]
except Exception as e:
    print(f"Unable to read files in {source_dir}: {e}")
    exit(1)

# DEBUG
# pp(titles)

# build a hash matching each title to an md5sum
title_hash = {hashlib.md5(title.encode('utf-8')).hexdigest()[:8]: title for title in titles}

pp(title_hash, indent=4)

choice = None

# Try to figure out what title they want...
while choice is None:
    _ = input("Select a title: ")
    match = process.extract(_, title_hash.keys(), limit=1).pop()
    if match[1] < MIN_LEV:
        match = process.extract(_, title_hash.values(), limit=1).pop()
        if match[1] < MIN_LEV:
            print("sry :( we couldn't tell what you meant, try again...\n(Hint: enter the hash or name of a title)")
            continue
        choice = match[0]
        break
    choice = title_hash[match[0]]

print(f"Selected: {choice}")
# set up working directory and make a list the available video files
wd = P(f"{source_dir}/{choice}")
eps = sorted([ep for ep in wd.glob('**/*') if re.match(filetypes, str(ep))])

# Create an mpv player instance and play the directory starting from the episode specified

# TODO: sanitize this input
ep_num = input("Episode: ")

player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, ytdl=True)
player.title = '${media-title} - Bot by Laevos'
player.playlist_start = int(ep_num) - 1

pp(player.playlist_start)
pp(str(wd))
player.play(str(wd))
player.wait_until_playing()
print(player.filename)

from time import sleep
while not player.core_shutdown:
    sleep(1)

player.quit()
another = input("Watch something else? (y/n): ")

#TODO: if a directory has subdirectories, prompt the user to supply which one they want by running the same algorithm
