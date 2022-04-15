import pyautogui

from pynput import keyboard
import time
import ctypes
import random

hmon_stopped = True
border_declined = False

obstitle = "OBS 26.0.2 (64-bit, windows) - Профиль: Безымянный - Сцены: Безымянный"
xsplittitle = "XSplit"

obsdeletetitle = "Подтвердить удаление"
browser_title = "OzWebLiveness Demo"

err_open = "D:/Downloads/open_err.png"
camera_path = "D:/Downloads/Screenshot_54.png"
camera_path_2 = "D:/Downloads/cam2.png"
liveness_path = "D:/Downloads/liveness_button.png"
scan_path = "D:/Downloads/scan_button.png"
cam_path = "D:/Downloads/cam.png"

pshow_image = {"x": 560, "y": 875}
ptarget_image = {"x": 540, "y": 875}
pborder = {"x": 957, "y": 245}
pborder2 = {"x": 957, "y": 275}
pborder3 = {"x": 957, "y": 285}
pdone = {"x": 22, "y": 226}

redborder_pix = [(220, 0, 0), (256, 30, 30)]
rdone_r_pix = [(220, 0, 0), (256, 70, 70)]
rdone_g_pix = [(0, 200, 0), (90, 256, 90)]


def pixel(x, y):
    hdc = ctypes.windll.user32.GetDC(0)
    color = ctypes.windll.gdi32.GetPixel(hdc, x, y)
    # color is in the format 0xbbggrr https://msdn.microsoft.com/en-us/library/windows/desktop/dd183449(v=vs.85).aspx
    r = color % 256
    g = (color // 256) % 256
    b = color // (256 ** 2)
    ctypes.windll.user32.ReleaseDC(0, hdc)
    return (r, g, b)


def check_pix_range(pix, min_max):
    mi = min_max[0]
    ma = min_max[1]
    if (pix[0] < ma[0]) and (pix[1] < ma[1]) and (pix[2] < ma[2]) and (pix[0] >= mi[0]) and (pix[1] >= mi[1]) and (
            pix[2] >= mi[2]):
        return True
    return False


def wait_for_cur_window_title(title, partial=True):
    print("waiting ", title)
    cur_title = None
    while cur_title is None:
        cur_title = pyautogui.getActiveWindowTitle()

    if partial:
        while title not in cur_title:
            print(cur_title)
            cur_title = pyautogui.getActiveWindowTitle()
            while cur_title is None:
                cur_title = pyautogui.getActiveWindowTitle()
    else:
        while cur_title != title:
            print(cur_title)
            cur_title = pyautogui.getActiveWindowTitle()
            while cur_title is None:
                cur_title = pyautogui.getActiveWindowTitle()


def show_top_image(title):
    # print(pyautogui.getWindowsWithTitle(title)[0])
    pyautogui.getWindowsWithTitle(title)[0].minimize()
    # time.sleep(1)
    pyautogui.getWindowsWithTitle(title)[0].maximize()
    # time.sleep(1)
    # pyautogui.getWindowsWithTitle(title)[0].
    wait_for_cur_window_title(title)
    pyautogui.click(**pshow_image)


def remove_top_image(title):
    # pyautogui.click(550, 884)
    pyautogui.click(**ptarget_image)
    pyautogui.press('delete')
    wait_for_cur_window_title(title)
    time.sleep(0.5)
    pyautogui.press('enter')


def get_button_coords(path):
    tries = 0
    button = None
    while tries < 3:
        # time.sleep(0.5)
        print(path, "try: ", tries + 1)
        button = pyautogui.locateOnScreen(path)
        if button is not None:
            break
        tries = tries + 1
    if button is not None:
        buttonpoint = pyautogui.center(button)
        return {"x": buttonpoint.x, "y": buttonpoint.y}
    else:
        return {"x": -1, "y": -1}


def proc_liveness_obs(title, saved_cam=False):
    global border_declined
    global camera_path
    global liveness_path
    global scan_path
    global cam_path
    pyautogui.getWindowsWithTitle(title)[0].minimize()
    pyautogui.getWindowsWithTitle(title)[0].maximize()
    wait_for_cur_window_title(title)
    if (border_declined == False):
        time.sleep(0.1)
        pyautogui.click(384, 400)

        # pyautogui.click(**get_button_coords(liveness_path))
    time.sleep(0.5)

    pyautogui.click(384, 770)
    time.sleep(5)
    # pyautogui.click(**get_button_coords(scan_path))
    # time.sleep(2)

    if saved_cam == True:
        ## select camera
        pyautogui.click(550, 150)
        # time.sleep(1)
        # pyautogui.click(**get_button_coords(cam_path))
        time.sleep(1.5)
        pyautogui.click(**get_button_coords(camera_path))

        # time.sleep(1)
        # pyautogui.click(550, 230)
        time.sleep(0.3)
        pyautogui.click(480, 200)


def proc_liveness_xsplit(title, saved_cam=False):
    global border_declined
    global camera_path_2
    global liveness_path
    global scan_path
    global cam_path
    pyautogui.getWindowsWithTitle(title)[0].minimize()
    pyautogui.getWindowsWithTitle(title)[0].maximize()
    time.sleep(0.1)
    wait_for_cur_window_title(title)
    if (border_declined == False):
        time.sleep(0.1)
        pyautogui.click(384, 400)

        # pyautogui.click(**get_button_coords(liveness_path))
    time.sleep(0.5)

    pyautogui.click(384, 770)
    time.sleep(3)
    # pyautogui.click(**get_button_coords(scan_path))
    # time.sleep(2)

    if saved_cam == True:
        ## select camera
        pyautogui.click(550, 150)
        # time.sleep(1)
        # pyautogui.click(**get_button_coords(cam_path))
        time.sleep(1.5)
        pyautogui.click(**get_button_coords(camera_path_2))

        # time.sleep(1)
        # pyautogui.click(550, 230)
        time.sleep(0.3)
        pyautogui.click(480, 200)

    # pyautogui.moveTo(550, 150)


def switch_from_liveness(titles):
    pyautogui.getWindowsWithTitle(titles[0])[0].minimize()
    time.sleep(0.1)
    pyautogui.getWindowsWithTitle(titles[0])[0].maximize()
    time.sleep(0.1)
    wait_for_cur_window_title(titles[0])
    pyautogui.click(60, 290)
    pyautogui.getWindowsWithTitle(titles[1])[0].minimize()
    pyautogui.getWindowsWithTitle(titles[1])[0].maximize()
    wait_for_cur_window_title(titles[1])


def on_deactivate():
    global hmon_stopped
    hmon_stopped = True

    time.sleep(1)

    print('Global hotkey DEactivated!')
    # print(hmon_stopped)


def stretch(is_obs=False):
    if is_obs == True:
        # pyautogui.press('ctrl')
        # pyautogui.press('s')
        pyautogui.hotkey('ctrl', 's')
    else:
        pyautogui.click(1665, 370)
        time.sleep(0.2)
        pyautogui.click(1896, 840)
        time.sleep(0.2)
        pyautogui.click(1900, 670)


def remove_media(cam):
    is_obs = False if cam != 1 else True
    is_xs = False if cam != 0 else True
    is_mc = False if cam != 2 else True
    is_sc = False if cam != 3 else True
    is_e2 = False if cam != 4 else True
    is_sparko = False if cam != 5 else True
    is_magic = False if cam != 6 else True
    is_fake_wbc = False if cam != 7 else True
    is_altercam = False if cam != 'altercam' else True
    is_chromacam = False if cam != 'chromacam' else True
    is_droidcam = False if cam != 'droidcam' else True

    if is_obs == True:
        pyautogui.press('delete')
        # wait_for_cur_window_title(title)
        time.sleep(0.5)
        pyautogui.press('enter')

    elif is_xs == True:
        pyautogui.click(1800, 165)
        time.sleep(0.1)
        pyautogui.click(1800, 165)
        time.sleep(0.2)
        # pyautogui.click(1115, 610)
        pyautogui.click(1740, 300)
        # time.sleep(0.2)

    elif is_mc == True:
        pyautogui.click(1855, 595)
        time.sleep(0.2)
        pyautogui.click(1855, 595)
        time.sleep(0.2)

    elif is_sc == True:
        pyautogui.click(377, 160)
        time.sleep(0.2)
        pyautogui.click(480, 230)
        time.sleep(0.2)

    elif is_e2 == True:
        # click show
        pyautogui.click(350, 420)
        time.sleep(4)

        # click stop
        pyautogui.click(390, 420)
        time.sleep(1)

        pyautogui.click(90, 450)
        time.sleep(0.2)
        pyautogui.click(90, 450)
        time.sleep(0.2)

    elif is_sparko:
        pyautogui.click(193, 338)
        time.sleep(0.2)
        pyautogui.press('enter')

    elif is_magic:
        pyautogui.click(798, 73)
        time.sleep(1)

    elif is_fake_wbc:
        pyautogui.click(57, 65, clicks=2, duration=0.2, interval=0.1)
        pyautogui.sleep(0.3)

    elif is_altercam:
        pyautogui.click(400, 120, duration=0.2)
        pyautogui.click(487, 187, duration=0.2)
        pyautogui.click(643, 211, duration=0.3)
        pyautogui.click(620, 360, duration=0.3) #выравниваем по окно СПРАВА
        pyautogui.click(865, 405, duration=0.3)
        pyautogui.sleep(0.1)

    elif is_chromacam:
        pyautogui.click(356, 233, duration=0.2)
        pyautogui.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.sleep(0.1)

    elif is_droidcam:
        pyautogui.click(170,200, button='right')
        pyautogui.sleep(0.2)
        pyautogui.click(217, 217)



def ofd():
    global hmon_stopped
    # click top left file
    pyautogui.click(230, 180, duration=0.2)
    pyautogui.sleep(0.6)
    # press delete
    pyautogui.press('delete')
    pyautogui.sleep(0.2)
    #pyautogui.press('F5')
    pyautogui.sleep(0.3)
    # click top left file
    pyautogui.click(230, 180, duration=0.2)
    pyautogui.sleep(0.2)
    # click ok
    #pyautogui.press('enter')
    pyautogui.click(790, 510, duration=0.2)
    #time.sleep(0.2)
    # check_finished = get_button_coords(err_open)
    # print(check_finished)
    # if check_finished['x'] != -1:
    #     hmon_stopped = True


def add_media(cam):
    global hmon_stopped
    is_obs = False if cam != 1 else True
    is_xs = False if cam != 0 else True
    is_mc = False if cam != 2 else True
    is_sc = False if cam != 3 else True
    is_e2 = False if cam != 4 else True
    is_sparko = False if cam != 5 else True
    is_magic = False if cam != 6 else True
    is_fake_wbc = False if cam != 7 else True
    is_altercam = False if cam != 'altercam' else True
    is_chromacam = False if cam != 'chromacam' else True
    is_droidcam = False if cam != 'droidcam' else True


    if is_obs == True:
        pyautogui.click(322, 1000)
        time.sleep(0.2)
        pyautogui.click(453, 767)
        time.sleep(2)
        pyautogui.click(1000, 666)
        time.sleep(0.3)
        # pyautogui.click(257, 143)
        # time.sleep(0.2)
        pyautogui.click(1263, 652)
        time.sleep(2.0)
        pyautogui.click(232, 169)
        time.sleep(1.0)
        pyautogui.press('delete')
        time.sleep(1.0)
        # time.sleep(5)
        # pyautogui.press('enter')
        # time.sleep(1)
        pyautogui.click(232, 169)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.click(1196, 798)
        time.sleep(0.2)
    elif is_xs == True:
        pyautogui.click(1810, 445)
        time.sleep(0.2)
        pyautogui.click(1810, 320)
        time.sleep(2.3)
        ofd()
    elif is_mc == True:
        # click add
        pyautogui.click(1855, 565)
        time.sleep(1)

        # click image
        pyautogui.click(1820, 635)
        time.sleep(2.3)
        ofd()
    elif is_sc == True:
        # click add
        pyautogui.click(365, 117)
        time.sleep(1)

        # click image
        pyautogui.click(455, 380)
        time.sleep(2.3)
        ofd()
    elif is_e2 == True:
        # click add
        pyautogui.click(40, 450)
        time.sleep(1)

        ofd()

    elif is_sparko:
        pyautogui.click(72, 850, duration=0.3)
        time.sleep(0.5)
        ofd()
        pyautogui.click(77, 338, duration=0.2)

    elif is_magic:
        pyautogui.moveTo(773, 74)
        pyautogui.mouseDown()
        # pyautogui.click(773, 74)
        time.sleep(4.0)
        pyautogui.mouseUp()
        ofd()

    elif is_fake_wbc:
        pyautogui.click(20, 65, clicks=2, duration=1, interval=1)
        time.sleep(1.0)
        ofd()
        pyautogui.click(138, 65, interval=1)

    elif is_altercam:
        pyautogui.click(400,120, duration=0.2)
        pyautogui.click(487, 187, duration=0.2)
        pyautogui.click(640, 187, duration=0.2)
        time.sleep(0.5)
        ofd()

    elif is_chromacam:
        pyautogui.click(587, 171, duration=0.2)
        time.sleep(0.3)
        ofd()
        pyautogui.click(310, 260, duration=0.2)
        time.sleep(0.2)


    elif is_droidcam:
        pyautogui.click(170, 200, button='right')
        pyautogui.sleep(0.2)
        pyautogui.click(230, 240, duration=0.15)
        time.sleep(1)
        ofd()




def loop_settings(is_obs=False, loop_all=False):
    if is_obs == True:
        # pyautogui.click(322, 1000)
        # time.sleep(0.2)
        # pyautogui.click(453, 767)
        # time.sleep(2)
        # pyautogui.click(1000, 666)
        # time.sleep(0.3)
        # # pyautogui.click(257, 143)
        # # time.sleep(0.2)
        # pyautogui.click(1263, 652)
        # time.sleep(2.0)
        # pyautogui.click(232, 169)
        # time.sleep(1.0)
        # pyautogui.press('delete')
        # time.sleep(1.0)
        # # time.sleep(5)
        # # pyautogui.press('enter')
        # # time.sleep(1)
        # pyautogui.click(232, 169)
        # time.sleep(0.3)
        # pyautogui.press('enter')
        # time.sleep(0.3)
        # pyautogui.click(1196, 798)
        # time.sleep(0.2)
        pass
    else:
        # x_coords = [1760, 1776, 1790, 1805, 1820, 1835, 1850]
        x_coords = [1776, 1805, 1835]
        y_coords_brightness = [112] * len(x_coords)
        y_coords_contrast = [162] * len(x_coords)
        y_coords_scale = [272] * len(x_coords)
        y_coords_lr = [316] * len(x_coords)
        y_coords_tb = [366] * len(x_coords)

        timer_stub = 0.3  # 0.2
        prob = 0.3

        if loop_all == True:
            # Click EDIT
            pyautogui.click(1665, 370)
            time.sleep(timer_stub)

            for ar_iter in range(1):
                for vflip_iter in range(2):
                    for hflip_iter in range(2):
                        for brightness_iter in zip(x_coords, y_coords_brightness):
                            if random.uniform(0.0, 1.0) < prob:
                                for contrast_iter in zip(x_coords, y_coords_contrast):
                                    if random.uniform(0.0, 1.0) < prob:
                                        for scale_iter in zip(x_coords, y_coords_scale):
                                            if random.uniform(0.0, 1.0) < prob:
                                                for lr_iter in zip(x_coords, y_coords_lr):
                                                    if random.uniform(0.0, 1.0) < prob:
                                                        for tb_iter in zip(x_coords, y_coords_tb):
                                                            if random.uniform(0.0, 1.0) < prob:
                                                                tbargs = {'x': tb_iter[0], 'y': tb_iter[1]}
                                                                pyautogui.click(**tbargs)
                                                                time.sleep(timer_stub)
                                                        # if random.uniform(0.0, 1.0) < prob:
                                                        lrargs = {'x': lr_iter[0], 'y': lr_iter[1]}
                                                        pyautogui.click(**lrargs)
                                                        time.sleep(timer_stub)
                                                scaleargs = {'x': scale_iter[0], 'y': scale_iter[1]}
                                                pyautogui.click(**scaleargs)
                                                time.sleep(timer_stub)
                                        contrastargs = {'x': contrast_iter[0], 'y': contrast_iter[1]}
                                        pyautogui.click(**contrastargs)
                                        time.sleep(timer_stub)
                                args = {'x': brightness_iter[0], 'y': brightness_iter[1]}
                                pyautogui.click(**args)
                                time.sleep(timer_stub)
                        # if random.uniform(0.0, 1.0) < 1.1:#prob:
                        #     arargs = {'x': 1900, 'y': 225}
                        #     pyautogui.click(**arargs)
                        #     time.sleep(timer_stub)
                        if random.uniform(0.0, 1.0) < 1.1:  # prob:
                            hflipargs = {'x': 1870, 'y': 400}
                            pyautogui.click(**hflipargs)
                            time.sleep(timer_stub)
                    if random.uniform(0.0, 1.0) < 1.1:  # prob:
                        vflipargs = {'x': 1900, 'y': 400}
                        pyautogui.click(**vflipargs)
                        time.sleep(timer_stub)
                arargs = {'x': 1900, 'y': 225}
                pyautogui.click(**arargs)
                time.sleep(timer_stub)

            # Click EDIT
            pyautogui.click(1665, 370)
            time.sleep(timer_stub)
        else:
            # Click EDIT
            pyautogui.click(1665, 370)
            time.sleep(timer_stub)

            arargs = {'x': 1900, 'y': 225}
            pyautogui.click(**arargs)
            time.sleep(timer_stub)

            # Click EDIT
            pyautogui.click(1665, 370)
            time.sleep(timer_stub)
            # # Click nearby
            # pyautogui.click(1700, 370)
        # time.sleep(timer_stub)

    #     # brightness -79
    #     pyautogui.click(1760, 112)
    #     time.sleep(0.2)
    #
    #     # brightness -51
    #     pyautogui.click(1776, 112)
    #     time.sleep(0.2)
    #
    #     # brightness -27
    #     pyautogui.click(1790, 112)
    #     time.sleep(0.2)
    #
    #     # brightness 26
    #     pyautogui.click(1820, 112)
    #     time.sleep(0.2)
    #
    #     pyautogui.click(1810, 320)
    #     time.sleep(2)
    #     pyautogui.click(257, 143)
    #     time.sleep(0.2)
    #     pyautogui.press('delete')
    #     time.sleep(1)
    #     pyautogui.click(257, 143)
    #     time.sleep(0.2)
    #     pyautogui.click(790, 505)
    #     time.sleep(0.2)
    # stretch(is_obs)


def on_activate_obs_old():
    global hmon_stopped
    global border_declined
    hmon_stopped = False

    time.sleep(1)

    print('Global hotkey activated!')

    while hmon_stopped == False:
        proc_liveness_obs(browser_title)

        time.sleep(3)

        if check_pix_range(pixel(**pborder), redborder_pix) or check_pix_range(pixel(**pborder2),
                                                                               redborder_pix) or check_pix_range(
                pixel(**pborder3), redborder_pix):
            border_declined = True
        else:
            while (check_pix_range(pixel(**pdone), rdone_r_pix) == False) and (
                    check_pix_range(pixel(**pdone), rdone_g_pix) == False):
                time.sleep(1)
            border_declined = False

        switch_from_liveness([browser_title, obstitle])
        remove_top_image(obsdeletetitle)


def on_activate_xs():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated!')

    while hmon_stopped == False:
        time.sleep(0.2)

        remove_media()
        add_media()
        time.sleep(0.5)
        loop_settings(loop_all=False)
    print(hmon_stopped)


def on_activate_manycam():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated!')

    while hmon_stopped == False:
        time.sleep(0.2)

        remove_media(2)
        add_media(2)
        time.sleep(0.5)
        # loop_settings(loop_all=False)
    print(hmon_stopped)


def on_activate_sc():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated!')

    while hmon_stopped == False:
        time.sleep(0.2)

        remove_media(3)
        add_media(3)
        time.sleep(0.5)
        # loop_settings(loop_all=False)
    print(hmon_stopped)


def on_activate_e2():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated!')

    while hmon_stopped == False:
        time.sleep(0.2)

        add_media(4)
        remove_media(4)
        time.sleep(0.5)
        # loop_settings(loop_all=False)
    print(hmon_stopped)


def on_activate_sparko():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        time.sleep(0.5)

        remove_media(cam=5)
        add_media(cam=5)
        time.sleep(0.5)

    print(hmon_stopped)


def on_activate_magic():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        time.sleep(0.5)

        remove_media(cam=6)
        time.sleep(1)
        add_media(cam=6)
        time.sleep(1)
    print(hmon_stopped)


def on_activate_fakeWbc():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        time.sleep(0.5)

        remove_media(cam=7)
        time.sleep(1)
        add_media(cam=7)
        time.sleep(2)
    print(hmon_stopped)


def on_activate_altercam():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        time.sleep(0.5)

        remove_media(cam='altercam')
        time.sleep(0.5)
        add_media(cam='altercam')
        time.sleep(0.5)
    print(hmon_stopped)


def on_activate_chromacam():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        #time.sleep(0.3)

        remove_media(cam='chromacam')
        time.sleep(0.5)
        add_media(cam='chromacam')
        time.sleep(0.8)
    print(hmon_stopped)


def on_activate_droidcam():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated')

    while not hmon_stopped:
        time.sleep(0.5)

        remove_media(cam='droidcam')
        time.sleep(0.6)
        add_media(cam='droidcam')
        time.sleep(1)
    print(hmon_stopped)



def on_activate_obs():
    global hmon_stopped
    global border_declined
    hmon_stopped = False
    time.sleep(1)
    print('Global hotkey activated!')

    first_time_cam_select = True
    while hmon_stopped == False:
        proc_liveness_obs(browser_title, first_time_cam_select)
        first_time_cam_select = False
        time.sleep(3)

        if check_pix_range(pixel(**pborder), redborder_pix) or check_pix_range(pixel(**pborder2),
                                                                               redborder_pix) or check_pix_range(
                pixel(**pborder3), redborder_pix):
            border_declined = True
        else:
            while (check_pix_range(pixel(**pdone), rdone_r_pix) == False) and (
                    check_pix_range(pixel(**pdone), rdone_g_pix) == False):
                time.sleep(1)
            border_declined = False
        switch_from_liveness([browser_title, obstitle])
        remove_media(True)
        add_media(True)


def on_activate_0():
    on_activate_obs()
    # on_activate_xs()


def on_activate_1():
    # on_activate_obs()
    on_activate_xs()


def on_activate_2():
    # on_activate_obs()
    on_activate_manycam()


def on_activate_3():
    # on_activate_obs()
    on_activate_sc()


def on_activate_4():
    # on_activate_obs()
    on_activate_e2()


def on_activate_5():
    on_activate_sparko()


def on_activate_6():
    on_activate_magic()


def on_activate_7():
    on_activate_fakeWbc()


def on_activate_8():
    on_activate_altercam()


def on_activate_9():
    on_activate_chromacam()


def on_activate_10():
    on_activate_droidcam()


# while True:
#     print(get_camera_coords(camera_path))
# pyautogui.moveTo(**pshow_image)
with keyboard.GlobalHotKeys({
    '<ctrl>+h': on_activate_0,
    '<ctrl>+g': on_activate_1,
    '<ctrl>+j': on_activate_2,
    '<ctrl>+k': on_activate_3,
    '<ctrl>+l': on_activate_4,
    '<ctrl>+s': on_activate_5,
    '<ctrl>+m': on_activate_6,
    '<ctrl>+w': on_activate_7,
    '<ctrl>+t': on_activate_8,
    '<ctrl>+c': on_activate_9,
    '<ctrl>+d': on_activate_10}) as h:
    h.join()
