#!/usr/bin/perl

use strict; #エラー検知

my $filename = $ARGV[0];
open(IN, $filename) || die "$filename: $!";
my $pattern = $ARGV[1];
while(<IN>){
 
      s/([a-zA-Z]+)$pattern/\<wall\/\> $1/g;			
      s/\_[a-zA-Z]+//g;
      s/\_.//g;
      print;
    
  }


close(IN);



