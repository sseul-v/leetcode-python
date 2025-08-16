import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    LeetCode 595. Big Countries (Pandas)

    조건:
      - area >= 3000000 또는 population >= 25000000
    반환 컬럼:
      - ["name", "population", "area"]
    """
    mask = (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)
    return world.loc[mask, ["name", "population", "area"]]