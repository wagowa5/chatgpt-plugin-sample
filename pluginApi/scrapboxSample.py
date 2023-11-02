import json
import requests

def lambda_handler(event, context):
    # パスパラメータを取得
    pagename = event['pathParameters']['pagename']
    
    # ScrapBoxのページ内容を取得
    # TODO projectnameを自分のプロジェクト名に変更
    response = requests.get(f"https://scrapbox.io/api/pages/projectname/{pagename}")
    
    if response.status_code == 200:
        data = response.json()
    else:
        data = {"error": "Page not found or failed to retrieve."}

    # TODO gpt用にレスポンスは調整する
    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json'
        },
    }
