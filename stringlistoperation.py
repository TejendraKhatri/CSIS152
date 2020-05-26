'''
This program uses several string and list operations to display a conversation properly with details including line number and number of characters in the line.
'''

__author__ = "Tejendra Khatri"
__date__ = "25/4/2017"

def main():
    max_linelength = int(input("Please enter the maximum line length you prefer:"))
    convo = '''Bernardo##Who's there?
Francisco##Nay, answer me: stand, and unfold yourself.
Bernardo##Long live the king!
Francisco##Bernardo?
Bernardo##He.
Francisco##You come most carefully upon your hour.
Bernardo##'Tis now struck twelve; get thee to bed, Francisco.
Francisco##For this relief much thanks: 'tis bitter cold, and I am sick at heart.
Bernardo##Have you had quiet guard?
Francisco##Not a mouse stirring.
Bernardo##Well, good night. If you do meet Horatio and Marcellus, the rivals of my watch, bid them make haste.
Francisco##I think I hear them. Stand, ho! Who's there?
Horatio##Friends to this ground.
Marcellus##And liegemen to the Dane.
Francisco##Give you good night.
Marcellus##O, farewell, honest soldier: Who hath relieved you?
Francisco##Bernardo has my place. Give you good night.
Marcellus##Holla! Bernardo!
Bernardo##Say, what, is Horatio there?
Horatio##A piece of him.
Bernardo##Welcome, Horatio: welcome, good Marcellus.
Marcellus##What, has this thing appear'd again to-night?
Bernardo##I have seen nothing.
Marcellus##Horatio says 'tis but our fantasy, and will not let belief take hold of him touching this dreaded sight, twice seen of us: therefore I have entreated him along with us to watch the minutes of this night; that if again this apparition come, he may approve our eyes and speak to it.
Horatio##Tush, tush, 'twill not appear.
Bernardo##Sit down awhile; and let us once again assail your ears, that are so fortified against our story what we have two nights seen.'''

    new_list = convo.split('\n')
    #print(new_list)
    integr = 1
    for lines in new_list:
        #print(eachline)
        newlines = lines.split("##")
        #print(newlines)
        names = newlines[0].upper()
        #print(names)
        final = names + " " + newlines[1]
        #print(final)
        integr = disp(final,integr,max_linelength)
        

def disp(stri,integr,max_linelength):
    '''it concatenates strings with the number of characters it possesses\ 
         along with some other characters to make it look better possessing only \
         upto a certain number of characters per line'''
    newlist = stri.split()
    newstri = ""
    #print(newlist)
    for words in newlist:
        if len(newstri)+len(words) <= max_linelength:
            newstri += " " + words
        else:
            x = str(integr).rjust(3) + "|" + newstri.strip() + "|" + str(len(newstri.strip()))
            print(x)
            integr += 1
            newstri = words
        
    newstri = str(integr).rjust(3) + "|" + newstri.strip() + "|" + str(len(newstri.strip()))
    print(newstri)
    integr += 1
    return integr


if __name__ == "__main__":
    main()
    
