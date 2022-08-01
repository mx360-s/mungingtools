# Start a web driver service with mozilla
# None to ingest, return a web driver service with mozilla
# Selenium and webdriver as dependencies
# Exceptions
class NonInstall(Exception):
	def __init__(NonInstall,error,message="o_0 \n Driver not present, and can't install"):NonInstall.error=error;NonInstall.message=message;super().__init__(NonInstall.message)
	def __str__(NonInstall):return f"{NonInstall.error} -> {NonInstall.message}"
#
def GetMozService():
    # instalamos el Gecko Driver solo la primera vez es necessario
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    options = Options()
    options.add_argument( '--disable-blink-features=AutomationControlled' )
    options.add_argument('--single-process')
    options.add_argument("disable-infobars")
    options.set_preference('useAutomationExtension', False)# Marioneta
    options.set_preference("dom.webdriver.enabled", True)# Shadowdom
    try:
        try:
            driver = webdriver.Firefox(options=options)            
        except:
            print('trantando de instalar webdriver')
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), executable_path='geckodriver.exe')
    except: raise NonInstall(Exception)
    return driver
