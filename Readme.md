# 2020 IEEE Transactions on Industrial Informatics
## AttractRank: District Attraction Ranking Analysis Based on Taxi Big Data
**Our taxi statistic data and codes are made publicly available for academic research usage.**

### source.csv


##### Data Introduction:

Period：2017.02.01--2017.03.31

Rows : 2306690

Position：Guangzhou, China



##### Data Structure:

| Column       | Explanation                         |
| ------------ | ----------------------------------- |
| id           | Primary key                         |
| from_idx     | The ordinal of  departure place's   |
| to_idx       | The ordinal of  destination place's |
| date_month   | month                               |
| date_day     | day                                 |
| date_hour    | hour                                |
| route_weight | The count of record in this hour    |



##### Data sample:

| id   | from_idx | to_idx | date_month | date_day | date_hour | route_weight |
| ---- | -------- | ------ | ---------- | -------- | --------- | ------------ |
| 0    | 0        | 0      | 2          | 1        | 0         | 9            |
| 1    | 0        | 1      | 2          | 1        | 0         | 1            |
| 2    | 0        | 2      | 2          | 1        | 0         | 2            |
| 3    | 0        | 3      | 2          | 1        | 0         | 1            |
| 4    | 0        | 4      | 2          | 1        | 0         | 3            |
| 5    | 0        | 5      | 2          | 1        | 0         | 3            |
| 6    | 0        | 7      | 2          | 1        | 0         | 2            |
| 7    | 0        | 8      | 2          | 1        | 0         | 3            |
| 8    | 0        | 9      | 2          | 1        | 0         | 4            |
| 9    | 0        | 10     | 2          | 1        | 0         | 1            |
| 10   | 0        | 11     | 2          | 1        | 0         | 10           |


### attractrank.py
This is the code of our attractrank algorithm.


### Data_visualization_application_system
This is the open source code of our visualization application system.


### distance_matrix.csv
This is the distance matrix required by our algorithm.

### districts_details.csv
This is the detailed data about districts of the Guangzhou that we divided, including the latitude and longitude point of the center of each area, and the set of latitude and longitude points of the outer contour of each area, etc.
