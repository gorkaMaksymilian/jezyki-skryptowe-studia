import sys
import socket
import os
import logging
sys.tracebacklimit=0


DEFAULT_SERVERHTTP={
        "port":8000,
        "boolean":True,
        "socketConfig":socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        }

DEFAULT_CONNECT_TTSS={
        "root":os.getcwd()+r"\webdrivers\chromedriver.exe",
        "xPathFirst":r'//*[@id="isg2_prediction_table"]/tbody/tr[',
        "xPathSecond":r']/td[2]',
        "xPathThird":r']/td[3]/div',
        "xPathFourth":r']/td[6]'
        
        }

DEFAULT_FIND_DATABASE={
        "url":r"http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"
        }



DEFAULT_LOG={
        "level":logging.INFO,
        "formatter": "%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        "file":"masterlog.log"
        }