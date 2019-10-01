#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
print(a_dictionary)
print("***SORTED***")
print_sorted_dictionary(a_dictionary)
print("--------------------------------------------------------------")

b_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3], 'adict': {"nam": 1, "crt": 2}, 'Aloha': None}
print(b_dictionary)
print("***SORTED***")
print_sorted_dictionary(b_dictionary)
print("--------------------------------------------------------------")

c_dictionary = {}
print(c_dictionary)
print("***SORTED***")
print_sorted_dictionary(c_dictionary)
print("--------------------------------------------------------------")
