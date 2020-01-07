#!/bin/bash
# sends a JSON POST request to a URL as the first argument, and displays the body.
curl -s -d @$2 -X POST -H "Content-Type: application/json" "$1"
