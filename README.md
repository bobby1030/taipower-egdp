# taipower-egdp
民間版臺電各機組發電量開放資料 Unofficial Taipower Electricity Generation Data Parser

## 緣起
政府資料開放平臺上[有一份由臺電公開的資料集](http://data.gov.tw/node/8931)，其中包含了各機組發電量的即時資訊，但是原資料集的格式實在太髒，甚至不支援 CORS，不適合網頁、程式進一步利用，因此萌生了再處理這份資料的念頭。

## 目標
* 從臺電的原資料中，重新自幹出一份較友善的格式
* 在資源允許的情況下，host 一份持續更新的資料開放在網路上