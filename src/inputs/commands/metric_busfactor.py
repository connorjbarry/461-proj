import requests
import json
from sys import argv
import numpy as np
import os
from dotenv import load_dotenv
import valid_url as vu

load_dotenv()

GH_token = os.getenv("GITHUB_TOKEN")

def npm_to_github_api(registry_url):
	# converts registry NPM format to api GitHub format
	package_name = registry_url.split("/")[-1]
	response = requests.get(registry_url)
	data = response.json()
	repository_url = data.get("repository", {}).get("url", "")
	repository_url = repository_url.replace("git+", "")
	repository_url = repository_url.replace("ssh://git@", "https://")
	if repository_url.startswith("https://github.com/"):
		owner, repo = repository_url.split("/")[-2:]
		repo = repo.replace(".git", "")
		return f"https://api.github.com/repos/{owner}/{repo}"

	else:
		# Return -1 if the repository URL is not in the GitHub format
		return -1

def import_package_github(url, token):
	try:
		# Imports the license dictionary from the URL
		new_url = url + "/master/package.json"
		new_url = new_url.replace("api", "raw")
		new_url = new_url.replace("repos/", "")
		new_url = new_url.replace("github", "githubusercontent")
		response = requests.get(new_url,headers={'Authorization': f'token {token}'})
		data = json.loads(response.text)
		
		count = 0
		try:
			dependencies = data.get("dependencies")
			count += len(dependencies)
		except:
			pass
		try:
			dependencies = data.get("devDependencies")
			count += len(dependencies)
		except:
			pass
		return count
	except:
		### Invalid URL ###
		return 0

def fit_score(num):
	# scored on a log function that has a max of 1, and slowly decreases
	if num > 0:
		score = (1 - (np.log10(num))/4)
	else:
		score = 0
	if score < 0:
		score = 0
	return score

def score(url,jsonfile):
	dependency_score = 0
	num_dependencies = 0
	# scores the URLs for license compatibility
	if "github" in url:
		num_dependencies = import_package_github(url.replace("github.com", "api.github.com/repos"), GH_token)
		dependency_score = fit_score(num_dependencies)
	
	elif "npmjs" in url:
		new_url = npm_to_github_api(url)
		# will run if url is converted correctly
		if new_url != -1:
			num_dependencies = import_package_github(new_url, GH_token)
			dependency_score = fit_score(num_dependencies)
	dependency_score = round(dependency_score, 2)
	# write data to output file
	try:
		with open(jsonfile, "r") as f:
			data = json.load(f)
	except:
		data = {}
	if url in data:
		data[url]["Bus Factor"] = dependency_score
	else:
		data[url] = {"Bus Factor": dependency_score}

	# Write the updated JSON data back to the file
	with open(jsonfile, "w") as f:
		json.dump(data, f, indent=4)
	
	return dependency_score

if __name__ == "__main__":
    score(str(argv[1]), argv[2])
	