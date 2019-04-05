#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def descramble(urls):
    d = {}
    for i in urls:
        match = re.search(r'-\w+-(\w+)\.jpg', i)
        d[match.group(1)] = i
    t=[]
    for key in sorted(d):
        t.append(d[key])
    return t
    

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  with open(filename, 'r') as f:
      log = f.read()
  urls = re.findall(r'GET\s(\S+puzzle\S+)', log)
  urls =list(set(urls))
  for i in range(len(urls)):
      urls[i] = "http://code.google.com" + urls[i]
  urls.sort()
  match = re.search(r'-(\w+)-(\w+)\.jpg', urls[1])
  if match: urls = descramble(urls)
  return urls
      
  

def download_images(img_urls, dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dir):
      os.mkdir(dir)
  index = open(os.path.join(dir, 'index.html'), 'w')
  index.write('<html><body>\n')
  n=0
  print(f'Downloading images to *{dir}* folder...')
  for i in img_urls:
      image = f'img{n}.jpg'
      urllib.request.urlretrieve(i, os.path.join(dir, image))
      n+=1
      index.write(f'<img src="{image}">')
  index.write('\n</body></html>\n')
  index.close()
  print('Image has been retrieved into index.html file')

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
