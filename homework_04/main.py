from abc import ABC, abstractmethod

class MediaFile():
    def __init__(self, name, size, creation_date, owner):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner


    @abstractmethod
    def info(self):
        pass

class AudioFile(MediaFile):
    def __init__(self,name, size, creation_date, owner, tags):
            super().__init__(name, size, creation_date, owner)
            self.tags = tags

    def info(self):
        print(f"Info file: {self.name}, with size: {self.size}, with creation date: {self.creation_date},"
              f" with owner: {self.owner}, with tags: {self.tags}")

class VideoFile(MediaFile):

    def __init__(self, name, size, creation_date, owner, description, codec, language, geo):
        super().__init__(name, size, creation_date, owner)
        self.description = description
        self.codec = codec
        self.language = language
        self.geo = geo

    def info(self):
        print(
            f"Info file: {self.name}, with size: {self.size}, with creation date: {self.creation_date},"
            f" with owner: {self.owner}, with tags: {self.codec}, with language: {self.language}, with geo: {self.geo}")


class PhotoFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, description, geo, author ):
        super().__init__(name, size, creation_date, owner)
        self.description = description
        self.geo = geo
        self.author = author

    def info(self):
        print(
            f"Info file: {self.name}, with size: {self.size}, with creation date: {self.creation_date},"
            f" with owner: {self.owner}, with description: {self.description}, with geo: {self.geo}, with author: {self.author}")


class StoragePlace:

    type = "Default Place"

    def __init__(self):
        pass

    @abstractmethod
    def createFile(self, file: MediaFile):
        pass

    @abstractmethod
    def removeFile(self, file: MediaFile):
        pass

    @abstractmethod
    def updateFile(self, file: MediaFile):
        pass


class S3StoragePlace(StoragePlace):
    def __init__(self):
        self.type = "S3 Storage"

    def createFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено создание файла:")
        file.info()
        print("Запись вставлена успешно.")

    def removeFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено удаление файла:")
        file.info()
        print("Запись успешно удалена.")

    def updateFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено обновление файла:")
        file.info()
        print("Запись обновлена успешно.")


class LocalStoragePlace(StoragePlace):
    def __init__(self):
        self.type = "Local Storage"

    def createFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено создание файла:")
        file.info()
        print("Запись вставлена успешно.")

    def removeFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено удаление файла:")
        file.info()
        print("Запись успешно удалена.")

    def updateFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено обновление файла:")
        file.info()
        print("Запись обновлена успешно.")


class CloudStoragePlace(StoragePlace):
    def __init__(self):
        self.type = "Cloud Storage"

    def createFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено создание файла:")
        file.info()
        print("Запись вставлена успешно.")

    def removeFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено удаление файла:")
        file.info()
        print("Запись успешно удалена.")

    def updateFile(self, file: MediaFile):
        print(f"В {self.type} будет выполнено обновление файла:")
        file.info()
        print("Запись обновлена успешно.")




audioTrack = AudioFile("Топ песня", "20mb", "10.07.2025", "SomeActor", 1)
move = VideoFile("3 кота", "200mb", "10.07.2025", "SomeActor", "Carton", "some code", "ru", "0001.01 0020.1")
photo = PhotoFile("Пейзаж", "3mb", "10.07.2025", "SomeActor", "Carton","0001.01 0020.1", "Some actor" )

storage = S3StoragePlace()
cloud = CloudStoragePlace()
local = LocalStoragePlace()

storage.createFile(photo)
cloud.createFile(audioTrack)
local.createFile(move)


cloud.removeFile(audioTrack)
local.updateFile(move)

