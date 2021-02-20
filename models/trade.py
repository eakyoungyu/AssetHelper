# -*- coding: utf-8 -*- 
class Trade:
	BUY = 0
	SOLD = 1
	KOR_BUY_OR_SOLD = ["매수", "매도"]

	def __init__(self, lines):
		self.lines = lines
		self.set_data()

	def set_data(self):
		# korean char = 3byte
		self.date = self.lines[1].strip()[-10:]
		self.buy_or_sold = self.lines[3].strip()[-6:]
		if self.buy_or_sold == self.KOR_BUY_OR_SOLD[self.BUY]:
			self.buy_or_sold = self.BUY
		elif self.buy_or_sold == self.KOR_BUY_OR_SOLD[self.SOLD]:
			self.buy_or_sold = self.SOLD
		semicolon = self.lines[5].find(":")
		self.symbol = self.lines[5][semicolon + 2: -1]
		semicolon = self.lines[7].find(":")
		self.amount = self.lines[7][semicolon + 2: -4]
		semicolon = self.lines[9].find(":")
		self.price = self.lines[9][semicolon + 2: -1]

	def __str__(self):
		return "%s %s %s %s %s" % (self.date, self.KOR_BUY_OR_SOLD[self.buy_or_sold], self.symbol, self.amount, self.price)