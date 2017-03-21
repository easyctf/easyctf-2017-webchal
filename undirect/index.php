<?php

$target = isset($_GET['target']) ? $_GET['target'] : '/';

header('Source: /source.php');
header('Location: ' . $target);

?>