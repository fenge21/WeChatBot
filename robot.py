# -*- coding:utf-8 -*-

from wx_robot.handler import MonitorHandler, XiaodouHandler, ChatterHandler
from wx_robot.robot import WxRobot


if __name__ == '__main__':
    robot = WxRobot(hot_reload=True)
    robot.register_handler(MonitorHandler())
    robot.register_handler(ChatterHandler()) #robot.register_handler(XiaodouHandler('ZDVRRGo2NWR3RGdUVEFlPUE1QXQvPVRlWXhJQUFBPT0'))
    robot.run()

