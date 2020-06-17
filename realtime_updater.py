import firebase_admin
from firebase_admin import credentials, db
from random import seed, randint
import os
from heatMeasure import BodyHeatMeasure
import multiprocessing
from multiprocessing import Process


class WatchDog():
    def __init__(self):
        self._cache = 0
        self.file = 'datas/heart_rate.txt'
        self.stepFile = 'datas/steps.txt'

    def checkFile(self):
        date = os.stat(self.file).st_mtime
        if date != self._cache:
            self._cache = date
            return 1
        else:
            return 0




class realtime_updater:

    def __init__(self, username):
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://alzheimertakip-e1d1e.firebaseio.com/'})
        
        self.username = username

        self.ref = db.reference('/')
        self.ref = self.ref.child('hastaDurum')
        self.run = 1



    def start(self):
        seed(1)

        with open('datas/steps.txt') as f:
            steps = f.readline()

        with open('datas/meters.txt') as f:
            meters = f.readline()


        with open('datas/callories.txt') as f:
            callories = f.readline()


        measure = BodyHeatMeasure()

        watchdog = WatchDog()

        while self.run == 1:
            bodyHeat = measure.measureHeat()
            if(watchdog.checkFile()):

                with open('datas/heart_rate.txt') as f:
                    heartRate = f.readline()

                heartRate = heartRate.strip('\n')
                

            self.ref.update({
                self.username: {
                    'kalpRitmi': heartRate,
                    'adimSayisi': steps,
                    'mesafe': meters,
                    'callories' : callories,
                    'bodyHeat' : bodyHeat
                }
            })

"""
    def start(self):
        self.p2 = Process(target=self.parallel_start)
        self.p2.start()
        self.p1.start()

    def stop(self):
        self.p1.terminate()
        self.p2.terminate()
        """
