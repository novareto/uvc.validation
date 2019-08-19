# -*- coding: utf-8 -*-
# jaskolka.dominik@bgetem.de
# andreas.stehr@bg-verkehr.de

import re
import time

from zope.schema import ValidationError



### ValidationError Klasse für Zahlen mit zugehöriger validier Methode
class NotValidEingabeZahl(ValidationError):
    u""" Ihre eingegebene Zahl entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
         Dem Format entsprechen alle Ziffern von 0 bis 9
    """


def validateZahl(value):
    """ validateZahl validiert eine Eingabe auf Zahlen
        default ist der zu prüfende Zahlenraum unbegrenz (laenge = None).
        Eine Begrenzung des Zahlenraums kann mittels des Parameters laenge
        gesetzte werden.
    """
    if value:
        checkzahl = re.compile(r'^[0-9]+$').match
        if not bool(checkzahl(value)):
            raise NotValidEingabeZahl(value)
    return True


### ValidationError Klase für E-Mail-Adressen mit zugehöriger validation Methode
class NotValidEingabeMail(ValidationError):
    u""" Ihre eingegebene E-Mail-Adresse entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe
    """


def validateMail(value):
    """ Der nachfolge RegEx Ausduck validiert die E-Mail wie folgt:
        True:    te_st@uvc.d.de | test.t-o@uv-c.de | t1est@123.de
        False:   te&amp;st@uvc.de1 | .test@uvc#.co.uk
    """
    if value:
        checkmail = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$").match
        if not bool(checkmail(value)):
            raise NotValidEingabeMail(value)
    return True


### ValidationError Klasse für Telefonnummern mit zugehöriger validation Methode
class NotValidEingabePhone(ValidationError):
    u""" Ihre eingegebene Telefonnummer entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validatePhone(value):
    """ Der nachfolge RegEx Ausdruck validiert die Telefonnummer wie folgt:
        True:   0815/1337 | 0815-1337 | 0815 1337 | 08151337 | (+49) 0815/1337
                0815.1337 | 0815-CALL-ME (Amerikanische Variante)
        False: Wenn die Eingabe kein string ist.
    """
    if value:
        checkphone = re.compile(r'((^\(\+?\d+[\ ]*\d*\)|^\(\d+\)|^\+?\d+|^\d+)+([\-\/\ ])*(\d)+)+([:blank:])*').match
        if not bool(checkphone(value)):
            raise NotValidEingabePhone(value)
    return True


### ValidationError Klasse für Fax mit zugehöriger validation Methode
class NotValidEingabeFax(ValidationError):
    u""" Ihre eingegebene Faxnummer entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validateFax(value):
    """ Der nachfolgende RegEx Ausdruck validert die Faxnummer wie folgt:
        True:   0815/1337 | 0815-1337 | 0815 1337 | 08151337 | (+49) 0815/1337
                0815.1337 | 0815-CALL-ME (Amerikanische Variante)
        False: Wenn die Eingabe kein string ist | " " leer String
    """
    if value:
        checkfax = re.compile(r'((^\(\+?\d+[\ ]*\d*\)|^\(\d+\)|^\+?\d+|^\d+)+([\-\/\ ])*(\d)+)').match
        if not bool(checkfax(value)):
            raise NotValidEingabeFax(value)
    return True


### ValidationError Kalsse für PLZ mit zugehöriger validiation Methode
class NotValidEingabePLZ(ValidationError):
    u""" Ihre eingegebene Postleitzahl entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validatePLZ(value):
    """ Der nachfolgende RegEx Ausdruck validiert die PLZ wie folgt:
        True: Alle Zahlen die 5 stellig sind und keinen Buchstaben haben im Gueltigkeitsbereich(von:01000 bis 99999) sind
        False: ABC12 | 1234a | 1
    """
    if value:
        checkplz = re.compile(r'^([0]{1}[1-9]{1}|[1-9]{1}[0-9]{1})[0-9]{3}$').match
        if not bool(checkplz(value)):
            raise NotValidEingabePLZ(value)
    return True


### ValidationError Klasse für KontoNummern mit zugehöriger validation Methode
class NotValidEingabeKontoNr(ValidationError):
    u""" Ihre eingegebene Kontonummer enspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe"""


def validateKontoNr(value):
    u""" Der nachfolgende RegEx Ausdruck validiert die KontoNr wie folgt:
         True: Alle Zahlenbereiche von 0 bis ~
         False: Buchstaben | abc1234 | 123 456 789
    """
    if value:
        checkkontonr = re.compile(r'^[0-9]+$').match
        if not bool(checkkontonr(value)):
            raise NotValidEingabeKontoNr(value)
    return True


### ValidationError Klasse für BLZ mit zugehöriger validation Methode
class NotValidEingabeBLZ(ValidationError):
    u""" Ihre eingegebene Bankleitzahl entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validateBLZ(value):
    u""" Der nachfolgende RegEx Ausdruck validiert die BLZ wie folgt:
         True: 87635123 | 45689123
         False: 012345678 | 0 | abc | 8216Test
    """
    if value:
        checkblz = re.compile(r'[1-8][0-9]{2}[0-9]{5}').match
        if not bool(checkblz(value)):
            raise NotValidEingabeBLZ(value)
    return True


### ValidationError Klasse für Datum mit zugehöriger validation Methode
class NotValidEingabeDatum(ValidationError):
    u""" Ihr eingegebenes Datum entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validateDatum(value):
    """ 
    Zuerst wird unterschieden, ob das Datum per Date oder per TextLine
    erstellt wurde. 
    Bei TextLine kommt es dann zu einer händischen Fehlerpruefung
    """
    if value:
        try:
            time.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise NotValidEingabeDatum(value)
        return True


### ValidationError Klase für Uhrzeit mit zugehöriger validation Methode
class NotValidEingabeUhrzeit(ValidationError):
    u""" Ihre eingegebene Uhrzeit entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validateUhrzeit(value):
    """ Der nachfolgende RegEx Ausdruck validiert die Uhrzeit wie folgt:
        True:   02:04 | 16:56 | 23:59
        False:  02:00 PM | PM2:00 | 24:00 | AB:CD | 89:12
    """
    if value:
        checkuhrzeit = re.compile(r'^([0-1][0-9]|[2][0-3]):([0-5][0-9])$').match
        if not bool(checkuhrzeit(value)):
            raise NotValidEingabeUhrzeit(value)
    return True


### ValidationError Klasse für BIC mit zugehöriger validation Methode

class NotValidEingabeBIC(ValidationError):
    u""" Ihre eingegebene BIC entspricht nicht dem geforderten Format.
         Bitte überprüfen Sie ihre Eingabe. 
    """

def validateBIC(value):
    """ Der nachfolgende RegEx Ausdruck validiert die BIC wie folgt:
        True: GENODEF1JEV, MARKDEFFXXX, UBSWCHZH80A, UBSWCHZH
        False: MARKDEFFXX, GENODEF1, UBSWCHZH80
    """
    checkbic = re.compile(r'^([a-zA-Z]{4}[a-zA-Z]{2}[A-Z2-9][A-Z0-9]([A-Za-z0-9]{3})?)$').match
    if not bool(checkbic(value)):
        raise NotValidEingabeBIC(value)
    return True


### ValidationError Klasse für IBAN mit zugehöriger validation Methode

class NotValidEingabeIBAN(ValidationError):
    u""" Ihre eingegebene IBAN entspricht nicht dem geforderten Format
         oder ist nicht korrekt. Bitte überprüfen Sie ihre Eingabe.
    """

def validateIBAN(value):
    """ Der nachfolgende RegEx-Ausdruck validiert die IBAN (Deutschland) wie folgt:
        True: DE89370400440532013000, de89370400440532013000, DE89 3704 0044 0532 0130 00, de89 3704 0044 0532 0130 00
        False: DE89-3704-0044-0532-0130-00, de89-3704-0044-0532-0130-00, DE08370400440532013000, de08370400440532013000,
               DE08 3704 0044 0532 0130 00, de08 3704 0044 0532 0130 00
        Mit anschliessender Berechnung und Vergleich der Pruefziffer (Position 3 und 4 der IBAN).
    """
    lkz_dict = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', 'G': '16',
                'H': '17', 'I': '18', 'J': '19', 'K': '20', 'L': '21', 'M': '22', 'N': '23',
                'O': '24', 'P': '25', 'Q': '26', 'R': '27', 'S': '28', 'T': '29', 'U': '30',
                'V': '31', 'W': '32', 'X': '33', 'Y': '34', 'Z': '35'}

    # PATTERN_ALL =  '^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}$'    # Alle IBAN, aber ohne Leerzeichen!
    PATTERN_DE    =  '^DE\d{2}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{2}|DE\d{20}$'         # nur Deutschland, mit und ohne Leerzeichen, Grossbuchstaben

    iban_up = value.upper()
    checkiban = re.match(PATTERN_DE, iban_up)
    iban = iban_up.replace(' ', '')
    # ist das Format richtig?
    if not checkiban:
        raise NotValidEingabeIBAN(value)
    else:
        # Pruefziffer in der IBAN
        pruef_str = iban[2:4]
        # Berechnung der Pruefziffer
        wert_str = iban[4:] + lkz_dict[iban[0]] + lkz_dict[iban[1]] + '00'
        rechnung = 98 - (int(wert_str) % 97)
        if rechnung < 10:
            rechnung = '0' + str(rechnung)
        # Pruefziffern vergleichen
        if int(rechnung) != int(pruef_str):
            raise NotValidEingabeIBAN(value)
        else:
            return True

