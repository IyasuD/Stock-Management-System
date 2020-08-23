'''The stock class holds data related to a single stock.
It provides the appropriate getters and setters'''
class Stock:
    def __init__(self, stock_id, symbol, date, open_stock, high, low, close, volume, share_no):
        '''Constructor for the stock class'''
        self._stock_id = stock_id
        self._symbol = symbol
        self._date = date
        self._open_stock = open_stock
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume
        self._share_no = share_no

    @property
    def stock_id(self):
        return self._Stock_id

    @stock_id.setter
    def stock_id(self, stock_id):
        self._stock_id = stock_id

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def open_stock(self):
        return self._open_stock

    @open_stock.setter
    def open_stock(self, open_stock):
        self._open_stock = open_stock

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        self._high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        self._low = low

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, close):
        self._close = close

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume
    @property
    def share_no(self):
        return self._share_no

    @share_no.setter
    def share_no(self, share_no):
        self._share_no = share_no

