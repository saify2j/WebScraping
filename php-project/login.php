<?php
//session_start();

include('connect.php');
include('banner.php');
//include('menu.php');
$msg = '';

if(isset($_REQUEST["userName"]) && isset($_REQUEST["password"]))
{
	$q ="SELECT * from user where UserName='" . $_REQUEST["userName"] . "' and Password='" . $_REQUEST["password"]. "'";
	$mq = mysqli_query($cn,$q);
	if(mysqli_num_rows($mq) > 0)
	{
		$row = mysqli_fetch_array($mq);
		$_SESSION['name'] = $_REQUEST["userName"];
		$_SESSION['type'] = $row['type'];
		header("Location: home.php");
	}
	else
	{
		$msg = "Invalid Username or password";
	}
}
?>
<div id="main_content">
		<div id="body_content"><form action="" method="post">
		 <br />
 <br />
<br />
		<table>
			<tr>
				<td>User Name:</td>
				<td><input type="text" name="userName" /></td>
			</tr>
			<tr>
				<td>Password:</td>
				<td><input type="password" name="password" /></td>
			</tr>
			
			<tr>
				<td></td>
				<td><input type="submit" value="Log in" /></td>
			</tr>
			<tr>
				<td></td>
				<td><?php if($msg!="") echo $msg; ?></td>
			</tr>
		</table>


</form></div>
		<?php include('advert.php'); ?>
</div>
<?php
include('footer.php');
?>
