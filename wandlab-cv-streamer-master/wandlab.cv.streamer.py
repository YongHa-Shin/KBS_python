# -*- encoding: utf-8 -*-
#-------------------------------------------------#
# Date created          : 2020. 8. 18.
# Date last modified    : 2020. 8. 19.
# Author                : chamadams@gmail.com
# Site                  : http://wandlab.com
# License               : GNU General Public License(GPL) 2.0
# Version               : 0.1.0
# Python Version        : 3.6+
#-------------------------------------------------#

from lab.wandlab.server import app

version = '0.1.0'

if __name__ == '__main__' :
    
    print('------------------------------------------------')
    print('Wandlab CV - version ' + version )
    print('------------------------------------------------')
    app.run( host = "127.0.0.1", debug=False, port=443 )
    # app.run( host='0.0.0.0', port=443 )

# http://127.0.0.1:443/stream?src=

# video_source = {
#     "마라도" : "https://stream1.ktict.co.kr:8083/livekbsd1/9982/chunks.m3u8?",
#     "세병교" : "https://stream1.ktict.co.kr:8083/livekbsd1/9967/chunks.m3u8?",
#     "수영만" : "https://stream1.ktict.co.kr:8083/livekbsd1/9991/chunks.m3u8?"
#     }
