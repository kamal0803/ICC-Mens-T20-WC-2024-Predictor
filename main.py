from master_dataset import AllT20WCMasterDataSet
from player_extraction import AllWCsPlayers
from avg_ratings_addition import AvgBattingBowlingRanking

wc_URLs = ['https://www.espncricinfo.com/records/season/team-match-results/2007to08-2007to08?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2009-2009?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2010-2010?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2012to13-2012to13?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2013to14-2013to14?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2015to16-2015to16?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2021to22-2021to22?trophy=89',
        'https://www.espncricinfo.com/records/season/team-match-results/2022to23-2022to23?trophy=89',
        'https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2024-15946']

all_WCs_teams = {
    'Afghanistan': {
        '2007': '',
        '2009': '',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/afghanistan-squad-454415/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/afghanistan-squad-579340/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/afghanistan-squad-719975/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/afghanistan-squad-970937/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/afghanistan-squad-1277123/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/afghanistan-squad-1334760/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/afghanistan-squad-1431702/series-squads'
    },
    'Australia': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/australia-squad-302811/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/australia-squad-402963/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/australia-squad-454007/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/australia-squad-577587/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/australia-squad-718021/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/australia-squad-970611/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/australia-squad-1274024/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/australia-squad-1331879/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/australia-squad-1431715/series-squads'
    },
    'Bangladesh': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/bangladesh-squad-306124/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/bangladesh-squad-402850/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/bangladesh-squad-454012/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/bangladesh-squad-577611/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/bangladesh-squad-719705/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/bangladesh-squad-968703/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/bangladesh-squad-1276977/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/bangladesh-squad-1334654/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/bangladesh-squad-1433740/series-squads'
    },
    'Canada': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': '',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/canada-squad-1431914/series-squads'
    },
    'England': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/england-squad-305707/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/england-squad-402457/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/england-squad-454166/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/england-squad-578597/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/england-squad-716897/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/england-squad-971143/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/england-squad-1276994/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-squad-1332100/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/england-squad-1431604/series-squads'
    },
    'Hong Kong': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/hong-kong-squad-718557/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/hong-kong-squad-966579/series-squads',
        '2021': '',
        '2022': '',
        '2024': ''
    },
    'India': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/india-squad-305846/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/india-squad-402820/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/india-squad-453550/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/india-squad-576822/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/india-squad-718061/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/india-squad-969277/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/india-squad-1276930/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/india-squad-1334371/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/india-squad-1431601/series-squads'
    },
    'Kenya': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/kenya-squad-306994/series-squads',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': '',
        '2022': '',
        '2024': ''
    },
    'Ireland': {
        '2007': '',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/ireland-squad-403251/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/ireland-squad-453047/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/ireland-squad-577781/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/ireland-squad-718629/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/ireland-squad-970515/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/ireland-squad-1277052/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/ireland-squad-1336390/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/ireland-squad-1432769/series-squads'
    },
    'Namibia': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/namibia-squad-1277169/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/namibia-squad-1335339/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/namibia-squad-1433240/series-squads'
    },
    'Nepal': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/nepal-squad-720593/series-squads',
        '2016': '',
        '2021': '',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/nepal-squad-1431788/series-squads'
    },
    'Netherlands': {
        '2007': '',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/netherlands-squad-402897/series-squads',
        '2010': '',
        '2012': '',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/netherlands-squad-720357/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/netherlands-squad-969699/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/netherlands-squad-1277265/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/netherlands-squad-1332846/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/netherlands-squad-1433671/series-squads'
    },
    'New Zealand': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/new-zealand-squad-306030/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/new-zealand-squad-398679/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/new-zealand-squad-454099/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/new-zealand-squad-577418/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/new-zealand-squad-719483/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/new-zealand-squad-967661/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/new-zealand-squad-1272863/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/new-zealand-squad-1335613/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/new-zealand-squad-1431440/series-squads'
    },
    'Oman': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/oman-squad-972415/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/oman-squad-1276928/series-squads',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/oman-squad-1431785/series-squads'
    },
    'Pakistan': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/pakistan-squad-305845/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/pakistan-squad-402879/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/pakistan-squad-451683/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/pakistan-squad-572771/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/pakistan-squad-719067/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/pakistan-squad-971159/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/pakistan-squad-1276475/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/pakistan-squad-1334804/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/pakistan-squad-1435201/series-squads'
    },
    'P.N.G.': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/papua-new-guinea-squad-1274534/series-squads',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/papua-new-guinea-squad-1432846/series-squads'
    },
    'Scotland': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/scotland-squad-305027/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/scotland-squad-403205/series-squads',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/scotland-squad-970519/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/scotland-squad-1277118/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/scotland-squad-1336388/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/scotland-squad-1432589/series-squads'
    },
    'South Africa': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/south-africa-squad-306554/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/south-africa-squad-402863/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/south-africa-squad-454127/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/south-africa-squad-576581/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/south-africa-squad-719873/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/south-africa-squad-971249/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/south-africa-squad-1277047/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/south-africa-squad-1332756/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/south-africa-squad-1431579/series-squads'
    },
    'Sri Lanka': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/sri-lanka-squad-306061/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/sri-lanka-squad-402864/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/sri-lanka-squad-454161/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/sri-lanka-squad-579003/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/sri-lanka-squad-719903/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/sri-lanka-squad-973531/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/sri-lanka-squad-1277261/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/sri-lanka-squad-1335180/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/sri-lanka-squad-1433061/series-squads'
    },
    'U.A.E.': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/united-arab-emirates-squad-720597/series-squads',
        '2016': '',
        '2021': '',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/united-arab-emirates-squad-1335338/series-squads',
        '2024': ''
    },
    'Uganda': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': '',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/uganda-squad-1432588/series-squads'
    },
    'U.S.A.': {
        '2007': '',
        '2009': '',
        '2010': '',
        '2012': '',
        '2014': '',
        '2016': '',
        '2021': '',
        '2022': '',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/united-states-of-america-squad-1432101/series-squads'
    },
    'West Indies': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/west-indies-squad-306992/series-squads',
        '2009': 'https://www.espncricinfo.com/series/icc-world-twenty20-2009-335113/west-indies-squad-403555/series-squads',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/west-indies-squad-454405/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/west-indies-squad-578947/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/west-indies-squad-720407/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/west-indies-squad-966973/series-squads',
        '2021': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2021-22-1267897/west-indies-squad-1277120/series-squads',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/west-indies-squad-1334700/series-squads',
        '2024': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/west-indies-squad-1432115/series-squads'
    },
    'Zimbabwe': {
        '2007': 'https://www.espncricinfo.com/series/icc-world-twenty20-2007-08-286109/zimbabwe-squad-306993/series-squads',
        '2009': '',
        '2010': 'https://www.espncricinfo.com/series/icc-world-twenty20-2010-412671/zimbabwe-squad-453538/series-squads',
        '2012': 'https://www.espncricinfo.com/series/icc-world-twenty20-2012-13-531597/zimbabwe-squad-577669/series-squads',
        '2014': 'https://www.espncricinfo.com/series/world-t20-2013-14-628368/zimbabwe-squad-722149/series-squads',
        '2016': 'https://www.espncricinfo.com/series/world-t20-2015-16-901359/zimbabwe-squad-972403/series-squads',
        '2021': '',
        '2022': 'https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/zimbabwe-squad-1334837/series-squads',
        '2024': ''
    }
}


country_code = {
    'SA': 'South Africa',
    'AUS': 'Australia',
    'BAN': 'Bangladesh',
    'CHI': 'Chile',
    'WI': 'West Indies',
    'SL': 'Sri Lanka',
    'ENG': 'England',
    'NZ': 'New Zealand',
    'PAK': 'Pakistan',
    'IND': 'India',
    'KEN': 'Kenya',
    'ZIM': 'Zimbabwe',
    'CAN': 'Canada',
    'SCO': 'Scotland',
    'NED': 'Netherlands',
    'NAM': 'Namibia',
    'MAW': 'Malawi',
    'ROM': 'Romania',
    'POR': 'Portugal',
    'HUN': 'Hungary',
    'BOT': 'Botswana',
    'AFG': 'Afghanistan',
    'IRE': 'Ireland',
    'HK': 'Hong Kong',
    'UAE': 'U.A.E',
    'OMA': 'Oman',
    'NEP': 'Nepal',
    'PNG': 'P.N.G'
}
inverse_country_code = {v: k for k, v in country_code.items()}

t20_wc_masterdataset = AllT20WCMasterDataSet(wc_URLs)
df_master_dataset = t20_wc_masterdataset.create_master_dataset()

players_dataset = AllWCsPlayers(all_WCs_teams)
df_players_dataset = players_dataset.all_players_list()

avg_batting_ratings = AvgBattingBowlingRanking(df_master_dataset, df_players_dataset, inverse_country_code)
df_master_dataset_with_batting_ratings = avg_batting_ratings.team_avg_ranking("batting")

avg_bowling_ratings = AvgBattingBowlingRanking(df_master_dataset_with_batting_ratings, df_players_dataset, inverse_country_code)
df_master_dataset_with_batting_bowling_ratings = avg_bowling_ratings.team_avg_ranking("bowling")
df_master_dataset_with_batting_bowling_ratings.to_excel(r'wc_final_dataset.xlsx', index=False)
