def eng_to_geo(ch):
	return { 
	"a": "ა",
	"b": "ბ",
	"c": "ც",
	"d": "დ",
	"e": "ე",
	"f": "ფ",
	"g": "გ",
	"h": "ჰ",
	"i": "ი",
	"j": "ჯ",
	"k": "კ",
	"l": "ლ",
	"m": "მ",
	"n": "ნ",
	"o": "ო",
	"p": "პ",
	"q": "ქ",
	"r": "რ",
	"s": "ს",
	"t": "ტ",
	"u": "უ",
	"v": "ვ",
	"w": "წ",
	"x": "ხ",
	"y": "ყ",
	"z": "ზ",
	"S": "შ",
	"C": "ჩ",
	"W": "ჭ",
	"Z": "ძ",
	"R": "ღ",
	"T": "თ",
	"J": "ჟ",
	}.get(ch, ch)

a = input("english text: ")
ans = ""
for char in a:
	ans += eng_to_geo(char)
print(ans)