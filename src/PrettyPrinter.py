spaces = '    '
space_buffer = ''

class PrettyPrinter():
  
  def incrementTab():
    global spaces 
    global space_buffer
    space_buffer = space_buffer + spaces
    
    
  def printTab():
    global space_buffer
    print(space_buffer, end='')
  
  def decrementTab():
    global space_buffer
    space_buffer = space_buffer[:-len(spaces)]