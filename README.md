This little project allows you to automate tasks on your router.
It uses Selenium and the gecko web driver.

Background:
A few of my routers need to be rebooted periodically, otherwise they slow down. The obvious approach is to schedule them to reboot, BUT TP-LINK doesnt think that's something that normal users want so no such option is provided.

So the next thing would be to run a script somewhere that connects to the router and reboot the thing. But how exactly?

<img  width="61%" src="images/SomethingToWorkWith.png?raw=true" />

A quick portscan with the useful IP Scanner tool (http://10base-t.com/macintosh-software/ip-scanner/) revealed that SSH and TELNET are available

Let's try SSH:

<img  width="61%" src="images/SshIsNotForUs.png" />
Fail, they keep ssh around only for the Tether 2.0 App

Let's try telnet:

<img  width="61%" src="images/telnetOnC2.png" />
<img  width="61%" src="images/rebootByTelnetWorksOnC2.png" />
I'm in and it works. Yay!


<img  width="61%" src="images/noTelnetOnC7.png" />
But another of my routers doesn't have telnet running. Darn it!


A crude alternative would be a power switch with a timer, but come on, we're both on github for the sweet sweet code :D
Selenium to the rescue! I thought I just write some UI tests that log into the webinterface and click around and this is the solution I stuck with.

Right now I only support some of my problematic routers: TP-LINK Archer C2 and the Archer C7, latest firmware.


<img  width="61%" src="images/Reboot.gif" />
