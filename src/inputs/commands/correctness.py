from datetime import datetime
import requests

GITHUB_TOKEN = ""

# Function to get the "correctness score" of a given GitHub repository
def getCorrectnessScore(link):
    # Extract the repository owner and name from the given link
    githubLink = link.split("github.com")[1].split("/")
    owner = githubLink[1]
    repo = githubLink[2].replace(".git", "")

    # Create a link to the API endpoint for the repository
    repoAPI_link = "https://api.github.com/repos"f"/{owner}/{repo}"
    # Make a GET request to the API endpoint using the token
    response = requests.get(repoAPI_link, headers={'Authorization': "token{}".format(GITHUB_TOKEN)})
    # Get the JSON data from the response
    result = response.json()
    forks_count = result["forks"]

    # Define a GraphQL query to get information about the open issues in the repository
    query = """
    query {
    repository(owner: "OWNER", name: "REPO") {
        issues(states:OPEN, first: 100) {
        totalCount
        edges {
            node {
            title
            labels(first:100) {
                edges {
                node {
                    name
                }
                }
            }
            }
        }
        }
    }
    """
    # Replace placeholders in the query with the repository owner and name
    query = query.replace("OWNER",owner)
    query = query.replace("REPO",repo)

    # Define a header for the API request
    headers = {
        "Authorization": "Bearer "
    }

    # Make a POST request to the GitHub API using the query
    response = requests.post("https://api.github.com/graphql", json={ "query": query }, headers=headers)
    # Get the JSON data from the response
    result = response.json()

    total_issue_count = result["data"]["repository"]["issues"]["totalCount"]
    firstHundredIssues = result["data"]["repository"]["issues"]["edges"]
    actualIssues = 100
    # Iterate over the first 100 open issues
    for issue in firstHundredIssues:
        # Get the labels for each issue
        labels = [label["node"]["name"] for label in issue["node"]["labels"]["edges"]]
        #discard issues with labels indicating that there is no problem with the package itself
        if "question" in labels or "awaiting more info" in labels or "discussion" in labels or "awaiting more information" in labels or "discuss" in labels or "invalid" in labels or "duplicate" in labels:
            actualIssues -= 1
    approx_real_issues = total_issue_count * (actualIssues/100)
    #Calc part of score using issue count and number of forks

    print(total_issue_count)
    print(approx_real_issues)

if __name__ == "__main__":
    getCorrectnessScore("https://github.com/expressjs/express")