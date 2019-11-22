#####
# @file : charts.py
# @desc : API route for charts
# @author : TBD
#####

# IMPORTS
import cherrypy
import json
from database import database

# @class : ChartsController
# @desc  : route for charts
class ChartsController(object):

    # @name : __init__
    # @desc : Constructor
    def __init__(self, db=None):
        if db is None:
            self.db = database()
        else:
            self.db = db
        
    # @name : GET_CHART
    # @desc : Get chart by symbol
    def GET_CHART(self, symbol):
        interval = '1d'
        rg = '5m'
        output = { 'result': 'success' }
        try:
            chart = self.db.load_chart(symbol, interval, rg)
            chart = chart['chart']['result'][0]
            indicators = chart['indicators']['quote'][0]
            if chart is not None:
                output['currentTradingPeriod'] = chart['meta']['currentTradingPeriod']
                output['timestamp']            = chart['timestamp']
                output['volume']               = indicators['volume']
                output['close']                = indicators['close']
                output['open']                 = indicators['open']
            else:
                output['result'] = 'error'
                output['message'] = 'chart not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
        
# @name : main
# @desc : main driver for file
if __name__ == '__main__':
    cc = ChartsController()
    cc.GET_CHART()
