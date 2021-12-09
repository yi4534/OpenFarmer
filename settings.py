from dataclasses import dataclass
from datetime import timedelta

@dataclass
class Settings:
    path_logs: str
    chrome_data_dir: str
    url_db: str = None
    # 发送http请求的间隔
    req_interval = 3
    # 每小时至少扫描一次，即使没有可用的作物，这样可以处理上次扫码后新种的作物
    max_scan_interval = timedelta(minutes=15)
    # 每次扫描至少间隔10秒，哪怕是出错重扫
    min_scan_interval = timedelta(seconds = 10)
    #账号中剩余多少材料不提现
    need_fww = 0
    need_fwf = 400
    need_fwg = 350
    #最少提现数量，3种材料总和
    withdraw_min = 200



# 用户配置参数
class user_param:
    wax_account: str = None
    proxy: str = None

    build: bool = True
    mining: bool = True
    chicken: bool = True
    plant: bool = True
    cow: bool = True
    mbs: bool = True
    withdraw: bool = True
    sell_corn: bool = True
    sell_barley: bool = True
    # 能量不够的时候，就去恢复那么多能量,但不超过最大能量
    recover_energy: int = 500

    on_server: bool = False

    #账号中剩余多少材料不提现
    need_fww: int = 200
    need_fwf: int = 200
    need_fwg: int = 200
    #最少提现数量，3种材料总和
    withdraw_min: int = 200


def load_user_param(user: dict):
    user_param.wax_account = user["wax_account"]
    user_param.proxy = user.get("proxy", None)
    user_param.build = user.get("build", True)
    user_param.mining = user.get("mining", True)
    user_param.chicken = user.get("chicken", True)
    user_param.plant = user.get("plant", True)
    user_param.cow = user.get("cow", True)
    user_param.mbs = user.get("mbs", True)
    user_param.sell_corn = user.get("sell_corn", True)
    user_param.sell_barley = user.get("sell_barley", True)
    user_param.recover_energy = user.get("recover_energy", 500)
    user_param.withdraw = user.get("withdraw", True)
    user_param.need_fww = user.get("need_fww", 200)
    user_param.need_fwf = user.get("need_fwf", 200)
    user_param.need_fwg = user.get("need_fwg", 200)
    user_param.withdraw_min = user.get("withdraw_min", 200)


cfg = Settings(
    path_logs="./logs/",
    chrome_data_dir="./data_dir/",
)

