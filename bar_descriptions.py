import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Python Projects"
chart.x_labels = ["Tensor flow", "django", "flask"]

plot_dicts = [
    {"value": 494, "label": "Description of Tensor flow."},
    {"value": 393, "label": "Description of django."},
    {"value": 561, "label": "Description of flask."},
    ]

chart.add("hello", plot_dicts)
chart.render_to_file("bar_description.svg")






