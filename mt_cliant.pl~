#!/usr/bin/perl 
#Usage 

use Encode;
use XMLRPC::Lite;
use utf8;
binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
binmode STDERR, ":utf8";

$url = "http://ahcclust02:10000/RPC2";
$proxy = XMLRPC::Lite->proxy($url);

my $text;

while($text = <STDIN>) {

    # Work-around for XMLRPC::Lite bug
    # $encoded = SOAP::Data->type(string => Encode::encode("utf8",$text));
    $encoded = SOAP::Data->type(string => $text);
    
    my %param = ("text" => $encoded );
    $result = $proxy->call("translate",\%param)->result;
    print $result->{'text'} . "\n";

}

