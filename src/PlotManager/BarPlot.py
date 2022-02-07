import matplotlib.pyplot as plt


def show_bar(commits):
    plt.bar(commits["date"], height=commits["NumberOfCommits"])
    plt.show()
