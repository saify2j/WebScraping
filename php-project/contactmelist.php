<?php
include('connect.php');
include('banner.php');
//include('menu.php');
?>
<div id="main_content">
		<div id="body_content"><?php

$q ="SELECT * from contact";
$mq = mysqli_query($cn,$q);


echo "<table border='1'><tr><th>Id</th><th>Name</th><th>Subject</th><th>Email</th><th>Message</th></tr>";

while($row = mysqli_fetch_array($mq))
{
	echo "<tr><td>";
	echo $row['ID'];
	echo "</td><td>";
	echo $row['name'];
	echo "</td><td>";
	echo $row['email'];
	echo "</td><td>";
	echo $row['subject'];
	echo "</td><td>";
	echo $row['message'];
	echo "</td>";
	
}

echo "</table>";

mysqli_close($cn);

?>
</div>
		<?php include('advert.php'); ?>
</div>
<?php
include('footer.php');
?>