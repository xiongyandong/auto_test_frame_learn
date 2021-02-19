# --*--coding:utf-8 --*--
from Base.setting import Setting
import os
from tools.readConfig import ReadConfig


class ProjectPath:
    p2p_report_path = os.path.join(Setting.BaseDir, r'Report\p2pReport')
    p2p_config_path = os.path.join(os.path.join(Setting.BaseDir, 'Config'), 'case.config')
    p2p_data_path = os.path.join(os.path.join(Setting.BaseDir, r'data\p2pData'),
                                 ReadConfig.read_config(p2p_config_path, 'WORKBOOK', 'file_name'))
    p2p_module = eval(ReadConfig.read_config(p2p_config_path, 'WORKBOOK', 'module'))


class SaaSWebsiteLogPath:
    login_log_path = os.path.join(Setting.BaseDir, r'Outputs\Logs\SaasWebsites\login\login.log')
    index_log_path = os.path.join(Setting.BaseDir, r'Outputs\Logs\SaasWebsites\index\index.log')
    screenshot_path = os.path.join(Setting.BaseDir, r'Outputs\screenshots')




