# uncompyle6 version 3.8.0
# Python bytecode 3.3 (3230)
# Decompiled from: Python 3.9.13 (main, May 24 2022, 21:28:44) 
# [Clang 13.0.0 (clang-1300.0.29.30)]
# Embedded file name: C:\Users\pouco\AppData\Roaming\Sublime Text 3\Packages\Guna\core\api.py
# Compiled at: 2022-09-18 14:00:24
# Size of source mod 2**32: 4836 bytes
import sublime, sublime_plugin, sys, time, datetime, threading, traceback
BujIRyx = 'DO NOT DECOMPILE ---------------------------------------------------'
from . import persist

def rVTsb_kzIWTx(name, hHDf=False):
    xG_qAYmw = False
    for th in threading.enumerate():
        if th.name == name:
            xG_qAYmw = True
            if hHDf:
                th.hHDf()
            else:
                break

    return xG_qAYmw


def set_except():
    sys.excepthook = vIcq_UouxHm


def vIcq_UouxHm(exctype, value, tb):
    GunaApi.alert_message(3, ' Uncaughted error is occured. Please, see the trace-back message in Sublime console.', 10, 1)
    sys.__excepthook__(exctype, value, tb)


class GunaApi:
    ALERT_CLOCK = 1
    ALERT_STATUS_LABEL = 2
    ALERT_STATUS_BG = 4
    INFO_CLOCK = 8
    INFO_STATUS_LABEL = 16
    FLICKER = 1

    @staticmethod
    def alert_message(flag=0, message='', timeout=4, action=0):
        if flag != 0:
            if message != '' and timeout >= 1:
                GunaApi.alert(flag, True)
                rVTsb_kzIWTx('GunaAlertThread', hHDf=True)
                pHwhvQu = GunaAlertThread(message, timeout, action, alert=True)
                pHwhvQu.setDaemon(True)
                pHwhvQu.start()

    @staticmethod
    def alert(flag=0, onoff=False):
        if flag & GunaApi.ALERT_CLOCK:
            GunaApi.set_prefs(persist.Vdz_RdxJm_xFJyh, onoff)
        if flag & GunaApi.ALERT_STATUS_LABEL:
            GunaApi.set_prefs(persist.Vdz_RdxJm_nNVprO_jzZDl, onoff)
        if flag & GunaApi.ALERT_STATUS_BG:
            GunaApi.set_prefs(persist.Vdz_RdxJm_nNVprO_zf, onoff)

    @staticmethod
    def info_message(flag=0, message='', timeout=4, action=0):
        if flag != 0:
            if message != '' and timeout >= 1:
                GunaApi.info(flag, True)
                rVTsb_kzIWTx('GunaAlertThread', hHDf=True)
                pHwhvQu = GunaAlertThread(message, timeout, action, alert=False)
                pHwhvQu.setDaemon(True)
                pHwhvQu.start()

    @staticmethod
    def info(flag=0, onoff=False):
        if flag & GunaApi.INFO_CLOCK:
            GunaApi.set_prefs(persist.Vdz_ZfWG_wEIXg, onoff)
        if flag & GunaApi.INFO_STATUS_LABEL:
            GunaApi.set_prefs(persist.Vdz_ZfWG_mMUoqp_iyYCk, onoff)

    @staticmethod
    def set_prefs(item, onoff):
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        hSii = CFTvj.get(item, False)
        if CFTvj.has(item):
            if hSii != onoff:
                if onoff:
                    CFTvj.set(item, True)
                else:
                    CFTvj.erase(item)
        else:
            CFTvj.set(item, onoff)


class GunaAlertThread(threading.Thread):

    def __init__(self, message, timeout, action, alert=True):
        threading.Thread.__init__(self, name='GunaAlertThread')
        self.bSHirWV = message
        self.GWBufKk = timeout
        self.pQiyfD = action
        self.pZThI = alert
        self.fIXj = False

    def run(self):
        while self.GWBufKk > 0:
            if self.fIXj:
                break
            if self.pQiyfD == GunaApi.FLICKER:
                sublime.status_message(self.bSHirWV)
                time.sleep(0.4)
                sublime.status_message(' ')
                time.sleep(0.1)
            else:
                sublime.status_message(self.bSHirWV)
                time.sleep(0.5)
            self.GWBufKk = self.GWBufKk - 1

        sublime.status_message('')
        if self.pZThI:
            GunaApi.alert(7, False)
        else:
            GunaApi.info(24, False)

    def hHDf(self):
        self.fIXj = True
# okay decompiling api.pyc
