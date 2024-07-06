from bs4 import BeautifulSoup
import requests
import pandas as pd


class AllT20WCMasterDataSet:

    def __init__(self, wc_URLs):
        self.wc_URLs = wc_URLs

    def create_master_dataset(self):

        columns = ['Team1', 'Team2', 'Winner', 'Margin', 'Ground', 'Ground 2', 'Match Date', 'T-20 Int Match',
                   'T-20 Int Match 2']
        df = pd.DataFrame(columns)

        k = 0
        for url in self.wc_URLs:
            response = requests.get(url)
            match_results = response.text

            soup = BeautifulSoup(match_results, "html.parser")

            rows = soup.find_all(name="tr")
            for i in range(len(rows)):
                for j in range(len(rows[i].find_all(name="span"))):
                    df.loc[k, columns[j]] = rows[i].find_all(name="span")[j].text
                k = k + 1

        df = df[df['Team1'] != 'Team 1']
        df = df.drop(0, axis=1)
        df = df.drop('Ground 2', axis=1)
        df = df.drop('T-20 Int Match 2', axis=1)
        df['Match Date'] = pd.to_datetime(df['Match Date']).dt.strftime('%Y/%m/%d')
        df.to_excel('all_t20_world_cup_matches_results.xlsx', index=False)

        return df
