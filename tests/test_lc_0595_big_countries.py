import pandas as pd
from src.pandas_solutions.lc_0595_big_countries import big_countries


def test_big_countries():
    # 가짜 world 데이터 (LeetCode 예시 비슷하게 구성)
    data = {
        "name": ["Afghanistan", "Albania", "Algeria", "Andorra"],
        "continent": ["Asia", "Europe", "Africa", "Europe"],
        "area": [652230, 28748, 2381741, 468],
        "population": [25500100, 2831741, 37100000, 78115],
        "gdp": [20343000000, 12960000000, 188681000000, 3712000000],
    }
    world = pd.DataFrame(data)

    # 함수 실행
    result = big_countries(world)

    # 조건을 만족하는 국가는 Afghanistan, Algeria
    expected = pd.DataFrame(
        {
            "name": ["Afghanistan", "Algeria"],
            "population": [25500100, 37100000],
            "area": [652230, 2381741],
        }
    )

    # DataFrame 비교 (순서 상관없이)
    assert set(map(tuple, result.to_records(index=False))) == set(
        map(tuple, expected.to_records(index=False))
    )