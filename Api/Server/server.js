// Imports
var express = require ('express');

// Instantiate server
var server = express();

server.get('/',function(req,res){
    res.setHeader('Content-Type','text/html');
    res.status(200).send('<h1> Bonjour ma couille<h1>');

});


// Launch server
server.listen(8080, function(){
    console.log('Server en écoute :)');
})