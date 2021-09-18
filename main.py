from yandex_music import Client

credentialsFile = open("credentials.txt", "r")

email = credentialsFile.read(23)
password = credentialsFile.read(9)

client = Client.from_credentials(email, password)

playlists = client.users_playlists_list()
	doomerId = 0
	
	for i in playlists:
		if i.title == "Doomer Music":
			doomerId = i.kind
			break

	print("Playlist ID:", doomerId)

def findTracksOfArtist(artistName):

	#searchResult = client.search(text=artistName, type_="track").tracks

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
