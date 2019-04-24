<?php
include('connect.php');
include('banner.php');
//include('menu.php');
?>
<div id="main_content">
		<div id="body_content"><?php
/*echo "First Name:" . $_REQUEST["firstName"] . "<br>";
echo "Last Name:" . $_REQUEST["lastName"] . "<br>" ;
echo "Age:" . $_REQUEST["age"] ;
*/
$q ="INSERT INTO contact (name,email,subject,message)
VALUES ('". $_REQUEST["name"] ."', '". $_REQUEST["email"] ."', '". $_REQUEST["subject"] ."', '". $_REQUEST["message"] ."')";

//echo $q;

$mq = mysqli_query($cn,$q);
if ( !$mq)
{
	echo "Could not inserted data".mysql_error();
}
else
{
	echo "data inserted successfuly";
}
mysqli_close($cn);

?>
</div>
		<?php include('advert.php'); ?>
</div>
<?php
include('footer.php');
?>
