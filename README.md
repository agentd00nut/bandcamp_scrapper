# bandcamp_scrapper

Usage
=====

	python bandcamp.py -d "https://daily.bandcamp.com/2016/09/06/posh-lost-mirror-universe-review/" -o tracks
	python bandcamp.py -a "http://homesafeil.bandcamp.com/album/inside-your-head" -o tracks

- -d daily_url, download tracks from a daily url
- -a album_url, download tracks from an albums url

What Is This
============

Give this script a url to a bandcamp album url or the link to one of their daily albums and an output dir and you will end up with 
all the tracks of the album on your disk!
Obviously you end up with low quality mp3-128's, nothing they weren't already giving to you for free, it's just a little easier than 
right clicking, save as, on every link.


How To Use
==========

Obviously since this only works on one album at a time it might be prudent to wrap it up in something that gets all the album
links for an artist and feed it those urls one at a time.
If you decide to do that then I won't be help responsible for who gets mad at you.


Don't be dumb
=============

This is just an example of how to do some web scraping in python.  Don't go downloading a million low quality tracks and cry at me.
I'm not liable for your rash decision making <3.

It Doesn't Work
===============

I only lightly tested this.  Check that you are passing the URL correctly.  Check that your output path is sane.
It's also very likely you ran into a band camp page that has a format that is different than what i had seen previously.
Congrats, Comment about it or fork, add that page as an argument, and I'll merge it back in.

