from datetime import datetime
import requests

# Constants for time intervals in seconds
MONTH_IN_SECONDS = 60 * 60 * 24 * 30
WEEK_IN_SECONDS = 60 * 60 * 24 * 7
GITHUB_TOKEN = ""  # Replace with actual Github token if available

# Function to calculate the responsive score of a Github repository
def getResponsiveScore(link):
    # Parse the repository details from the link
    githubLink = link.split("github.com")[1].split("/")
    owner = githubLink[1]
    repo = githubLink[2].replace(".git", "")

    # Make a request to the Github API to get the repository details
    repoAPI_link = "https://api.github.com/repos" + "/{}/{}".format(owner, repo)
    response = requests.get(repoAPI_link, headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    result = response.json()

    # Get the list of last 100 commits to the repository
    commitsURL = result["commits_url"].replace("{/sha}", "")
    response = requests.get(commitsURL + "?per_page=100", headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    lastHundredCommits = response.json()

    # Get the list of closed issues in the repository
    issuesURL = result["issues_url"].replace("{/number}", "")
    response = requests.get(issuesURL + "?state=closed&per_page=100", headers={'Authorization': "token {}".format(GITHUB_TOKEN)})
    issues = response.json()

    # Calculate the number of commits and closed issues
    numIssues = len(issues)
    numCommits = len(lastHundredCommits)

    # Calculate the average time between commits
    commitTimeSum = 0
    for i in range(1, len(lastHundredCommits)):
        current = lastHundredCommits[i]["commit"]["committer"]["date"]
        current = datetime.strptime(current, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        prev = lastHundredCommits[i - 1]["commit"]["committer"]["date"]
        prev = datetime.strptime(prev, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        commitTimeSum += prev - current

    # Calculate the average time to close an issue
    issueCloseSum = 0
    for issue in issues:
        createdAt = issue["created_at"]
        closedAt = issue["closed_at"]
        openDate = datetime.strptime(createdAt, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        closeDate = datetime.strptime(closedAt, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        issueCloseSum += closeDate-openDate


    averageCloseTime = issueCloseSum / numIssues
    commitFrequency = commitTimeSum / numCommits


    issueCloseScore = 0

    if commitFrequency < 2*WEEK_IN_SECONDS:
        commitFrequencyScore = 1
    elif commitFrequency < MONTH_IN_SECONDS and commitFrequency >= 2*WEEK_IN_SECONDS:
        commitFrequencyScore = 0.7
    elif commitFrequency < 3*MONTH_IN_SECONDS and commitFrequency >= MONTH_IN_SECONDS:
        commitFrequencyScore = 0.35
    else:
        commitFrequencyScore = 0

    if averageCloseTime < 0.5*WEEK_IN_SECONDS:
        issueCloseScore = 1
    elif averageCloseTime < 0.5*MONTH_IN_SECONDS and averageCloseTime >= 0.5*WEEK_IN_SECONDS:
        issueCloseScore = 0.7
    elif averageCloseTime < MONTH_IN_SECONDS and averageCloseTime >= 0.5*MONTH_IN_SECONDS:
        issueCloseScore = 0.35
    else:
        issueCloseScore = 0
    print("Commit Score: " + str(commitFrequencyScore) + "  Average commit time(days):" + str(commitFrequency/60/60/24))
    print("Issue Score: " + str(issueCloseScore) + "  Avg close time(days):" + str(averageCloseTime / 60 / 60 / 24))
    print(0.5 * commitFrequencyScore + 0.5 *issueCloseScore)

if __name__ == "__main__":
    getResponsiveScore('https://github.com/cloudinary/cloudinary_npm')