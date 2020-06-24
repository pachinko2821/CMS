<?php

include '../includes/php/connect.php';
session_start();
$username = $_SESSION['user'];

if(!isset($_COOKIE[$username])){
    header("Location: admin-login.php");
}
?>
    

<?php 
//function to delete a dir with all its contents
function delete_directory($dirname) {
    if (is_dir($dirname))
      $dir_handle = opendir($dirname);
if (!$dir_handle)
     return false;
while($file = readdir($dir_handle)) {
      if ($file != "." && $file != "..") {
           if (!is_dir($dirname."/".$file))
                unlink($dirname."/".$file);
           else
                delete_directory($dirname.'/'.$file);
      }
}
closedir($dir_handle);
rmdir($dirname);
return true;
}

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
    delete_directory("../includes/posts/images/".$title);
    header("Location: dashboard.php");
}
elseif($decision == 'approve'){
    //insert file data into approvedPosts table, remove it from the postDetails table, and move the file to blog/posts if approved
    $get_data = $db->prepare("SELECT * FROM postDetails WHERE Title=?;");
    $get_data->bindValue(1, $title);
    $result = $get_data->execute();
    
    $row = $result->fetchArray();

    $put_data = $db->prepare("INSERT INTO approvedPosts(Date, Author, Title, small_content) VALUES(?,?,?,?);");
    $put_data->bindValue(1,$row['Date']);
    $put_data->bindValue(2,$row['Author']);
    $put_data->bindValue(3,$row['Title']);
    $put_data->bindValue(4,$row['small_content']);
    $put_data->execute();
    
    rename($row['Profanity']."-posts/".$title.".html", "../blog/posts/$title.html"); //move approved file to blog posts
     
    $delete_data = $db->prepare("DELETE FROM postDetails WHERE Title=?;");
    $delete_data->bindValue(1, $title);
    $delete_data->execute();
    header("Location: dashboard.php");
}
?>