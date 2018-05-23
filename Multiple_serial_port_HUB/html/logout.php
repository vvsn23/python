<?php

    
    session_start();
	session_destroy();
	

?>

<html>
<head>

<h3>Logged out scuccessfully</h3>
<title>Login Form</title>
</head>
<body>

<body  style="height:100px;background-color:; margin-top: 80px;margin-left: 500px; ">

<div id="rcorners3" style="width:480px;padding-left:155px;height:480px;background-color:skyblue" ><br><br><br>
<h2>Login TO HD-DVR ControlPannel</h2>
<div style="background-color:white;width:320px;height:300px;border:2px solid #B0C4DE;" >

<form name="login" method="post" style=" align:center;background-color:white;margin-top:100px;width:300px;padding-left:20px;height:26px;"   action="check.php">

<div  style="float:right;margin-right:0px;"><img style="margin-top:-100px;padding-left:-50px; z-index: -1" src="img.png" height="85px" width="320px;"  ></img></div>



UserName :<input type="text" name='uid'/><br><br>
Password :&nbsp&nbsp<input type="password" name="pw"/><br><br>
<input type="submit" value="Login">

</form>

</div>
</div>

</body>

</html>