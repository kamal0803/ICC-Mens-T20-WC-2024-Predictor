from bs4 import BeautifulSoup
import requests
import pandas as pd

class AllWCsPlayers:

    def __init__(self, all_WCs_teams):
        self.all_WCs_teams = all_WCs_teams

    def all_players_list(self):

        columns = ['Team', 'Year', 'Player Name']
        df = pd.DataFrame(columns)

        years = ['2007', '2009', '2010', '2012', '2014', '2016', '2021', '2022', '2024']

        k = 0
        for key, value in self.all_WCs_teams.items():

            for i in range(len(years)):

                try:
                    response = requests.get(value[years[i]])
                    players = response.text
                    soup = BeautifulSoup(players, "html.parser")
                    rows = soup.find_all(class_="ds-relative ds-flex ds-flex-row ds-space-x-4 ds-p-3")
                    t = 1

                    for j in range(len(rows)):
                        try:
                            if rows[j].find_all(class_="ds-flex-1")[0].find(
                                    class_="ds-text-tight-xs").text == "Withdrawn":
                                continue
                        except AttributeError:
                            df.loc[k, 'Team'] = key
                            df.loc[k, 'Year'] = years[i]
                            df.loc[k, 'Player Name'] = rows[j].find_all(class_="ds-popper-wrapper ds-inline")[1].find(
                                name="span").text
                            k = k + 1

                except requests.exceptions.MissingSchema:
                    continue

        df = df.drop(0, axis=1)
        df.to_excel('all_t20_world_cup_players_list.xlsx', index=False)

        return df

