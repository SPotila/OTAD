# importerar Tkinter, PIL och MySQL Connector
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PIL
import mysql.connector
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime,date
import os
import traceback

#funktioner


def clickButton():
     pass

def miljodeklaration():
     global maskinnummer

     cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + maskinnummer + ';')
     maskinInfo = cursor.fetchone()
     maskinInfo = list(maskinInfo)
     
     cursor.execute('SELECT Fornamn, Efternamn, Foretagsnamn, Gatuadress, Postnummer, Postadress FROM foretagsregister WHERE Medlemsnummer = ' + str(maskinInfo[4]) + ';')
     delagarInfoLista = cursor.fetchone()
     delagarInfoLista = list(delagarInfoLista)


     packet = io.BytesIO()
     c = canvas.Canvas(packet, pagesize=letter)

     for item in range(len(maskinInfo)):
          if maskinInfo[item] == None:
               maskinInfo[item] = ""
          else:
               pass

     #Översta delen
     c.drawString(130, 722, str(maskinInfo[4]))
     c.drawString(130, 702, str(delagarInfoLista[2]))
     c.drawString(130, 682, str(delagarInfoLista[0]))
     c.drawString(195, 682, str(delagarInfoLista[1]))
     c.drawString(130, 662, str(delagarInfoLista[3]))
     c.drawString(130, 642, str(delagarInfoLista[4]))
     c.drawString(190, 642, str(delagarInfoLista[5]))
     c.drawString(470, 722, str(maskinInfo[0]))
     c.drawString(458, 702, str(maskinInfo[1]))
     c.drawString(458, 682, str(maskinInfo[6]))
     c.drawString(458, 662, str(maskinInfo[26]))
     c.drawString(458, 642, str(maskinInfo[2]))
     c.drawString(458, 622, str(maskinInfo[27]))

     #Motor
     c.drawString(50, 540, str(maskinInfo[8]))
     c.drawString(160, 540, str(maskinInfo[9]))
     c.drawString(270, 540, str(maskinInfo[10]))

     #Eftermonterad avgasreninsutrustning
     c.drawString(50, 482, str(maskinInfo[14]))
     c.drawString(120, 482, str(maskinInfo[15]))
     c.drawString(195, 482, str(maskinInfo[12]))
     c.drawString(280, 482, str(maskinInfo[11]))


     #Bullernivå
     c.drawString(340, 482, str(maskinInfo[29]))
     c.drawString(430, 482, str(maskinInfo[31]))

     #Oljor och smörjmedel - Volym, liter
     c.drawString(50, 420, str(maskinInfo[16])) 
     c.drawString(205, 420, str(maskinInfo[17]))
     c.drawString(50, 390, str(maskinInfo[18]))
     c.drawString(205, 390, str(maskinInfo[19]))
     c.drawString(50, 360, str(maskinInfo[20]))
     c.drawString(205, 360, str(maskinInfo[21]))
     c.drawString(50, 325, str(maskinInfo[24]))

     #Miljöklassificering
     c.drawString(340, 420, str(maskinInfo[30]))
     c.drawString(345, 330, str(maskinInfo[22]))

     #Övrigt
     c.drawString(50, 244, str(maskinInfo[13]))
     c.drawString(125, 244, str(maskinInfo[37]))
     c.drawString(205, 244, str(maskinInfo[25]))
     c.drawString(375, 244, str(maskinInfo[35]))
     c.drawString(470, 244, str(maskinInfo[38]))
     c.drawString(50, 210, str(maskinInfo[33]))
     c.drawString(205, 210, str(maskinInfo[34]))
     c.drawString(375, 210, str(maskinInfo[36]))
     c.drawString(470, 210, str(maskinInfo[39]))

     #Bränsle
     c.drawString(50, 155, str(maskinInfo[23]))
     c.drawString(125, 155, str( maskinInfo[7]))

     #Försärking 
     c.drawString(50, 102, str(maskinInfo[3]))

     #Datum
     c.drawString(435, 56, str(datetime.date(datetime.now())))

     c.save()

     packet.seek(0)
     new_pdf = PdfFileReader(packet)

     existing_pdf = PdfFileReader(open("miljödeklaration.pdf", "rb"))
     output = PdfFileWriter()

     page = existing_pdf.getPage(0)
     page.mergePage(new_pdf.getPage(0))
     output.addPage(page)

     outputStream = open( "miljödeklaration - " + maskinnummer + ".pdf", "wb")
     output.write(outputStream)
     outputStream.close()
     os.startfile("miljödeklaration - " + maskinnummer + ".pdf" )

def maskinpresentation():     #behöver lägga till funktion för bilder
     global maskinnummer

     cursor.execute('SELECT Medlemsnummer, MarkeModell, Arsmodell, Registreringsnummer, ME_Klass, Maskintyp, Forarid FROM maskinregister WHERE Maskinnummer = ' + maskinnummer + ';')
     maskinInfo = cursor.fetchone()
     maskinInfo = list(maskinInfo)

     cursor.execute('SELECT Foretagsnamn FROM foretagsregister WHERE medlemsnummer = ' + str(maskinInfo[0]) + ';')
     foretag = cursor.fetchone()
     foretag = list(foretag)

     cursor.execute('SELECT tillbehor FROM tillbehor WHERE Maskinnummer = ' + maskinnummer + ';')
     tillbehor = cursor.fetchall()
     tillbehor = list(tillbehor)

     cursor.execute('select namn from forare where forarid ='+ str(maskinInfo[6])+';')
     forarnamn = cursor.fetchone()
     forarnamn = list(forarnamn)

     cursor.execute('SELECT Beskrivning FROM referens WHERE forarid = ' + str(maskinInfo[6]) + ';')
     referenser = cursor.fetchall()
     referenser = list(referenser)

     packet = io.BytesIO()
     c = canvas.Canvas(packet, pagesize=letter)
     rad1=""
     rad2=""
     rad3=""
     rad4=""
     rad5=""
     y=1

     c.drawImage("1.jpg", 72, 132, 450, 340)
     c.drawString(133, 710, str(maskinInfo[0])) 
     c.drawString(455, 690, str(maskinInfo[1]))
     c.drawString(455, 670, str(maskinInfo[2]))
     c.drawString(455, 650, str(maskinInfo[3]))
     c.drawString(455, 630, str(maskinInfo[4]))
     c.drawString(455, 610, str(maskinInfo[5]))
     c.drawString(133, 670, str(forarnamn[0]))
     c.drawString(133, 690, str(foretag[0]))
     c.drawString(467, 710, str(maskinnummer))
     for x in tillbehor:
          s = x[0]
          s+=", "
          if y>12:
               rad5+=s
          elif y>9:
               y+=1
               rad4+=s          
          elif y>6:
               y+=1
               rad3+=s
          elif y>3:
               y+=1
               rad2+=s
          else:
               y+=1
               rad1+=s         


     c.drawString(140, 558, str(rad1))
     c.drawString(140, 538, str(rad2))
     c.drawString(140, 518, str(rad3))
     c.drawString(140, 498, str(rad4))
     c.drawString(140, 478, str(rad5))
     c.drawString(152, 112, str(referenser[0][0]))
     c.drawString(152, 86, str(referenser[1][0]))

     c.save()

     packet.seek(0)
     new_pdf = PdfFileReader(packet)

     existing_pdf = PdfFileReader(open("maskinpresentation.pdf", "rb"))
     output = PdfFileWriter()

     page = existing_pdf.getPage(0)
     page.mergePage(new_pdf.getPage(0))
     output.addPage(page)
     #Fixa i framtiden så att man kan använda sig av custom paths (till servern) för att spara dokumenten på andra ställen.
     outputStream = open( "maskinpresentation - " + maskinnummer + ".pdf", "wb")
     output.write(outputStream)
     outputStream.close()
     #Öppnar dokumentet efter man skapat det. Måste ändra sökväg efter vi fixat servern.
     os.startfile("maskinpresentation - " + maskinnummer + ".pdf" )

def fyllMaskinInfo(self):
     global maskinnummer

     selectedMaskin = LbMaskiner.get(LbMaskiner.curselection())
     index2 = selectedMaskin.index(" ")
     stringSelectedMaskin = str(selectedMaskin[0:index2])
     maskinnummer = "".join(stringSelectedMaskin)
     cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + maskinnummer + ';')
     maskinInfo = cursor.fetchone()
     maskinInfo = list(maskinInfo)
     
     try:
          txtMaskinnummermaskininfo.config(state=NORMAL)
          txtMaskinnummermaskininfo.delete('1.0', 'end')
          txtMaskinnummermaskininfo.insert('end', maskinInfo[0])
          txtMaskinnummermaskininfo.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbeteckning.config(state=NORMAL)
          txtMaskinbeteckning.delete('1.0', 'end')
          txtMaskinbeteckning.insert('end', maskinInfo[1])
          txtMaskinbeteckning.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinme_klass.config(state=NORMAL)
          txtMaskinme_klass.delete('1.0', 'end')
          txtMaskinme_klass.insert('end', maskinInfo[2])
          txtMaskinme_klass.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinmotorfabrikat.config(state=NORMAL)
          txtMaskinmotorfabrikat.delete('1.0', 'end')
          txtMaskinmotorfabrikat.insert('end', maskinInfo[8])
          txtMaskinmotorfabrikat.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotortyp.config(state=NORMAL)
          txtMaskinmotortyp.delete('1.0', 'end')
          txtMaskinmotortyp.insert('end', maskinInfo[9])
          txtMaskinmotortyp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotor.config(state=NORMAL)
          txtMaskinmotor.delete('1.0', 'end')
          txtMaskinmotor.insert('end', maskinInfo[16])
          txtMaskinmotor.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinvaxellada.config(state=NORMAL)
          txtMaskinvaxellada.delete('1.0', 'end')
          txtMaskinvaxellada.insert('end', maskinInfo[18])
          txtMaskinvaxellada.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinhydraulsystem.config(state=NORMAL)
          txtMaskinhydraulsystem.delete('1.0', 'end')
          txtMaskinhydraulsystem.insert('end', maskinInfo[20])
          txtMaskinhydraulsystem.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinkylvatska.config(state=NORMAL)
          txtMaskinkylvatska.delete('1.0', 'end')
          txtMaskinkylvatska.insert('end', maskinInfo[33])
          txtMaskinkylvatska.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinmotoreffekt.config(state=NORMAL)
          txtMaskinmotoreffekt.delete('1.0', 'end')
          txtMaskinmotoreffekt.insert('end', maskinInfo[10])
          txtMaskinmotoreffekt.config(state=DISABLED)
     except:
          pass

     try:
          if maskinInfo[12] == 1:
               cbMaskinmotorvarmare.state(['selected'])
               cbMaskinmotorvarmare.state(['disabled'])
          else:
               cbMaskinmotorvarmare.state(['!selected'])
               cbMaskinmotorvarmare.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[14] == 1:
               cbMaskinkatalysator.state(['selected'])
               cbMaskinkatalysator.state(['disabled'])
          else:
               cbMaskinkatalysator.state(['!selected'])
               cbMaskinkatalysator.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[15] == 1:
               cbMaskinpartikelfilter.state(['selected'])
               cbMaskinpartikelfilter.state(['disabled'])
          else:
               cbMaskinpartikelfilter.state(['!selected'])
               cbMaskinpartikelfilter.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[11] == 1:
               cbMaskinvattenbaseradlack.state(['selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
          else:
               cbMaskinvattenbaseradlack.state(['!selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
     except:
          pass

     try:
          txtMaskinkylmedia.config(state=NORMAL)
          txtMaskinkylmedia.delete('1.0', 'end')
          txtMaskinkylmedia.insert('end', maskinInfo[13])
          txtMaskinkylmedia.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbullernivautv.config(state=NORMAL)
          txtMaskinbullernivautv.delete('1.0', 'end')
          txtMaskinbullernivautv.insert('end', maskinInfo[29])
          txtMaskinbullernivautv.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbullernivainv.config(state=NORMAL)
          txtMaskinbullernivainv.delete('1.0', 'end')
          txtMaskinbullernivainv.insert('end', maskinInfo[31])
          txtMaskinbullernivainv.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinsmorjfett.config(state=NORMAL)
          txtMaskinsmorjfett.delete('1.0', 'end')
          txtMaskinsmorjfett.insert('end', maskinInfo[24])
          txtMaskinsmorjfett.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinBatterityp.config(state=NORMAL)
          txtMaskinBatterityp.delete('1.0', 'end')
          txtMaskinBatterityp.insert('end', maskinInfo[38])
          txtMaskinBatterityp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinperiod.config(state=NORMAL)
          txtMaskinperiod.delete('1.0', 'end')
          txtMaskinperiod.insert('end', maskinInfo[7])
          txtMaskinperiod.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinarsbelopp.config(state=NORMAL)
          txtMaskinarsbelopp.delete('1.0', 'end')
          txtMaskinarsbelopp.insert('end', maskinInfo[5])
          txtMaskinarsbelopp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmiljostatus.config(state=NORMAL)
          txtMaskinmiljostatus.delete('1.0', 'end')
          txtMaskinmiljostatus.insert('end', maskinInfo[30])
          txtMaskinmiljostatus.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinarsmodell.config(state=NORMAL)
          txtMaskinarsmodell.delete('1.0', 'end')
          txtMaskinarsmodell.insert('end', maskinInfo[6])
          txtMaskinarsmodell.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinregistreringsnummer.config(state=NORMAL)
          txtMaskinregistreringsnummer.delete('1.0', 'end')
          txtMaskinregistreringsnummer.insert('end', maskinInfo[26])
          txtMaskinregistreringsnummer.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskintyp.config(state=NORMAL)
          txtMaskintyp.delete('1.0', 'end')
          txtMaskintyp.insert('end', maskinInfo[27])
          txtMaskintyp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotoroljevolym.config(state=NORMAL)
          txtMaskinmotoroljevolym.delete('1.0', 'end')
          txtMaskinmotoroljevolym.insert('end', maskinInfo[17])
          txtMaskinmotoroljevolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinvaxelladevolym.config(state=NORMAL)
          txtMaskinvaxelladevolym.delete('1.0', 'end')
          txtMaskinvaxelladevolym.insert('end', maskinInfo[19])
          txtMaskinvaxelladevolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinhydraulsystemvolym.config(state=NORMAL)
          txtMaskinhydraulsystemvolym.delete('1.0', 'end')
          txtMaskinhydraulsystemvolym.insert('end', maskinInfo[21])
          txtMaskinhydraulsystemvolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinkylvatskavolym.config(state=NORMAL)
          txtMaskinkylvatskavolym.delete('1.0', 'end')
          txtMaskinkylvatskavolym.insert('end', maskinInfo[32])
          txtMaskinkylvatskavolym.config(state=DISABLED)
     except:
          pass

     try:
          TxtOvrigtext.config(state=NORMAL)
          TxtOvrigtext.delete('1.0', 'end')
          TxtOvrigtext.insert('end', maskinInfo[41])
          TxtOvrigtext.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbransle.config(state=NORMAL)
          txtMaskinbransle.delete('1.0', 'end')
          txtMaskinbransle.insert('end', maskinInfo[23])
          txtMaskinbransle.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskindackfabrikat.config(state=NORMAL)
          txtMaskindackfabrikat.delete('1.0', 'end')
          txtMaskindackfabrikat.insert('end', maskinInfo[25])
          txtMaskindackfabrikat.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskindimension.config(state=NORMAL)
          txtMaskindimension.delete('1.0', 'end')
          txtMaskindimension.insert('end', maskinInfo[34])
          txtMaskindimension.config(state=DISABLED)
     except:
          pass

     try:
          if maskinInfo[37] == 1:
               cbMaskingasolanlaggning.state(['selected'])
               cbMaskingasolanlaggning.state(['disabled'])
          else:
               cbMaskingasolanlaggning.state(['!selected'])
               cbMaskingasolanlaggning.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[22] == 1:
               cbMaskinSaneringsvatska.state(['selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
          else:
               cbMaskinSaneringsvatska.state(['!selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
     except:
          pass

     forarnamn=""
     if maskinInfo[40] != None:
          cursor.execute('SELECT Namn FROM forare WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          forarnamn = cursor.fetchone()

     try:
          txtMaskinforare.config(state=NORMAL)
          txtMaskinforare.delete('1.0', 'end')
          txtMaskinforare.insert('end', forarnamn[0])
          txtMaskinforare.config(state=DISABLED)
     except:
          pass
     
     referenser = []     
     referenser.clear()
     if maskinInfo[40] != None:
          cursor.execute('SELECT Beskrivning FROM referens WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          referenser = cursor.fetchall()
          
     try:
          if lbMaskinreferens.index("end") != 0:
               lbMaskinreferens.delete(0, "end")
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
          else:
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
     except:
          pass

     try:
          if maskinInfo[28] == 1:
               cbMaskininsatserlagd.state(['selected'])
               cbMaskininsatserlagd.state(['disabled'])
          else:
               cbMaskininsatserlagd.state(['!selected'])
               cbMaskininsatserlagd.state(['disabled'])
     except:
          pass
     
     try:
          if maskinInfo[36] == 1:
               cbMaskinregummerade.state(['selected'])
               cbMaskinregummerade.state(['disabled'])
          else:
               cbMaskinregummerade.state(['!selected'])
               cbMaskinregummerade.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[35] == 1:
               cbMaskinregummerbara.state(['selected'])
               cbMaskinregummerbara.state(['disabled'])
          else:
               cbMaskinregummerbara.state(['!selected'])
               cbMaskinregummerbara.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[3] == 1:
               cbMaskinKollektivforsakring.state(['selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
          else:
               cbMaskinKollektivforsakring.state(['!selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
     except:
          pass
     
     cursor.execute('SELECT Tillbehor FROM tillbehor WHERE Maskinnummer = ' + maskinnummer + ';')
     tillbehor = cursor.fetchall()
     
     if lbMaskintillbehor.index("end") != 0:
          lbMaskintillbehor.delete(0, "end")
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     else:
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     
     cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
     maskiner = cursor.fetchall()

     if LbDelagaresMaskiner.index("end") != 0:
          LbDelagaresMaskiner.delete(0, "end")
          for x in maskiner:
               LbDelagaresMaskiner.insert("end", x)
     else:
          for x in maskiner:
               LbDelagaresMaskiner.insert("end", x)    


     tabControl.select(delagare)

def fyllMaskinInfoIgen(self):
     global maskinnummer
     
     maskinnummer = LbDelagaresMaskiner.get(LbDelagaresMaskiner.curselection())
     maskinnummer = maskinnummer[0]
     cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + str(maskinnummer) + ';')
     maskinInfo = cursor.fetchone()
     maskinInfo = list(maskinInfo)

     try:
          txtMaskinnummermaskininfo.config(state=NORMAL)
          txtMaskinnummermaskininfo.delete('1.0', 'end')
          txtMaskinnummermaskininfo.insert('end', maskinInfo[0])
          txtMaskinnummermaskininfo.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbeteckning.config(state=NORMAL)
          txtMaskinbeteckning.delete('1.0', 'end')
          txtMaskinbeteckning.insert('end', maskinInfo[1])
          txtMaskinbeteckning.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinme_klass.config(state=NORMAL)
          txtMaskinme_klass.delete('1.0', 'end')
          txtMaskinme_klass.insert('end', maskinInfo[2])
          txtMaskinme_klass.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinmotorfabrikat.config(state=NORMAL)
          txtMaskinmotorfabrikat.delete('1.0', 'end')
          txtMaskinmotorfabrikat.insert('end', maskinInfo[8])
          txtMaskinmotorfabrikat.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotortyp.config(state=NORMAL)
          txtMaskinmotortyp.delete('1.0', 'end')
          txtMaskinmotortyp.insert('end', maskinInfo[9])
          txtMaskinmotortyp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotor.config(state=NORMAL)
          txtMaskinmotor.delete('1.0', 'end')
          txtMaskinmotor.insert('end', maskinInfo[16])
          txtMaskinmotor.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinvaxellada.config(state=NORMAL)
          txtMaskinvaxellada.delete('1.0', 'end')
          txtMaskinvaxellada.insert('end', maskinInfo[18])
          txtMaskinvaxellada.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinhydraulsystem.config(state=NORMAL)
          txtMaskinhydraulsystem.delete('1.0', 'end')
          txtMaskinhydraulsystem.insert('end', maskinInfo[20])
          txtMaskinhydraulsystem.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinkylvatska.config(state=NORMAL)
          txtMaskinkylvatska.delete('1.0', 'end')
          txtMaskinkylvatska.insert('end', maskinInfo[33])
          txtMaskinkylvatska.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinmotoreffekt.config(state=NORMAL)
          txtMaskinmotoreffekt.delete('1.0', 'end')
          txtMaskinmotoreffekt.insert('end', maskinInfo[10])
          txtMaskinmotoreffekt.config(state=DISABLED)
     except:
          pass

     try:
          if maskinInfo[12] == 1:
               cbMaskinmotorvarmare.state(['selected'])
               cbMaskinmotorvarmare.state(['disabled'])
          else:
               cbMaskinmotorvarmare.state(['!selected'])
               cbMaskinmotorvarmare.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[14] == 1:
               cbMaskinkatalysator.state(['selected'])
               cbMaskinkatalysator.state(['disabled'])
          else:
               cbMaskinkatalysator.state(['!selected'])
               cbMaskinkatalysator.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[15] == 1:
               cbMaskinpartikelfilter.state(['selected'])
               cbMaskinpartikelfilter.state(['disabled'])
          else:
               cbMaskinpartikelfilter.state(['!selected'])
               cbMaskinpartikelfilter.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[11] == 1:
               cbMaskinvattenbaseradlack.state(['selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
          else:
               cbMaskinvattenbaseradlack.state(['!selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
     except:
          pass

     try:
          txtMaskinkylmedia.config(state=NORMAL)
          txtMaskinkylmedia.delete('1.0', 'end')
          txtMaskinkylmedia.insert('end', maskinInfo[13])
          txtMaskinkylmedia.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbullernivautv.config(state=NORMAL)
          txtMaskinbullernivautv.delete('1.0', 'end')
          txtMaskinbullernivautv.insert('end', maskinInfo[29])
          txtMaskinbullernivautv.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbullernivainv.config(state=NORMAL)
          txtMaskinbullernivainv.delete('1.0', 'end')
          txtMaskinbullernivainv.insert('end', maskinInfo[31])
          txtMaskinbullernivainv.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinsmorjfett.config(state=NORMAL)
          txtMaskinsmorjfett.delete('1.0', 'end')
          txtMaskinsmorjfett.insert('end', maskinInfo[24])
          txtMaskinsmorjfett.config(state=DISABLED)
     except:
          pass
     
     try:
          txtMaskinBatterityp.config(state=NORMAL)
          txtMaskinBatterityp.delete('1.0', 'end')
          txtMaskinBatterityp.insert('end', maskinInfo[38])
          txtMaskinBatterityp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinperiod.config(state=NORMAL)
          txtMaskinperiod.delete('1.0', 'end')
          txtMaskinperiod.insert('end', maskinInfo[7])
          txtMaskinperiod.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinarsbelopp.config(state=NORMAL)
          txtMaskinarsbelopp.delete('1.0', 'end')
          txtMaskinarsbelopp.insert('end', maskinInfo[5])
          txtMaskinarsbelopp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmiljostatus.config(state=NORMAL)
          txtMaskinmiljostatus.delete('1.0', 'end')
          txtMaskinmiljostatus.insert('end', maskinInfo[30])
          txtMaskinmiljostatus.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinarsmodell.config(state=NORMAL)
          txtMaskinarsmodell.delete('1.0', 'end')
          txtMaskinarsmodell.insert('end', maskinInfo[6])
          txtMaskinarsmodell.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinregistreringsnummer.config(state=NORMAL)
          txtMaskinregistreringsnummer.delete('1.0', 'end')
          txtMaskinregistreringsnummer.insert('end', maskinInfo[26])
          txtMaskinregistreringsnummer.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskintyp.config(state=NORMAL)
          txtMaskintyp.delete('1.0', 'end')
          txtMaskintyp.insert('end', maskinInfo[27])
          txtMaskintyp.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinmotoroljevolym.config(state=NORMAL)
          txtMaskinmotoroljevolym.delete('1.0', 'end')
          txtMaskinmotoroljevolym.insert('end', maskinInfo[17])
          txtMaskinmotoroljevolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinvaxelladevolym.config(state=NORMAL)
          txtMaskinvaxelladevolym.delete('1.0', 'end')
          txtMaskinvaxelladevolym.insert('end', maskinInfo[19])
          txtMaskinvaxelladevolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinhydraulsystemvolym.config(state=NORMAL)
          txtMaskinhydraulsystemvolym.delete('1.0', 'end')
          txtMaskinhydraulsystemvolym.insert('end', maskinInfo[21])
          txtMaskinhydraulsystemvolym.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinkylvatskavolym.config(state=NORMAL)
          txtMaskinkylvatskavolym.delete('1.0', 'end')
          txtMaskinkylvatskavolym.insert('end', maskinInfo[32])
          txtMaskinkylvatskavolym.config(state=DISABLED)
     except:
          pass

     try:
          TxtOvrigtext.config(state=NORMAL)
          TxtOvrigtext.delete('1.0', 'end')
          TxtOvrigtext.insert('end', maskinInfo[41])
          TxtOvrigtext.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskinbransle.config(state=NORMAL)
          txtMaskinbransle.delete('1.0', 'end')
          txtMaskinbransle.insert('end', maskinInfo[23])
          txtMaskinbransle.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskindackfabrikat.config(state=NORMAL)
          txtMaskindackfabrikat.delete('1.0', 'end')
          txtMaskindackfabrikat.insert('end', maskinInfo[25])
          txtMaskindackfabrikat.config(state=DISABLED)
     except:
          pass

     try:
          txtMaskindimension.config(state=NORMAL)
          txtMaskindimension.delete('1.0', 'end')
          txtMaskindimension.insert('end', maskinInfo[34])
          txtMaskindimension.config(state=DISABLED)
     except:
          pass

     try:
          if maskinInfo[37] == 1:
               cbMaskingasolanlaggning.state(['selected'])
               cbMaskingasolanlaggning.state(['disabled'])
          else:
               cbMaskingasolanlaggning.state(['!selected'])
               cbMaskingasolanlaggning.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[22] == 1:
               cbMaskinSaneringsvatska.state(['selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
          else:
               cbMaskinSaneringsvatska.state(['!selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
     except:
          pass

     forarnamn=""
     if maskinInfo[40] != None:
          cursor.execute('SELECT Namn FROM forare WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          forarnamn = cursor.fetchone()

     try:
          txtMaskinforare.config(state=NORMAL)
          txtMaskinforare.delete('1.0', 'end')
          txtMaskinforare.insert('end', forarnamn[0])
          txtMaskinforare.config(state=DISABLED)
     except:
          pass

     referenser = []     
     referenser.clear()
     if maskinInfo[40] != None:
          cursor.execute('SELECT Beskrivning FROM referens WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          referenser = cursor.fetchall()

     try:
          if lbMaskinreferens.index("end") != 0:
               lbMaskinreferens.delete(0, "end")
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
          else:
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
     except:
          pass

     try:
          if maskinInfo[28] == 1:
               cbMaskininsatserlagd.state(['selected'])
               cbMaskininsatserlagd.state(['disabled'])
          else:
               cbMaskininsatserlagd.state(['!selected'])
               cbMaskininsatserlagd.state(['disabled'])
     except:
          pass
     
     try:
          if maskinInfo[36] == 1:
               cbMaskinregummerade.state(['selected'])
               cbMaskinregummerade.state(['disabled'])
          else:
               cbMaskinregummerade.state(['!selected'])
               cbMaskinregummerade.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[35] == 1:
               cbMaskinregummerbara.state(['selected'])
               cbMaskinregummerbara.state(['disabled'])
          else:
               cbMaskinregummerbara.state(['!selected'])
               cbMaskinregummerbara.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[3] == 1:
               cbMaskinKollektivforsakring.state(['selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
          else:
               cbMaskinKollektivforsakring.state(['!selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
     except:
          pass
     
     cursor.execute('SELECT Tillbehor FROM tillbehor WHERE Maskinnummer = ' + str(maskinnummer) + ';')
     tillbehor = cursor.fetchall()
     
     if lbMaskintillbehor.index("end") != 0:
          lbMaskintillbehor.delete(0, "end")
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     else:
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     
def nyDelagare(Typ):
     global medlemsnummer

     if Typ == "Ändra":
          titel = "Ändra befintlig delägare"
     elif Typ == "Ny":
          titel = "Lägg till ny delägare"
          
     def spara(Typ):
          global medlemsnummer
          
          if Typ == "Ändra":               
               cursor.execute("UPDATE foretagsregister SET Foretagsnamn = '" + entNyForetag.get() + "', Fornamn = '" + entNyFornamn.get() + "', Efternamn = '" + entNyEfternamn.get() + "', Gatuadress = '" + entNyGatuadress.get() + "', Postnummer = '" + entNyPostnummer.get() + "', Postadress = '" + entNyPostadress.get() + "', Telefon = '" + entNyTelefon.get() + "' WHERE Medlemsnummer = " + medlemsnummer +";")
               db.commit()
               fyllDelagarInfo()
               nyDelagare.destroy()
               tabControl.select(delagare)
               fyllListboxDelagare()

          elif Typ == "Ny":
               cursor.execute("INSERT INTO foretagsregister (Medlemsnummer, Foretagsnamn, Fornamn, Efternamn, Gatuadress, Postnummer, Postadress, Telefon) VALUES ('" + entNyMedlemsnummer.get() + "', '" + entNyForetag.get() + "', '" + entNyFornamn.get() + "', '" + entNyEfternamn.get() + "', '" + entNyGatuadress.get() + "', '" + entNyPostnummer.get() + "', '" + entNyPostadress.get() + "', '" + entNyTelefon.get() + "');")
               db.commit()
               medlemsnummer = entNyMedlemsnummer.get()
               fyllDelagarInfo()
               nyDelagare.destroy()
               tabControl.select(delagare)
               fyllListboxDelagare()

     nyDelagare = Toplevel(root)

     nyDelagare.title(titel)

     nyDelagare.geometry("300x275")

     lblNyMedlemsnummer = Label(nyDelagare, text="Medlemsnr")
     lblNyMedlemsnummer.grid(row = 0, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyMedlemsnummer = Entry(nyDelagare, width = 5)
     entNyMedlemsnummer.grid(row = 0, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyForetag = Label(nyDelagare, text= "Företag")
     lblNyForetag.grid(row = 1, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyForetag = Entry(nyDelagare, width = 25)
     entNyForetag.grid(row = 1, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyFornamn = Label(nyDelagare, text= "Förnamn")
     lblNyFornamn.grid(row = 2, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyFornamn = Entry(nyDelagare, width = 25)
     entNyFornamn.grid(row = 2, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyEfternamn = Label(nyDelagare, text= "Efternamn")
     lblNyEfternamn.grid(row = 3, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyEfternamn = Entry(nyDelagare, width = 25)
     entNyEfternamn.grid(row = 3, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyGatuadress = Label(nyDelagare, text= "Gatuadress")
     lblNyGatuadress.grid(row = 4, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyGatuadress = Entry(nyDelagare, width = 25)
     entNyGatuadress.grid(row = 4, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyPostnummer = Label(nyDelagare, text= "Postnummer")
     lblNyPostnummer.grid(row = 5, column = 0, sticky = W, padx = (10, 0), pady=(7, 0))
     entNyPostnummer = Entry(nyDelagare, width = 25)
     entNyPostnummer.grid(row = 5, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyPostadress = Label(nyDelagare, text= "Postadress")
     lblNyPostadress.grid(row = 6, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyPostadress = Entry(nyDelagare, width = 25)
     entNyPostadress.grid(row = 6, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyTelefon = Label(nyDelagare, text= "Telefon")
     lblNyTelefon.grid(row = 7, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyTelefon = Entry(nyDelagare, width = 25)
     entNyTelefon.grid(row = 7, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     btnSparaNyDelagare = Button(nyDelagare, text="Spara", command = lambda: spara(Typ))
     btnSparaNyDelagare.grid(row = 8, column = 1, sticky = W, pady = (10, 0), padx=(5,0))

     btnAvbrytNyDelagare = Button(nyDelagare, text="Avbryt", command = lambda: nyDelagare.destroy())
     btnAvbrytNyDelagare.grid(row = 8, column = 1, pady = (10, 0), padx=(5,0))

     if Typ == "Ändra":
          cursor.execute('SELECT * FROM foretagsregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
          delagarInformation = cursor.fetchone()
          delagarInformation = list(delagarInformation)

          try:
               entNyMedlemsnummer.insert('end', medlemsnummer)
               entNyMedlemsnummer.config(state = 'disabled')
          except:
               pass

          try:
               entNyForetag.insert('end', delagarInformation[1])
          except:
               pass

          try:
               entNyFornamn.insert('end', delagarInformation[6])
          except:
               pass

          try:
               entNyEfternamn.insert('end', delagarInformation[7])
          except:
               pass

          try:
               entNyGatuadress.insert('end', delagarInformation[2])
          except:
               pass

          try:
               entNyPostnummer.insert('end', delagarInformation[3])
          except:
               pass

          try:
               entNyPostadress.insert('end', delagarInformation[4])
          except:
               pass

          try:
               entNyTelefon.insert('end', delagarInformation[5])
          except:
               pass

def taBortDelagare():
     global medlemsnummer

     response = messagebox.askyesno("Varning!", "Är du säker på att du vill ta bort delägare nr. " + medlemsnummer + "? \nDetta tar även bort alla maskiner på detta medlemsnummer.")
     if response == 1:
          cursor.execute("DELETE FROM maskinregister WHERE Medlemsnummer = " + medlemsnummer + ";")
          cursor.execute("DELETE FROM foretagsregister WHERE Medlemsnummer = " + medlemsnummer + ";" )
          db.commit()
          medlemsnummer = ""
          tomMaskinInfo()
          tomDelagareInfo()
          fyllListboxDelagare()

     else:
          pass

def nyMaskinFonster(Typ):

     def sparaMaskin(Typ):
          if Typ=="Byt":
               #sparaHistoriken
               #andraMaskin()
               print("NyMaskin Byt")
               pass
          elif Typ=="Ny":
               #andraMaskin(Typ)
               print("nyMaskin Ny")
               pass
          else:
               print("nyMaskin Ändra")
               try:
                    andraMaskin(Typ)
                    nyMaskin.destroy()
               except:
                    print("Kunde inte ändra maskin")

     def andraMaskin(Typ):
          
          if cbMaskinregummerbara.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET regummerbar = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET regummerbar = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          
          if cbMaskinregummerade.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET regummerad = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET regummerad = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          
          if cbMaskinKollektivforsakring.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Forsakring = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Forsakring = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          
          if cbMaskininsatserlagd.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Maskininsats = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Maskininsats = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskinmotorvarmare.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Motorvarmare = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Motorvarmare = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskinkatalysator.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Katalysator = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Katalysator = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskinpartikelfilter.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Partikelfilter = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Partikelfilter = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskinvattenbaseradlack.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Vattenbaseradlack = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Vattenbaseradlack = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskingasolanlaggning.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Gasol = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Gasol = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          if cbMaskinSaneringsvatska.instate(['selected']) == True:
               try:
                    cursor.execute("UPDATE maskinregister SET Saneringsvatska = 1 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass
          else:
               try:
                    cursor.execute("UPDATE maskinregister SET Saneringsvatska = 0 WHERE Maskinnummer = " + Typ +";")
               except:
                    pass

          try:

               cursor.execute("UPDATE maskinregister SET Maskinnummer = '" + txtMaskinnummermaskininfo.get('1.0','end') + "', MarkeModell = '" + txtMaskinbeteckning.get('1.0','end') + "', ME_Klass = '" + txtMaskinme_klass.get('1.0','end') + "', Motorfabrikat = '" + txtMaskinmotorfabrikat.get('1.0','end') + "', Motortyp = '" + txtMaskinmotortyp.get('1.0','end') + "', Motorolja = '" + txtMaskinmotor.get('1.0','end') + "', Vaxelladsolja = '" + txtMaskinvaxellada.get('1.0','end') + "', Hydraulolja = '" + txtMaskinhydraulsystem.get('1.0','end') + "', Kylvatska = '" + txtMaskinkylvatska.get('1.0','end') + "', Motoreffekt = '" + txtMaskinmotoreffekt.get('1.0','end') + "', Kylmedia = '" + txtMaskinkylmedia.get('1.0','end') + "', Bullernivaute = '" + txtMaskinbullernivautv.get('1.0','end') + "', Bullernivainne = '" + txtMaskinbullernivainv.get('1.0','end') + "', Smorjfett = '" + txtMaskinsmorjfett.get('1.0','end') + "', Batterityp = '" + txtMaskinBatterityp.get('1.0','end') + "', Arsbelopp = '" + txtMaskinarsbelopp.get('1.0','end') + "', Miljostatus = '" + txtMaskinmiljostatus.get('1.0','end') + "', Arsmodell = '" + txtMaskinarsmodell.get('1.0','end') + "', Registreringsnummer = '" + txtMaskinregistreringsnummer.get('1.0','end') + "', Maskintyp = '" + txtMaskintyp.get('1.0','end') + "', Motorvolymolja = '" + txtMaskinmotoroljevolym.get('1.0','end') + "', Vaxelladavolym = '" + txtMaskinvaxelladevolym.get('1.0','end') + "', Hydraulvolym = '" + txtMaskinhydraulsystemvolym.get('1.0','end') + "', Kylvatskavolym = '" + txtMaskinkylvatskavolym.get('1.0','end') + "', Ovrig_text = '" + TxtOvrigtext.get('1.0','end') + "', Bransle = '" + txtMaskinbransle.get('1.0','end') + "', Dackfabrikat = '" + txtMaskindackfabrikat.get('1.0','end') + "', Dimension = '" + txtMaskindimension.get('1.0','end') + "'WHERE Maskinnummer = " + Typ +";")
          except Exception:
               traceback.print_exc()
          
          try:
               for x in tillbehorAttTaBort:
                    cursor.execute("DELETE tillbehor FROM Tillbehor WHERE Maskinnummer = " + Typ +" AND Tillbehor = '" + x +"';")     
                    

          except Exception:
               traceback.print_exc()

          try:
               for x in tillbehorAttLaggaTill:
                    print(x)
                    cursor.execute("INSERT INTO tillbehor (Tillbehor, Maskinnummer) values ('" + x + "', " + Typ + ");" )

          except Exception:
               traceback.print_exc()
          db.commit()
          fyllMaskinInfo(Typ)

     def bytNyMaskin():
          

     nyMaskin = Toplevel(root)

     if Typ=="Ny":
          nyMaskin.title("Lägg till ny maskin")
     elif Typ=="Byt":
          nyMaskin.title("Byt maskin")
     else:
          nyMaskin.title("Ändra maskin")

     nyMaskin.geometry("975x680")

     lblMaskinnummermaskininfo = Label(nyMaskin, text= "Maskinnummer")
     lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(7,8))
     txtMaskinnummermaskininfo = Text(nyMaskin, width = 5, height=0.1)
     txtMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0), pady=(7,0))

     lblMaskinbeteckning = Label(nyMaskin, text="Beteckning")
     lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbeteckning = Text(nyMaskin, width = 25, height=0.1)
     txtMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))


     lblMaskinme_klass = Label(nyMaskin, text="ME-Klass")
     lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinme_klass = Text(nyMaskin, width = 25, height=0.1)
     txtMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))


     lblMaskinmotorfabrikat = Label(nyMaskin, text="Motorfabrikat")
     lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotorfabrikat = Text(nyMaskin, width = 25, height=0.1)
     txtMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))


     lblMaskinmotortyp = Label(nyMaskin, text="Motortyp")
     lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotortyp=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))


     lblMaskinmotor = Label(nyMaskin, text="Motor")
     lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotor = Text(nyMaskin, width = 25, height=0.1)
     txtMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))


     lblMaskinvaxellada = Label(nyMaskin, text="Växellåda")
     lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinvaxellada=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))

     lblMaskinhydraulsystem = Label(nyMaskin, text="Hydraulsystem")
     lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinhydraulsystem=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))


     lblMaskinkylvatska = Label(nyMaskin, text="Kylvätska")
     lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinkylvatska=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))


     lblMaskinmotoreffekt = Label(nyMaskin, text="Motoreffekt/KW")
     lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotoreffekt=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))

     lblMaskinmotorvarmare = Label(nyMaskin, text="Motorvärmare")
     lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
     #txtMaskinmotorvarmare=Text(nyMaskin, width = 25, height=0.1)
     #txtMaskinmotorvarmare.grid(column=1, row=10, sticky=W, padx=(10,0))
     cbMaskinmotorvarmare = ttk.Checkbutton(nyMaskin)
     cbMaskinmotorvarmare.state(['!alternate', '!selected', '!disabled'])
     cbMaskinmotorvarmare.grid(column = 1, row = 10, sticky = W, padx=(5,0))

     lblMaskinkatalysator = Label(nyMaskin, text="Katalysator")
     lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
     #txtMaskinkatalysator=Text(nyMaskin, width = 25, height=0.1)
     #txtMaskinkatalysator.grid(column=1,row=11, sticky=W, padx=(10,0))
     cbMaskinkatalysator = ttk.Checkbutton(nyMaskin)
     cbMaskinkatalysator.state(['!alternate', '!selected', '!disabled'])
     cbMaskinkatalysator.grid(column = 1, row = 11, sticky = W, padx=(5,0))

     lblMaskinpartikelfilter = Label(nyMaskin, text="Partikelfilter")
     lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
     #txtMaskinpartikelfilter=Text(nyMaskin, width = 25, height=0.1)
     #txtMaskinpartikelfilter.grid(column=1,row=12, sticky=W, padx=(10,0))
     cbMaskinpartikelfilter = ttk.Checkbutton(nyMaskin)
     cbMaskinpartikelfilter.state(['!alternate', '!selected', '!disabled'])
     cbMaskinpartikelfilter.grid(column = 1, row = 12, sticky = W, padx=(5,0))

     lblMaskinvattenbaseradlack = Label(nyMaskin, text="Vattenbaserad lack")
     lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
     #txtMaskinvattenbaseradlack=Text(nyMaskin, width = 25, height=0.1)
     #txtMaskinvattenbaseradlack.grid(column=1, row=13, sticky=W, padx=(10,0))
     cbMaskinvattenbaseradlack = ttk.Checkbutton(nyMaskin)
     cbMaskinvattenbaseradlack.state(['!alternate', '!selected', '!disabled'])
     cbMaskinvattenbaseradlack.grid(column = 1, row = 13, sticky = W, padx=(5,0))

     lblMaskinkylmedia = Label(nyMaskin, text="Kylmedia")
     lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinkylmedia=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))

     lblMaskinbullernivautv = Label(nyMaskin, text="Bullernivå utvändigt")
     lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbullernivautv=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))

     lblMaskinbullernivainv = Label(nyMaskin, text="Bullernivå invändigt")
     lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbullernivainv=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))

     lblMaskinsmorjfett = Label(nyMaskin, text="Smörjfett")
     lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinsmorjfett=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))

     lblMaskinBatterityp = Label(nyMaskin, text="Batterityp")
     lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinBatterityp=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))

     #checkbox
     lblMaskinKollektivforsakring = Label(nyMaskin, text="Kollektiv försäkring")
     lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
     cbMaskinKollektivforsakring = ttk.Checkbutton(nyMaskin)
     cbMaskinKollektivforsakring.state(['!alternate', '!selected', '!disabled'])
     cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

     lblMaskinperiod = Label(nyMaskin, text="Period")
     lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))

     #Date entry
     deMaskinperiod1 = DateEntry(nyMaskin, values="Text", date_pattern="yyyy-mm-dd")
     deMaskinperiod1.delete(0, 'end')
     deMaskinperiod1.grid(column=1, row=20, sticky=W, padx=(10,0))

     deMaskinperiod2 = DateEntry(nyMaskin, values="Text", date_pattern="yyyy-mm-dd")
     deMaskinperiod2.delete(0, 'end')
     deMaskinperiod2.grid(column=1, row=20, sticky=E)

     lblMaskinarsbelopp = Label(nyMaskin, text="Årsbelopp")
     lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinarsbelopp=Text(nyMaskin, width = 25, height=0.1)
     txtMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))

     #Buttons

     btnSparaNyMaskin=Button(nyMaskin, text="Spara", command = lambda: sparaMaskin(Typ))
     btnSparaNyMaskin.grid(column=5, row=21, sticky=E, padx=(0,55))
     btnAvbrytNyMaskin=Button(nyMaskin, text="Avbryt", command = lambda: nyMaskin.destroy())
     btnAvbrytNyMaskin.grid(column=5, row=21,sticky=E)

     #--------------------

     lblMaskinmiljostatus = Label(nyMaskin, text="Miljöstatus")
     lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0), pady=(7,0))
     txtMaskinmiljostatus=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0), pady=(7,0))

     lblMaskinarsmodell = Label(nyMaskin, text="Årsmodell")
     lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
     txtMaskinarsmodell=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))

     lblMaskinregistreringsnummer = Label(nyMaskin, text="Reg. nr/Ser. nr")
     lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
     txtMaskinregistreringsnummer=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))

     lblMaskintyp = Label(nyMaskin, text="Maskintyp")
     lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
     txtMaskintyp=Text(nyMaskin, width = 20, height=0.1)
     txtMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))

     lblMaskinmotoroljevolym  = Label(nyMaskin, text="Motorolja volym/liter")
     lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
     txtMaskinmotoroljevolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))

     lblMaskinvaxelladevolym = Label(nyMaskin, text="Växellåda volym/liter")
     lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
     txtMaskinvaxelladevolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))

     lblMaskinhydraulsystemvolym = Label(nyMaskin, text="Hydraul volym/liter")
     lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
     txtMaskinhydraulsystemvolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))

     lblMaskinkylvatskavolym = Label(nyMaskin, text="Kylvätska volym/liter")
     lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
     txtMaskinkylvatskavolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))

     lblOvrigtext = Label(nyMaskin, text="Övrig Text")
     lblOvrigtext.grid(column=2, row=9, sticky = W, padx=(10,0))
     TxtOvrigtext = Text(nyMaskin, width = 20, height=3)
     TxtOvrigtext.grid(row=10, column=2, columnspan=2, rowspan=4, sticky=NSEW, padx=(10,15))

     #Scrollbar
     ScbTxtOvrigText = Scrollbar(nyMaskin, orient="vertical")
     ScbTxtOvrigText.grid(row = 10, column = 3, sticky = N+S+E, rowspan = 4)
     ScbTxtOvrigText.config(command =TxtOvrigtext.yview)

     TxtOvrigtext.config(yscrollcommand=ScbTxtOvrigText.set) 

     def fileDialog():
 
          global img3
          filename = filedialog.askopenfilename(initialdir =  "/", title = "Välj en fil", filetype = (("jpeg files","*.jpg"),("all files","*.*")) )
          txtSokvag = Text(nyMaskin, width = 20, height=0.1)
          txtSokvag.grid(column = 2, row = 14, padx=(10,0), columnspan=2, sticky=W+E)
          txtSokvag.insert('end', filename)
          nyMaskin.lift()
          imgNyBild = Image.open(filename)  
          imgNyBild = imgNyBild.resize((150,145), Image. ANTIALIAS)
          img3 = ImageTk.PhotoImage(imgNyBild)
          img_NyBild = Label(nyMaskin, image=img3) 
          img_NyBild.grid(row=15, column=2, columnspan=2, rowspan=6)
          
     btnNyBild = Button(nyMaskin, text="Lägg till bild", command= fileDialog)
     btnNyBild.grid(column=2, row=21, sticky=W, padx=(10,0))

     #------------------------

     lblMaskinbransle = Label(nyMaskin, text="Bränsle")
     lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0), pady=(7,0))
     txtMaskinbransle=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0), pady=(7,0))

     lblMaskindackfabrikat = Label(nyMaskin, text="Däckfabrikat")
     lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
     txtMaskindackfabrikat=Text(nyMaskin, width = 20, height=0.1)
     txtMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))

     lblMaskindimension = Label(nyMaskin, text="Dimension/typ")
     lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
     txtMaskindimension=Text(nyMaskin, width = 20, height=0.1)
     txtMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))

     #Checkbox
     lblMaskinregummerbara = Label(nyMaskin, text="Regummerbara")
     lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
     cbMaskinregummerbara = ttk.Checkbutton(nyMaskin)
     cbMaskinregummerbara.state(['!alternate', '!selected', '!disabled'])
     cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

     #Checkbox
     lblMaskinregummerade = Label(nyMaskin, text="Regummerade")
     lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
     cbMaskinregummerade = ttk.Checkbutton(nyMaskin)
     cbMaskinregummerade.state(['!alternate', '!selected', '!disabled'])
     cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

     lblMaskingasolanlaggning = Label(nyMaskin, text="Gasolanläggning")
     lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
     #txtMaskingasolanlaggning=Text(nyMaskin, width = 20, height=0.1)
     #txtMaskingasolanlaggning.grid(column=5, row=5, sticky=W, padx=(10,0))
     cbMaskingasolanlaggning = ttk.Checkbutton(nyMaskin)
     cbMaskingasolanlaggning.state(['!alternate', '!selected', '!disabled'])
     cbMaskingasolanlaggning.grid(column = 5, row = 5, sticky = W, padx=(5,0))

     lblMaskinSaneringsvatska = Label(nyMaskin, text="Saneringsvätska")
     lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
     #txtMaskinSaneringsvatska=Text(nyMaskin, width = 20, height=0.1)
     #txtMaskinSaneringsvatska.grid(column=5, row=6, sticky=W, padx=(10,0))
     cbMaskinSaneringsvatska = ttk.Checkbutton(nyMaskin)
     cbMaskinSaneringsvatska.state(['!alternate', '!selected', '!disabled'])
     cbMaskinSaneringsvatska.grid(column = 5, row = 6, sticky = W, padx=(5,0))

     #Checkbox
     lblMaskininsattserlagd = Label(nyMaskin, text="Maskininsats erlagd")
     lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
     cbMaskininsatserlagd = ttk.Checkbutton(nyMaskin)
     cbMaskininsatserlagd.state(['!alternate', '!selected', '!disabled'])
     cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

     lblMaskinforare = Label(nyMaskin, text="Förare")
     lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
     txtMaskinforare=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))

     lblMaskinreferens = Label(nyMaskin, text="Referensjobb")
     lblMaskinreferens.grid(column=4, row=9, sticky = W, padx=(10,0))
     txtMaskinreferens=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinreferens.grid(column=5, row=9, sticky=W, padx=(10,0))

     lbMaskinreferens = Listbox(nyMaskin, height=4)
     lbMaskinreferens.grid(column=4, row=10, columnspan=2, rowspan=4, sticky=NSEW, padx=(10,0))
     
     lblMaskintillbehor = Label(nyMaskin, text="Tillbehör")
     lblMaskintillbehor.grid(column=4, row=15, sticky = W, padx=(10,0))
     txtMaskintillbehor=Text(nyMaskin, width = 20, height=0.1)
     txtMaskintillbehor.grid(column=5, row=15, sticky=W, padx=(10,0))

     tillbehorAttTaBort=[]
     tillbehorAttLaggaTill=[]

     def taBortTillbehor(self):
          nyMaskin.lift()
          response = messagebox.askyesno("Ta bort tillbehör", "Vill du ta bort " + lbMaskintillbehor.get(lbMaskintillbehor.curselection()) + "?")
          nyMaskin.lift()
          if response == True:
               tillbehorAttTaBort.append(lbMaskintillbehor.get(lbMaskintillbehor.curselection()))
               try:
                    tillbehorAttLaggaTill.remove(lbMaskintillbehor.get(lbMaskintillbehor.curselection()))
               except:
                    pass
               lbMaskintillbehor.delete(lbMaskintillbehor.curselection())

         
     
     lbMaskintillbehor = Listbox(nyMaskin, height=4)
     lbMaskintillbehor.bind('<Double-Button>', taBortTillbehor)
     lbMaskintillbehor.grid(column=4, row=16, columnspan=2, rowspan=4, sticky=NSEW, padx=(10,0), pady=(5,5))  

     ScbLbMaskintillbehor = Scrollbar(nyMaskin, orient="vertical")
     ScbLbMaskintillbehor.grid(row = 16, column = 6, sticky = N+S+W, rowspan = 4)
     ScbLbMaskintillbehor.config(command =lbMaskintillbehor.yview)
     lbMaskintillbehor.config(yscrollcommand=ScbLbMaskintillbehor.set)

     scbLbReferenser = Scrollbar(nyMaskin, orient="vertical")
     scbLbReferenser.grid(row = 10, column=6, sticky = N+S+W, rowspan=4)
     scbLbReferenser.config(command=lbMaskinreferens.yview)
     lbMaskinreferens.config(yscrollcommand=scbLbReferenser.set)
     
     txtMaskintillbehor.bind('<Return>', lambda x: (lbMaskintillbehor.insert('end', txtMaskintillbehor.get('1.0', 'end')), tillbehorAttLaggaTill.append(txtMaskintillbehor.get('1.0', 'end')), txtMaskintillbehor.delete('1.0','end')))
     txtMaskinreferens.bind('<Return>', lambda x: (lbMaskinreferens.insert('end', txtMaskinreferens.get('1.0', 'end')), txtMaskinreferens.delete('1.0','end')))
     #txtMaskintillbehor.bind('<Return>', lambda x=None: addTillbehor())

     if Typ !="Ny" and Typ!="Byt":
          try:
               cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + Typ + ';')
               maskinInfo = cursor.fetchone()
               maskinInfo = list(maskinInfo)
          except:
               pass
          
          try:
               txtMaskinnummermaskininfo.config(state=NORMAL)
               txtMaskinnummermaskininfo.delete('1.0', 'end')
               txtMaskinnummermaskininfo.insert('end', maskinInfo[0])
          except:
               pass

          try:
               txtMaskinbeteckning.config(state=NORMAL)
               txtMaskinbeteckning.delete('1.0', 'end')
               txtMaskinbeteckning.insert('end', maskinInfo[1])
          except:
               pass

          try:
               txtMaskinme_klass.config(state=NORMAL)
               txtMaskinme_klass.delete('1.0', 'end')
               txtMaskinme_klass.insert('end', maskinInfo[2])
          except:
               pass
          
          try:
               txtMaskinmotorfabrikat.config(state=NORMAL)
               txtMaskinmotorfabrikat.delete('1.0', 'end')
               txtMaskinmotorfabrikat.insert('end', maskinInfo[8])
          except:
               pass

          try:
               txtMaskinmotortyp.config(state=NORMAL)
               txtMaskinmotortyp.delete('1.0', 'end')
               txtMaskinmotortyp.insert('end', maskinInfo[9])
          except:
               pass

          try:
               txtMaskinmotor.config(state=NORMAL)
               txtMaskinmotor.delete('1.0', 'end')
               txtMaskinmotor.insert('end', maskinInfo[16])
          except:
               pass
          
          try:
               txtMaskinvaxellada.config(state=NORMAL)
               txtMaskinvaxellada.delete('1.0', 'end')
               txtMaskinvaxellada.insert('end', maskinInfo[18])
          except:
               pass
          
          try:
               txtMaskinhydraulsystem.config(state=NORMAL)
               txtMaskinhydraulsystem.delete('1.0', 'end')
               txtMaskinhydraulsystem.insert('end', maskinInfo[20])
          except:
               pass
          
          try:
               txtMaskinkylvatska.config(state=NORMAL)
               txtMaskinkylvatska.delete('1.0', 'end')
               txtMaskinkylvatska.insert('end', maskinInfo[33])
          except:
               pass
          
          try:
               TxtOvrigtext.config(state=NORMAL)
               TxtOvrigtext.delete('1.0', 'end')
               TxtOvrigtext.insert('end', maskinInfo[41])
               TxtOvrigtext.config(state=DISABLED)
          except:
               pass

          try:
               txtMaskinmotoreffekt.config(state=NORMAL)
               txtMaskinmotoreffekt.delete('1.0', 'end')
               txtMaskinmotoreffekt.insert('end', maskinInfo[10])
          except:
               pass

          try:
               if maskinInfo[12] == 1:
                    cbMaskinmotorvarmare.state(['selected'])
                    cbMaskinmotorvarmare.state(['!disabled'])
               else:
                    cbMaskinmotorvarmare.state(['!selected'])
                    cbMaskinmotorvarmare.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[14] == 1:
                    cbMaskinkatalysator.state(['selected'])
                    cbMaskinkatalysator.state(['!disabled'])
               else:
                    cbMaskinkatalysator.state(['!selected'])
                    cbMaskinkatalysator.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[15] == 1:
                    cbMaskinpartikelfilter.state(['selected'])
                    cbMaskinpartikelfilter.state(['!disabled'])
               else:
                    cbMaskinpartikelfilter.state(['!selected'])
                    cbMaskinpartikelfilter.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[11] == 1:
                    cbMaskinvattenbaseradlack.state(['selected'])
                    cbMaskinvattenbaseradlack.state(['!disabled'])
               else:
                    cbMaskinvattenbaseradlack.state(['!selected'])
                    cbMaskinvattenbaseradlack.state(['!disabled'])
          except:
               pass

          try:
               txtMaskinkylmedia.config(state=NORMAL)
               txtMaskinkylmedia.delete('1.0', 'end')
               txtMaskinkylmedia.insert('end', maskinInfo[13])
          except:
               pass

          try:
               txtMaskinbullernivautv.config(state=NORMAL)
               txtMaskinbullernivautv.delete('1.0', 'end')
               txtMaskinbullernivautv.insert('end', maskinInfo[29])
          except:
               pass

          try:
               txtMaskinbullernivainv.config(state=NORMAL)
               txtMaskinbullernivainv.delete('1.0', 'end')
               txtMaskinbullernivainv.insert('end', maskinInfo[31])
          except:
               pass

          try:
               txtMaskinsmorjfett.config(state=NORMAL)
               txtMaskinsmorjfett.delete('1.0', 'end')
               txtMaskinsmorjfett.insert('end', maskinInfo[24])
          except:
               pass
          
          try:
               txtMaskinBatterityp.config(state=NORMAL)
               txtMaskinBatterityp.delete('1.0', 'end')
               txtMaskinBatterityp.insert('end', maskinInfo[38])
          except:
               pass

          try:
               dates = maskinInfo[7].split(" - ")
               #deMaskinperiod1.config(state=NORMAL)
               #deMaskinperiod1.delete('1.0', 'end')
               deMaskinperiod1.set_date(datetime.strptime(dates[0], "%Y-%m-%d"))
               deMaskinperiod2.set_date(datetime.strptime(dates[1], "%Y-%m-%d"))
               
               
          except:
               pass

          try:
               txtMaskinarsbelopp.config(state=NORMAL)
               txtMaskinarsbelopp.delete('1.0', 'end')
               txtMaskinarsbelopp.insert('end', maskinInfo[5])
          except:
               pass

          try:
               txtMaskinmiljostatus.config(state=NORMAL)
               txtMaskinmiljostatus.delete('1.0', 'end')
               txtMaskinmiljostatus.insert('end', maskinInfo[30])
          except:
               pass

          try:
               txtMaskinarsmodell.config(state=NORMAL)
               txtMaskinarsmodell.delete('1.0', 'end')
               txtMaskinarsmodell.insert('end', maskinInfo[6])
          except:
               pass

          try:
               txtMaskinregistreringsnummer.config(state=NORMAL)
               txtMaskinregistreringsnummer.delete('1.0', 'end')
               txtMaskinregistreringsnummer.insert('end', maskinInfo[26])
          except:
               pass

          try:
               txtMaskintyp.config(state=NORMAL)
               txtMaskintyp.delete('1.0', 'end')
               txtMaskintyp.insert('end', maskinInfo[27])
          except:
               pass

          try:
               txtMaskinmotoroljevolym.config(state=NORMAL)
               txtMaskinmotoroljevolym.delete('1.0', 'end')
               txtMaskinmotoroljevolym.insert('end', maskinInfo[17])
          except:
               pass

          try:
               txtMaskinvaxelladevolym.config(state=NORMAL)
               txtMaskinvaxelladevolym.delete('1.0', 'end')
               txtMaskinvaxelladevolym.insert('end', maskinInfo[19])
          except:
               pass

          try:
               txtMaskinhydraulsystemvolym.config(state=NORMAL)
               txtMaskinhydraulsystemvolym.delete('1.0', 'end')
               txtMaskinhydraulsystemvolym.insert('end', maskinInfo[21])
          except:
               pass

          try:
               txtMaskinkylvatskavolym.config(state=NORMAL)
               txtMaskinkylvatskavolym.delete('1.0', 'end')
               txtMaskinkylvatskavolym.insert('end', maskinInfo[32])
          except:
               pass

          try:
               txtMaskinbransle.config(state=NORMAL)
               txtMaskinbransle.delete('1.0', 'end')
               txtMaskinbransle.insert('end', maskinInfo[23])
          except:
               pass

          try:
               txtMaskindackfabrikat.config(state=NORMAL)
               txtMaskindackfabrikat.delete('1.0', 'end')
               txtMaskindackfabrikat.insert('end', maskinInfo[25])
          except:
               pass

          try:
               txtMaskindimension.config(state=NORMAL)
               txtMaskindimension.delete('1.0', 'end')
               txtMaskindimension.insert('end', maskinInfo[34])
          except:
               pass

          try:
               if maskinInfo[37] == 1:
                    cbMaskingasolanlaggning.state(['selected'])
                    cbMaskingasolanlaggning.state(['!disabled'])
               else:
                    cbMaskingasolanlaggning.state(['!selected'])
                    cbMaskingasolanlaggning.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[22] == 1:
                    cbMaskinSaneringsvatska.state(['selected'])
                    cbMaskinSaneringsvatska.state(['!disabled'])
               else:
                    cbMaskinSaneringsvatska.state(['!selected'])
                    cbMaskinSaneringsvatska.state(['!disabled'])
          except:
               pass

          forarnamn=""
          if maskinInfo[40] != None:
               cursor.execute('SELECT Namn FROM forare WHERE Forarid = ' + str(maskinInfo[40]) + ';')
               forarnamn = cursor.fetchone()

          try:
               txtMaskinforare.config(state=NORMAL)
               txtMaskinforare.delete('1.0', 'end')
               txtMaskinforare.insert('end', forarnamn[0])
               txtMaskinforare.config(state=DISABLED)
          except:
               pass
          
          referenser = []     
          referenser.clear()
          if maskinInfo[40] != None:
               cursor.execute('SELECT Beskrivning FROM referens WHERE Forarid = ' + str(maskinInfo[40]) + ';')
               referenser = cursor.fetchall()
               
          try:
               if lbMaskinreferens.index("end") != 0:
                    lbMaskinreferens.delete(0, "end")
                    for x in referenser:
                         lbMaskinreferens.insert("end", x[0])
               else:
                    for x in referenser:
                         lbMaskinreferens.insert("end", x[0])
          except:
               pass

          try: 
               if maskinInfo[28] == 1:
                    cbMaskininsatserlagd.state(['selected'])
                    cbMaskininsatserlagd.state(['!disabled'])
               else:
                    cbMaskininsatserlagd.state(['!selected'])
                    cbMaskininsatserlagd.state(['!disabled'])
          except:
               pass
          
          try:
               if maskinInfo[36] == 1:
                    cbMaskinregummerade.state(['selected'])
                    cbMaskinregummerade.state(['!disabled'])
               else:
                    cbMaskinregummerade.state(['!selected'])
                    cbMaskinregummerade.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[35] == 1:
                    cbMaskinregummerbara.state(['selected'])
                    cbMaskinregummerbara.state(['!disabled'])
               else:
                    cbMaskinregummerbara.state(['!selected'])
                    cbMaskinregummerbara.state(['!disabled'])
          except:
               pass

          try:
               if maskinInfo[3] == 1:
                    cbMaskinKollektivforsakring.state(['selected'])
                    cbMaskinKollektivforsakring.state(['!disabled'])
               else:
                    cbMaskinKollektivforsakring.state(['!selected'])
                    cbMaskinKollektivforsakring.state(['!disabled'])
          except:
               pass

          cursor.execute('SELECT Tillbehor FROM tillbehor WHERE Maskinnummer = ' + str(maskinnummer) + ';')
          tillbehor = cursor.fetchall()
     
          if lbMaskintillbehor.index("end") != 0:
               lbMaskintillbehor.delete(0, "end")
               for x in tillbehor:
                    lbMaskintillbehor.insert("end", x[0])
          else:
               for x in tillbehor:
                    lbMaskintillbehor.insert("end", x[0])
          
          cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
          maskiner = cursor.fetchall()

          if LbDelagaresMaskiner.index("end") != 0:
               LbDelagaresMaskiner.delete(0, "end")
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)
          else:
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)    

def fyllListboxDelagare():

     cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn FROM foretagsregister")
     delagareLista = []
     delagareLista = cursor.fetchall()
     LbDelagare.delete(0, 'end')
     for item in delagareLista:
         for item in delagareLista:
               item = list(item)
               if item[1] == None:
                    item[1] = ""
               if item[2] == None:
                    item[2] = ""
               s=""
               s += str(item[0])
               s+= " "
               s+=str(item[1])
               s+= " "
               s+=str(item[2])                              
               
               LbDelagare.insert("end", s)

def fetchMaskiner(self):
     global medlemsnummer

     selectedDelagare = LbDelagare.get(LbDelagare.curselection())
     indexSpace = selectedDelagare.index(" ")
     stringSelectedDelagare = str(selectedDelagare[0:indexSpace])
     delagare = "".join(stringSelectedDelagare)
     medlemsnummer = delagare
     cursor.execute('SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Medlemsnummer = ' + delagare + ';')
     result = cursor.fetchall()
        
     if LbMaskiner.index("end") != 0:
          LbMaskiner.delete(0, "end")
          for x in result:
               s=""
               s += str(x[0])
               s+= " "
               s+=str(x[1])                              
               LbMaskiner.insert("end",s )
     else:
          for x in result:
               s=""
               s += str(x[0])
               s+= " "
               s+=str(x[1])                              
               LbMaskiner.insert("end",s )

     fyllDelagarInfo()

def fyllDelagarInfo():
          global medlemsnummer

          cursor.execute('SELECT medlemsnummer, foretagsnamn, fornamn, efternamn, gatuadress, postnummer, postadress, telefon FROM foretagsregister WHERE medlemsnummer = ' + medlemsnummer + ';')
          delagarInfo = cursor.fetchone()
          delagarInfo = list(delagarInfo)

          #sätter delägaresidans info

          txtMedlemsnummerDelagare.delete('1.0', 'end')
          txtMedlemsnummerDelagare.insert('end', delagarInfo[0])
          
          txtForetag.config(state=NORMAL)
          txtForetag.delete('1.0', 'end')
          txtForetag.insert('end', delagarInfo[1])
          txtForetag.config(state=DISABLED)

          txtFornamn.config(state=NORMAL)
          txtFornamn.delete('1.0', 'end')
          txtFornamn.insert('end', delagarInfo[2])
          txtFornamn.config(state=DISABLED)

          txtEfternamn.config(state=NORMAL)
          txtEfternamn.delete('1.0', 'end')
          txtEfternamn.insert('end', delagarInfo[3])
          txtEfternamn.config(state=DISABLED)

          txtAdress.config(state=NORMAL)
          txtAdress.delete('1.0', 'end')
          txtAdress.insert('end', delagarInfo[4])
          txtAdress.config(state=DISABLED)

          txtPostnummer.config(state=NORMAL)
          txtPostnummer.delete('1.0', 'end')
          txtPostnummer.insert('end', delagarInfo[5])
          txtPostnummer.config(state=DISABLED)

          txtPostadress.config(state=NORMAL)
          txtPostadress.delete('1.0', 'end')
          txtPostadress.insert('end', delagarInfo[6])
          txtPostadress.config(state=DISABLED)

          try:
               txtTelefon.config(state=NORMAL)
               txtTelefon.delete('1.0', 'end')
               txtTelefon.insert('end', delagarInfo[7])
               txtTelefon.config(state=DISABLED)
          except:
               pass

def tomMaskinInfo():
     
          txtMaskinnummermaskininfo.config(state=NORMAL)
          txtMaskinnummermaskininfo.delete('1.0', 'end')
          txtMaskinnummermaskininfo.config(state=DISABLED)

          txtMaskinbeteckning.config(state=NORMAL)
          txtMaskinbeteckning.delete('1.0', 'end')
          txtMaskinbeteckning.config(state=DISABLED)

          txtMaskinme_klass.config(state=NORMAL)
          txtMaskinme_klass.delete('1.0', 'end')
          txtMaskinme_klass.config(state=DISABLED)

          txtMaskinmotorfabrikat.config(state=NORMAL)
          txtMaskinmotorfabrikat.delete('1.0', 'end')
          txtMaskinmotorfabrikat.config(state=DISABLED)

          txtMaskinmotortyp.config(state=NORMAL)
          txtMaskinmotortyp.delete('1.0', 'end')
          txtMaskinmotortyp.config(state=DISABLED)

          txtMaskinmotor.config(state=NORMAL)
          txtMaskinmotor.delete('1.0', 'end')
          txtMaskinmotor.config(state=DISABLED)

          txtMaskinvaxellada.config(state=NORMAL)
          txtMaskinvaxellada.delete('1.0', 'end')
          txtMaskinvaxellada.config(state=DISABLED)

          txtMaskinhydraulsystem.config(state=NORMAL)
          txtMaskinhydraulsystem.delete('1.0', 'end')
          txtMaskinhydraulsystem.config(state=DISABLED)

          txtMaskinkylvatska.config(state=NORMAL)
          txtMaskinkylvatska.delete('1.0', 'end')
          txtMaskinkylvatska.config(state=DISABLED)

          txtMaskinmotoreffekt.config(state=NORMAL)
          txtMaskinmotoreffekt.delete('1.0', 'end')
          txtMaskinmotoreffekt.config(state=DISABLED)

          txtMaskinmotorvarmare.config(state=NORMAL)
          txtMaskinmotorvarmare.delete('1.0', 'end')
          txtMaskinmotorvarmare.config(state=DISABLED)

          txtMaskinkatalysator.config(state=NORMAL)
          txtMaskinkatalysator.delete('1.0', 'end')
          txtMaskinkatalysator.config(state=DISABLED)

          txtMaskinpartikelfilter.config(state=NORMAL)
          txtMaskinpartikelfilter.delete('1.0', 'end')
          txtMaskinpartikelfilter.config(state=DISABLED)

          txtMaskinvattenbaseradlack.config(state=NORMAL)
          txtMaskinvattenbaseradlack.delete('1.0', 'end')
          txtMaskinvattenbaseradlack.config(state=DISABLED)

          txtMaskinkylmedia.config(state=NORMAL)
          txtMaskinkylmedia.delete('1.0', 'end')
          txtMaskinkylmedia.config(state=DISABLED)

          txtMaskinbullernivautv.config(state=NORMAL)
          txtMaskinbullernivautv.delete('1.0', 'end')
          txtMaskinbullernivautv.config(state=DISABLED)

          txtMaskinbullernivainv.config(state=NORMAL)
          txtMaskinbullernivainv.delete('1.0', 'end')
          txtMaskinbullernivainv.config(state=DISABLED)

          txtMaskinsmorjfett.config(state=NORMAL)
          txtMaskinsmorjfett.delete('1.0', 'end')
          txtMaskinsmorjfett.config(state=DISABLED)

          txtMaskinBatterityp.config(state=NORMAL)
          txtMaskinBatterityp.delete('1.0', 'end')
          txtMaskinBatterityp.config(state=DISABLED)

          txtMaskinperiod.config(state=NORMAL)
          txtMaskinperiod.delete('1.0', 'end')
          txtMaskinperiod.config(state=DISABLED)

          txtMaskinarsbelopp.config(state=NORMAL)
          txtMaskinarsbelopp.delete('1.0', 'end')
          txtMaskinarsbelopp.config(state=DISABLED)

          txtMaskinmiljostatus.config(state=NORMAL)
          txtMaskinmiljostatus.delete('1.0', 'end')
          txtMaskinmiljostatus.config(state=DISABLED)

          txtMaskinarsmodell.config(state=NORMAL)
          txtMaskinarsmodell.delete('1.0', 'end')
          txtMaskinarsmodell.config(state=DISABLED)

          txtMaskinregistreringsnummer.config(state=NORMAL)
          txtMaskinregistreringsnummer.delete('1.0', 'end')
          txtMaskinregistreringsnummer.config(state=DISABLED)

          txtMaskintyp.config(state=NORMAL)
          txtMaskintyp.delete('1.0', 'end')
          txtMaskintyp.config(state=DISABLED)

          txtMaskinmotoroljevolym.config(state=NORMAL)
          txtMaskinmotoroljevolym.delete('1.0', 'end')
          txtMaskinmotoroljevolym.config(state=DISABLED)

          txtMaskinvaxelladevolym.config(state=NORMAL)
          txtMaskinvaxelladevolym.delete('1.0', 'end')
          txtMaskinvaxelladevolym.config(state=DISABLED)

          txtMaskinhydraulsystemvolym.config(state=NORMAL)
          txtMaskinhydraulsystemvolym.delete('1.0', 'end')
          txtMaskinhydraulsystemvolym.config(state=DISABLED)

          txtMaskinkylvatskavolym.config(state=NORMAL)
          txtMaskinkylvatskavolym.delete('1.0', 'end')
          txtMaskinkylvatskavolym.config(state=DISABLED)

          txtMaskinbransle.config(state=NORMAL)
          txtMaskinbransle.delete('1.0', 'end')
          txtMaskinbransle.config(state=DISABLED)

          txtMaskindackfabrikat.config(state=NORMAL)
          txtMaskindackfabrikat.delete('1.0', 'end')
          txtMaskindackfabrikat.config(state=DISABLED)

          txtMaskindimension.config(state=NORMAL)
          txtMaskindimension.delete('1.0', 'end')
          txtMaskindimension.config(state=DISABLED)

          txtMaskingasolanlaggning.config(state=NORMAL)
          txtMaskingasolanlaggning.delete('1.0', 'end')
          txtMaskingasolanlaggning.config(state=DISABLED)

          txtMaskinSaneringsvatska.config(state=NORMAL)
          txtMaskinSaneringsvatska.delete('1.0', 'end')
          txtMaskinSaneringsvatska.config(state=DISABLED)

          txtMaskinforare.config(state=NORMAL)
          txtMaskinforare.delete('1.0', 'end')
          txtMaskinforare.config(state=DISABLED)

          cbMaskininsatserlagd.state(['!selected'])
          cbMaskininsatserlagd.state(['disabled'])

          cbMaskinregummerade.state(['!selected'])
          cbMaskinregummerade.state(['disabled'])

          cbMaskinregummerbara.state(['!selected'])
          cbMaskinregummerbara.state(['disabled'])

          cbMaskinKollektivforsakring.state(['!selected'])
          cbMaskinKollektivforsakring.state(['disabled'])

          lbMaskinreferens.delete(0, "end")
          lbMaskintillbehor.delete(0, "end")

def tomDelagareInfo():
          
          txtMedlemsnummerDelagare.delete('1.0', 'end')
          
          txtForetag.config(state=NORMAL)
          txtForetag.delete('1.0', 'end')
          txtForetag.config(state=DISABLED)

          txtFornamn.config(state=NORMAL)
          txtFornamn.delete('1.0', 'end')
          txtFornamn.config(state=DISABLED)

          txtEfternamn.config(state=NORMAL)
          txtEfternamn.delete('1.0', 'end')
          txtEfternamn.config(state=DISABLED)

          txtAdress.config(state=NORMAL)
          txtAdress.delete('1.0', 'end')
          txtAdress.config(state=DISABLED)

          txtPostnummer.config(state=NORMAL)
          txtPostnummer.delete('1.0', 'end')
          txtPostnummer.config(state=DISABLED)

          txtPostadress.config(state=NORMAL)
          txtPostadress.delete('1.0', 'end')
          txtPostadress.config(state=DISABLED)

          txtTelefon.config(state=NORMAL)
          txtTelefon.delete('1.0', 'end')
          txtTelefon.config(state=DISABLED)   

def taBortMaskin():
     global maskinnummer, medlemsnummer

     response = messagebox.askyesno("Varning!", "Är du säker på att du vill ta bort maskin nr. " + str(maskinnummer) + "?")
     if response == 1:          
          cursor.execute("DELETE FROM maskinregister WHERE Maskinnummer = " + str(maskinnummer) + ";")
          db.commit() 
          hamtaDelagarensMaskiner()
     else:
          pass

def hamtaDelagarensMaskiner():
     global medlemsnummer
     
     cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
     maskiner = cursor.fetchall()
     LbDelagaresMaskiner.selection_clear(0, "end")
     if LbDelagaresMaskiner.index("end") != 0:
          LbDelagaresMaskiner.delete(0, "end")
          for x in maskiner:
               LbDelagaresMaskiner.insert("end", x)
     else:
          for x in maskiner:
               LbDelagaresMaskiner.insert("end", x)   
     LbDelagaresMaskiner.selection_set(0)
     maskinnummer = LbDelagaresMaskiner.get(0)
     maskinnummer = maskinnummer[0]
     tomMaskinInfo()
     fyllMaskinInfoIgen(maskinnummer)
     
def hamtaDelagare(medlemsnr):
     global medlemsnummer

     medlemsnummer = medlemsnr

     fyllDelagarInfo()
     hamtaDelagarensMaskiner()

def historikFonster():

     historikFonster = Toplevel(root)

     historikFonster.title("Historik")

     historikFonster.geometry("475x280")

     def hamtaHistorik():

          cursor.execute('SELECT Maskinnummer, Beteckning, Registreringsnummer, ME_klass, Datum FROM historik')
          result = cursor.fetchall()
          
          count = 0
          
          #LbHistorik.delete(0, "end")
          for x in result:                           
               LbHistorik.insert(parent='', index="end", iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4]))
               count += 1
          #else:
          #     for x in result:                   
          #          LbHistorik.insert("end", x)


     LbHistorik = ttk.Treeview(historikFonster)
     LbHistorik.grid(row=1, column=1, padx=(10,0), pady=(10,0))
     LbHistorik['columns'] = ("Maskinnummer", "Beteckning", "Reg.nr", "ME-klass", "Datum")
     LbHistorik.column('#0', width=0)
     LbHistorik.column("Maskinnummer", anchor=W, width=65)
     LbHistorik.column("Beteckning", anchor=W, width=125)
     LbHistorik.column("Reg.nr", anchor=W, width=75)
     LbHistorik.column("ME-klass", anchor=W, width=75)
     LbHistorik.column("Datum", anchor=W, width=100)

     LbHistorik.heading('#0', text="")
     LbHistorik.heading("Maskinnummer", text="Maskinnr.", anchor=W)
     LbHistorik.heading("Beteckning", text="Beteckning", anchor=W)
     LbHistorik.heading("Reg.nr", text="Reg.nr", anchor=W)
     LbHistorik.heading("ME-klass", text="ME-klass", anchor=W)
     LbHistorik.heading("Datum", text="Datum", anchor=W)

     btnTaBortHistorik = Button(historikFonster, text="Ta bort")
     btnTaBortHistorik.grid(row=2, column=1, sticky=E, pady=(5,0))

     hamtaHistorik()


# skapar en databasanslutning
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "sennaa66",
     database = "tschakt"
)
cursor = db.cursor()

# skapar och namnger fönster samt bestämmer storlek på fönstret
root = Tk()
root.title("T-schakts delägarregister")
root.geometry("1310x750")
 
#tabs?#

tabControl = ttk.Notebook(root)
home = ttk.Frame(tabControl)
delagare = ttk.Frame(tabControl)
tabControl.add(home, text='Home')
tabControl.add(delagare, text='Delägare')
tabControl.grid(column=0, row=0)


#variables

medlemsnummer = ""
maskinnummer = ""

#skapar textfält och textboxar
EntMedlemsnummer = Entry(home, width=20, text = "Medlemsnummer") 
EntMedlemsnummer.grid(row=1, column=1, pady = 10)
EntMedlemsnummer.insert(0,"Medlemsnummer")
EntMedlemsnummer.bind("<FocusIn>", lambda args: EntMedlemsnummer.delete('0', 'end'))

EntMaskinnummer = Entry(home, width=20, text ="Maskinnummer") 
EntMaskinnummer.grid(row=1, column=3)
EntMaskinnummer.insert(0, "Maskinnummer")
EntMaskinnummer.bind("<FocusIn>", lambda args: EntMaskinnummer.delete('0', 'end'))

BtnMedlemsnummerSok = Button(home, text = "Sök", width = 5, height = 1) 
BtnMedlemsnummerSok.grid (row = 1, column = 2, sticky ="w")

BtnMaskinnummerSok = Button (home, text="Sök", width=5, height = 1, command= lambda: clickButton()) 
BtnMaskinnummerSok.grid(row=1, column=4, sticky ="w")

BtnNyDelagare = Button (home, text ="Ny delägare", height = 1, command = lambda: nyDelagare("Ny"))
BtnNyDelagare.grid(row = 2, column = 5, padx= 10, sticky="n")

BtnRapport = Button (home, text = "Rapport", width = 9, height = 1, command = clickButton)
BtnRapport.grid(row = 2, column =5, sticky = N, pady=(50, 50))

BtnUppdateraForsakring = Button (home, text="Uppdatera försäkring", height = 1, command = clickButton)
BtnUppdateraForsakring.grid(row = 2, column = 5, sticky = N, pady=(100, 50))

BtnInstallningar = Button (home, text ="Inställningar", command = clickButton)
BtnInstallningar.grid(row = 2, column =5, stick = N, pady=(150, 50))

# skapar en listbox
LbDelagare = Listbox(home, width = 50, height = 25, exportselection=0)
LbDelagare.grid(row = 2, column = 1, columnspan = 2, rowspan = 2, padx=(5,10))
LbDelagare.bind('<<ListboxSelect>>', fetchMaskiner)

LbMaskiner = Listbox(home, width = 50, height = 25, exportselection=0)
LbMaskiner.grid(row = 2, column = 3, columnspan = 2, rowspan = 2)
LbMaskiner.bind('<Double-Button>', fyllMaskinInfo)

# skapar en scrollbar
ScbDelagare = Scrollbar(home, orient="vertical")
ScbDelagare.grid(row = 2, column = 2, sticky = N+S+E, rowspan = 2)
ScbDelagare.config(command =LbDelagare.yview)

ScbDMaskiner = Scrollbar(home, orient="vertical")
ScbDMaskiner.grid(row = 2, column = 4, sticky = N+S+E, rowspan = 2)
ScbDMaskiner.config(command =LbMaskiner.yview)

LbDelagare.config(yscrollcommand=ScbDelagare.set)
LbMaskiner.config(yscrollcommand=ScbDMaskiner.set)


#frames

delagare.columnconfigure(1, weight=1)
delagare.rowconfigure(0, weight=1)

frameDelagare = Frame(delagare)
frameDelagare.grid(row = 0, column = 0, sticky = NW, padx=(10,0), pady=(10,0))
frameMaskiner= Frame(delagare)
frameMaskiner.grid(row = 1, column =0, sticky = N+E+W, padx=(10,0), pady=(10,0))
frameOvrigText= Frame(delagare)
frameOvrigText.grid(row=2, column=0, sticky=NSEW, padx=(10,0), pady=(10,0))
frameMaskininfo = Frame(delagare)
frameMaskininfo.grid(row = 0, column =1, rowspan = 3, sticky = NSEW, pady=(10,0))

#Listbox, maskiner tillhörande delägare
LbDelagaresMaskiner = Listbox(frameMaskiner, width = 45, height = 12, exportselection=0)
LbDelagaresMaskiner.grid(row = 0, column = 0)
LbDelagaresMaskiner.grid_rowconfigure(1, weight=1)
LbDelagaresMaskiner.grid_columnconfigure(0, weight=1)
LbDelagaresMaskiner.bind('<<ListboxSelect>>', fyllMaskinInfoIgen)

#Scrollbar
ScbLbDelagaresMaskiner = Scrollbar(frameMaskiner, orient="vertical")
ScbLbDelagaresMaskiner.grid(row = 0, column = 0, sticky = N+S+E)
ScbLbDelagaresMaskiner.config(command =LbMaskiner.yview)

LbDelagaresMaskiner.config(yscrollcommand=ScbLbDelagaresMaskiner.set)

#Maskinbild
img = Image.open("c:/filer/OTAD/OTAD/1.jpg")  
img = img.resize((225,200), Image. ANTIALIAS)
img2 = ImageTk.PhotoImage(img)
img_label = Label(frameOvrigText, image=img2)
img_label.grid(row=0, column=0, sticky = NW)

#Delägareinfo

lblMedlemsnummer = Label(frameDelagare, text = "Medlemsnr.")
lblMedlemsnummer.grid(row = 1, column = 0, sticky=W, pady=(0,8))
txtMedlemsnummerDelagare = Text(frameDelagare, width = 5, height=0.1)
txtMedlemsnummerDelagare.grid(row = 1, column =1, sticky = W)

entSokMedlem = Entry(frameDelagare, width = 5)
entSokMedlem.grid(row = 1, column =1, sticky=E, padx=(40, 40))
btnSokMedlem = Button(frameDelagare, text = "Sök", command= lambda: hamtaDelagare(entSokMedlem.get()))
btnSokMedlem.grid(row =1, column = 1, sticky=E)

lblForetag = Label(frameDelagare, text = "Företag")
lblForetag.grid(row = 2, column = 0, sticky=W, pady=(0,8))
txtForetag = Text(frameDelagare, width = 25, height=0.1)
txtForetag.grid(row = 2, column =1, sticky = W)

lblFornamn = Label(frameDelagare, text = "Förnamn")
lblFornamn.grid(row = 3, column = 0, sticky=W, pady=(0,8))
txtFornamn = Text(frameDelagare, width = 25, height=0.1)
txtFornamn.grid(row = 3, column =1, sticky = W)

lblEfternamn = Label(frameDelagare, text = "Efternamn")
lblEfternamn.grid(row = 4, column = 0, sticky=W, pady=(0,8))
txtEfternamn = Text(frameDelagare, width = 25, height=0.1)
txtEfternamn.grid(row = 4, column =1, sticky = W)

lblAdress = Label(frameDelagare, text = "Adress")
lblAdress.grid(row = 5, column = 0, sticky=W, pady=(0,8))
txtAdress = Text(frameDelagare, width = 25, height=0.1)
txtAdress.grid(row = 5, column =1, sticky = W)

lblPostnummer = Label(frameDelagare, text = "Postnummer")
lblPostnummer.grid(row = 6, column = 0, sticky=W, pady=(0,8))
txtPostnummer = Text(frameDelagare, width = 25, height=0.1)
txtPostnummer.grid(row = 6, column =1, sticky = W)

lblPostadress = Label(frameDelagare, text = "Ort")
lblPostadress.grid(row = 7, column = 0, sticky=W, pady=(0,8))
txtPostadress = Text(frameDelagare, width = 25, height=0.1)
txtPostadress.grid(row = 7, column =1, sticky = W)

lblTelefon = Label(frameDelagare, text = "Telefon")
lblTelefon.grid(row = 8, column = 0, sticky=W, pady=(0,8))
txtTelefon = Text(frameDelagare, width = 25, height=0.1)
txtTelefon.grid(row = 8, column =1, sticky = W)

btnAndraDelagare = Button(frameDelagare, text ="Ändra", command = lambda: nyDelagare("Ändra"))
btnAndraDelagare.grid(row=9, column=1, sticky=W, padx=(100,0))

btnTaBortDelagare = Button(frameDelagare, text="Ta bort", command = lambda: taBortDelagare())
btnTaBortDelagare.grid(row=9, column =1, sticky=E)

#Maskininfo

lblMaskinnummermaskininfo = Label(frameMaskininfo, text= "Maskinnummer")
lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinnummermaskininfo = Text(frameMaskininfo, width = 5, height=0.1)
txtMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0))

lblMaskinbeteckning = Label(frameMaskininfo, text="Beteckning")
lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbeteckning = Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))


lblMaskinme_klass = Label(frameMaskininfo, text="ME-Klass")
lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinme_klass = Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))


lblMaskinmotorfabrikat = Label(frameMaskininfo, text="Motorfabrikat")
lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotorfabrikat = Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))


lblMaskinmotortyp = Label(frameMaskininfo, text="Motortyp")
lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotortyp=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))


lblMaskinmotor = Label(frameMaskininfo, text="Motor")
lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotor = Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))


lblMaskinvaxellada = Label(frameMaskininfo, text="Växellåda")
lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinvaxellada=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))


lblMaskinhydraulsystem = Label(frameMaskininfo, text="Hydraulsystem")
lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinhydraulsystem=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))


lblMaskinkylvatska = Label(frameMaskininfo, text="Kylvätska")
lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinkylvatska=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))


lblMaskinmotoreffekt = Label(frameMaskininfo, text="Motoreffekt/KW")
lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotoreffekt=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))

lblMaskinmotorvarmare = Label(frameMaskininfo, text="Motorvärmare")
lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
#txtMaskinmotorvarmare=Text(frameMaskininfo, width = 25, height=0.1)
#txtMaskinmotorvarmare.grid(column=1, row=10, sticky=W, padx=(10,0))
cbMaskinmotorvarmare = ttk.Checkbutton(frameMaskininfo)
cbMaskinmotorvarmare.state(['!alternate', '!selected', 'disabled'])
cbMaskinmotorvarmare.grid(column = 1, row = 10, sticky = W, padx=(5,0))

lblMaskinkatalysator = Label(frameMaskininfo, text="Katalysator")
lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
#txtMaskinkatalysator=Text(frameMaskininfo, width = 25, height=0.1)
#txtMaskinkatalysator.grid(column=1,row=11, sticky=W, padx=(10,0))
cbMaskinkatalysator = ttk.Checkbutton(frameMaskininfo)
cbMaskinkatalysator.state(['!alternate', '!selected', 'disabled'])
cbMaskinkatalysator.grid(column = 1, row = 11, sticky = W, padx=(5,0))

lblMaskinpartikelfilter = Label(frameMaskininfo, text="Partikelfilter")
lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
#txtMaskinpartikelfilter=Text(frameMaskininfo, width = 25, height=0.1)
#txtMaskinpartikelfilter.grid(column=1,row=12, sticky=W, padx=(10,0))
cbMaskinpartikelfilter = ttk.Checkbutton(frameMaskininfo)
cbMaskinpartikelfilter.state(['!alternate', '!selected', 'disabled'])
cbMaskinpartikelfilter.grid(column = 1, row = 12, sticky = W, padx=(5,0))

lblMaskinvattenbaseradlack = Label(frameMaskininfo, text="Vattenbaserad lack")
lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
#txtMaskinvattenbaseradlack=Text(frameMaskininfo, width = 25, height=0.1)
#txtMaskinvattenbaseradlack.grid(column=1, row=13, sticky=W, padx=(10,0))
cbMaskinvattenbaseradlack = ttk.Checkbutton(frameMaskininfo)
cbMaskinvattenbaseradlack.state(['!alternate', '!selected', 'disabled'])
cbMaskinvattenbaseradlack.grid(column = 1, row = 13, sticky = W, padx=(5,0))

lblMaskinkylmedia = Label(frameMaskininfo, text="Kylmedia")
lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinkylmedia=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))

lblMaskinbullernivautv = Label(frameMaskininfo, text="Bullernivå utvändigt")
lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbullernivautv=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))

lblMaskinbullernivainv = Label(frameMaskininfo, text="Bullernivå invändigt")
lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbullernivainv=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))

lblMaskinsmorjfett = Label(frameMaskininfo, text="Smörjfett")
lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinsmorjfett=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))

lblMaskinBatterityp = Label(frameMaskininfo, text="Batterityp")
lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinBatterityp=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))

#checkbox
lblMaskinKollektivforsakring = Label(frameMaskininfo, text="Kollektiv försäkring")
lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinKollektivforsakring = ttk.Checkbutton(frameMaskininfo)
cbMaskinKollektivforsakring.state(['!alternate', '!selected', 'disabled'])
cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

lblMaskinperiod = Label(frameMaskininfo, text="Period")
lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinperiod=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinperiod.grid(column=1, row=20, sticky=W, padx=(10,0))

lblMaskinarsbelopp = Label(frameMaskininfo, text="Årsbelopp")
lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinarsbelopp=Text(frameMaskininfo, width = 25, height=0.1)
txtMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))

#Buttons

btnMaskinpresentation=Button(frameMaskininfo,text="Maskinpresentation", command = lambda: maskinpresentation())
btnMaskinpresentation.grid(column=0, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnMiljodeklaration=Button(frameMaskininfo, text="Miljödeklaration", command = lambda: miljodeklaration())
btnMiljodeklaration.grid(column=1, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnHistorik=Button(frameMaskininfo, text="Historik", command = lambda: historikFonster())
btnHistorik.grid(column=6, row=0, sticky=W, padx=(10,10))

btnLaggtillmaskin=Button(frameMaskininfo, text="Lägg till ny", command = lambda: nyMaskinFonster("Ny"))
btnLaggtillmaskin.grid(column=4, row=22, sticky=W, pady=(20,0))

btnAndramaskin=Button(frameMaskininfo, text="Ändra", command = lambda: nyMaskinFonster(txtMaskinnummermaskininfo.get('1.0', 'end')))
btnAndramaskin.grid(column=4, row=22,sticky=E, pady=(20,0))

btnBytmaskin=Button(frameMaskininfo, text="Byt maskin", command = lambda: nyMaskinFonster("Byt"))
btnBytmaskin.grid(column=5, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnTabortmaskin=Button(frameMaskininfo, text="Ta bort maskin", command  = lambda: taBortMaskin())
btnTabortmaskin.grid(column=5, row=22, sticky=E, pady=(20,0))



#--------------------

lblMaskinmiljostatus = Label(frameMaskininfo, text="Miljöstatus")
lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0))
txtMaskinmiljostatus=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0))

lblMaskinarsmodell = Label(frameMaskininfo, text="Årsmodell")
lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
txtMaskinarsmodell=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))

lblMaskinregistreringsnummer = Label(frameMaskininfo, text="Reg. nr/Ser. nr")
lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
txtMaskinregistreringsnummer=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))

lblMaskintyp = Label(frameMaskininfo, text="Maskintyp")
lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
txtMaskintyp=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))

lblMaskinmotoroljevolym  = Label(frameMaskininfo, text="Motorolja volym/liter")
lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
txtMaskinmotoroljevolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))

lblMaskinvaxelladevolym = Label(frameMaskininfo, text="Växellåda volym/liter")
lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
txtMaskinvaxelladevolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))

lblMaskinhydraulsystemvolym = Label(frameMaskininfo, text="Hydraul volym/liter")
lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
txtMaskinhydraulsystemvolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))

lblMaskinkylvatskavolym = Label(frameMaskininfo, text="Kylvätska volym/liter")
lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
txtMaskinkylvatskavolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))

#Textruta, fält för Övrig Text
lblOvrigtext = Label(frameMaskininfo, text="Övrig text")
lblOvrigtext.grid(column=2, row=9, sticky=W, padx=(10,0))
TxtOvrigtext = Text(frameMaskininfo, width = 20, height=4)
TxtOvrigtext.grid(row=10, column=2, columnspan=2, rowspan=3, sticky=NSEW, padx=(10,15))

#Scrollbar
ScbTxtOvrigText = Scrollbar(frameMaskininfo, orient="vertical")
ScbTxtOvrigText.grid(row = 10, column = 3, sticky = N+S+E, rowspan = 3)
ScbTxtOvrigText.config(command =TxtOvrigtext.yview)

TxtOvrigtext.config(yscrollcommand=ScbTxtOvrigText.set)

#------------------------

lblMaskinbransle = Label(frameMaskininfo, text="Bränsle")
lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0))
txtMaskinbransle=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0))

lblMaskindackfabrikat = Label(frameMaskininfo, text="Däckfabrikat")
lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
txtMaskindackfabrikat=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))

lblMaskindimension = Label(frameMaskininfo, text="Dimension/typ")
lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
txtMaskindimension=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))

#Checkbox
lblMaskinregummerbara = Label(frameMaskininfo, text="Regummerbara")
lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
cbMaskinregummerbara = ttk.Checkbutton(frameMaskininfo)
cbMaskinregummerbara.state(['!alternate', '!selected', 'disabled'])
cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

#Checkbox
lblMaskinregummerade = Label(frameMaskininfo, text="Regummerade")
lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
cbMaskinregummerade = ttk.Checkbutton(frameMaskininfo)
cbMaskinregummerade.state(['!alternate', '!selected', 'disabled'])
cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

lblMaskingasolanlaggning = Label(frameMaskininfo, text="Gasolanläggning")
lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
#txtMaskingasolanlaggning=Text(frameMaskininfo, width = 20, height=0.1)
#txtMaskingasolanlaggning.grid(column=5, row=5, sticky=W, padx=(10,0))
cbMaskingasolanlaggning = ttk.Checkbutton(frameMaskininfo)
cbMaskingasolanlaggning.state(['!alternate', '!selected', 'disabled'])
cbMaskingasolanlaggning.grid(column = 5, row = 5, sticky = W, padx=(5,0))

lblMaskinSaneringsvatska = Label(frameMaskininfo, text="Saneringsvätska")
lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
#txtMaskinSaneringsvatska=Text(frameMaskininfo, width = 20, height=0.1)
#txtMaskinSaneringsvatska.grid(column=5, row=6, sticky=W, padx=(10,0))
cbMaskinSaneringsvatska = ttk.Checkbutton(frameMaskininfo)
cbMaskinSaneringsvatska.state(['!alternate', '!selected', 'disabled'])
cbMaskinSaneringsvatska.grid(column = 5, row = 6, sticky = W, padx=(5,0))

#Checkbox
lblMaskininsattserlagd = Label(frameMaskininfo, text="Maskininsats erlagd")
lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
cbMaskininsatserlagd = ttk.Checkbutton(frameMaskininfo)
cbMaskininsatserlagd.state(['!alternate', '!selected', 'disabled'])
cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

lblMaskinforare = Label(frameMaskininfo, text="Förare")
lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
txtMaskinforare=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))



lblMaskinreferens = Label(frameMaskininfo, text="Referensjobb")
lblMaskinreferens.grid(column=4, row=9, sticky =W, padx=(10,0))
lbMaskinreferens=Listbox(frameMaskininfo, width = 20, height=5)
lbMaskinreferens.grid(column=4, row=10, sticky=NSEW, padx=(10,0), columnspan=2, rowspan=3)

#Scrollbar
ScbTxtMaskinreferens = Scrollbar(frameMaskininfo, orient="vertical")
ScbTxtMaskinreferens.grid(row = 10, column = 6, sticky = W+N+S, rowspan = 3)
ScbTxtMaskinreferens.config(command =LbMaskiner.yview)

lbMaskinreferens.config(yscrollcommand=ScbTxtMaskinreferens.set)

#Listbox
lblMaskintillbehor = Label(frameMaskininfo, text="Tillbehör")
lblMaskintillbehor.grid(column=4, row=14, sticky = W, padx=(10,0))
lbMaskintillbehor=Listbox(frameMaskininfo)
lbMaskintillbehor.grid(column=4, row=15, rowspan=6, columnspan=2,sticky=NSEW, padx=(10,0))

#Scrollbar
ScbLbMaskintillbehor = Scrollbar(frameMaskininfo, orient="vertical")
ScbLbMaskintillbehor.grid(row = 15, column = 6, sticky = N+W+S, rowspan = 6)
ScbLbMaskintillbehor.config(command =lbMaskintillbehor.yview)

lbMaskintillbehor.config(yscrollcommand=ScbLbMaskintillbehor.set)

cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn FROM foretagsregister")
delagareLista = cursor.fetchall()
delagareLista = list(delagareLista)

if LbDelagare.index("end") == 0:
     for item in delagareLista:
          item = list(item)
          if item[1] == None:
               item[1] = ""
          if item[2] == None:
               item[2] = ""

          s=""
          s += str(item[0])
          s+= " "
          s+=str(item[1])
          s+= " "
          s+=str(item[2])                              
          
          LbDelagare.insert("end", s)


# kör fönstret
root.mainloop()