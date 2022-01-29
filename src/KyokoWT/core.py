from abc import ABCMeta, abstractmethod,ABC


class KyokoWTCore(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,lang_kun="ja-JP"):
        self.lang=lang_kun
    @abstractmethod
    def gettext(self,audio_path):
        pass

