class TaLib:
    def __init__(self, Price, Open, High, Low, Vols):
        self.Price = Price
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Vols = Vols
    
    def WMA(self, Price):
        real = talib.WMA(Price, timeperiod=30)
        return real
    
    def DEMA(self,Price):
        real = talib.DEMA(self.Price, timeperiod=30)
        return real
    
    def SMA(self, Price):
        real = talib.SMA(Price, timeperiod=30)
        return real
    
    def EMA(self, Price):
        real = talib.EMA(Price, timeperiod=30)
        return real
    
    def MACD(self, Price):
        EMA12 = talib.EMA(Price, timeperiod = 12)
        EMA26 = talib.EMA(Price, timeperiod = 26)
        real = EMA12 - EMA26
        return real
    
    def RSI(self, Price):
        real = talib.RSI(Price, timeperiod=14)
        return real
    
    def CMO(self, Price):
        real = talib.CMO(Price, timeperiod=14)
        return real
    
    def TRIX(self, Price):
        real = talib.TRIX(Price, timeperiod=30)
        return real
    
    def DPO(Price):
        p = talib.MA(Price, timeperiod = 30)
        p.shift()
        return close-p
    
    def ROC(self, Price):
        real = talib.ROC(Price, timeperiod=10)
        return real
    
    def CCI(self, High, Low, Price):
        real = talib.CCI(High, Low, Price, timeperiod=14)
        return real
    
    
    def ADX(self, High, Low, Price):
        real = talib.ADX(High, Low, Price, timeperiod=14)
        return real
    
    def AROONOSC(self, High, Low,):
        real = talib.AROONOSC(High, Low, timeperiod=14)
        return real
    
    def VHF(self, Price):
        LCP = talib.MIN(Price, timeperiod = 14)
        HCP = talib.MAX(Price, timeperiod = 14)
        NUM = HCP - LCP
        pre = Price.copy()
        pre = pre.shift()
        DEN = abs(Price - Price.shift())
        DEN = talib.MA(DEN, timeperiod = 14)*14
        return NUM.div(DEN)
    
    def OBV(self, Price, Vols):
        real = talib.OBV(Price, Vols)
        return real
    
    def ATR(self, High, Low, Price):
        real = talib.ATR(High, Low, Price, timeperiod=14)
        return real