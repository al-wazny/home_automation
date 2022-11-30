from googlehomepush import GoogleHome
import pychromecast

browser = pychromecast.discovery.discover_chromecasts()
services = pychromecast.discovery.start_discovery()
print(services)
pychromecast.discovery.stop_discovery(browser)