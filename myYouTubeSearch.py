from youtubesearchpython import VideosSearch

print("hello, world")

delimiter = "="*30
def print_videos(video, index):
    print(f'{index}. {video["title"]}')
    print(f'Numar de vizualizari: {video["viewCount"]["text"]}')
    print(f'Autor: {video["channel"]["name"]}')
    print(delimiter)

nume = input("Cum te numesti? ")
print("Buna, " + nume + "!")

# Infinite loop
while True:
    print("Optiunile acestei aplicatii sunt:")
    print("1. Cautarea video-urilor pe YouTube")
    print("2. exit")
    option = input(f"Ce optiune alegi, {nume}? ")
    if option == "1":
        title = input("Cauta un video dupa titlu: ")
        videosSearch = VideosSearch(title, limit=2)
        result = videosSearch.result()["result"]
        for index, video in enumerate(result):
            print_videos(video, index)
    elif option == "2":
        print(f"La revedere, {nume}!")
        break
