import speech_recognition

from src import KyokoWTCore


class KyokoWTGoogle(KyokoWTCore):
    def __init__(self,lang_kun="ja-JP"):
        super(KyokoWTGoogle,self).__init__(lang_kun)
        self.r=speech_recognition.Recognizer()
    def gettextfa(self,audiodt):
        jsondt=self.r.recognize_google(audiodt,language=self.lang,show_all=True)

        return jsondt.get('alternative')[0].get('transcript')

    def gettext(self, audio_path):
        with speech_recognition.AudioFile(audio_path) as s:
            audiokun=self.r.record(s)
        jsondt = self.r.recognize_google(audiokun, language=self.lang, show_all=True)

        return jsondt.get('alternative')[0].get('transcript')
    def getaudio(self, audiopt):
        return self.r.record(audiopt)