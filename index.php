<?php

$current = file_get_contents("/var/www/html/current");
$cstring = substr($current, 0, 5);
$cost = substr((strval(floatval($current)*0.12157*1.2)), 0, 5);

$lastday = file_get_contents("/var/www/html/lastday");
$ldstring = substr($lastday, 0, 5);
$ldcost = substr((strval(floatval($lastday)*0.12157*1.2)), 0, 5);

?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Power Meter</title>
      <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
      
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container theme-showcase" role="main">
        <div class="jumbotron">
            <p>Current usage:</p>
            <h1><?php echo($cstring); ?>kW</h1>
            <p>That costs £<?php echo($cost); ?> per hour.</p>
        </div>
        
        <div class="page-header">
            <h1>Last 24h:</h1>
        </div>
        <p>
            <img class="img-responsive" src="https://plot.ly/~benstobbs/2.png" />
        </p>
        <p><?php echo($ldstring); ?>kWh = £<?php echo($ldcost); ?> was used in the last 24 hours.</p>
        
    </div>
      
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
    
    <script src="https://www.amcharts.com/lib/3/amcharts.js"></script>
    <script src="https://www.amcharts.com/lib/3/serial.js"></script>
    <script src="https://www.amcharts.com/lib/3/plugins/export/export.min.js"></script>
    <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
    <script src="https://www.amcharts.com/lib/3/themes/light.js"></script>
</html>
