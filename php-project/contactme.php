<?php 
			if(isset($_SESSION['type']))
			{
				if($_SESSION['type'] == "admin")
				{
					include('contactmelist.php');
				}
				else
				{
					include('login.php');
				}
			}
			else
			{
				include('login.php');
			}
?>