import pyqrcode

channel_url = 'https://www.youtube.com/shorts/xB-O_-PyWic'

url = pyqrcode.create(channel_url)

url.svg('subscribe_my_channel.svg')
url.png('subscribe_my_channel.png')
