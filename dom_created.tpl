<!DOCTYPE html>
<html>
<head>
Автоматическое тестирование верстки веб-сайтов
</head>
<body>
<p>DOM-дерево успешно построено. Выберите тип теста:</p>
<p>{{xpath}}</p>
<p>Введите url сайта, верстку которого нужно проверить</p>
<form method="POST" action="/dom_created">
    <input name="submit" type="submit" value="Элементы вне зоны видимости">
</form>


%end
</body>
</html>
