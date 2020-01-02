# non structured info
# calculate

# football scores, calc win, draw, loss

scores = [
	"baierni 4 0 arsenali",
	"chelsea 8 1 gladbaxi",
	"galatasarai 3 6 manchester",
	"borusia 1 1 albaneti"
	]

def add_result(team_name, result, results):
	if team_name in results:
		new_result = {}
		temp = results[team_name]
		for k in result.keys():
			new_result[k] = temp[k] + result[k]
		results[team_name] = new_result
	else:
		results[team_name] = result

def get_results(scores):
	results = {}
	for match in scores:
		team1, score1, score2, team2 = match.split()
		if score1 > score2:
			add_result(team1, {"win": 1, "draw": 0, "loss": 0}, results)
			add_result(team2, {"win": 0, "draw": 0, "loss": 1}, results)
		elif score1 < score2:
			add_result(team1, {"win": 0, "draw": 0, "loss": 1}, results)
			add_result(team2, {"win": 1, "draw": 0, "loss": 0}, results)
		else:
			add_result(team1, {"win": 0, "draw": 1, "loss": 0}, results)
			add_result(team2, {"win": 0, "draw": 1, "loss": 0}, results)
	return results