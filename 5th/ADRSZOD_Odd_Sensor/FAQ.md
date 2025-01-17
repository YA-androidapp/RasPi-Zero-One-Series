# よくある質問

## Q: 基板上のGroveコネクタに別のセンサを接続したい

### A: GROVEコネクタはアナログ入力専用となります。
デジタルGPIO端子・I2Cなどの汎用バスにつきましてはご用意がございませんのでご了承下さい。 

----

## Q: サンプルプログラムの4つの値は何を意味していますか？

### A: ch1の値がにおいセンサからの出力値になります。
煙やアルコールに反応するのでご確認くださいませ。

### ch2,3はGROVEコネクタから入力できるアナログ値です。

### ch4は平衡（差動）入力値です。
他chはGNDレベルを基準とした値ですが、基準となる値も基板上の4chから入力することができます。  

#### 詳細は回路図をご確認ください。  

----

## Q: 搭載しているにおいセンサについて教えてください。

### A: TP-401Tを搭載しております。

データシートはこちらにございます。 https://btoshop.jp/products/b01821?_pos=3&_sid=437decf23&_ss=r  

----

## Q: どのようなにおいに反応しますか？

### A: 広域のにおいに反応します。
室内空気環境に異変があるか無いかに反応する広域センサのため、  
多くのにおいに反応すると思われます。  
(特定の物質のみに反応するセンサではございません。)   
詳しくはセンサ開発元データシートをご覧ください。  

----
