import subprocess
import sys

def change_android_locale(language_code):
    try:
        # Check if ADB is available
        subprocess.run(["adb", "version"], check=True)

        # Establish ADB root connection
        subprocess.run(["adb", "root"], check=True)

        # Verify device is connected and authorized
        devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "device" not in devices.stdout:
            print("No authorized Wear OS device found. Please connect and authorize the device.")
            return

        # Set locale using settings command
        locale_command = [
            "adb", "shell",
            "settings", "put", "secure",
            "system_locales", language_code
        ]

        result = subprocess.run(locale_command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Locale successfully changed to: {language_code}")

            # Optional: Force locale refresh
            subprocess.run(["adb", "shell", "am", "broadcast",
                           "-a", "android.intent.action.LOCALE_CHANGED"])
        else:
            print(f"Locale change failed: {result.stderr}")

    except subprocess.CalledProcessError as e:
        print(f"ADB command error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Usage example
# python3 locale_changer.py en_US
if __name__ == "__main__":
    if len(sys.argv) > 1:
        change_android_locale(sys.argv[1])
    else:
        print("Please provide a language code (e.g., en_US)")
