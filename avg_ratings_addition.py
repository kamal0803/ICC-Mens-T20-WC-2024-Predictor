import pandas as pd
from bs4 import BeautifulSoup
import requests

class AvgBattingBowlingRanking:

    def __init__(self, df_master_dataset, df_players_dataset, inverse_country_code):
        self.df_master_dataset = df_master_dataset
        self.df_players_dataset = df_players_dataset
        self.inverse_country_code = inverse_country_code

    def team_avg_ranking(self, skill):

        for j in range(len(self.df_master_dataset)):

            year = int(pd.to_datetime(self.df_master_dataset['Match Date'])[j].year)

            date_req = f"{pd.to_datetime(self.df_master_dataset['Match Date'])[j].year}/{pd.to_datetime(self.df_master_dataset['Match Date'])[j].month}/{pd.to_datetime(self.df_master_dataset['Match Date'])[j].day - 1}"
            url = f"https://www.relianceiccrankings.com/datespecific/t20/{skill}/"
            url = url + date_req + "/"

            response = requests.get(url, timeout=10)
            icc_ratings = response.text
            soup = BeautifulSoup(icc_ratings, "html.parser")

            rows = soup.find_all(name="tr")
            count = 0
            total_ranking = 0
            total_players = len(self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team1'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist())
            for i in range(1, len(rows)):

                try:
                    if rows[i].find(name="img")['alt'] == self.inverse_country_code[self.df_master_dataset['Team1'][j]] and rows[i].find(class_="players").text.strip() in self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team1'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist():
                        count = count + 1
                        total_ranking = total_ranking + int(rows[i].find_all(name="td")[0].text)

                except KeyError:
                    if rows[i].find(name="img")['alt'] == self.df_master_dataset['Team1'][j] and rows[i].find(class_="players").text.strip() in self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team1'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist():
                        count = count + 1
                        total_ranking = total_ranking + int(rows[i].find_all(name="td")[0].text)

            total_ranking = total_ranking + (total_players - count) * 101

            if skill == "batting":
                self.df_master_dataset.at[j, 'Team1 Avg Batting Ranking'] = round(total_ranking / total_players, 2)
            else:
                self.df_master_dataset.at[j, 'Team1 Avg Bowling Ranking'] = round(total_ranking / total_players, 2)

            count = 0
            total_ranking = 0
            total_players = len(self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team2'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist())
            for i in range(1, len(rows)):
                try:
                    if rows[i].find(name="img")['alt'] == self.inverse_country_code[self.df_master_dataset['Team2'][j]] and rows[i].find(class_="players").text.strip() in self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team2'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist():
                        count = count + 1
                        total_ranking = total_ranking + int(rows[i].find_all(name="td")[0].text)
                except KeyError:
                    if rows[i].find(name="img")['alt'] == self.df_master_dataset['Team2'][j] and rows[i].find(class_="players").text.strip() in self.df_players_dataset[(self.df_players_dataset['Team'] == self.df_master_dataset['Team2'][j]) & (self.df_players_dataset['Year'] == year)]['Player Name'].tolist():
                        count = count + 1
                        total_ranking = total_ranking + int(rows[i].find_all(name="td")[0].text)
            total_ranking = total_ranking + (total_players - count) * 101

            if skill == "batting":
                self.df_master_dataset.at[j, 'Team2 Avg Batting Ranking'] = round(total_ranking / total_players, 2)
            else:
                self.df_master_dataset.at[j, 'Team2 Avg Bowling Ranking'] = round(total_ranking / total_players, 2)

        return self.df_master_dataset

