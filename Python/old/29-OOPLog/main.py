import datetime

class LogFile():
	'''Logs entries and saves them with log date. No chaining allowed, because the last item 
		overwrites everything since the time (key) is the same for each chained item'''

	@staticmethod
	def is_valid_entry(entry):
		return isinstance(entry, str) or isinstance(entry, int)

	def __init__(self):
		self.state = {}

	def write(self, text):
		if LogFile.is_valid_entry(text):
			self.state.update({ datetime.datetime.now(): str(text) })

	def __str__(self):
		'''Gets the dates of each entry on each new line '''
		ret = ""
		for date, entry in self.state.items():
			ret = f"{date} - {entry}\n{ret}"
		return ret


class DelimFile(LogFile):
	'''Allows logging multiple entries at once, either by list or additional args. When read, 
		returns entries separated by given delimiter. Does not save log time'''

	def __init__(self, delimiter):
		self.state = [] # We don't store any date so a dictionary is unnecessary
		self.delimiter = delimiter

	def write(self, text, *args):
		if not args:
			if LogFile.is_valid_entry(text):
				self.state.append(str(text))
			elif isinstance(text, list):
				self.write(*text)
		else:
			all_entries = [text] + list(args)
			valid_entries = filter(lambda x: LogFile.is_valid_entry(x), all_entries)
			self.state.extend(map(lambda x: str(x), valid_entries))
		return self

	def __str__(self):
		'''Returns logs separated by the delimiter'''
		return self.delimiter.join(self.state)