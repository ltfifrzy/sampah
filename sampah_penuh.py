import threading
import time
from datetime import datetime


class SampahPenuh:

    def __init__(self):
        self.sampah_penuh = False
        self.thread = threading.Thread(target=self._deteksi_sampah_penuh)
        self.thread.daemon = True
        self.thread.start()

    def _deteksi_sampah_penuh(self):
        while True:
            time.sleep(10)
            self.sampah_penuh = True

    def kirim_notifikasi(self):
        title = "Sampah Penuh"
        text = "Sampah di tempat pembuangan Anda telah penuh"
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        time = now.strftime("%H:%M:%S")
        message = f"{title} - {date} - {time}"

        import notify2

        notify2.init("Sampah Penuh")
        notify2.Notification(title, message).show()


if __name__ == "__main__":
    sampah_penuh = SampahPenuh()

    while True:
        time.sleep(1)
