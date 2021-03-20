# anime-club-bot

A silly little discord bot that allows you to play series using libmpv. As of the time of writing, currently just a script containing the main logic, but we'll make this into a bot when we decide on a framework to use. ;P

## Requirements

anime-club-bot was built and tested on Python 3.9.2. It requires the following libraries:

### python-mpv

Python binding for `libmpv`. See https://github.com/jaseg/python-mpv/ for installation instructions.

### fuzzywuzzy

Used for matching title or hash name. See https://github.com/seatgeek/fuzzywuzzy for installation instructions.

### python-Levenshtein

Provides a more efficient Levenshtein distance algorithm to `fuzzywuzzy`. Not strictly required, but may affect search efficiency. See https://pypi.org/project/python-Levenshtein for installation instructions.
