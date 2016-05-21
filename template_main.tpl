<!DOCTYPE html>
<html>
<head>
<title>Test</title>
</head>
<script language="JavaScript">

function fulltime() {

	var time=new Date();

	document.clock.full.value=time.toLocaleString();

	setTimeout('fulltime()',500)

}
</script>
<body bgcolor=ffffff  text=ff0000>

<center>

<form name=clock>

<input type=text size=17 name=full>

</form>

<script language="JavaScript">

fulltime();

</script>

</center>
<p>Автоматическое тестирование верстки веб-сайтов</p>
<p>{{xpath}}</p>
<p>Введите url сайта, верстку которого нужно проверить</p>
<form method="POST" action="/dom_created">
    <input name="url" type="input" value="http://www.zoopicture.ru/">
    <input name="submit" type="submit" value="Начать">
</form>

<script language="JavaScript">
clock_form();
</script>
</body>
</html>
