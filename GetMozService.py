# Start a web driver service with mozilla
# None to ingest, return a web driver service with mozilla
# Selenium and webdriver as dependencies
def GetMozService():
    # instalamos el Gecko Driver solo la primera vez es necesario
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service as FirefoxService
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
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), executable_path='geckodriver.exe')
    except: print('0_o error de navegacion')
    return driver
#
