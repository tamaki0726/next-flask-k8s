# app/usecase/content_usecase.py
from flask import jsonify
from app.port.content_openai_repository import ContentOpenAiRepository
from app.domain.content import Content
import pandas as pd
import json

class UploadUseCase:
    def __init__(self, content_repository: ContentOpenAiRepository):
        self.content_repository = content_repository
        
    def upload_file(self, file):
        try:
            df = pd.read_excel(file)
            prompt = create_prompt(df)
            response = self.content_repository.extract(prompt)
            return {'data': response}
        except Exception as e:
            return {'error': str(e)}
        
def create_prompt(df):
    # DataFrameの内容を文字列に変換（ChatGPT APIに渡す用）
    document_entries = []
    for _, row in df.iterrows():
        document_entries.append(", ".join([f"{col}: {row[col]}" for col in df.columns]))

    # prompt = f"以下の表形式のデータに基づいて、どのような種類のドキュメントか推定してください。ただ回答は特殊文字を使わず、単純な文字列のみ使用してください。:\n\n" + "\n".join(document_entries)
    prompt = f"以下の表形式のデータから下記のファイルからコンテンツ名、ユーザー名、作成日（本日の日付）、部品名、価格、数量を抽出してください。アウトプット形式は下記の通りとし、取得できない項目があれば、値を空としてください。補足や説明は不要なため、アウトプット形式は例として添付したsonの型に必ずあわせてください。 {{contentsName: 'コンテンツA',userName: 'テスト太郎',createdAt: '2024-10-19',details: [{{ detailName: '部品1', amount: 2000, count: 2 }},{{ detailName: '部品2', amount: 3000, count: 1 }}]}},:\n\n" + "\n".join(document_entries)
    return prompt