# Clicker 

___
<span id="0"></span>

### <span id="1">1. </span><span style="color:purple">Описание</span>

Сервис занимается посещением некого не называемого интернет ресурса и выполняет рутинные задачи, на которые нет
возможности подключать людей так как есть более важные дела да и собирать людей сложно. А потребность посещать 
данный ресурс есть и она является обязательной. 
 - Заложены случайности

### <span id="2">2. </span><span style="color:purple">Служебные команды для запуска</span> 

Монтировать образ
```bash
docker build -t ii_clicker_lb .
```
Запуск приложения в docker контейнере
```bash
docker run --rm --name ii_clicker_lb  vivera83/ii_labor_protect:1
```

```bash
docker build -t vivera83/ii_labor_protect:1 .
```


```bash
docker push vivera83/ii_labor_protect:1
```  
