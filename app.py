# app.py
# 実行: streamlit run app.py

import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="AI Opportunity Scout", layout="wide")

st.title("🚀 AI Opportunity Scout")
st.caption("対象分野を入力すると、画期的な産業AI活用モデル・新規事業機会を構造化して策定します")


def default_api_key() -> str:
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.getenv("GEMINI_API_KEY", "")


# 入力フォーム
with st.sidebar:
    st.header("設定")
    api_key = st.text_input("Gemini API Key", type="password", value=default_api_key())
    st.caption("APIキーは保存されず、このセッション内でのみ使用されます。")
    selected_focus = st.multiselect(
        "重視するブレークスルー軸",
        [
            "逆問題・未然防止(目標値からのパラメータ逆算)",
            "暗黙知・熟練者ノウハウの自律学習",
            "デジタルツイン × 高速シミュレーション",
            "物理・安全制約考慮型モデリング",
            "データフライホイール・競争優位(Moat)設計",
        ],
        default=[
            "逆問題・未然防止(目標値からのパラメータ逆算)",
            "暗黙知・熟練者ノウハウの自律学習",
        ],
    )

domain_input = st.text_area(
    "検討したい分野・業界・業務プロセスを入力してください",
    placeholder="例：半導体材料の結晶成長プロセス、木造建築の構造ヘルスモニタリング、中小製造業の金型設計と射出成形...",
)

if st.button("AI活用機会を分析・生成", type="primary"):
    if not api_key:
        st.error("Gemini API Keyを入力してください。")
    elif not domain_input.strip():
        st.warning("対象分野を入力してください。")
    else:
        system_instruction = (
            "あなたは産業DX・数理最適化・ディープテックに精通したAIアーキテクトです。"
            "一般的な定型自動化にとどまらず、逆問題、デジタルツイン、暗黙知の形式知化、"
            "制約考慮型最適化を軸にした画期的なAI活用・新規事業コンセプトを構造化して出力してください。"
        )

        prompt = f"""
対象分野: {domain_input}
特に重視する軸: {', '.join(selected_focus)}

以下の構成で具体的かつ論理的に分析してください。
1. 業界の構造的課題と従来の限界
2. 画期的なAI活用コンセプト案(Before/Afterと核となるメカニズム)
3. 想定技術アーキテクチャ(データ要件・モデル選定・安全制約)
4. ビジネスインパクトとROI
5. PoC(概念実証)の実行ステップ
"""
        try:
            with st.spinner("分析中..."):
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model="gemini-3.1-pro-preview",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.4,
                    ),
                )
                st.markdown(response.text)
        except Exception as e:
            st.error(f"分析中にエラーが発生しました。APIキーやネットワーク接続をご確認ください。\n\n詳細: {e}")
