#!/bin/bash
# takes a URL as an argument, sends a GET request, and displays the body
curl -s "$1" -H "X-HolbertonSchool-User-Id:98"
