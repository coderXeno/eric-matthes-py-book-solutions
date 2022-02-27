def make_album(artist_name,album_title,number_of_tracks=0):
    album = {}
    
    if(number_of_tracks):
        album = {
        'artist name': artist_name,
        'album name': album_title,
        'number of tracks': number_of_tracks
    }
    else:
        album = {
        'artist name': artist_name,
        'album name': album_title,
    }

    return album

album_1 = make_album("Daddy Yankee","Hits",14)
print(album_1)

album_2 = make_album("Alan Walker","EDM",30)
print(album_2)

album_3 = make_album("Arijit Singh","Romantic Mix")
print(album_3)

print("----------------------------")

while(True):
    choice = input("Type 'yes' to continue. Type 'no' to quit\n")
    if(choice == 'no'):
        break
    else:
        artist = input("Enter the artist name: \n")
        album = input("Enter album name: \n")

        print(make_album(artist,album))
    