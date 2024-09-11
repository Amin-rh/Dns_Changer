Well , pay attention to a few points :

1.Run Adminstrator
2.Follow the pattern (in static case)

when you open the program you will see 3 option :
1.static
2.Dhcp(dynamic host configuration protocol)
3.shecan

Static :
if you want to set dns manual choose this option (Enter 1)

you should know , Which network interface are you connected.
usually in windows it's 'Ethernet' or 'Wi-Fi'.
if you don't know, don't worry you can enter 'netsh interface show interface' in command prompt it will show you.

ATTENTION : you should enter your dns according to the pattern
(X,X,X,X,Y,Y,Y,Y) e.g --> 8.8.8.8,8.8.4.4
when you enter your dns like this pattern , it will set

DHCP :
if you want to reset pervious command, you should run this case of program.
like Static case you should know which netwrok interface are you connected.

Shecan :
it's already prepared, this dns is for Shecan.ir.
Some platforms banned iranian people , but they use this dns to use that platforms.