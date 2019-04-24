<?php
					if(isset($_SESSION['name']))
					{
						echo "Welcome " . $_SESSION['name'];
						echo " | ";
						echo "<a href='logout.php'>Logout</a>";
					}
					else
					{
						echo "<a href='login.php'>Login</a>";
					}
				?>
				
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