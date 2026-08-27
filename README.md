# AI Opportunity Scout

対象分野を入力すると、Gemini APIを使って画期的な産業AI活用モデル・新規事業機会を構造化して提案するStreamlitアプリ。

## ローカル実行

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloudへのデプロイ

1. このリポジトリをGitHubにpushする。
2. https://share.streamlit.io にアクセスし、GitHubアカウントでサインインする。
3. 「Create app」→ このリポジトリ・ブランチ・`app.py` を選択してデプロイする。
4. (任意) 「Settings → Secrets」で `GEMINI_API_KEY` を設定すると、サイドバーのAPIキー欄が事前入力される。設定しなくても、利用者が各自のGemini APIキーをその場で入力すれば動作する。

デプロイ後に発行されるURLを共有すれば、他の人もブラウザからアプリを利用できる。
