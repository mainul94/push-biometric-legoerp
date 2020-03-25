import time
from pathlib import Path
from SMWinservice import SMWinservice
from push_to_legoerp import main

class PythonCornerExample(SMWinservice):
    _svc_name_ = "LegoERPBiometricPushService"
    _svc_display_name_ = "LegoERP Biometric Push Service"
    _svc_description_ = "Service to push biometric data from device to LegoERP"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            main()
            time.sleep(15)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()