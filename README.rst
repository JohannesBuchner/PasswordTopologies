Commonly used password topologies
===================================

Some patterns of passwords are extremely common,
for example Denver14 follows the pattern Ullllldd
where

* u=uppercase
* l=lowercase
* d=digit
* s=special (other character)

Risk
-----

* Password crackers can search the most common patterns systematically (and do already).
* Users who use these common patterns are thus at risk.

Therefore, to increase security of your system you should not allow
users to choose passwords following these patterns!

This project identifies the most common password topologies.

See the `Report <report.rst>`_

Actions
---------
* Additional to the other OWASP recommendations (see below).
* When users set their passwords, check if that password is in a common topology.
* Encourage users to set pass-phrases, not passwords, and allow long passwords.

References
--------------- 

* `Pathwell Topologies <https://blog.korelogic.com/blog/2014/04/04/pathwell_topologies>`_
* `OWASP Security Guidelines <https://www.owasp.org/index.php/Authentication_Cheat_Sheet#Authentication_General_Guidelines>`_


