# YT SMTP Catcher

ローカル環境でのテスト時向けSMTPメールサーバーです。<br>
到達した全てのメールをローカルに保存します。<br>
また、特定のドメイン宛のメールを指定したサーバーに転送することもできます。

## 何に使うの？

- ローカル環境でメール送信のテストができます。
- 実際のインターネットにメールを飛ばすことなく、SMTPの結合試験を行うことができます。
- テスト対象のドメインを指定したサーバーに転送することで、ローカル環境でもメール受信のテストができます。


## ただのメモ

- たぶんaiosmtpdあたりでSMTPを受けるのが適切だと思うけど、現状個人的な事情でPostfixの動作も習熟しておきたいため、MTAにPostfixを使っている。
