# F1-standings-forecasting

Predicting a season's final standings using race results of the first half of the season

# Dataset

## Source

The standings and race results data in the csv files come from [this kaggle dataset](https://www.kaggle.com/datasets/patelris/formula-1-complete-dataset-1950-2026)

Since the above data contains results only for the first 3 races of 2026, the results for the next few races were queried from [Jolpica F1 API](https://api.jolpi.ca/ergast/) (Ergast successor), which is also the original source of the data in the aforementioned Kaggle dataset.

## License

The data is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). For detailed information on this license, refer to the Creative Commons website.(https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)

## Modifications
- Engineered features derived from the data include aggregates of driver performance for current and past seasons
- Missing 2026 data in the kaggle dataset (Race 4 onwards) is supplemented via direct Jopica API calls
- Top aggregate gains/loss from qualifying positions is presented in a graph
