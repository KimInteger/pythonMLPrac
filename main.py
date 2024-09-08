from scraping.scraper import scrape_data
from preprocessing.preprocess import preprocess_data
from models.model_trainer import train_model

# 1. 웹 스크래핑 단계
print("Starting web scraping...")
scraped_data = scrape_data()

# 2. 데이터 전처리 단계
print("Preprocessing data...")
processed_data = preprocess_data(scraped_data)

# 3. 모델 학습 단계
print("Training model...")
model = train_model(processed_data)

# 4. 예측 or 분류 작업
print("Model training complete. Ready for predictions.")
