SECRET_KEY = '^s-local$'
INTERFACE_NAME = 'enp7s0'
# INTERFACE_NAME = 'wlp8s0'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

# GREP_FILTER = '162.243.136.175:80'

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_DB = 'ss_status'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB

PROVINCE = {'tianjin': '天津', 'guangxi': '广西', 'ningxia': '宁夏', 'jilin': '吉林', 'jiangsu': '江苏', 'taiwan': '台湾',
            'guizhou': '贵州', 'hainan': '海南', 'liaoning': '辽宁', 'zhejiang': '浙江', 'yunnan': '云南', 'sichuan': '四川',
            'aomen': '澳门', 'hebei': '河北', 'shandong': '山东', 'chongqing': '重庆', 'anhui': '安徽', 'heilongjiang': '黑龙江',
            'shanxi': '陕西', 'xianggang': '香港', 'gansu': '甘肃', 'neimenggu': '内蒙古', 'henan': '河南', 'fujian': '福建',
            'qinghai': '青海', 'guangdong': '广东', 'xizang': '西藏', 'jiangxi': '江西', 'shanghai': '上海', 'xinjiang': '新疆',
            'beijing': '北京', 'hunan': '湖南', 'hubei': '湖北'}
geoDbPath = '/home/yy/projects/ss-status-backend/GeoLite2-City.mmdb'
grepStr = 'ss -atn |grep ESTAB | grep 80 |awk "{print $5}" |cut -d ":" -f1 |sort |uniq'
