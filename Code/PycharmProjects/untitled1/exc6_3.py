song = "Εγώ μετράω τα ρέστα μου να βγάλω κι άλλο μήνα " \
       "ανοίγω και δε βλέπω ουρανό " \
       "εσύ έχεις στο πιάτο σου ολόκληρη Αθήνα " \
       "ανοίγεις και χαζεύεις το κενό"

words = song.rsplit(" ")
print("===========")
for x in sorted(words):
    print(x)
print("===========")
print('The number of words is {} \n'
      'The number of letters is {}'.format(len(words), sum(len(i) for i in words))
      )
