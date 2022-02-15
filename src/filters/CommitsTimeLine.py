import pandas as pd


class CommitsTimeline:
    def get_commits_per_week(self, commitsDf):
        commitsDf['date'] = pd.to_datetime(commitsDf['date'], utc=True)
        commitsDf = commitsDf.set_index(pd.DatetimeIndex(commitsDf['date']))

        commits_by_week = (
            commitsDf
            .resample('W')
            .size()
            .to_frame('NumberOfCommits')
            .reset_index()
        )

        return commits_by_week
