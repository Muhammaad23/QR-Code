import pyqrcode

channel_url = 'https://github.com/Muhammaad23'

url = pyqrcode.create(channel_url)

url.svg('subscribe_my_channel.svg')
url.png('subscribe_my_channel.png')
