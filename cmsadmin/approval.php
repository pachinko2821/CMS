<?php

include '../includes/php/connect.php';
session_start();
$username = $_SESSION['user'];
setcookie($username, "7355608");

if(empty($username)){
    header("Location: admin-login.php");
}
elseif(!isset($_COOKIE)){
    header("Location: admin-login.php");
}
?>
    

<?php 

$file = $_GET['file'];
echo file_get_contents($file);

$explode1 = explode('/', $file);
$explode2 = explode(".", $explode1[1]); 
$title = $explode2[0];  

$decision = $_POST['decision'];

?>

<form action="approval.php?file=<?php $file ?>" method="POST">
    <input type="submit" value="approve" name="decision">
    <input type="submit" value="disapprove" name="decision">
</form>

<?php

if($decision == 'disapprove'){
    $statement = $db->prepare("DELETE FROM postDetails WHERE Title=?;");
    $statement->bindValue(1, $title);
    $result = $statement->execute();
    unlink($file);
    header("Location: dashboard.php");
}
elseif($decision == 'approve'){
    $statement = $db->prepare("SELECT * FROM postDetails WHERE Title=?;");
    $statement->bindValue(1, $title);
    $result = $statement->execute();
    while($row = $result->fetchArray(SQLITE3_ASSOC)){
        echo "<script>alert(".$row['Title'].")</script>";
    }
}
?>