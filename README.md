A machine learning model to predict the winner of the ICC Mens T20 World Cup 2024.

# Data Extraction
**BeautifulSoup** was used to extract the data of each historic ICC T20 Mens World Cup. The features extracted were - Teams involved, Winner, Margin, Ground where the match is played, Match date, T20 Int #.
This comprised of the master dataset. Additional features such as - each teams's avg. batting and bowling ranking was calculated basis one day prior of the match from the official page of ICC Rankings. Each team's
WC participation and total WCs won was recorded manually from Cricinfo basis on the day the match was played, and for each match the win % of one team over the other leading upto that match was recorded manually
using Cricinfo's popular Statsguru.

With data extraction, 16 feautures were extracted (out of which some were ignored later for training the model) - 

1. Team 1
2. Team 2
3. Winner
4. Margin
5. Ground
6. Match Date
7. T20 Int #
8. Team 1 Avg Batting Ranking (till one day before the match)
9. Team 2 Avg Batting Ranking (till one day before the match)
10. Team 1 Avg Bowling Ranking (till one day before the match)
11. Team 2 Avg Bowling Ranking (till one day before the match)
12. Team 1 Total WCs participation (till one day before the start of each WC)
13. Team 1 Total WCs won (till one day before the start of each WC)
14. Team 2 Total WCs participation (till one day before the start of each WC)
15. Team 2 Total WCs won (till one day before the start of each WC)
16. Team 1 win % over Team 2 (leading upto that match including all T-20 Int matches played outside WCs too)

## Data sources -
As an example, results of all matches played in ICC T20 World Cup 2007 was available on https://www.espncricinfo.com/records/season/team-match-results/2007to08-2007to08?trophy=89
and as an example, the players from India who participated in ICC T20 World Cup 2007 was available on  https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/india-squad-305846/series-squads
