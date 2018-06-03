from __future__ import unicode_literals
from django.shortcuts import render
import youtube_dl

def result(request):
	yt_url=request.POST['id']
	def my_hook(d):
		if d['status'] == 'finished':
			print('Done downloading, now converting...')
			print (d['filename'])

	ydl_opts = {
    'format': 'bestaudio/best',
	'outtmpl': 'download/%(id)s.%(ext)s',
    'postprocessors': [{
    	'key': 'FFmpegExtractAudio',
    	'preferredcodec': 'mp3',
    	'preferredquality': '192',
    }],

}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		result= ydl.extract_info("{}".format(yt_url))
		id= result.get('id')
		link = 'home\\aliya\\Desktop\\projects\\conv\\download\\' + id + '.mp3'
	return render(request, "converter/result.py", {'download_link': link})

def index(request):
	return render(request, "converter/index.html", {})

