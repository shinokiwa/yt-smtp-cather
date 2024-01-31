"""
メイン処理 通常使わない
"""
from yt_testing_smtpserver import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)