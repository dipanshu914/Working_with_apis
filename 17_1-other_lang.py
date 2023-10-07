import  requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
r = requests.get(url)
print("Status code : ", r.status_code)

# Store API response in a variable
response_dict = r.json()
print("Total repositories : ", response_dict["total_count"])

# Process results
print(response_dict.keys())

# Explore info about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned : ", len(repo_dicts))

# Examine the first repo
repo_dict = repo_dicts[0]
print("\nkeys : ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("\nSelected info about first repo")

names, plot_dicts = [], []
for repo_dict in repo_dicts:

    print("\nName : ", repo_dict['name'])
    print("Owner : ", repo_dict['owner']['login'])
    print('stars : ', repo_dict['stargazers_count'])
    print('Repository : ', repo_dict['html_url'])
    print('Description : ', repo_dict['description'])

    names.append(repo_dict['name'])
    plot_dict = {
        "value": repo_dict['stargazers_count'],
        "label": repo_dict["description"],
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)

# Make the Visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 14
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-starred python Projects on github"
chart.x_labels = names

chart.add("hello", plot_dicts)
chart.render_to_file("java_repo.svg")
