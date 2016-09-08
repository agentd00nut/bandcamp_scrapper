import requests, re, os
import getopt, json



def save_tracks(tracks, artist=False, album=False):
	global out_dir

	for trackinfo in tracks:
		if "file" in trackinfo:

			if "track_num" in trackinfo:
				track_num = str(trackinfo["track_num"])+"-"
			elif "tracknum" in trackinfo:
				track_num = str(trackinfo["tracknum"])+"-"

			if artist == False:
				if "artist" in trackinfo:
					artist = trackinfo["artist"].replace(" ","_")+"-"
				else:
					artist = False
			elif "-" not in artist:
				artist +="-"

			if album != False:
				if "-" not in album:
					album +="-"

			write_track_to_disk(trackinfo["file"]["mp3-128"], out_dir+artist+album+track_num+trackinfo["title"].strip()+".mp3")

def make_dir_if_not_exists(path):
	if os.path.isdir(path) == False:
		os.makedirs(path)

def write_track_to_disk(track_url, path):

	if "http:" not in track_url:
		track_url="http:"+track_url

	print "	"+track_url+"	=>	"+path
	
	r = requests.get(track_url, stream=True)
	
	if r.status_code == 200:
		with open(path, 'wb') as f:
			for chunk in r.iter_content(1024):
				f.write(chunk)

def get_text_from_url(url):
	return requests.get(url).text.encode('ascii','ignore')

def get_pattern_from_url(pattern, url, trim_start=0, trim_end=-1):
	r 			= get_text_from_url(url)
	contents	= re.search(pattern, r).group(0)[trim_start:trim_end]
	return contents

def get_pattern_from_text(pattern, text, trim_start=0, trim_end=-1):
	return re.search(pattern, text).group(0)[trim_start:trim_end]


## INIT

album_url 	= False
daily_url 	= False
out_dir		= "./tracks/"



## GET OPTS

options, remainder = getopt.getopt(sys.argv[1:], 'a:d:o:', ['album='])


for opt, arg in options:
    if opt in ('-a', '--album'):
        album_url 	= arg

    if opt in ('-d', '--daily'):
    	daily_url 	= arg

    if opt in ('-o', '--out_dir'):
    	out_dir 	= arg

    	if out_dir.endswith("/") == False:
    		out_dir += "/"


## MAIN

make_dir_if_not_exists(out_dir)


if album_url != False:
	tracks = json.loads( get_pattern_from_url("trackinfo : \[.*\}\],", album_url, 12, -1) )
	save_tracks(tracks)
	

if daily_url != False:

	html		= get_text_from_url(daily_url);
	artist		= get_pattern_from_text(":.*?,", html, 2,-1)
	album 		= get_pattern_from_text(",.*?&laquo;", html, 2, -8)
	album_id 	= get_pattern_from_url("/album=[0-9]*/", daily_url, 7, -1);
	print "Arist: 		"+artist
	print "Album: 		"+album
	print "Album_id:	"+album_id

	embed_url 	= "http://bandcamp.com/EmbeddedPlayer/v=2/album="+album_id+"/size=large/bgcol=ffffff/linkcol=0687f5/"

	tracks 		= json.loads( get_pattern_from_url("tracks\":.*?\}\],\"", embed_url, 8, -2) )

	save_tracks(tracks, artist, album)




