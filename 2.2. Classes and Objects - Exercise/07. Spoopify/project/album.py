from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        for item in self.songs:
            if item.name == song_name:
                self.songs.remove(item)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for item in self.songs:
            result += f"== {item.get_info()}\n"
        return result


song = Song("Running in the 90s", 3.45, False)
second_song = Song("guza me boli", 2.34, False)
album = Album("Initial D", song, second_song)
third_song = Song("Around the World", 2.34, False)
print(album.add_song(third_song))
print(album.details())
print(album.publish())

