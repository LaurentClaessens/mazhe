"""Some generic utilities."""

import sys
import time
import math
import json
import string
import random
import datetime
import contextlib
from pathlib import Path

from colorama import Fore, Style
_ = sys


dprint = print


class ColorPrint:
    """Print in color."""

    def __init__(self, color):
        """Initialize."""
        self.color = color

    def __enter__(self):
        """Initiate the color."""
        color_to_fore = {}
        try:
            fore_color = color_to_fore[self.color]
        except KeyError:
            fore_color = getattr(Fore, self.color.upper())
        print(fore_color, end="")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        _ = exc_type, exc_value, exc_traceback
        print(Style.RESET_ALL, end="")


def human_duration(duration):
    """Write a human readable duration (in seconds)"""
    hours = int(duration // 3600)
    minutes = int(duration // 60 % 60)
    seconds = int(duration % 60)
    return f"{hours}h{minutes}m{seconds}s"


def random_string(length):
    """Return a random string of letters of the given length."""
    rn_list = [random.choice(string.ascii_letters) for _ in range(1, length)]
    return "".join(rn_list)


def human_timestamp(now=None, format_str=None):
    """Return a human readable timestamp."""
    if now is None:
        now = time.time()
    if format_str is None:
        format_str = "%Z - %A  %Y/%B/%d, %H:%M:%S"
    local_time = time.localtime(now)
    return time.strftime(format_str, local_time)


def json_serial(obj):
    """Serialize the datetime."""
    if isinstance(obj, datetime.datetime):
        timestamp = obj.timestamp()
        return human_timestamp(timestamp)
    with contextlib.suppress(AttributeError):
        return obj.to_json()
    return str(obj)


def print_json(json_dict, pretty=True):
    """Print the json"""
    str_json = json_to_str(json_dict, pretty=pretty)
    print(str_json)


def json_to_str(json_dict, pretty=False, default=None):
    """Return a string representation of the given json."""
    default = default or json_serial
    if pretty:
        return json.dumps(json_dict,
                          sort_keys=True,
                          indent=4,
                          default=default)
    return json.dumps(json_dict, default=json_serial)


def write_json_file(json_dict,
                    filename,
                    pretty=False,
                    default=None,
                    parents=False):
    """Write the dictionary in the given file."""
    if parents:
        parent = filename.parent
        parent.mkdir(parents=True, exist_ok=True)
    my_str = json_to_str(json_dict, pretty=pretty, default=default)
    with open(filename, 'w') as json_file:
        json_file.write(my_str)


def read_json_file(json_path, default=None):
    """
    Return the given json file as dictionary.

    @param {string} `json_path`
    @return {dictionary}
    """
    json_path = Path(json_path)
    if not json_path.is_file():
        if default is None:
            raise ValueError(f"You try to read {json_path}. "
                             f"The file does not exist and you "
                             f"furnished no default.")
        return default
    with open(json_path, 'r') as json_data:
        try:
            answer = json.load(json_data)
        except json.decoder.JSONDecodeError as err:
            print("JSONDecodeError:", err)
            message = f"Json error in {json_path}:\n {err}"
            raise ValueError(message) from err
    return answer


def human_seconds(total):
    """
    Return a human readable time.

    `total` is a number of seconds and we return xxh:yym:zzs
    """
    days = math.floor(total / 86400)
    remainder = total - 86400 * days
    hours = math.floor(remainder / 3600)
    remainder = remainder - 3600 * hours
    minutes = math.floor(remainder / 60)
    remainder = remainder - 60 * minutes
    seconds = round(remainder)
    answer = "  "
    if days:
        answer = f"{days}j"
    answer = answer + f"{hours}h{minutes}m{seconds}s"
    return answer.ljust(12)


def ciao(text=None):
    """Exit the program."""
    print("ciao!")
    if text:
        print("")
        print(text)
    if random.random() < 2:
        sys.exit(1)
