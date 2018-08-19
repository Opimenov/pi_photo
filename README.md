# pi_photo
####Problem. 
How do we receive
a picture of a particular location via email every
24 hours to monitor objects condition? 
####Solution:

Raspberry pi with a camera, bullet M4 network module,
solar panel + rechargeable battery, voltage regulator,
power supply clock/timer.    
Plan is to use this very simple script (citpse.py)
with SystemD to check internet connection few times.
If internet connection is available, 
take a picture and send it 
to predefined email address. Easy!   
