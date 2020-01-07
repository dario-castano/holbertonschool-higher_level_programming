#!/bin/bash
# sends a request to a URL, and displays only the status code.
curl -sI "$1" | head -n 1 | cut -d " " -f 2
