# uncompyle6 version 3.8.0
# Python bytecode 3.3 (3230)
# Decompiled from: Python 3.9.13 (main, May 24 2022, 21:28:44) 
# [Clang 13.0.0 (clang-1300.0.29.30)]
# Embedded file name: C:\Users\pouco\AppData\Roaming\Sublime Text 3\Packages\Guna\core\engine.py
# Compiled at: 2022-09-18 14:00:24
# Size of source mod 2**32: 72316 bytes
import sublime, sublime_plugin, datetime
from datetime import datetime
import time, threading, traceback, os, shutil, re, webbrowser, plistlib, colorsys, urllib.request, json, hashlib
BujIRyx = 'DO NOT DECOMPILE ---------------------------------------------------'
from . import api
from . import persist
HjKUi = int(sublime.version())
rORxvFRlY = ''
suUQLdK_mbzGZ = 'Default.sublime-theme'
suUQLdK_ViEIm = 'Packages/Color Scheme - Default/Monokai.sublime-color-scheme'
XsfDJ_GSVevAZ = 'A File Icon'
hHDfEUu = False
GWBujJReG = 0
tLeyGUu = False
YCRa_VZdx = [
 (
  'Guna', 'Guna.py'),
 (
  'Guna', 'Guna.sublime-settings'),
 (
  'Guna', 'themes', 'preset', 'Guna-dark.sublime-settings'),
 (
  'Guna', 'themes', 'preset', 'Guna-light.sublime-settings')]
YCRa_VZdx_iuMB = []
for f in YCRa_VZdx:
    COix = os.path.join(*f)
    YCRa_VZdx_iuMB.append(COix)

YOHj_JywfW = ''
YOHj_SFdhJ = ''
YOHj_RXuCJ = ''
YOHj_WFhKK = ''
YOHj_MZyhF = ''
lWswvJ_aEVXr = 0
ACZ_tDk = 0

def start():
    # rORxv_cgtVXx()
    api.set_except()
    VIcqDQZfmZkyvX.rZTqC_XfbK()
    if VIcqDQZfmZkyvX.rVTsb_VpGAkyW():
        VIcqDQZfmZkyvX.rZTqC_gjWK()
        tLeyGUu = True
        return
    rVTsb_Xhn_PcGXJs_XRdCCq()
    dPHuGLV_GJXzn()
    sublime.set_timeout_async(engine_reload, 0)
    SIab_ITjxWg_jH_oOWor()
    lOXj_Qev_KmuKN()


def stop():
    global hHDfEUu
    hHDfEUu = True
    rVTsb_kzIWTx('prproc', stop=True)
    rVTsb_kzIWTx('fkproc', stop=True)
    rVTsb_kzIWTx('mnproc', stop=True)
    VIcqDQZfmZkyvX.rZTqC_XfbK()
    VIcqDQZfmZkyvX.rZTqC_gjWK()
    VIcqDQZfmZkyvX.rZTqC_Xfv()
    VIcqDQZfmZkyvX.rZTqC_Xfp()
    VIcqDQZfmZkyvX.rZTqC_XfU()
    VIcqDQZfmZkyvX.rZTqC_NaUYXn_IodbN(True)
    ESHjfHV_KZXgz()


def dPHuGLV_GJXzn(observer=None):
    if hHDfEUu:
        return
    CFTvj = sublime.load_settings('Preferences.sublime-settings')
    CFTvj.clear_on_change('Guna-prefs')
    CFTvj.add_on_change('Guna-prefs', observer or dB_fGUwk_MixvNZ)
    vIcqj = sublime.load_settings('Guna.sublime-settings')
    vIcqj.clear_on_change('Guna-gunas')
    vIcqj.add_on_change('Guna-gunas', observer or dB_fGUwk_MixvNZ)
    vIcqS = sublime.load_settings('Guna-dark.sublime-settings')
    vIcqS.clear_on_change('Guna-gunad')
    vIcqS.add_on_change('Guna-gunad', GKTqb_kzxEX)
    vIcqA = sublime.load_settings('Guna-light.sublime-settings')
    vIcqA.clear_on_change('Guna-gunal')
    vIcqA.add_on_change('Guna-gunal', GKTqb_kzxEX)


def GKTqb_kzxEX():
    CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
    if xG_wlDR:
        sublime.active_window().run_command('guna_tweak_theme')
    else:
        sublime.active_window().run_command('guna_tweak_widget')


def dB_fGUwk_MixvNZ():
    if hHDfEUu:
        return

    def CFTvj_iwCGTx():
        dPHuGLV_GJXzn()

    dPHuGLV_GJXzn(observer=CFTvj_iwCGTx)
    xG_qAYmw = rVTsb_kzIWTx('prproc', stop=False)
    if not xG_qAYmw:
        CHwhvQu = VIcqgHVxmZkyvX()
        CHwhvQu.setDaemon(True)
        CHwhvQu.start()


def engine_reload():
    global YOHj_JywfW
    global YOHj_MZyhF
    global YOHj_RXuCJ
    global YOHj_SFdhJ
    global YOHj_WFhKK
    dPHuGLV_GJXzn(observer=dB_fGUwk_MixvNZ)
    GKTqb = False
    CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
    rCaeG = CFTvj.get('color_scheme', '')
    vIcqj = sublime.load_settings('Guna.sublime-settings')
    OURbG = vIcqj.get('guna_bgcolor', '#161C23')
    rGDfI = vIcqj.get('guna_color_saturation', 100)
    rPDfI = vIcqj.get('guna_color_brightness', 100)
    vRRbG = vIcqj.get('guna_guide', '#20272E')
    pURbG = vIcqj.get('guna_active_guide', '#AAFF9954')
    OFRbG = vIcqj.get('guna_brackets_color', '#FF0000')
    GURbG = vIcqj.get('guna_tags_color', '#FF5242')
    OFDfI = vIcqj.get('guna_brackets_options', 'foreground')
    GUDfI = vIcqj.get('guna_tags_options', 'foreground')
    GHqqG = vIcqj.get('title_bar_color', True)
    vCejj = str(rGDfI) + str(rPDfI) + vRRbG + pURbG + OFRbG + GURbG + OFDfI + GUDfI + str(GHqqG)
    if GVTcv != YOHj_JywfW or rCaeG != YOHj_SFdhJ or OURbG != YOHj_RXuCJ or vCejj != YOHj_WFhKK:
        ESReGT_lYWFy()
        YOHj_SFdhJ = rCaeG
        GKTqb = True
    GWBujJReGB = 2638983600
    vIcqj, lWswI, lWVeC, xG_sAETc = vSi_xKesl('clock')
    if not xG_wlDR and not lWVeC and YOHj_MZyhF == 'False':
        if YOHj_JywfW == 'Guna.sublime-theme':
            VIcqDQZfmZkyvX.rZTqC_XfbK()
            VIcqDQZfmZkyvX.rZTqC_gjWK()
            VIcqDQZfmZkyvX.rZTqC_Xfv()
            VIcqDQZfmZkyvX.rZTqC_Xfp()
            VIcqDQZfmZkyvX.rZTqC_XfU()
        YOHj_JywfW = GVTcv
        return
    if str(lWVeC) != YOHj_MZyhF:
        YOHj_MZyhF = str(lWVeC)
    if GVTcv != YOHj_JywfW:
        YOHj_JywfW = GVTcv
        VIcqDQZfmZkyvX.rZTqC_Xfv()
        VIcqDQZfmZkyvX.rZTqC_Xfp()
        VIcqDQZfmZkyvX.rZTqC_XfU()
        VIcqDQZfmZkyvX.rZTqC_NaUYXn_IodbN(xG_wlDR)
    VIcqDQZfmZkyvX.xBXj_FiwWK(CFTvj, vIcqj, xG_wlDR, lWVeC)
    if xG_wlDR and GKTqb:
        sublime.active_window().run_command('guna_tweak_theme')
    else:
        sublime.active_window().run_command('guna_tweak_widget')


def vSi_EHVxl():
    CFTvj = sublime.load_settings('Preferences.sublime-settings')
    GVTcv = CFTvj.get('theme', '')
    xG_wlDR = rAe_jJi(GVTcv, 'Guna.sublime-theme')
    return (CFTvj, GVTcv, xG_wlDR)


def vSi_xKesl(widget='clock'):
    vIcqj = sublime.load_settings('Guna.sublime-settings')
    lWswI = vIcqj.get('sidebar_widget', [])
    lWVeC = vIcqj.get('sidebar_widget_on_other_theme', True)
    lWVjU = True if widget in lWswI else False
    return (vIcqj, lWswI, lWVeC, lWVjU)


vSicIYDw = os.path.getmtime

def vSi_jJPdx():
    pJXun = sublime.active_window().active_view()
    CFTvj = sublime.load_settings('Preferences.sublime-settings')
    rGRxd = CFTvj.get('color_scheme')
    IWTmt = '' if pJXun is None else pJXun.settings().get('color_scheme')
    if pJXun is None or rGRxd != IWTmt:
        IWTm = sublime.active_window().new_file()
        hHNbv = IWTm.style()
        sublime.active_window().focus_view(IWTm)
        sublime.active_window().run_command('close_file')
        return hHNbv
    else:
        return pJXun.style()
        return


def rAe_jJi(item, string):
    return isinstance(item, str) and item == string


def lOXj_Qev_KmuKN():
    xG_qAYmw = rVTsb_kzIWTx('fkproc', stop=False)
    if not xG_qAYmw:
        SHwhvQu = VIcqwEicmZkyvX()
        SHwhvQu.setDaemon(True)
        SHwhvQu.start()


def rVTsb_kzIWTx(name, stop=False):
    xG_qAYmw = False
    for th in threading.enumerate():
        if th.name == name:
            xG_qAYmw = True
            if stop:
                th.stop()
            else:
                break

    return xG_qAYmw


def rVTsb_JltLNm(CFTvj=None, IWTm=None):
    if hHDfEUu:
        return
    else:
        pJXm = sublime.active_window().active_view()
        if pJXm is None:
            return
        if IWTm is None:
            IWTm = pJXm
        else:
            if IWTm != pJXm:
                return
            if CFTvj is None:
                CFTvj = sublime.load_settings('Preferences.sublime-settings')
            GVTcv = CFTvj.get('theme', '')
            vIcqj = sublime.load_settings('Guna.sublime-settings')
            lWVeC = vIcqj.get('sidebar_widget_on_other_theme', True)
            if rAe_jJi(GVTcv, 'Guna.sublime-theme') or lWVeC:
                if not IWTm.settings().get('is_widget'):
                    xG_hvQug = CFTvj.get(persist.Vdt_iwtV_iGFT, False)
                    if IWTm.is_read_only():
                        if not xG_hvQug:
                            CFTvj.set(persist.Vdt_iwtV_iGFT, True)
                    elif xG_hvQug:
                        CFTvj.set(persist.Vdt_iwtV_iGFT, False)
                    if IWTm.is_read_only():
                        CFTvj.set(persist.Vdt_uaILR, False)
                    else:
                        xG_tzHkq = CFTvj.get(persist.Vdt_uaILR, False)
                        if IWTm.is_dirty() or IWTm.is_scratch():
                            if not xG_tzHkq:
                                CFTvj.set(persist.Vdt_uaILR, True)
                        elif xG_tzHkq:
                            CFTvj.set(persist.Vdt_uaILR, False)
        return


def SIab_ITjxWg_jH_oOWor():
    try:
        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        vIcqj = sublime.load_settings('Guna.sublime-settings')
        SIabj = vIcqj.get('full_screen_on_start', False)
        if xG_wlDR:
            if SIabj:
                w = sublime.active_window()
                w.run_command('toggle_full_screen')
                w.set_menu_visible(False)
    except Exception:
        QWHf_UijhJ()


def ESReGT_lYWFy():
    try:
        EQixv = suUQLdK_mbzGZ
        EQRbG = suUQLdK_ViEIm
        GWBujJReGH = 1934292400
        SBPcv = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.record_theme')
        if os.path.exists(SBPcv):
            with open(SBPcv, 'r', encoding='utf8') as (f):
                GLi = str(f.read())
            for line in GLi.splitlines():
                if line.endswith('.sublime-theme'):
                    EQixv = line
                elif line.endswith('.tmTheme') or line.endswith('.sublime-color-scheme'):
                    EQRbG = line
                    continue

        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        rCaeG = CFTvj.get('color_scheme', suUQLdK_ViEIm)
        if xG_wlDR:
            GVTcv = EQixv
        if rCaeG.startswith('Packages/Guna'):
            rCaeG = EQRbG
        SDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache')
        if not os.path.exists(SDPjW):
            os.makedirs(SDPjW)
        SBPcv = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.record_theme')
        GSmj = GVTcv + '\n' + rCaeG + '\n'
        with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
            f.write(GSmj)
    except Exception:
        QWHf_UijhJ()


def ESHjfHV_KZXgz():
    try:
        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        if not xG_wlDR:
            return
        GVTcv = suUQLdK_mbzGZ
        rCaeG = suUQLdK_ViEIm
        GWBujJReGH = 2228185400
        SBPcv = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.record_theme')
        if os.path.exists(SBPcv):
            with open(SBPcv, 'r', encoding='utf8') as (f):
                GLi = str(f.read())
            for line in GLi.splitlines():
                if line.endswith('.sublime-theme'):
                    GVTcv = line
                elif line.endswith('.tmTheme') or line.endswith('.sublime-color-scheme'):
                    rCaeG = line
                    continue

        GZXiI = sublime.find_resources(GVTcv)
        if len(GZXiI) == 0:
            GVTcv = suUQLdK_mbzGZ
        rZXiI = sublime.find_resources(os.path.basename(rCaeG))
        if not any(rCaeG == c for c in rZXiI):
            rCaeG = suUQLdK_ViEIm
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        CFTvj.set('color_scheme', rCaeG)
        CFTvj.set('theme', GVTcv)
        # sublime.save_settings('Preferences.sublime-settings')
    except Exception:
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        CFTvj.set('color_scheme', suUQLdK_ViEIm)
        CFTvj.set('theme', suUQLdK_mbzGZ)
        # sublime.save_settings('Preferences.sublime-settings')
        QWHf_UijhJ()


def vSi_IYDw():
    global rORxvFRlY
    if rORxvJZex == 0:
        return vSicIYDw(rORxvFRlY)
    else:
        return rORxvJZex


def rORxv_cgtVXx():
    global rORxvFRlY
    global rORxvJZex
    SDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache')
    if not os.path.exists(SDPjW):
        os.makedirs(SDPjW)
    try:
        QOi = urllib.request.urlopen('http://api.openweathermap.org').headers['Date']
        rORxvJZex = int(bOZuIYDw(QOi, '%a, %d %b %Y %H:%M:%S %Z'))
    except:
        rORxvJZex = 0
        SDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.loaded.num')
        open(SDPjW, 'w').close()
        rORxvFRlY = SDPjW


def rVTsb_Xhn_PcGXJs_XRdCCq():
    if sublime.platform() == 'osx':
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        vKqyj = CFTvj.get('gpu_window_buffer', 'auto')
        if isinstance(vKqyj, bool) and vKqyj == False:
            pass
        else:
            CFTvj.set('gpu_window_buffer', False)
            sublime.message_dialog("GUNA MESSAGE :\n\nTo prevent flickering for OSX, 'gpu_window_buffer' is set as false.\nPlease, restart sublime text.\n\nIf you don't want this message, set 'gpu_window_buffer_false': false in Guna.sublime-settings")


def icons():
    CYVsIHck = sublime.load_settings('Package Control.sublime-settings')
    if XsfDJ_GSVevAZ in CYVsIHck.get('installed_packages', []):
        return
    xQDdfA = sublime.ok_cancel_dialog("GUNA MESSAGE :\n\nGuna recommends 'A File Icon' for sidebar icons. Do you want to install it?", 'Install')
    if xQDdfA:
        print('Installing `{}` ...'.format(XsfDJ_GSVevAZ))
        sublime.active_window().run_command('advanced_install_package', {'packages': XsfDJ_GSVevAZ})


def QWHf_UijhJ():
    print('GUNA : ERROR ________________________________________________')
    traceback.print_exc()
    print('============================================================')
    api.GunaApi.alert_message(3, ' GUNA : Error is occured. Please, see the trace-back message in Sublime console.', 10, 1)


def GWBuCEN():
    return datetime.now()


def SHXcvIksfH(arg):
    return datetime.fromtimestamp(arg)


def bOZuIYDw(arg1, arg2):
    return time.mktime(time.strptime(arg1, arg2))


class VIcqgHVxmZkyvX(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name='prproc')
        self.fIXj = False

    def run(self):
        try:
            time.sleep(1)
            if not self.fIXj:
                engine_reload()
        except Exception:
            QWHf_UijhJ()

    def stop(self):
        self.fIXj = True


class VIcqwEicmZkyvX(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name='fkproc')
        self.fIXj = False

    def run(self):
        while True:
            try:
                if self.fIXj:
                    break
                xG_qAYmw = rVTsb_kzIWTx('mnproc', stop=True)
                if xG_qAYmw:
                    time.sleep(1)
                else:
                    vIcq_JyjxSw = VIcqDQZfmZkyvX()
                    vIcq_JyjxSw.setDaemon(True)
                    vIcq_JyjxSw.start()
                    break
            except Exception:
                QWHf_UijhJ()
                break

    def stop(self):
        self.fIXj = True


class VIcqDQZfmZkyvX(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name='mnproc')
        self.fIXj = False
        self.GWRa = 0

    def run(self):
        while True:
            try:
                time.sleep(30)
                self.GWRa = 0 if self.GWRa == 1000 else self.GWRa + 1
                if self.fIXj:
                    break
                VIcqDQZfmZkyvX.hSi_IYDw()
                VIcqDQZfmZkyvX.hSi_SQkw()
                VIcqDQZfmZkyvX.hSi_nURlYWk(self.GWRa)
            except Exception:
                QWHf_UijhJ()
                break

    def stop(self):
        self.fIXj = True

    def hHPjlI(self):
        return not self.fIXj

    @staticmethod
    def rZTqC_XfbK():
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        rVPdxU = False
        for k in persist.VkCQ_yEAL:
            if CFTvj.has(k):
                rVPdxU = True
                CFTvj.erase(k)
                continue

        # if rVPdxU:
        #     sublime.save_settings('Preferences.sublime-settings')

    @staticmethod
    def rZTqC_gjWK():
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        for k in persist.VkCQ_hIWy:
            if CFTvj.has(k):
                CFTvj.erase(k)
                continue

    @staticmethod
    def rZTqC_NaUYXn_IodbN(xG_wlDR):
        try:
            if xG_wlDR:
                GDPjW = os.path.join(sublime.packages_path(), 'zzz Guna Widget zzz')
                if os.path.exists(GDPjW):
                    shutil.rmtree(GDPjW)
            else:
                CFTvj = sublime.load_settings('Preferences.sublime-settings')
                GVTcv = CFTvj.get('theme', '')
                GDPjW = os.path.join(sublime.packages_path(), 'zzz Guna Widget zzz/themes')
                for _dir in os.walk(GDPjW):
                    SWauj = _dir[2]
                    for _file in SWauj:
                        if _file != GVTcv:
                            GTXbv = os.path.join(GDPjW, _file)
                            os.remove(GTXbv)
                            continue

        except:
            pass

    @staticmethod
    def xBXj_FiwWK(CFTvj, vIcqj, xG_wlDR, lWVeC):
        global lWswvJ_aEVXr
        rIghvDk_lWmm = {}
        for k in persist.VkCQ_hIWy:
            if CFTvj.has(k):
                v = CFTvj.get(k)
                rIghvDk_lWmm[k] = v
                continue

        rVPdxU = False
        rVTsb_JwKK = {}
        if xG_wlDR or lWVeC:
            hSii = vIcqj.get('sidebar_widget', [])
            if len(hSii) > 0:
                lWswvJ_aEVXr = lWswvJ_aEVXr % len(hSii)
                if hSii[lWswvJ_aEVXr] == 'clock':
                    lWswvJ_lrHX = 1
                    rVTsb_JwKK[persist.Vdn_NaUYXn_WgkzG] = True
                else:
                    if hSii[lWswvJ_aEVXr] == 'date':
                        lWswvJ_lrHX = 2
                        rVTsb_JwKK[persist.Vdn_NaUYXn_XVpb] = True
                    else:
                        if hSii[lWswvJ_aEVXr] == 'weather':
                            lWswvJ_lrHX = 3
                            rVTsb_JwKK[persist.Vdn_NaUYXn_QZwODBp] = True
                        else:
                            lWswvJ_lrHX = 0
                            rVTsb_JwKK[persist.Vdn_NaUYXn_Iab] = True
            else:
                lWswvJ_lrHX = 0
                rVTsb_JwKK[persist.Vdn_NaUYXn_Iab] = True
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'hide_tab_close', persist.Vdj_yaUW_nvV_yGKPc, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'hide_tab_dropdown', persist.Vdj_yaUW_nvV_zMKmbnUm, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'overlay_scroll_bars', persist.Vdj_FnxJeut_NyMKij_ZZrt, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'scroll_bars_convex', persist.Vdj_JuIGef_VVnp_ZmKTDx, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'sidebar_selected_box', persist.Vdj_JaUWuuK_wkS, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'sidebar_head', persist.Vdj_JaUWuuK_caxZ, False)
            VIcqDQZfmZkyvX.hSi_QEFd(vIcqj, rVTsb_JwKK, 'title_bar_color', persist.Vdj_kaKDX_UUm_zKimO, False)
            if vIcqj.get('sidebar_widget_on_other_theme', True):
                rVTsb_JwKK[persist.Vdn_NaUYXn_IodbN] = True
            for k in rIghvDk_lWmm.keys():
                if k in rVTsb_JwKK:
                    if rIghvDk_lWmm[k] != rVTsb_JwKK[k]:
                        CFTvj.set(k, rVTsb_JwKK[k])
                        rVPdxU = True
                else:
                    CFTvj.erase(k)
                    rVPdxU = True

            for k in rVTsb_JwKK.keys():
                if k not in rIghvDk_lWmm:
                    CFTvj.set(k, rVTsb_JwKK[k])
                    rVPdxU = True
                    continue

            if lWswvJ_lrHX == 1:
                VIcqDQZfmZkyvX.hSi_IYDw()
            if lWswvJ_lrHX == 2:
                VIcqDQZfmZkyvX.hSi_SQkw()
            if lWswvJ_lrHX == 3:
                VIcqDQZfmZkyvX.hSi_nURlYWk()
        else:
            for k in persist.VkCQ_hIWy:
                if CFTvj.has(k):
                    CFTvj.erase(k)
                    rVPdxU = True
                    continue

        # if rVPdxU:
        #     sublime.save_settings('Preferences.sublime-settings')

    @staticmethod
    def hSi_QEFd(vIcqj, pref_sets, gitem, CWiud, default):
        hSii = vIcqj.get(gitem, default)
        if hSii != default:
            pref_sets[CWiud] = hSii

    @staticmethod
    def hSi_EHwp(vIcqj, pref_sets, gitem, CWiud, default):
        hSii = vIcqj.get(gitem, default)
        CWiud = CWiud + hSii.lower()
        if hSii != default:
            if any(CWiud == s for s in persist.VkCQ_hIWy):
                pref_sets[CWiud] = True

    @staticmethod
    def tFPiv_gjxXL(CFTvj, key):
        if CFTvj.has(key):
            CFTvj.erase(key)

    @staticmethod
    def rZTqC_Xfv():
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdt_uaILR)
        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdt_iwtV_iGFT)
        for x in range(0, 24):
            zGih = 'gnc_h{:02d}'.format(x)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        for w in range(0, 7):
            for x in range(0, 6):
                zGih = 'gnc_w{:d}m1{:d}'.format(w, x)
                VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        for x in range(0, 10):
            zGih = 'gnc_m0{:d}'.format(x)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        # sublime.save_settings('Preferences.sublime-settings')
        if not hHDfEUu:
            sublime.set_timeout_async(VIcqDQZfmZkyvX.hSi_IYDw, 1000)

    @staticmethod
    def hSi_IYDw():
        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        vIcqj, lWswI, lWVeC, xG_sAETc = vSi_xKesl('clock')
        if not xG_wlDR and not lWVeC or not xG_sAETc:
            return
        else:
            rVTsb_JltLNm(CFTvj=CFTvj, IWTm=None)
            ACL = GWBuCEN()
            if vIcqj.get('sidebar_widget_clock_mode', '24h') == '24h':
                UCJh = ACL.hour
            else:
                UCJh = 12 if ACL.hour % 12 == 0 else ACL.hour % 12
            UFZup = VIcqDQZfmZkyvX.vSi_WELj(UCJh)
            b1Zup = VIcqDQZfmZkyvX.vSi_nNDaE1q(ACL.weekday(), ACL.minute)
            b0Zup = VIcqDQZfmZkyvX.vSi_dYe0O(ACL.minute)
            if not CFTvj.has(UFZup):
                for x in range(0, 24):
                    zGih = 'gnc_h{:02d}'.format(x)
                    VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(UFZup, True)
            if not CFTvj.has(b1Zup):
                for x in range(0, 7):
                    for y in range(0, 6):
                        zGih = 'gnc_w{:d}m1{:d}'.format(x, y)
                        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(b1Zup, True)
            if not CFTvj.has(b0Zup):
                for x in range(0, 10):
                    zGih = 'gnc_m0{:d}'.format(x)
                    VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(b0Zup, True)
            return

    @staticmethod
    def vSi_WELj(UCJh):
        UGih = 'gnc_h{:02d}'.format(UCJh)
        return UGih

    @staticmethod
    def vSi_dYe1O(min):
        return 'gnc_m1' + str(min // 10)

    @staticmethod
    def vSi_dYe0O(min):
        return 'gnc_m0' + str(min - 10 * (min // 10))

    @staticmethod
    def vSi_nNDaE1q(wday, min):
        return 'gnc_w' + str(wday) + 'm1' + str(min // 10)

    @staticmethod
    def rZTqC_XfU():
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdt_uaILR)
        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdt_iwtV_iGFT)
        for x in range(1, 13):
            zGih = 'gnd_m{:02d}'.format(x)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        for w in range(0, 7):
            for x in range(0, 4):
                zGih = 'gnd_w{:d}d1{:d}'.format(w, x)
                VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        for x in range(0, 10):
            zGih = 'gnd_d0{:d}'.format(x)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        # sublime.save_settings('Preferences.sublime-settings')
        if not hHDfEUu:
            sublime.set_timeout_async(VIcqDQZfmZkyvX.hSi_IYDw, 1000)

    @staticmethod
    def hSi_SQkw():
        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        vIcqj, lWswI, lWVeC, xG_trJV = vSi_xKesl('date')
        if not xG_wlDR and not lWVeC or not xG_trJV:
            return
        else:
            rVTsb_JltLNm(CFTvj=CFTvj, IWTm=None)
            ACL = GWBuCEN()
            bBZup = VIcqDQZfmZkyvX.vSi_dEelY(ACL.month)
            Q1Zup = VIcqDQZfmZkyvX.vSi_nNusr1q(ACL.weekday(), ACL.day)
            Q0Zup = VIcqDQZfmZkyvX.vSi_SQP0O(ACL.day)
            if not CFTvj.has(bBZup):
                for x in range(1, 13):
                    zGih = 'gnd_m{:02d}'.format(x)
                    VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(bBZup, True)
            if not CFTvj.has(Q1Zup):
                for x in range(0, 7):
                    for y in range(0, 4):
                        zGih = 'gnd_w{:d}d1{:d}'.format(x, y)
                        VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(Q1Zup, True)
            if not CFTvj.has(Q0Zup):
                for x in range(0, 10):
                    zGih = 'gnd_d0{:d}'.format(x)
                    VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

                CFTvj.set(Q0Zup, True)
            return

    @staticmethod
    def vSi_dEelY(month):
        bGih = 'gnd_m{:02d}'.format(month)
        return bGih

    @staticmethod
    def vSi_SQP0O(day):
        return 'gnd_d0' + str(day - 10 * (day // 10))

    @staticmethod
    def vSi_nNusr1q(wday, day):
        return 'gnd_w' + str(wday) + 'd1' + str(day // 10)

    @staticmethod
    def hSi_nURlYWk(tick=0):
        global ACZ_tDk
        CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
        vIcqj, lWswI, lWVeC, xG_mvQkzxJ = vSi_xKesl('weather')
        if not xG_wlDR and not lWVeC or not xG_mvQkzxJ:
            return
        lWiud = False
        for x in persist.VkCQ_oxSmbzLN:
            zGih = 'gnw_0' + x
            if CFTvj.has(zGih):
                lWiud = True
                continue

        if lWiud and tick % 20 != 0:
            return
        if not lWiud and ACZ_tDk > 5:
            return
        ok, l0XsC, l3XsC, l6XsC = VIcqDQZfmZkyvX.vSi_nURlYWk()
        if not ok:
            ACZ_tDk += 1
        else:
            ACZ_tDk = 0
        if not CFTvj.has(l0XsC):
            for x in persist.VkCQ_oxSmbzLN:
                zGih = 'gnw_0' + x
                VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

            if ok:
                CFTvj.set(l0XsC, True)
        if not CFTvj.has(l3XsC):
            for x in persist.VkCQ_oxSmbzLN:
                zGih = 'gnw_3' + x
                VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

            if ok:
                CFTvj.set(l3XsC, True)
        if not CFTvj.has(l6XsC):
            for x in persist.VkCQ_oxSmbzLN:
                zGih = 'gnw_6' + x
                VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

            if ok:
                CFTvj.set(l6XsC, True)

    @staticmethod
    def vSi_nURlYWk():
        SDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache')
        if not os.path.exists(SDPjW):
            os.makedirs(SDPjW)
        lDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.weather')
        SDPjW = os.path.join(sublime.cache_path(), 'Guna', 'cache', '.forecast')
        vIcqj, lWswI, lWVeC, xG_mvQkzxJ = vSi_xKesl('weather')
        if vIcqj.has('weather'):
            lSPiI = vIcqj.get('weather')
            if 'appid' in lSPiI:
                pDeyS = str(lSPiI['appid'])
            else:
                pDeyS = ''
            if 'city_name' in lSPiI:
                rBPcv = str(lSPiI['city_name']).lower()
            else:
                rBPcv = ''
            if 'geographic' in lSPiI:
                vSDwG = lSPiI['geographic']
                if 'lat' in vSDwG:
                    vCaqI = int(vSDwG.get('lat'))
                else:
                    vCaqI = -1
                if 'lon' in vSDwG:
                    vCaeC = int(vSDwG.get('lon'))
                else:
                    vCaeC = -1
            else:
                vSDwG = None
                vCaqI = -1
                vCaeC = -1
            if 'proxy' in lSPiI:
                CFDnp = lSPiI['proxy']
            else:
                CFDnp = ''
        try:
            ESPt_EB = False
            lSPjWZJ = {}
            SQPiIZJ = {}
            if not os.path.exists(lDPjW) or not os.path.exists(SDPjW):
                VIcqDQZfmZkyvX.jDsqIU_oxSmbzL(lDPjW, SDPjW, pDeyS, rBPcv, vSDwG, vCaqI, vCaeC, CFDnp)
                ESPt_EB, lSPjWZJ, SQPiIZJ = VIcqDQZfmZkyvX.ESPt_MVsKZXl(lDPjW, SDPjW)
            else:
                ESPt_EB, lSPjWZJ, SQPiIZJ = VIcqDQZfmZkyvX.ESPt_MVsKZXl(lDPjW, SDPjW)
                if ESPt_EB:
                    ACLtI = GWBuCEN()
                    lSPtI = SHXcvIksfH(lSPjWZJ['dt'])
                    QSajr = ACLtI - lSPtI
                    rWioC = str(lSPjWZJ['name']).lower() + ',' + str(lSPjWZJ['sys']['country']).lower()
                    if QSajr.seconds > 1800 or rBPcv != rWioC:
                        VIcqDQZfmZkyvX.jDsqIU_oxSmbzL(lDPjW, SDPjW, pDeyS, rBPcv, vSDwG, vCaqI, vCaeC, CFDnp)
                        ESPt_EB, lSPjWZJ, SQPiIZJ = VIcqDQZfmZkyvX.ESPt_MVsKZXl(lDPjW, SDPjW)
                else:
                    VIcqDQZfmZkyvX.jDsqIU_oxSmbzL(lDPjW, SDPjW, pDeyS, rBPcv, vSDwG, vCaqI, vCaeC, CFDnp)
                    ESPt_EB, lSPjWZJ, SQPiIZJ = VIcqDQZfmZkyvX.ESPt_MVsKZXl(lDPjW, SDPjW)
            if ESPt_EB:
                lSPtI = SHXcvIksfH(lSPjWZJ['dt'])
                SCgsI = SHXcvIksfH(SQPiIZJ['list'][0]['dt'])
                QSajr = SCgsI - lSPtI
                l0XsC = 'gnw_0' + str(lSPjWZJ['weather'][0]['icon'])[:2]
                if QSajr.seconds < 5400:
                    l3XsC = 'gnw_3' + str(SQPiIZJ['list'][1]['weather'][0]['icon'])[:2]
                    l6XsC = 'gnw_6' + str(SQPiIZJ['list'][2]['weather'][0]['icon'])[:2]
                else:
                    l3XsC = 'gnw_3' + str(SQPiIZJ['list'][0]['weather'][0]['icon'])[:2]
                    l6XsC = 'gnw_6' + str(SQPiIZJ['list'][1]['weather'][0]['icon'])[:2]
                return (True, l0XsC, l3XsC, l6XsC)
            else:
                return (False, 'gnw_0xx', 'gnw_3xx', 'gnw_6xx')
        except:
            QWHf_UijhJ()
            return (False, 'gnw_0xx', 'gnw_3xx', 'gnw_6xx')

        return

    @staticmethod
    def ESPt_MVsKZXl(lDPjW, SDPjW):
        ESPt_EB = False
        lSPjWZJ = {}
        SQPiIZJ = {}
        try:
            if os.path.exists(lDPjW):
                with open(lDPjW, 'r', encoding='utf8') as (dfile):
                    lSPjWZJ = json.load(dfile)
            if os.path.exists(SDPjW):
                with open(SDPjW, 'r', encoding='utf8') as (dfile):
                    SQPiIZJ = json.load(dfile)
            if 'dt' in lSPjWZJ:
                if 'list' in SQPiIZJ:
                    ESPt_EB = True
        except:
            pass

        return (
         ESPt_EB, lSPjWZJ, SQPiIZJ)

    @staticmethod
    def jDsqIU_oxSmbzL(lDPjW, SDPjW, pDeyS, rBPcv, vSDwG, vCaqI, vCaeC, CFDnp):
        try:
            if pDeyS != '' and (rBPcv != '' or vSDwG != None and vCaqI != -1 and vCaeC != -1):
                if rBPcv != '':
                    lZXdb = 'http://api.openweathermap.org/data/2.5/weather?q=' + rBPcv + '&APPID=' + pDeyS
                    SZXdb = 'http://api.openweathermap.org/data/2.5/forecast?q=' + rBPcv + '&APPID=' + pDeyS
                else:
                    lZXdb = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(vCaqI) + '&lon=' + str(vCaeC) + '&APPID=' + pDeyS
                    SZXdb = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + str(vCaqI) + '&lon=' + str(vCaeC) + '&APPID=' + pDeyS
                jFahh = urllib.request.Request(lZXdb)
                if CFDnp != '':
                    jFahh.set_proxy(CFDnp, 'http')
                jFatr = urllib.request.urlopen(jFahh)
                lSPjW = jFatr.read().decode('utf-8')
                lXHeC = json.loads(lSPjW)
                if 'dt' in lXHeC:
                    with open(lDPjW, 'w', newline='', encoding='utf8') as (dfile):
                        json.dump(lXHeC, dfile)
                    jFahh = urllib.request.Request(SZXdb)
                    if CFDnp != '':
                        jFahh.set_proxy(CFDnp, 'http')
                    jFatr = urllib.request.urlopen(jFahh)
                    lSPjW = jFatr.read().decode('utf-8')
                    lXHeC = json.loads(lSPjW)
                    with open(SDPjW, 'w', newline='', encoding='utf8') as (dfile):
                        json.dump(lXHeC, dfile)
                else:
                    VIcqDQZfmZkyvX.rZTqC_NwtLayK_aeGAP(lDPjW, SDPjW)
            else:
                VIcqDQZfmZkyvX.rZTqC_NwtLayK_aeGAP(lDPjW, SDPjW)
        except:
            VIcqDQZfmZkyvX.rZTqC_NwtLayK_aeGAP(lDPjW, SDPjW)
            QWHf_UijhJ()

        return

    @staticmethod
    def rZTqC_NwtLayK_aeGAP(lDPjW, SDPjW):
        if os.path.exists(lDPjW):
            os.remove(lDPjW)
        if os.path.exists(SDPjW):
            os.remove(SDPjW)

    @staticmethod
    def rZTqC_Xfp():
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        for x in persist.VkCQ_oxSmbzLN:
            zGih = 'gnw_0' + x
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)
            zGih = 'gnw_3' + x
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)
            zGih = 'gnw_6' + x
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, zGih)

        # sublime.save_settings('Preferences.sublime-settings')
        if not hHDfEUu:
            sublime.set_timeout_async(VIcqDQZfmZkyvX.hSi_nURlYWk, 1000)

    @staticmethod
    def hKXjtX_obVZyM():
        global lWswvJ_aEVXr
        CFTvj = sublime.load_settings('Preferences.sublime-settings')
        vIcqj = sublime.load_settings('Guna.sublime-settings')
        lWswI = vIcqj.get('sidebar_widget', [])
        if len(lWswI) > 0:
            lWswvJ_aEVXr = (lWswvJ_aEVXr + 1) % len(lWswI)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdn_NaUYXn_WgkzG)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdn_NaUYXn_XVpb)
            VIcqDQZfmZkyvX.tFPiv_gjxXL(CFTvj, persist.Vdn_NaUYXn_QZwODBp)
            if lWswI[lWswvJ_aEVXr] == 'clock':
                CFTvj.set(persist.Vdn_NaUYXn_WgkzG, True)
            else:
                if lWswI[lWswvJ_aEVXr] == 'date':
                    CFTvj.set(persist.Vdn_NaUYXn_XVpb, True)
                elif lWswI[lWswvJ_aEVXr] == 'weather':
                    CFTvj.set(persist.Vdn_NaUYXn_QZwODBp, True)

    @staticmethod
    def rVTsb_VpGAkyW():
        vIcqj = sublime.load_settings('Guna.sublime-settings')
        dKcuG = vIcqj.get('dKcuG', '')
        hVPxM = str(hashlib.sha256(dKcuG.encode()))
        if hVPxM.startswith('0c896fc0b5abf1f'):
            return False
        else:
            AHXcv = vSi_IYDw()
            if AHXcv >= GWBujJReG:
                return True
            return False


class GunaEventListener(sublime_plugin.EventListener):

    def on_new_async(self, IWTm):
        rVTsb_JltLNm(CFTvj=None, IWTm=IWTm)
        return

    def on_load_async(self, IWTm):
        rVTsb_JltLNm(CFTvj=None, IWTm=IWTm)
        return

    def on_modified_async(self, IWTm):
        rVTsb_JltLNm(CFTvj=None, IWTm=IWTm)
        return

    def on_activated_async(self, IWTm):
        SWau_DRex = IWTm.file_name()
        if isinstance(SWau_DRex, str):
            if any(SWau_DRex.endswith(p) for p in YCRa_VZdx_iuMB):
                IWTm.set_read_only(True)
        rVTsb_JltLNm(CFTvj=None, IWTm=IWTm)
        return

    def on_post_save_async(self, IWTm):
        rVTsb_JltLNm(CFTvj=None, IWTm=IWTm)
        return

    def on_close(self, IWTm):
        global tLeyGUu
        SWau_DRex = IWTm.file_name()
        if isinstance(SWau_DRex, str):
            if not tLeyGUu:
                if not hHDfEUu and (SWau_DRex.endswith('User/Preferences.sublime-settings') or SWau_DRex.endswith('User\\Preferences.sublime-settings')):
                    VIcqDQZfmZkyvX.rZTqC_Xfv()
                    VIcqDQZfmZkyvX.rZTqC_Xfp()
                    VIcqDQZfmZkyvX.rZTqC_XfU()


class GunaSwitchWidget(sublime_plugin.WindowCommand):

    def run(self):
        VIcqDQZfmZkyvX.hKXjtX_obVZyM()


class GunaSetTheme(sublime_plugin.WindowCommand):

    def run(self):
        try:
            ESReGT_lYWFy()
            GWBujJReG_ = 1573354800
            CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
            CFTvj = sublime.load_settings('Preferences.sublime-settings')
            CFTvj.set('theme', 'Guna.sublime-theme')
            CFTvj.set('color_scheme', 'Packages/Guna/themes/Guna.sublime-color-scheme')
            # sublime.save_settings('Preferences.sublime-settings')
        except Exception:
            QWHf_UijhJ()


class GunaToggleFullScreen(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = sublime.active_window()
            w.run_command('toggle_full_screen')
            CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
            vIcqj = sublime.load_settings('Guna.sublime-settings')
            SIabj = vIcqj.get('full_screen_on_start', False)
            if xG_wlDR:
                if SIabj:
                    w.set_menu_visible(not w.is_menu_visible())
        except Exception:
            QWHf_UijhJ()


class GunaReadme(sublime_plugin.WindowCommand):

    def run(self):
        try:
            w = sublime.active_window()
            for v in w.views():
                if v.name() == 'Guna - README':
                    v.close()
                    continue

            IWTm = sublime.active_window().new_file()
            IWTm.set_name('Guna - README')
            IWTm.settings().set('gutter', False)
            IWTm.settings().set('line_numbers', False)
            UHBb = str(sublime.load_resource('Packages/Guna/.guna/guna-readme.html'))
            IWTm.add_phantom('guna-readme', sublime.Region(0), UHBb, sublime.LAYOUT_INLINE, on_navigate=self.on_navigate)
            IWTm.set_read_only(True)
            IWTm.set_scratch(True)
        except Exception:
            QWHf_UijhJ()

    def on_navigate(self, href):
        try:
            webbrowser.open(href)
        except Exception:
            QWHf_UijhJ()


class GunaIssue(sublime_plugin.WindowCommand):

    def run(self):
        try:
            webbrowser.open_new_tab('https://github.com/poucotm/Guna/issues')
        except Exception:
            QWHf_UijhJ()


GWBujJReG = 1731207600
Hs1Esb = re.compile('(?P<front>.*?)#scale1\\s+(?:((?P<el00>[\\d]+)-(?P<el01>[\\d]+))|(?P<el0>[\\d\\-]+))(?P<back>.*)')
Hs2Esb = re.compile('(?P<front>.*?)#scale2-(?P<eli>[\\d]+)\\s*\\[(?P<el0>[\\d]+)\\s*,\\s*(?P<el1>[\\d]+)\\](?P<back>.*)')
Hs4Esb = re.compile('(?P<front>.*?)#scale4-(?P<eli>[\\d]+)\\s*\\[(?P<el0>[\\d]+)\\s*,\\s*(?P<el1>[\\d]+)\\s*,\\s*(?P<el2>[\\d]+)\\s*,\\s*(?P<el3>[\\d]+)\\](?P<back>.*)')
Hm2Esb = re.compile('(?P<front>.*?)#switch-scale2-(?P<eli>[\\d]+)\\s*\\[(?P<el0>[\\d]+)\\s*,\\s*(?P<el1>[\\d]+)\\](?P<back>.*)')
RcxEsb = re.compile('"content_margin"\\s*:\\s*\\[\\s*\\d+\\s*,\\s*\\d+\\s*\\]')
PvzEsb = re.compile('"size"\\s*:\\s*\\d+')
aiIFRl = ''

class GunaTweakTheme(sublime_plugin.WindowCommand):
    VkCQ_uhDHln = [
     'white', 'red', 'green', 'blue', 'yellow', 'orange', 'lBlue', 'rOrange', 'lOrange']

    def run(self):
        global HjKUi
        global YOHj_RXuCJ
        global YOHj_WFhKK
        global aiIFRl
        try:
            CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
            if not xG_wlDR:
                return
            rGRxd = CFTvj.get('color_scheme')
            vIcqt = rAe_jJi(rGRxd, 'Packages/Guna/themes/Guna.sublime-color-scheme')
            vIcqj = sublime.load_settings('Guna.sublime-settings')
            GHqqG = vIcqj.get('title_bar_color', True)
            if not vIcqt:
                if HjKUi >= 3150:
                    hHNbv = vSi_jJPdx()
                    OURbG = hHNbv.get('background')
                else:
                    rGRxd = CFTvj.get('color_scheme')
                    rGinI = str(sublime.load_resource(rGRxd))
                    GFTuE = plistlib.readPlistFromBytes(rGinI.encode())
                    OURbG = GFTuE['settings'][0]['settings']['background']
            else:
                OURbG = vIcqj.get('guna_bgcolor', '#161C23')
                rGDfI = vIcqj.get('guna_color_saturation', 100)
                rPDfI = vIcqj.get('guna_color_brightness', 100)
                vRRbG = vIcqj.get('guna_guide', '#20272E')
                pURbG = vIcqj.get('guna_active_guide', '#AAFF9954')
                OFRbG = vIcqj.get('guna_brackets_color', '#FF0000')
                GURbG = vIcqj.get('guna_tags_color', '#FF5242')
                OFDfI = vIcqj.get('guna_brackets_options', 'foreground')
                GUDfI = vIcqj.get('guna_tags_options', 'foreground')
                vCejj = str(rGDfI) + str(rPDfI) + vRRbG + pURbG + OFRbG + GURbG + OFDfI + GUDfI + str(GHqqG)
                YOHj_RXuCJ = OURbG
                YOHj_WFhKK = vCejj
            GHmj = str(sublime.load_resource('Packages/Guna/.guna/guna.sublime-theme-templ'))
            lHmj = str(sublime.load_resource('Packages/Guna/.guna/widget-guna.sublime-color-scheme-templ'))
            if vIcqt:
                rHmj = str(sublime.load_resource('Packages/Guna/.guna/guna.sublime-color-scheme-templ'))
            rPPiv = self.rCcl_XVp_UHfjL(OURbG)
            h, s, v = colorsys.rgb_to_hsv(rPPiv[0], rPPiv[1], rPPiv[2])
            if v >= 200:
                vIcqj = sublime.load_settings('Guna-light.sublime-settings')
            else:
                vIcqj = sublime.load_settings('Guna-dark.sublime-settings')
            if v >= 230:
                rZHj = [
                 5, 4, 3, 2, 1]
                for t in rZHj:
                    hFRi = '#base-color+{0}i'.format(t)
                    QSHj = '"color(var(--background) l(- {0}%))"'.format(t * 2)
                    QSHm = 'color(var(bgcolor) l(- {0}%))'.format(t * 2)
                    GHmj = GHmj.replace(hFRi, QSHj)
                    lHmj = lHmj.replace(hFRi, QSHm)
                    hFRi = '#base-color-{0}i'.format(t)
                    QSHj = '"color(var(--background) l(+ {0}%))"'.format(t * 2)
                    QSHm = 'color(var(bgcolor) l(+ {0}%))'.format(t * 2)
                    GHmj = GHmj.replace(hFRi, QSHj)
                    lHmj = lHmj.replace(hFRi, QSHm)

                GHmj = GHmj.replace('#dark-', '//')
                GHmj = GHmj.replace('#light-', '')
            else:
                rZHj = [
                 5, 4, 3, 2, 1]
                for t in rZHj:
                    hFRi = '#base-color+{0}i'.format(t)
                    QSHj = '"color(var(--background) l(+ {0}%))"'.format(t * 2)
                    QSHm = 'color(var(bgcolor) l(+ {0}%))'.format(t * 2)
                    GHmj = GHmj.replace(hFRi, QSHj)
                    lHmj = lHmj.replace(hFRi, QSHm)
                    hFRi = '#base-color-{0}i'.format(t)
                    QSHj = '"color(var(--background) l(- {0}%))"'.format(t * 2)
                    QSHm = 'color(var(bgcolor) l(- {0}%))'.format(t * 2)
                    GHmj = GHmj.replace(hFRi, QSHj)
                    lHmj = lHmj.replace(hFRi, QSHm)

                GHmj = GHmj.replace('#dark-', '')
                GHmj = GHmj.replace('#light-', '//')
            if GHqqG:
                GHmj = GHmj.replace('#title-bar', '')
            else:
                GHmj = GHmj.replace('#title-bar', '//')
            lHmj = lHmj.replace('#base-color', OURbG)
            if vIcqt:
                rHmj = rHmj.replace('#base-color', OURbG)
                rHmj = rHmj.replace('#guide-color', vRRbG)
                rHmj = rHmj.replace('#active-guide-color', pURbG)
                rHmj = rHmj.replace('#bracket-color', OFRbG)
                rHmj = rHmj.replace('#tag-color', GURbG)
                if OFDfI in ('foreground', 'underline', 'stippled_underline', 'squiggly_underline'):
                    rHmj = rHmj.replace('#bracket-option', OFDfI)
                if GUDfI in ('foreground', 'underline', 'stippled_underline', 'squiggly_underline'):
                    rHmj = rHmj.replace('#tag-option', GUDfI)
                ESVn = '"(?P<name>[\\w]+)"\\s*:\\s*"#(?P<color>[\\w]+)"'
                dPyj = re.compile(ESVn)
                for mtch in dPyj.finditer(rHmj):
                    if mtch.group('name') in GunaTweakTheme.VkCQ_uhDHln:
                        dHTnI = mtch.group()
                        rPPiv = self.rCcl_XVp_UHfjL('#' + mtch.group('color'))
                        h, s, v = colorsys.rgb_to_hsv(rPPiv[0], rPPiv[1], rPPiv[2])
                        v = v * (float(rPDfI) / 100.0)
                        v = 255 if v > 255 else v
                        s = s * (float(rGDfI) / 100.0)
                        s = 1.0 if s > 1.0 else s
                        r, g, b = colorsys.hsv_to_rgb(h, s, v)
                        ULRbG = '#{:02X}{:02X}{:02X}'.format(int(r), int(g), int(b))
                        AHTnI = dHTnI.replace('#' + mtch.group('color'), ULRbG)
                        rHmj = rHmj.replace(dHTnI, AHTnI)
                        continue

            rPRbG = vIcqj.get('clock.color', '#FFCC67')
            rPRbG = str(self.rCcl_XVp_UHfjL(rPRbG))
            rRRbG = vIcqj.get('clock.color.dirty', '#FF3377')
            rRRbG = str(self.rCcl_XVp_UHfjL(rRRbG))
            rFRbG = vIcqj.get('clock.color.readonly', '#B4B4B4')
            rFRbG = str(self.rCcl_XVp_UHfjL(rFRbG))
            rORbG = vIcqj.get('clock.color.alert', '#FF1919')
            rORbG = str(self.rCcl_XVp_UHfjL(rORbG))
            rWRbG = vIcqj.get('clock.color.info', '#19FFFF')
            rWRbG = str(self.rCcl_XVp_UHfjL(rWRbG))
            GHmj = GHmj.replace('#clock-color-dirty', rRRbG)
            GHmj = GHmj.replace('#clock-color-readonly', rFRbG)
            GHmj = GHmj.replace('#clock-color-alert', rORbG)
            GHmj = GHmj.replace('#clock-color-info', rWRbG)
            GHmj = GHmj.replace('#clock-color', rPRbG)
            xPRbG = vIcqj.get('icon.color', '#677A83')
            xPRbG = str(self.rCcl_XVp_UHfjL(xPRbG))
            xGRbG = vIcqj.get('icon.color.selected', '#FFCC67')
            xGRbG = str(self.rCcl_XVp_UHfjL(xGRbG))
            xDRbG = vIcqj.get('icon.color.pressed', '#FF5500')
            xDRbG = str(self.rCcl_XVp_UHfjL(xDRbG))
            xVRbG = vIcqj.get('icon.color.hover', '#FF5500')
            xVRbG = str(self.rCcl_XVp_UHfjL(xVRbG))
            GHmj = GHmj.replace('#icon-color-selected', xGRbG)
            GHmj = GHmj.replace('#icon-color-pressed', xDRbG)
            GHmj = GHmj.replace('#icon-color-hover', xVRbG)
            GHmj = GHmj.replace('#icon-color', xPRbG)
            GPRbG = vIcqj.get('tab_font.color', '#969696')
            GPRbG = str(self.rCcl_XVp_UHfjL(GPRbG))
            GGRbG = vIcqj.get('tab_font.color.selected', '#FFFFFF')
            GGRbG = str(self.rCcl_XVp_UHfjL(GGRbG))
            GVRbG = vIcqj.get('tab_font.color.hover', '#FFCC67')
            GVRbG = str(self.rCcl_XVp_UHfjL(GVRbG))
            GRRbG = vIcqj.get('tab_font.color.dirty', '#F92672')
            GIRbG = GRRbG + '96'
            GRRbG = str(self.rCcl_XVp_UHfjL(GRRbG))
            GIRbG = str(self.rCcl_XVp_UHfjL(GIRbG))
            GHmj = GHmj.replace('#tab-font-color-selected', GGRbG)
            GHmj = GHmj.replace('#tab-font-color-hover', GVRbG)
            GHmj = GHmj.replace('#tab-font-color-dirty-unsel', GIRbG)
            GHmj = GHmj.replace('#tab-font-color-dirty', GRRbG)
            GHmj = GHmj.replace('#tab-font-color', GPRbG)
            YPRbG = vIcqj.get('label_font.color', '#969696')
            YPRbG = str(self.rCcl_XVp_UHfjL(YPRbG))
            GHmj = GHmj.replace('#label-font-color', YPRbG)
            hPRbG = vIcqj.get('sidebar_font.color', '#969696')
            hPRbG = str(self.rCcl_XVp_UHfjL(hPRbG))
            hGRbG = vIcqj.get('sidebar_font.color.selected', '#FFFFFF')
            hGRbG = str(self.rCcl_XVp_UHfjL(hGRbG))
            hVRbG = vIcqj.get('sidebar_head.color', '#FFFFFF')
            hVRbG = str(self.rCcl_XVp_UHfjL(hVRbG))
            GHmj = GHmj.replace('#sidebar-font-color-selected', hGRbG)
            GHmj = GHmj.replace('#sidebar-font-color', hPRbG)
            GHmj = GHmj.replace('#sidebar-head-color', hVRbG)
            jPRbG = vIcqj.get('status_bar_font.color', '#0095B3')
            jPRbG = str(self.rCcl_XVp_UHfjL(jPRbG))
            GHmj = GHmj.replace('#status_bar-font-color', jPRbG)
            CBqsA = vIcqj.get('panel_font.color', '#A6988D')
            CBqsA = str(self.rCcl_XVp_UHfjL(CBqsA))
            CPRbG = vIcqj.get('panel_font.color.selected', '#FFEE99')
            CPRbG = str(self.rCcl_XVp_UHfjL(CPRbG))
            CBBsA = vIcqj.get('panel_font.color.match', '#61DAF2')
            CBBsA = str(self.rCcl_XVp_UHfjL(CBBsA))
            CARbG = vIcqj.get('panel_font.color.match.selected', '#FF5242')
            CARbG = str(self.rCcl_XVp_UHfjL(CARbG))
            GHmj = GHmj.replace('#panel-font-color-sel-match', CARbG)
            GHmj = GHmj.replace('#panel-font-color-sel', CPRbG)
            GHmj = GHmj.replace('#panel-font-color-match', CBBsA)
            GHmj = GHmj.replace('#panel-font-color', CBqsA)
            CBqsA = vIcqj.get('panel_path.color', '#A6988D')
            CBqsA = str(self.rCcl_XVp_UHfjL(CBqsA))
            CPRbG = vIcqj.get('panel_path.color.selected', '#FFEE99')
            CPRbG = str(self.rCcl_XVp_UHfjL(CPRbG))
            CBBsA = vIcqj.get('panel_path.color.match', '#61DAF2')
            CBBsA = str(self.rCcl_XVp_UHfjL(CBBsA))
            CARbG = vIcqj.get('panel_path.color.match.selected', '#FF5242')
            CARbG = str(self.rCcl_XVp_UHfjL(CARbG))
            GHmj = GHmj.replace('#panel-path-color-sel-match', CARbG)
            GHmj = GHmj.replace('#panel-path-color-sel', CPRbG)
            GHmj = GHmj.replace('#panel-path-color-match', CBBsA)
            GHmj = GHmj.replace('#panel-path-color', CBqsA)
            CKRbG = vIcqj.get('input_font.color', '#FFCC99')
            lHmj = lHmj.replace('#input-font-color', CKRbG)
            EPRbG = vIcqj.get('scroll_bars.color', '#297080')
            EPRbG = str(self.rCcl_XVp_UHfjL(EPRbG))
            GHmj = GHmj.replace('#scroll_bars-color', EPRbG)
            GTPsv = vIcqj.get('tab_font.face', 'Dejavu Sans')
            GTPsv = '"{0}"'.format(GTPsv)
            GPDbS = vIcqj.get('tab_font.bold', False)
            GPDbS = str(GPDbS).lower()
            GGXpv = vIcqj.get('tab_font.size', 13)
            GGXpv = str(GGXpv)
            GHmj = GHmj.replace('#tab-font-face', GTPsv)
            GHmj = GHmj.replace('#tab-font-bold', GPDbS)
            GHmj = GHmj.replace('#tab-font-size', GGXpv)
            YTPsv = vIcqj.get('label_font.face', 'Dejavu Sans')
            YTPsv = '"{0}"'.format(YTPsv)
            YGXpv = vIcqj.get('label_font.size', 12)
            YGXpv = str(YGXpv)
            GHmj = GHmj.replace('#label-font-face', YTPsv)
            GHmj = GHmj.replace('#label-font-size', YGXpv)
            hTPsv = vIcqj.get('sidebar_font.face', 'Dejavu Sans')
            hTPsv = '"{0}"'.format(hTPsv)
            hGXpv = vIcqj.get('sidebar_font.size', 13)
            hGXp2 = hGXpv + 2
            hGXpv = str(hGXpv)
            hGXp2 = str(hGXp2)
            hGXp2 = str(hGXp2)
            GHmj = GHmj.replace('#sidebar-font-face', hTPsv)
            GHmj = GHmj.replace('#sidebar-font-size+2', hGXp2)
            GHmj = GHmj.replace('#sidebar-font-size', hGXpv)
            jTPsv = vIcqj.get('status_bar_font.face', 'Roboto Condensed')
            jTPsv = '"{0}"'.format(jTPsv)
            jGXpv = vIcqj.get('status_bar_font.size', 12)
            jGXpv = str(jGXpv)
            GHmj = GHmj.replace('#status_bar-font-face', jTPsv)
            GHmj = GHmj.replace('#status_bar-font-size', jGXpv)
            CTPsv = vIcqj.get('panel_font.face', 'system')
            CTPsv = '"{0}"'.format(CTPsv)
            CGXpv = vIcqj.get('panel_font.size', 14)
            CGXp2 = CGXpv - 2
            CGXpv = str(CGXpv)
            CGXp2 = str(CGXp2)
            GHmj = GHmj.replace('#panel-font-face', CTPsv)
            GHmj = GHmj.replace('#panel-font-size-2', CGXp2)
            GHmj = GHmj.replace('#panel-font-size', CGXpv)
            GVDfr = vIcqj.get('tab.opacity.hover', 0.6)
            GCeqt = vIcqj.get('tab.opacity', 0.3)
            GIRbW = vIcqj.get('tab.underscore.color.hover', '#AAFF99')
            GIRbW = str(self.rCcl_XVp_UHfjL(GIRbW))
            GIRbG = vIcqj.get('tab.underscore.color', '#FFCC67')
            GIRbG = str(self.rCcl_XVp_UHfjL(GIRbG))
            GHmj = GHmj.replace('#tab-opacity-hover', str(GVDfr))
            GHmj = GHmj.replace('#tab-opacity', str(GCeqt))
            GHmj = GHmj.replace('#tab-underscore-color-hover', GIRbW)
            GHmj = GHmj.replace('#tab-underscore-color', GIRbG)
            hVPtn = vIcqj.get('overlay_shadow', 4)
            hDTht = '"color(var(--background) l(- {0}%))"'.format(hVPtn)
            GHmj = GHmj.replace('#overlay-shadow', hDTht)
            hQPbv = vIcqj.get('scale', 1)
            hKXjtX_kvSey = vIcqj.get('switch_icon_scale', 1)
            hHmj = ''
            for line in GHmj.splitlines():
                hHmj += self.hQPbzDX(line, hQPbv, hKXjtX_kvSey) + '\n'

            AGXpv = str(int(8 * hQPbv))
            SBPcv = os.path.join(sublime.packages_path(), 'zzz A File Icon zzz', 'patches', 'general', 'multi', 'Guna.sublime-theme')
            if os.path.exists(SBPcv):
                with open(SBPcv, 'r', encoding='utf8') as (f):
                    COisW = str(f.read())
                rAinI = '"content_margin": [' + AGXpv + ', ' + AGXpv + ']'
                COisW = RcxEsb.sub(rAinI, COisW)
                with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                    f.write(COisW)
            SBPcv = os.path.join(sublime.packages_path(), 'User', 'A File Icon.sublime-settings')
            COisW = ''
            if os.path.exists(SBPcv):
                with open(SBPcv, 'r', encoding='utf8') as (f):
                    COisW = str(f.read())
                hNinI = '"size": ' + AGXpv
                COisW = PvzEsb.sub(hNinI, COisW)
            else:
                COisW = '{ "size": ' + AGXpv + ' }'
            if aiIFRl != COisW:
                aiIFRl = COisW
                with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                    f.write(COisW)
            LwjSc = [
             1, 1.5]
            lGRqA = vIcqj.get('scale', 1)
            QWuvA = [abs(lGRqA - x) for x in LwjSc]
            bWcyM = QWuvA.index(min(QWuvA))
            lGRqA = LwjSc[bWcyM]
            if lGRqA == 1:
                hQan = ''
                hHmj = hHmj.replace('#sscale-@1.0x', '')
                hHmj = hHmj.replace('#sscale-@1.5x', '//')
                hHmj = hHmj.replace('#sscale-@2.0x', '//')
            else:
                if lGRqA == 1.5:
                    hQan = '-s1.5'
                    hHmj = hHmj.replace('#sscale-@1.0x', '//')
                    hHmj = hHmj.replace('#sscale-@1.5x', '')
                    hHmj = hHmj.replace('#sscale-@2.0x', '//')
                else:
                    if lGRqA == 2:
                        hQan = '-s2.0'
                        hHmj = hHmj.replace('#sscale-@1.0x', '//')
                        hHmj = hHmj.replace('#sscale-@1.5x', '//')
                        hHmj = hHmj.replace('#sscale-@2.0x', '')
                    hHmj = hHmj.replace('-sscale', hQan)
                    LwjSc = [1, 1.33]
                    lGRqA = vIcqj.get('widget_scale', 1)
                    QWuvA = [abs(lGRqA - x) for x in LwjSc]
                    bWcyM = QWuvA.index(min(QWuvA))
                    lGRqA = LwjSc[bWcyM]
                    if lGRqA == 1:
                        hQan = ''
                        hQac = '[120, 40, 0, 0]'
                        hHmj = hHmj.replace('#wscale-@1.0x', '')
                        hHmj = hHmj.replace('#wscale-@1.3x', '//')
                        hHmj = hHmj.replace('#wscale-@1.8x', '//')
                    else:
                        if lGRqA == 1.33:
                            hQan = '-s1.3'
                            hQac = '[160, 52, 0, 0]'
                            hHmj = hHmj.replace('#wscale-@1.0x', '//')
                            hHmj = hHmj.replace('#wscale-@1.3x', '')
                            hHmj = hHmj.replace('#wscale-@1.8x', '//')
                        elif lGRqA == 1.8:
                            hQan = '-s1.8'
                            hQac = '[210, 72, 0, 0]'
                            hHmj = hHmj.replace('#wscale-@1.0x', '//')
                            hHmj = hHmj.replace('#wscale-@1.3x', '//')
                            hHmj = hHmj.replace('#wscale-@1.8x', '')
                hHmj = hHmj.replace('-wscale', hQan)
                lUinI = ''
                for i in range(0, 24):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnc_h{:02d}",   "gnwidg1"], "layer1.texture": "Guna/assets/simple/sidebar/clock/clock_h{:02d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                lUinI += '\n'
                for w in range(0, 7):
                    for m in range(10, 16):
                        lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnc_w{:d}m{:02d}", "gnwidg1"], "layer2.texture": "Guna/assets/simple/sidebar/clock/clock_w{:d}m{:02d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, w, m, w, m, hQan)

                lUinI += '\n'
                for i in range(0, 10):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnc_m{:02d}",   "gnwidg1"], "layer3.texture": "Guna/assets/simple/sidebar/clock/clock_m{:02d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                hHmj = hHmj.replace('#widget-clock', lUinI)
                lUinI = ''
                for i in range(1, 13):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnd_m{:02d}",   "gnwidg2"], "layer1.texture": "Guna/assets/simple/sidebar/clock/clock_dm{:02d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                lUinI += '\n'
                for w in range(0, 7):
                    for m in range(10, 14):
                        lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnd_w{:d}d{:02d}", "gnwidg2"], "layer2.texture": "Guna/assets/simple/sidebar/clock/clock_w{:d}m{:02d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, w, m, w, m, hQan)

                lUinI += '\n'
                for i in range(0, 10):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnd_d{:02d}",   "gnwidg2"], "layer3.texture": "Guna/assets/simple/sidebar/clock/clock_m{:02d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                hHmj = hHmj.replace('#widget-date', lUinI)
                lUinI = ''
                xLLur = [1, 2, 3, 4, 9, 10, 11, 13, 50]
                xKLur = [1, 2, 3, 3, 9, 10, 11, 13, 50]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer1.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                lUinI += '\n'
                xLLur = [x + 300 for x in xLLur]
                xKLur = [x + 300 for x in xKLur]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer2.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                lUinI += '\n'
                xLLur = [x + 300 for x in xLLur]
                xKLur = [x + 300 for x in xKLur]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer3.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                hHmj = hHmj.replace('#widget-weather', lUinI)
                SBPcv = os.path.join(sublime.packages_path(), 'Guna/themes/Guna.sublime-theme')
                with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                    f.write(hHmj)
                SBPcv = os.path.join(sublime.packages_path(), 'Guna/widgets/Widget - Guna.sublime-color-scheme')
                with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                    f.write(lHmj)
                if vIcqt:
                    SBPcv = os.path.join(sublime.packages_path(), 'Guna/themes/Guna.sublime-color-scheme')
                    with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                        f.write(rHmj)
        except Exception:
            QWHf_UijhJ()

    def hOi_tEcgI(self, c):
        if c > 255:
            return 255
        return c

    def rCcl_XVp_UHfjL(self, hc):
        if len(hc) == 7:
            return [int(hc[1:3], 16), int(hc[3:5], 16), int(hc[5:7], 16)]
        else:
            if len(hc) == 9:
                return [int(hc[1:3], 16), int(hc[3:5], 16), int(hc[5:7], 16), int(hc[7:9], 16)]
            raise
            return

    def hQPbzDX(self, GLi, hQPbv, hKXjtX_kvSey):
        bQw = Hs1Esb.match(GLi)
        if bQw:
            if bQw.group('el00') and bQw.group('el01'):
                tZH = str(int((int(bQw.group('el00')) - int(bQw.group('el01'))) * hQPbv + int(bQw.group('el01'))))
                return bQw.group('front') + tZH + bQw.group('back')
            else:
                tZH = str(int(int(bQw.group('el0')) * hQPbv))
                return bQw.group('front') + tZH + bQw.group('back')
        else:
            bQw = Hs2Esb.match(GLi)
            tZT = []
            if bQw:
                tZX = bQw.group('eli')
                tZT.append(bQw.group('el0'))
                tZT.append(bQw.group('el1'))
                for e in tZX:
                    i = int(e)
                    tZT[i] = str(int(int(tZT[i]) * hQPbv))

                tZH = '[' + ', '.join(tZT) + ']'
                return bQw.group('front') + tZH + bQw.group('back')
            bQw = Hs4Esb.match(GLi)
            if bQw:
                tZX = bQw.group('eli')
                tZT.append(bQw.group('el0'))
                tZT.append(bQw.group('el1'))
                tZT.append(bQw.group('el2'))
                tZT.append(bQw.group('el3'))
                for e in tZX:
                    i = int(e)
                    tZT[i] = str(int(int(tZT[i]) * hQPbv))

                tZH = '[' + ', '.join(tZT) + ']'
                return bQw.group('front') + tZH + bQw.group('back')
            else:
                bQw = Hm2Esb.match(GLi)
                tZT = []
                if bQw:
                    tZX = bQw.group('eli')
                    tZT.append(bQw.group('el0'))
                    tZT.append(bQw.group('el1'))
                    for e in tZX:
                        i = int(e)
                        tZT[i] = str(int(int(tZT[i]) * hQPbv * hKXjtX_kvSey))

                    tZH = '[' + ', '.join(tZT) + ']'
                    return bQw.group('front') + tZH + bQw.group('back')
                return GLi


class GunaTweakWidget(sublime_plugin.WindowCommand):

    def run(self):
        try:
            CFTvj, GVTcv, xG_wlDR = vSi_EHVxl()
            vIcqj, lWswI, lWVeC, xG_sAETc = vSi_xKesl('clock')
            if not lWVeC or GVTcv == 'Guna.sublime-theme':
                return
            if HjKUi >= 3150:
                hHNbv = vSi_jJPdx()
                OURbG = hHNbv.get('background')
            else:
                rGRxd = CFTvj.get('color_scheme')
                rGinI = str(sublime.load_resource(rGRxd))
                GFTuE = plistlib.readPlistFromBytes(rGinI.encode())
                OURbG = GFTuE['settings'][0]['settings']['background']
            rPPiv = self.rCcl_XVp_UHfjL(OURbG)
            h, s, v = colorsys.rgb_to_hsv(rPPiv[0], rPPiv[1], rPPiv[2])
            if v >= 200:
                vIcqj = sublime.load_settings('Guna-light.sublime-settings')
            else:
                vIcqj = sublime.load_settings('Guna-dark.sublime-settings')
            hHmj = str(sublime.load_resource('Packages/Guna/.guna/guna-widget.sublime-theme-templ'))
            rPRbG = vIcqj.get('clock.color', '#FFCC67')
            rPRbG = str(self.rCcl_XVp_UHfjL(rPRbG))
            rRRbG = vIcqj.get('clock.color.dirty', '#FF3377')
            rRRbG = str(self.rCcl_XVp_UHfjL(rRRbG))
            rFRbG = vIcqj.get('clock.color.readonly', '#B4B4B4')
            rFRbG = str(self.rCcl_XVp_UHfjL(rFRbG))
            rORbG = vIcqj.get('clock.color.alert', '#FF1919')
            rORbG = str(self.rCcl_XVp_UHfjL(rORbG))
            rWRbG = vIcqj.get('clock.color.info', '#19FFFF')
            rWRbG = str(self.rCcl_XVp_UHfjL(rWRbG))
            hHmj = hHmj.replace('#clock-color-dirty', rRRbG)
            hHmj = hHmj.replace('#clock-color-readonly', rFRbG)
            hHmj = hHmj.replace('#clock-color-alert', rORbG)
            hHmj = hHmj.replace('#clock-color-info', rWRbG)
            hHmj = hHmj.replace('#clock-color', rPRbG)
            LwjSc = [1, 1.33]
            lGRqA = vIcqj.get('widget_scale', 1)
            QWuvA = [abs(lGRqA - x) for x in LwjSc]
            bWcyM = QWuvA.index(min(QWuvA))
            lGRqA = LwjSc[bWcyM]
            if lGRqA == 1:
                hQan = ''
                hQac = '[120, 40, 0, 0]'
                hHmj = hHmj.replace('#wscale-@1.0x', '')
                hHmj = hHmj.replace('#wscale-@1.3x', '//')
                hHmj = hHmj.replace('#wscale-@1.8x', '//')
            else:
                if lGRqA == 1.33:
                    hQan = '-s1.3'
                    hQac = '[160, 52, 0, 0]'
                    hHmj = hHmj.replace('#wscale-@1.0x', '//')
                    hHmj = hHmj.replace('#wscale-@1.3x', '')
                    hHmj = hHmj.replace('#wscale-@1.8x', '//')
                elif lGRqA == 1.8:
                    hQan = '-s1.8'
                    hQac = '[210, 72, 0, 0]'
                    hHmj = hHmj.replace('#wscale-@1.0x', '//')
                    hHmj = hHmj.replace('#wscale-@1.3x', '//')
                    hHmj = hHmj.replace('#wscale-@1.8x', '')
                hHmj = hHmj.replace('-wscale', hQan)
                lUinI = ''
                for i in range(0, 24):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnc_h{:02d}",   "gnwidg1"], "layer1.texture": "Guna/assets/simple/sidebar/clock/clock_h{:02d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                lUinI += '\n'
                for w in range(0, 7):
                    for m in range(10, 16):
                        lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnc_w{:d}m{:02d}", "gnwidg1"], "layer2.texture": "Guna/assets/simple/sidebar/clock/clock_w{:d}m{:02d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, w, m, w, m, hQan)

                lUinI += '\n'
                for i in range(0, 10):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnc_m{:02d}",   "gnwidg1"], "layer3.texture": "Guna/assets/simple/sidebar/clock/clock_m{:02d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                hHmj = hHmj.replace('#widget-clock', lUinI)
                lUinI = ''
                for i in range(1, 13):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnd_m{:02d}",   "gnwidg2"], "layer1.texture": "Guna/assets/simple/sidebar/clock/clock_dm{:02d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                lUinI += '\n'
                for w in range(0, 7):
                    for m in range(10, 14):
                        lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnd_w{:d}d{:02d}", "gnwidg2"], "layer2.texture": "Guna/assets/simple/sidebar/clock/clock_w{:d}m{:02d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, w, m, w, m, hQan)

                lUinI += '\n'
                for i in range(0, 10):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnd_d{:02d}",   "gnwidg2"], "layer3.texture": "Guna/assets/simple/sidebar/clock/clock_m{:02d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, i, i, hQan)

                hHmj = hHmj.replace('#widget-date', lUinI)
                lUinI = ''
                xLLur = [1, 2, 3, 4, 9, 10, 11, 13, 50]
                xKLur = [1, 2, 3, 3, 9, 10, 11, 13, 50]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer1.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer1.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer1.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                lUinI += '\n'
                xLLur = [x + 300 for x in xLLur]
                xKLur = [x + 300 for x in xKLur]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer2.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer2.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer2.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                lUinI += '\n'
                xLLur = [x + 300 for x in xLLur]
                xKLur = [x + 300 for x in xKLur]
                for i in range(0, 9):
                    lUinI += '\t{{ "class": "sidebar_container", "layer3.inner_margin": {}, "settings" : ["gnw_{:03d}",   "gnwidg3"], "layer3.texture": "Guna/assets/simple/sidebar/weather/w{:03d}{}.png", "layer3.opacity": 1 }},\n'.format(hQac, xLLur[i], xKLur[i], hQan)

                hHmj = hHmj.replace('#widget-weather', lUinI)
                GDPjW = os.path.join(sublime.packages_path(), 'zzz Guna Widget zzz')
                if not os.path.exists(GDPjW):
                    os.mkdir(GDPjW)
                    GDPjW = os.path.join(GDPjW, 'themes')
                    os.mkdir(GDPjW)
            SBPcv = os.path.join(sublime.packages_path(), 'zzz Guna Widget zzz/themes', GVTcv)
            with open(SBPcv, 'w', newline='', encoding='utf8') as (f):
                f.write(hHmj)
        except Exception:
            QWHf_UijhJ()

    def rCcl_XVp_UHfjL(self, hc):
        if len(hc) == 7:
            return [int(hc[1:3], 16), int(hc[3:5], 16), int(hc[5:7], 16)]
        else:
            if len(hc) == 9:
                return [int(hc[1:3], 16), int(hc[3:5], 16), int(hc[5:7], 16), int(hc[7:9], 16)]
            raise
            return


ujpEsb = re.compile('(?P<name>file_type_\\w+[^\\.\\@]*)\\.png')

class GunaUpscaleIcon(sublime_plugin.WindowCommand):

    def run(self):
        try:
            pTXtzH = os.path.join(sublime.packages_path(), 'zzz A File Icon zzz', 'patches', 'general', 'multi')
            if os.path.exists(pTXtzH):
                for SWau in os.listdir(pTXtzH):
                    bQw = ujpEsb.match(SWau)
                    if bQw:
                        SWau = bQw.group('name')
                        SWau = os.path.join(pTXtzH, SWau)
                        if os.path.exists(SWau + '_1x.png'):
                            break
                        if os.path.exists(SWau + '.png'):
                            os.rename(SWau + '.png', SWau + '_1x.png')
                        if os.path.exists(SWau + '@2x.png'):
                            os.rename(SWau + '@2x.png', SWau + '_2x.png')
                        if os.path.exists(SWau + '@3x.png'):
                            os.rename(SWau + '@3x.png', SWau + '_3x.png')
                        if os.path.exists(SWau + '_3x.png'):
                            shutil.copy(SWau + '_3x.png', SWau + '.png')
                        else:
                            if os.path.exists(SWau + '_2x.png'):
                                shutil.copy(SWau + '_2x.png', SWau + '.png')
                            else:
                                if os.path.exists(SWau + '_1x.png'):
                                    shutil.copy(SWau + '_1x.png', SWau + '.png')
                                else:
                                    continue

        except Exception:
            QWHf_UijhJ()
# okay decompiling engine.pyc
