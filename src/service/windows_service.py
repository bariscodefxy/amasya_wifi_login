import win32service
import win32serviceutil
import win32event
import servicemanager

class WindowsService(win32serviceutil.ServiceFramework):
    _svc_name_ = "Amasya Wifi Login"
    _svc_display_name_ = "Amasya Wifi Login's Windows Service"
    
    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg(self._svc_name_ + " is starting...")
        while True:
            # Your service logic here
            if win32event.WaitForSingleObject(self.stop_event, 5000) == win32event.WAIT_OBJECT_0:
                break
        servicemanager.LogInfoMsg(self._svc_name_ + " is stopping...")

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(MyService)