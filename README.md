A machine learning model to predict the winner of the ICC Mens T20 World Cup 2024.

# Data Extraction
**BeautifulSoup** was used to extract the data of each historic ICC T20 Mens World Cup. The features extracted were - Teams involved, Winner, Margin, Ground where the match is played, Match date, T20 Int #.
This comprised of the master dataset. Additional features such as - each teams's avg. batting and bowling ranking was calculated basis one day prior of the match from the official page of ICC Rankings (https://www.relianceiccrankings.com/datespecific/t20/batting/2024/07/06/ for batting as ane example and https://www.relianceiccrankings.com/datespecific/t20/bowling/2024/07/06/ for bowling as an example) using BeautifulSoup. Each team's WC participation and total WCs won was recorded manually from Cricinfo basis on the day the match was played, and for each match the win % of one team over the other leading upto that match was recorded manually
using Cricinfo's popular Statsguru (https://stats.espncricinfo.com/ci/engine/stats/index.html).

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

#### Manual Touch Points

After running master_dataset.py, data inconsistencies in Team's name was seen, which was corrected manually, such as U.A.E was corrected to UAE, P.N.G was corrected to PNG, U.S.A was corrected to USA
in all_t20_world_cup_matches_results.xlsx
Further to make this consistent with data in all_t20_world_cup_players_list.xlsx, changes in all_t20_world_cup_players_list was also made, such as United Arab Emirates was corrected to UAE, United States of America was corrected to USA, and Papa New Guinea.

Effectively, countries such as USA, UAE & PNG using abbreviations at some data sets, and full forms at other, this manual touch point took care of everything by using a standard name of UAE, USA & PNG whenever required. 

### Data sources -
As an example, results of all matches played in ICC T20 World Cup 2007 was available on https://www.espncricinfo.com/records/season/team-match-results/2007to08-2007to08?trophy=89
and as an example, the players from India who participated in ICC T20 World Cup 2007 was available on  https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/india-squad-305846/series-squads

# Predicting Results

## Data Pre-processing
Columns such as 'Margin', 'Match Date', 'Ground', 'T-20 Int Match' were removed from the training dataset. The Super-Eight Fixtures of the 2024 WC were separated out, and were part of the test dataset. Feature Scaling and Encoding of categorical variables was performed.

## Building Machine Learning Models
After data pre-processing, accuracy, F1 score, precision, and recall was calculated for various classification models such as **Logistic Regression**, **Random Forest Classifier**, **SVM**, **Naive Bayes**, **Kernel SVM**, **K-Nearest Neighbours**, and **Decision Tree Classifier**. 

Out of all these, the best was **Logistic Regression** in terms of closeness to the actual match results, and second best was **Random Forest Classifier**.
