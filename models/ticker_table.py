class TickerTable:
	def __init__(self, tickers, symbols):
		self.tickers = tickers
		self.symbols = symbols
		self.ticker_to_symbol = dict(zip(tickers, symbols))
		self.symbol_to_ticker = dict(zip(symbols, tickers))

	def __str__(self):
		return "ticker_to_symbol %s" % self.ticker_to_symbol

	#def add_ticker(ticker):		
