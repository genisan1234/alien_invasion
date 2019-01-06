import json
def write_high_score(hi_score):
	with open('index.json','w') as fd:
		value=(hi_score,0)
		json.dump(value,fd)
	fd.close()

def read_high_score():
	with open('index.json','r') as fd:
		value=json.load(fd)
	fd.close()
	return  value[0]

