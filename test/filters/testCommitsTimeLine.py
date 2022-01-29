import unittest
import pandas as pd
import json


from src.filters.CommitsTimeLine import CommitsTimeline


class TestCommitsTimeLine(unittest.TestCase):

    def test_should_has_3_items_when_filter_per_week(self):
        expected_rows = 3
        expected_columns = 2

        commits = '[' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 25 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 25 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 18 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 11 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 11 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 25 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 25 Jan 2022 09:24:59 -0500"},' \
                  '{"name": "Antonio Banderas", "email": "abanderas@elmariachi.com", "date": "Tue, 25 Jan 2022 09:24:59 -0500"}' \
                  ']'

        json_var = json.loads(commits)
        commitsDf = pd.DataFrame(json_var)

        commits_per_week = CommitsTimeline().get_commits_per_week(commitsDf)
        dfShape = commits_per_week.shape

        print(F" commits: {commits_per_week.shape}")
        assert dfShape[0] == expected_rows
        assert dfShape[1] == expected_columns
