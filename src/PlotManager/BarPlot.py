import matplotlib.pyplot as plt


def draw_bar(commits_peer_week):
    plt.bar(commits_peer_week["date"], height=commits_peer_week["NumberOfCommits"])
    plt.show()
