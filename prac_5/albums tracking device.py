"""
Update this module docstring with your own details
Name:qunweiShi
Date:2021-10-16
"""
from operator import itemgetter
import csv


MENU='''Menu:
L - List all albums
A - Add new album

M - Markan album as completed
Q - Quit'''



choicess=[]
def exist(a):
    if '4' in a and '1' in a and '5' in a:
        return 5
    elif '4' in a and '1' in a :
        return 3
    elif '1' in a:
        return 1
    elif '4' in a:
        return 4

def main():
    print("albums tracking device-by<qunweiShi>")
    print("4 albums loaded")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
      if choice == "L":
         if exist (choice)==1:
     albums_file = open("albums.csv")
        albums_date=albums_file.readlines()
        albums_date.sort(key=itemgetter(1))
        albums_using=[]
        for i in range(len(albums_data)):
            albums_user = albums_data[i].strip().split(",")
            albums_using.append(albums_user)
        albums_using.sort(key=itemgetter(1, 0))
