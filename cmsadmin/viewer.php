<?php

include '../includes/php/connect.php';
session_start();

if(!isset($_COOKIE)){
    header("Location: admin-login.php");
}

$file = $_GET['file'];
echo file_get_contents($file);

?>

<form action="approval.php?file=<?php echo $file; ?>" method="POST">
    <input type="submit" value="approve" name="decision">
    <input type="submit" value="disapprove" name="decision">
</form>