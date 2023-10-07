import pygal
import requests
from pygal.style import Style
from operator import itemgetter

# Make an api call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("status code : ", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.

    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json")
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
        'xlink': response_dict['url']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

# Extract data for visualization
titles = []
comments = []

for submission in submission_dicts:
    titles.append(submission['title'])
    comments.append(submission['comments'])

# Make the visualization
my_style = Style(
    background='transparent',  # Make the background transparent
    plot_background='#B0E0E6',  # Use sky blue as the plot background color
    value_label_font_size=14,   # Adjust font size for value labels
    label_font_size=12,         # Adjust font size for axis labels
    major_label_font_size=14,   # Adjust font size for major axis labels
    colors=('#007acc',),        # Set the color of the bars to sky blue
)

chart = pygal.Bar(style=my_style, x_label_rotation=45, truncate_label=15)
chart.title = "Top 30 Hacker News Submissions by Comments"
chart.x_labels = titles

chart.add("", comments)
chart.render_to_file("hn_submission.svg")
