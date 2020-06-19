<?php

include '../includes/php/connect.php';
session_start();

if(!isset($_COOKIE)){
    header("Location: admin-login.php");
}
?>
    

<?php 

//get the file location
$file = $_GET['file'];
$decision = $_POST['decision'];

//extract file title
$explode1 = explode('/', $file);
$explode2 = explode(".", $explode1[1]); 
$title = $explode2[0];  

if($decision == 'disapprove'){
    //delete the file and its entry from the db if disapproved
    $statement = $db->prepare("DELETE FROM postDetails WHERE Title=?;");
    $statement->bindValue(1, $title);
    $result = $statement->execute();
    unlink($file);
    header("Location: dashboard.php");
}
elseif($decision == 'approve'){
    //insert file data into approvedPosts table, remove it from the postDetails table, and move the file to blog/posts if approved
    $statement = $db->prepare("SELECT * FROM postDetails WHERE Title=?;");
    $statement->bindValue(1, $title);
    $result = $statement->execute();
    
    $statement = $db->prepare("INSERT INTO approvedPosts(Date, Author, Title, small_content) VALUES(?,?,?,?);");
    $statement->bindValue(1,$row['Date']);
    $statement->bindValue(2,$row['Author']);
    $statement->bindValue(3,$row['Title']);
    $statement->bindValue(4,$row['small_content']);
    $statement->execute();
    
    rename($file, "../blog/posts/$title.html"); //move approved file to blog posts
     
    $statement = $db->prepare("DELETE FROM postDetails WHERE Title=?;");
    $statement->bindValue(1, $title);
    $statement->execute();
    header("Location: dashboard.php");
}
?>