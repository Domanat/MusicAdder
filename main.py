from yandex_music import Client
import math

tokenFile = open("token.txt", "r")

token = tokenFile.readline()
client = Client(token, report_new_fields=False)

def isTrackInPlaylist(playlistId, trackName):
    playlist = client.users_playlists(playlistId)
    listOfTracks = playlist.tracks

    for shortTrack in listOfTracks:
        if shortTrack.track.title == trackName:
            print("Track is already in playlist")
            return True

    return False

def addTracksByArtist(artistName, playlistName):

    listOfPlaylists = client.users_playlists_list()
    for playlist in listOfPlaylists:
        if playlist.title == playlistName:
            revision = playlist.revision
            doomerId = playlist.kind

    counter = 0
    search = client.search(artistName, type_="Track")

    if search.tracks == None:
        print("No such artist\nTry again")
        return

    numberOfPages = math.ceil(search.tracks.total/search.tracks.per_page)
    for i in range(numberOfPages):

        search = client.search(artistName, type_="Track", page=i)
        if search.tracks == None:
            print("No tracks on page", i)
            return

        isRightTrack = False

        listOfTracks = search.tracks.results
        for track in listOfTracks:
            listOfArtists = track.artists
            for artist in listOfArtists:
                if artist.name == artistName:
                    isRightTrack = True
                    break

            if isRightTrack:
                counter = counter + 1
                print("Add track: ", track.title)
                if not isTrackInPlaylist(doomerId, track.title):
                    client.users_playlists_insert_track(kind=doomerId, track_id=track.id, album_id=track.albums[0].id, revision=revision)
                    revision = revision + 1
                isRightTrack = False
    

    print("Number of tracks: ", counter)


if __name__ == '__main__':
    while True:
        query = input('Enter artist name: ')
        if query == "!quit":
                break;
        addTracksByArtist(query, "Doomer Music")