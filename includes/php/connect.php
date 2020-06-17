<?php
    $db = new SQLite3('/home/pachinko/github/CMS/includes/php/CMS.db');

    if(!$db){
        echo $db->lastErrorCode();
    }
?>