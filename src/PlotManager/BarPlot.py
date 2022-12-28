import matplotlib.pyplot as plt


def show_bar(commits):
    bar_width = 2
    plt.bar(commits["date"], width=bar_width, height=commits["NumberOfCommits"])
    plt.ylabel("Numero de Commits")
    plt.xlabel("Semanas")
    plt.title("Commits / Semana")

    plt.show()


def show_bar_by_people(commits, column):
    bar_width = 0.8
    plt.bar(commits[column], width=bar_width, height=commits["NumberOfCommits"])
    plt.ylabel("Numero de Commits")
    plt.xlabel("Persona")
    plt.title("Commit/Persona")
    plt.xticks(rotation=90)

    plt.show()

def show_horizontal_bar(commits):
    name = commits['name'] #.head(12)
    numberOfCommits = commits['NumberOfCommits']#.head(12)

    # Figure Size
    fig, ax = plt.subplots(figsize=(10, 8))

    # Horizontal Bar Plot
    ax.barh(name, numberOfCommits, align='center')

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')

    # Add Plot Title
    ax.set_title('Commits X Usuarios',
                 loc='left', )

    # Add Text watermark
    fig.text(0.9, 0.15, '', fontsize=12,
             color='grey', ha='right', va='bottom',
             alpha=0.7)

    # Show Plot
    plt.show()
