<<<<<<< Updated upstream
import os
import subprocess

def getRampUpScore(link):
    repo_url = "https://github.com/lodash/lodash.git"
    repo_dir = "lodash"

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir])

=======
import json
import os
import shutil
import subprocess
from sys import argv
import requests
import re

def getRampUpScore(link):
    if "npmjs.com" in link:
        npm_reg_link = "https://registry." + link.split("www.")[1].replace("/package",'')
        response = requests.get(npm_reg_link)
        result = response.json()
        githubLink = result["repository"]["url"].split("github.com")[1].split("/")
        repo_url = "https://github.com" + result["repository"]["url"].split("github.com")[1]
    elif "github.com" in link:
        repo_url = link
    else:
        return "URLs from this organization are not supported currently."
        
    repo_dir = (repo_url.split("github.com")[1].split("/"))[2].replace(".git", "")
    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
>>>>>>> Stashed changes
    # Change the current working directory to the repository
    os.chdir(repo_dir)

    # Open the README file
<<<<<<< Updated upstream
    with open("README.md", "r") as file:
        lines = file.readlines()
    
=======
    try:
        with open("README.md", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        try:
            with open("README.markdown", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            total_score = 0
            return
    file.close()
>>>>>>> Stashed changes
    install_section = 0
    usage_section = 0 
    examples_section = 0
    docs_section = 0
    #Search README for helpful sections
    for line in lines:
<<<<<<< Updated upstream
        if line.startswith("## Installation"):
            install_section = 1
        if line.startswith("## Usage") or line.startswith("## Examples"):
            usage_section = 1
        if line.startswith("## Docs") or line.startswith("## Documentation"):
=======
        if re.match(r"#+ *install(ation)?", line, re.IGNORECASE):
            install_section = 1
        if re.match(r"#+ *Usage", line, re.IGNORECASE) or re.match(r"#+ *Examples", line, re.IGNORECASE):
            usage_section = 1
        if re.match(r"#+ *Doc(umentation)?", line, re.IGNORECASE):
>>>>>>> Stashed changes
            docs_section = 1
    
    readmeSectionScore = (install_section + usage_section + docs_section) / 3
    readmeLengthScore = 0
    readmeLineCount = len(lines)
<<<<<<< Updated upstream
    if readmeLineCount > 100: #decide on better metrics
        readmeLengthScore = 1
    elif readmeLineCount < 100 and readmeLineCount > 50:
        readmeLengthScore = 0.7
    elif readmeLineCount < 50 and readmeLineCount > 25:
        readmeLengthScore = 0.35
    else:
        readmeLengthScore = 0
    
    print("Section Score: "+str(readmeSectionScore))
    print("Length Score: "+str(readmeLengthScore) + "  Length: " + str(readmeLineCount))
    print("Total score: " + str((readmeLengthScore + readmeSectionScore)/2))


if __name__ == "__main__":
    getRampUpScore("https://github.com/expressjs/express.git")
=======
    if readmeLineCount > 150: #decide on better metrics
        readmeLengthScore = 1
    elif readmeLineCount < 150 and readmeLineCount > 125:
        readmeLengthScore = 0.9
    elif readmeLineCount < 125 and readmeLineCount > 100:
        readmeLengthScore = 0.8
    elif readmeLineCount < 30 and readmeLineCount > 0:
        readmeLengthScore = 0
    else:
        readmeLengthScore = readmeLineCount/100 * 0.8
    
    print("Section Score: "+str(readmeSectionScore))
    print("Length Score: "+str(readmeLengthScore) + "  Length: " + str(readmeLineCount))
    total_score = round((readmeLengthScore + readmeSectionScore)/2,2)
    
    print("Total score: " + str(total_score))

    
    os.chdir("..")

    # Delete the repository directory
    full_dir = os.path.join(os.getcwd(), repo_dir)
    # shutil.rmtree(full_dir)

    try:
        with open("metrics.json", "r") as f:
            data = json.load(f)
    except:
        data = {}

    # Update the score of the "ResponsiveMaintainer" metric
    if link in data:
        data[link]["RampUp"] = total_score
    else:
        data[link] = {"RampUp": total_score}

    # Write the updated JSON data back to the file
    with open("metrics.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    getRampUpScore(str(argv[1]))
>>>>>>> Stashed changes
