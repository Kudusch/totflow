#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess
import sys

try:
    query = sys.argv[1]
except:
    query = ""

def get_tots(tot_id=0):
    tots = {}
    if tot_id == 0:
        for tot_id in range(1, 8):
            tots[tot_id] = subprocess.check_output(["osascript", "-e", f"tell application \"Tot\" to open location \"tot://{tot_id}/conte\
nt\""]).decode("utf-8")
    else:
        tots[tot_id] = subprocess.check_output(["osascript", "-e", f"tell application \"Tot\" to open location \"tot://{tot_id}/conte\
nt\""]).decode("utf-8")
    return tots

def make_item(uid, title, subtitle, arg="", autocomplete="", icon=0):
    return {
        "title": title,
        "subtitle": subtitle,
        "arg": f"empty" if uid == 0 else f"{uid}/open",
        "autocomplete": autocomplete,
        "icon": {"path": f"icons/{icon}.png"},
        "mods": {
            "alt": {
                "valid": True,
                "arg": f"{uid}/replace?text=",
                "subtitle": f"Clear dot {uid}"
            },
            "cmd": {
                "valid": True,
                "arg": f"{uid}/append?text=\n{arg}",
                "subtitle": f"Append text to dot {uid}"
            },
            "cmd+alt": {
                "valid": True,
                "arg": f"{uid}/append?text= {arg}",
                "subtitle": f"Append text to dot {uid}, without a new line"
            }
        }
    }
def return_items(items):
    print(json.dumps({"items":items}))

items = []
items.append(make_item(0, title = "New dot", subtitle = f"Open a new empty dot", arg = "empty"))

for tot_id, tot in get_tots(tot_id=0).items():
    if len(tot) != 1:
        items.append(make_item(tot_id, title = f"{tot_id}: {tot}", subtitle = f"Open dot {tot_id}", arg = query, icon=tot_id))

return_items(items)