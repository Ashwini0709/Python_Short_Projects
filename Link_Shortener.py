#!/usr/bin/env python

#Install the library on local machine 'pip install pyshorteners' 
import pyshorteners

#Get the link from the user
link = input("Enter the Link: ")

#Create a Shortener object
shortener = pyshorteners.Shortener()


#Shorten the link using TinyURL
shortened_link = shortener.tinyurl.short(link)


#print the Shortened link
print("Shortened Link: ", shortened_link)
