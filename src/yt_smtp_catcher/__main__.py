"""
メイン処理 通常使わない
"""
from yt_smtp_catcher import create_app

if __name__ == '__main__': # pragma: no cover
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)