import requests
from operator import itemgetter
from matplotlib import pyplot as plt

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extract data for visualization
titles = []
comments = []

for submission in submission_dicts:
    titles.append(submission['title'])
    comments.append(submission['comments'])

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(titles, comments, color='skyblue')
plt.xlabel('Number of Comments')
plt.title('Top 30 Hacker News Submissions by Comments')

# Invert the y-axis to display the submission with the most comments at the top
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()






