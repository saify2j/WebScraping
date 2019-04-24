<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
	<title>Test Page</title>
	<link rel="stylesheet" type="text/css" href="demo.css">
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div id="content">
		<div id="banner">Easy PC Buy
			<div id="user_info">
				
			</div>
		</div>
		<?php 
			if(isset($_SESSION['type']))
			{
				if($_SESSION['type'] == "admin")
				{
					include('menu_admin.php');

				}
				else
				{
					include('menu.php');
				}
			}
			else
			{
				include('menu.php');
			}
		?>