=======
Doctest
=======

:doctest: 

Dieses Modul stellt verschiedene Funktion zum Validieren von StandardFeldern bereit:


Test für validateZahl
---------------------

   >>> from uvc.validation.validation import validateZahl
   >>> validateZahl("0")
   True
   
   >>> validateZahl("0123456789")
   True

   >>> validateZahl("abc")
   Traceback (most recent call last):
   ...
   NotValidEingabeZahl: abc

   >>> validateZahl("ABC")
   Traceback (most recent call last):
   ...
   NotValidEingabeZahl: ABC

   >>> validateZahl("a1b")
   Traceback (most recent call last):
   ...
   NotValidEingabeZahl: a1b



Test für validateMail
---------------------

   >>> from uvc.validation.validation import validateMail
   >>> validateMail("test@adresse.de")
   True

   >>> validateMail("eins_test@adresse.de")
   True

   >>> validateMail("eins_test@addresse.d.de")
   True

   >>> validateMail("test.t-o@uv-c.de")
   True

   >>> validateMail("te123st@bla123.de")
   True

   >>> validateMail("te123st@bla_123.de")
   True

   >>> validateMail("te&amp;st@uvc.de1")
   Traceback (most recent call last):
   ...
   NotValidEingabeMail: te&amp;st@uvc.de1

   >>> validateMail(".test@uvc#.co.uk")
   Traceback (most recent call last):
   ...
   NotValidEingabeMail: .test@uvc#.co.uk

   >>> validateMail('fdjkasfjkasdfjaksfjdkasfjdkfjdkfjdaskfjdaskfjdaskfj')
   Traceback (most recent call last):
   ...
   NotValidEingabeMail: fdjkasfjkasdfjaksfjdkasfjdkfjdkfjdaskfjdaskfjdaskfj

Test validatePhone
------------------

   >>> from uvc.validation.validation import validatePhone
   >>> validatePhone("0815/1337")
   True

   >>> validatePhone("0815-1337")
   True

   >>> validatePhone("0815 1337")
   True

   >>> validatePhone("08151337")
   True

   >>> validatePhone("(+49) 0815/1337")
   True

   >>> validatePhone("0815.1337")
   True

   >>> validatePhone("0815-CALL-ME")
   True



Test validateFax
----------------

   >>> from uvc.validation.validation import validateFax
   >>> validateFax("0815/1337")
   True

   >>> validateFax("0815-1337")
   True

   >>> validateFax("0815 1337")
   True

   >>> validateFax("08151337")
   True

   >>> validateFax("(+49) 0815/1337")
   True

   >>> validateFax("0815.1337")
   True

   >>> validateFax("0815-CALL-ME")
   True
 


Test für validatePLZ
--------------------

   >>> from uvc.validation.validation import validatePLZ
   >>> validatePLZ("01234")
   True

   >>> validatePLZ("1")
   Traceback (most recent call last):
   ...
   NotValidEingabePLZ: 1

   >>> validatePLZ("99999")
   True

   >>> validatePLZ("ABC12")
   Traceback (most recent call last):
   ...
   NotValidEingabePLZ: ABC12

   >>> validatePLZ("53819")
   True

Wertebereich fuer PLZ's ungueltig
   >>> validatePLZ("00999")
   Traceback (most recent call last):
   ...
   NotValidEingabePLZ: 00999

Wertebreich fuer PLZ's gueltig
   >>> validatePLZ("01000")
   True


Test für validateKontoNr
------------------------

   >>> from uvc.validation.validation import validateKontoNr
   >>> validateKontoNr("1234567")
   True

   >>> validateKontoNr("123 456 789")
   Traceback (most recent call last):
   ...
   NotValidEingabeKontoNr: 123 456 789

   >>> validateKontoNr("1234abc")
   Traceback (most recent call last):
   ...
   NotValidEingabeKontoNr: 1234abc

   >>> validateKontoNr("abc1234ABC")
   Traceback (most recent call last):
   ...
   NotValidEingabeKontoNr: abc1234ABC


Test für validateBLZ
--------------------

   >>> from uvc.validation.validation import validateBLZ
   >>> validateBLZ("12345678")
   True

   >>> validateBLZ("40099999")
   True

   >>> validateBLZ("822457833")
   True

   >>> validateBLZ("01234567")
   Traceback (most recent call last):
   ...
   NotValidEingabeBLZ: 01234567


Test für validateDatum
----------------------

   >>> from uvc.validation.validation import validateDatum
   >>> validateDatum("01.01.2000")
   True

   >>> validateDatum("88.88.8888")
   Traceback (most recent call last):
   ...
   NotValidEingabeDatum: 88.88.8888

   >>> validateDatum("01.40.2010")
   Traceback (most recent call last):
   ...
   NotValidEingabeDatum: 01.40.2010

   >>> validateDatum("ab.cd.efgh")
   Traceback (most recent call last):
   ...
   NotValidEingabeDatum: ab.cd.efgh


Test für validateIBAN
---------------------

  >>> from uvc.validation.validation import validateIBAN
  >>> IBAN  = 'DE08700901001234567890'
  >>> IBAN_LEER  = 'DE08 7009 0100 1234 5678 90'
  >>> IBAN_KLEIN = 'de08700901001234567890'
  >>> IBAN_KLEIN_LEER  = 'de08 7009 0100 1234 5678 90'
  >>> IBAN_FALSCH = 'DE63700901001234567890'
  >>> IBAN_FALSCH_LEER  = 'DE63 7009 0100 1234 5678 90'

  >>> validateIBAN(IBAN)
  True

  >>> validateIBAN(IBAN_LEER)
  True

  >>> validateIBAN(IBAN_KLEIN)
  True

  >>> validateIBAN(IBAN_KLEIN_LEER)
  True

  >>> validateIBAN(IBAN_FALSCH)
  Traceback (most recent call last):
  ...
  NotValidEingabeIBAN: DE63700901001234567890
  
  >>> validateIBAN(IBAN_FALSCH_LEER)
  Traceback (most recent call last):
  ...
  NotValidEingabeIBAN: DE63 7009 0100 1234 5678 90


Test für validateBIC
--------------------

  >>> from uvc.validation.validation import validateBIC
  >>> validateBIC('GENODEF1JEV')
  True

  >>> validateBIC('MARKDEFFXXX')
  True

  >>> validateBIC('UBSWCHZH80A')
  True

  >>> validateBIC('UBSWCHZH')
  True

  >>> validateBIC('MARKDEFFXX')
  Traceback (most recent call last):
  ...
  NotValidEingabeBIC: MARKDEFFXX

  >>> validateBIC('GENODEF1')
  True

  >>> validateBIC('UBSWCH0H')
  Traceback (most recent call last):
  ...
  NotValidEingabeBIC: UBSWCH0H

  >>> validateBIC('RZTIAT02263')
  Traceback (most recent call last):
  ...
  NotValidEingabeBIC: RZTIAT02263

  >>> validateBIC('RZTIAT12263')
  Traceback (most recent call last):
  ...
  NotValidEingabeBIC: RZTIAT12263
