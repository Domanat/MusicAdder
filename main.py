from yandex_music import Client

#email@yandex.ruPassword
credentialsFile = open("credentials.txt", "r")

email = credentialsFile.read(23)
password = credentialsFile.read(9)

client = Client()

'''client = Client.from_credentials(email, password)

playlists = client.users_playlists_list()
doomerId = 0
	
for i in playlists:
	if i.title == "Doomer Music":
		doomerId = i.kind
		break

print("Playlist ID:", doomerId)'''

def findTracksOfArtist(artistName):

	#type Search
	search = client.search(artistName)

	if search.tracks == None:
		print("No tracks")
		return

	rightTrack = False
	print("Number of tracks", search.tracks.total)

	print(type(search.tracks.results[0]))

	for i in range(search.tracks.total):
		track = search.tracks.results[i]
		print("Track title: ", track.title)
		for j in range(len(track.artists)):
			artist = track.artists
			if artist == artistName:
				print("Right tracks")
				rightTrack = True
				break

		if rightTrack:
			print("Add to playlist track: ", search.tracks[i].title)
			rightTrack = False

	'''for track in search.tracks.results:
					for artist in track.artists:
						print("title: ", track.title)
						print("Artist: ", artist['name'])
						if artist['name'] == artistName:
							print("Right track")
							rightTrack = True
							break'''

		

	'''
	if searchResult.best == None:
		print("No such artist")
		return
	
	print("Number of artists", searchResult.tracks.total)
	'''

if __name__ == '__main__':
	query = ''
	while query != 'q':
		query = str(input())
		findTracksOfArtist(query)
