<?php
session_start();
unset($_SESSION['name']);
unset($_SESSION['type']);
session_destroy();
header("Location: home.php");
?>

