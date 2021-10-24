import tkinter as tk
import tkinter.ttk as ttk
import os
from tkinter import filedialog as fd


class AudioManipulationProgram(tk.Tk):
    song_file_name = ""
    temp_files_path = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self.title("Audio Manipulation Program")
        self.geometry("1000x500")

        file_open_button = ttk.Button(self, text=" Open Audio File ", command=self.open_song_file)
        file_open_button.grid(row=0, column=4, columnspan=1)

        compress_button = ttk.Button(self, text=" Compress Audio ", command=self.compress_audio)

        compress_button.grid(row=1, column=4, columnspan=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(1, weight=1)

    @staticmethod
    def compress_audio():
        i=AudioManipulationProgram.song_file_name
        j=AudioManipulationProgram.temp_files_path
        if os.name=="nt":
            os.system("ffmpeg\\ffmpeg.exe -i \"" + i + "\" -acodec libmp3lame -b:a 16k -ac 1 -ar 22050 \"" + j + "\"")
        else:
            os.system("ffmpeg/ffmpeg.exe -i \"" + i + "\" -acodec libmp3lame -b:a 16k -ac 1 -ar 22050 \"" + j + "\"")

    @staticmethod
    def open_song_file():
        AudioManipulationProgram.song_file_name = fd.askopenfilename()
        AudioManipulationProgram.temp_files_path = AudioManipulationProgram.song_file_name.replace(".mp3", "_compressed.mp3")
        print(AudioManipulationProgram.temp_files_path)


if __name__ == "__main__":
    if os.name == "nt":
        ffmpeg1 = os.path.abspath(os.path.dirname(__file__))+"\\ffmpeg_os\\ffmpeg_win.exe "
        ffmpeg2 = os.path.abspath(os.path.dirname(__file__))+"\\ffmpeg\\ffmpeg.exe"
        os.system("copy "+ffmpeg1+ffmpeg2)
    else:
        ffmpeg1 = os.path.abspath(os.path.dirname(__file__)) + "/ffmpeg_os/ffmpeg_linux.exe "
        ffmpeg2 = os.path.abspath(os.path.dirname(__file__)) + "/ffmpeg/ffmpeg.exe"
        os.system("cp " + ffmpeg1 + ffmpeg2)

    app = AudioManipulationProgram()
    app.mainloop()
