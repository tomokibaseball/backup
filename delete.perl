#!/usr/bin/perl 
  
my $file = "/home/is/tomoki-f/sim/confirm.txt";
open(IN, $file) or die "Can't open $file: $!\n";
while(<IN>){
   s/\|.*?\|//g; 
   print;
  }
close(IN);

   

