
<?php
$N = 10;

function Main($argc, $argv){
    global $N;
    $i;$j;$t;
    $a =  array();
    $p;
    
    $p = $argv[1];
    
    $i=0;
    foreach($_POST as $t){
        if ($i == $N-1)
            break;
        $a[i] = t;
        $i++;    
    }    
    $a[$i]=0;
    for($i=0;$a[i]!=0;$i++){
        for($j=0;$p[$j]!=0;$j++){
            if($a[$i+$j] != $p[$j])
                break;
            if($p[$j]==0)
                echo "$i<br>";

        }
    }
}

Main(10,[10,2])

?>





