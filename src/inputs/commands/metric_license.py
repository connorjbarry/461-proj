import requests
import numpy as np

def import_package_github(url, token):
	try:
		# find license for GITHUB api format
		response = requests.get(url,headers={'Authorization': f"token {token}"})
		data = response.json()
		return data
	except:
		### No license ###
		return -1

def import_package_npmjs(url):
	try:
		response = requests.get(url)
		data = response.json()
		return data
	except:
		### No license ###
		return -1

def calc_license_github(data, url, GH_token):
	# if text contains "MIT License", or any similar string, score is 1
	# if not, the score is 0
	
	# if len(data['license']) > 1

	if len(data['license']) > 1 and "MIT" in data['license']['name']:
		return 1
	elif len(data['license']) > 1 and "Other" in data['license']['name']:
		return 0.5
	else:
		# change url from api format to standard and look for README.md file
		new_url = url.replace('api.', '')
		new_url = new_url.replace('repos/', '')
		new_url = new_url + '/blob/master/README.md'
		try:
			response = requests.get(new_url, headers={'Authorization': f"token {GH_token}"})
			data = response.json()
			if "MIT license" in data:
				return 1
			else:
				return 0
		except:		
			return 0

def calc_license_npmjs(data, url):
	# if text contains "MIT License", or any similar string, score is 1
	# if not, the score is 0

	if "'license':'MIT'" in data:
		return 1
	else:
		# change url from api format to standard and look for README.md file
		new_url = url.replace('registry.', '')
		new_url = new_url + '/README.md'
		try:
			response = requests.get(new_url)
			data = response.json()
			if "MIT" in data:
				return 1
			else:
				return 0
		except:		
			return 0

def score(url):
	license_score = 0
	
	GH_token = "PLACEHOLDER"
	
	if "github" in url:
		package_data = import_package_github(url, GH_token)
		if package_data != -1:
			license_score = calc_license_github(package_data, url, GH_token)
	
	elif "npmjs" in url:
		package_data = import_package_npmjs(url)
		if package_data != -1:
			license_score = calc_license_npmjs(package_data, url)
	
	return license_score

if __name__ == "__main__":
	# URL examples
	url = "https://api.github.com/repos/nullivex/nodist"
	url = "https://registry.npmjs.com/express"
	l_score = score(url)
	print(l_score)