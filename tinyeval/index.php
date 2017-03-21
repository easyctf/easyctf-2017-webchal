<p>Give me something to eval!</p>

<?php
if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];
    if (strlen($cmd) > 11) {
        echo "sorry, your string is too long :(";
    } else {
        echo eval($cmd . ";");
    }
}
?>

<form method=post>
<input type=text name=cmd>
<input type=submit>
</form>