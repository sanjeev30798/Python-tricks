import pywhatkit as kit

#text to handwriting tool using python
kit.text_to_handwriting("Sanjeev\n UG in CSE from IIITG.\n This is made using python pywhatkit package","E:\python\program1.png")

#using python for web search

kit.search("pywhatkit library")

#send message using whatsaap
kit.sendwhatmsg("+918434781781","Sent using python",10,17)

"""Sending mail using kit
for sending you need to switch on less secure app in security tab in Gmail settings.
Then only you will be able to send the messages """

kit.sendMail("kumarsanjeev30798@gmail.com","sanjeev@metro032", "sanjeev.k@iiitg.ac.in", "Sent via kit. This is just a test mail")
