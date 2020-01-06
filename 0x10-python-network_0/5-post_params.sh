#!/bin/bash
# takes a URL, sends a POST request, and displays the body
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
