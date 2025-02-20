"""this script fetches the touch/tap coordinates from android device"""

import subprocess


def get_display_size(device_id):
    """get the display size of the device"""
    adb_command = f"adb -s {device_id} shell wm size"
    process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, text=True)
    output = process.stdout.readline()
    if "Physical size" not in output:
        raise ValueError("Failed to get display size")
    resolution = output.split(":")[-1].strip()
    print(output)
    width, height = map(int, resolution.split("x"))
    return (width, height)


def collect_touch_events(device_id):
    """Collect the output of adb into a variable until enter is pressed"""
    display_width, display_height = get_display_size(device_id)
    print("Start tapping on the device....")
    adb_command = f"adb -s {device_id} shell getevent -l"
    process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    last_x = -1 
    last_y = -1 
    while True:
        try:
            line = process.stdout.readline()
            if "ABS_MT_POSITION_X" in line:
                parts = line.split()
                hexvalue = parts[-1]
                last_x = int(hexvalue, 16)
            if "ABS_MT_POSITION_Y" in line:
                parts = line.split()
                hexvalue = parts[-1]
                last_y = int(hexvalue, 16)
            if "BTN_TOUCH" in line and "DOWN" in line:
                print(f"Touch down at physical coordinates {last_x}, {last_y}, normalized-"
                      f"coordinates {last_x / display_width} ({last_x} /"
                      f"{display_width}), {last_y / display_height} ({last_y}/"
                      f"{display_height})")
            if not line:
                break
        except KeyboardInterrupt:
            break
    return


if __name__ == "__main__":
    # device could be here anything, realated to your usb device connected type adb devices -l to know
    # 46131JEAYL02AF 
    device_id = "46131JEAYL02AF"
    collect_touch_events(device_id)