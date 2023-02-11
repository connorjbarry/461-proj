import os
import subprocess

def getRampUpScore(link):
    repo_url = "https://github.com/lodash/lodash.git"
    repo_dir = "lodash"

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir])

    # Change the current working directory to the repository
    os.chdir(repo_dir)

    # Open the README file
    with open("README.md", "r") as file:
        lines = file.readlines()
    
    install_section = 0
    usage_section = 0 
    examples_section = 0
    docs_section = 0
    #Search README for helpful sections
    for line in lines:
        if line.startswith("## Installation"):
            install_section = 1
        if line.startswith("## Usage") or line.startswith("## Examples"):
            usage_section = 1
        if line.startswith("## Docs") or line.startswith("## Documentation"):
            docs_section = 1
    
    readmeSectionScore = (install_section + usage_section + docs_section) / 3
    readmeLengthScore = 0
    readmeLineCount = len(lines)
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