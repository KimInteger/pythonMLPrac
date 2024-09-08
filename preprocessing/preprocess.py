import pandas as pd

def preprocess_data(data):
    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    # 날짜 정리, 공백 제거 등의 전처리 작업
    df['date'] = pd.to_datetime(df['date'])
    df['title'] = df['title'].str.strip()
    return df
