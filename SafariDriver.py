from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


def __init__(self, port=0, executable_path="/usr/bin/safaridriver",
                 desired_capabilities=DesiredCapabilities.SAFARI, quiet=False):
    self.service = Service(executable_path, port=port, quiet=quiet)
    self.service.start()





    


