from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(data):
    # 데이터 분리 및 모델 학습
    X = data['title']
    y = data['date']  # 예시로 분류 작업을 날짜로
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 학습된 모델 저장
    joblib.dump(model, 'models/model.pkl')
    return model
