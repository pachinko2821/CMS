<?php
    $db = new SQLite3('CMS.db');

    if(!$db){
        echo $db->lastErrorCode();
    } 
?>