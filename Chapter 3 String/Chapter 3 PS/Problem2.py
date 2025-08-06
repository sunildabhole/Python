letter = ''' Dear <|NAME|>,
  You are selected!
  <|DATE|> '''

print(letter.replace("<|NAME|>","SUNIL").replace("<|DATE|>","5-Aug-25"))