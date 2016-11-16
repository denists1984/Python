def findXML():
      print ("List of available XML files: ")
      xml_list = []
      for root, dirs, files in os.walk("."):
          for file in files:
              if file.endswith(".xml"): 
                  xml_list.append(os.path.join(root, file))
      length=len(xml_list)
      for i in range(length):
          print xml_list[i]
      print
      return xml_list



def chooseXML():
      xml_file = raw_input("Please provide full path with File name from the list: ")
      return xml_file


   
def validXMLname(xml_file, xml_list):
      while True:    
            if xml_file in xml_list:
                  print ('File exists in the list')
                  ##extension = os.path.splitext(xml_name)[1]
                  extension = os.path.splitext(xml_name)[1][1:].strip()
                  print os.path.splitext(xml_file)[0]
                  #print extension
                  #print xml_file
                  return xml_file
            else:
                  print ('Can not find file in the list')
                  #extension = os.path.splitext(xml_name)[1]
                  #extension = os.path.splitext(filename)[1][1:].strip() 
                  #print extension
                  #print os.path.splitext(os.path.basename(xml_name))[2]
                  xml_file = chooseXML()


def parseXML(xml_file):
      dom = parse(xml_file)
      exp_value = raw_input("Please provide search creteria : ")
      values = dom.getElementsByTagName(exp_value)
      print
      print
      print
      return values, dom

def changeXML(values):
      print "available list: "
      for n,i in enumerate(values):
            x = ''.join(t.nodeValue for t in i.childNodes if t.nodeType == t.TEXT_NODE)
            print n,".", x
      print 
      chg_val = raw_input("Enter the value number to change: ")
      chg_val = int(chg_val)
      for i in range(len(values)):    
            i = chg_val
            values[i].firstChild.nodeValue = 'aaaaaaaaaaaaaaa'
            y = values[i].firstChild.nodeValue
      print "Changing to: ", y
      return values
      print 
      print
      print 

def saveXML(dom, xml_name): 
      file1 = open(xml_name,"wb")
      dom.writexml(file1, encoding="utf-8")
      file1.close()
      return dom



def main():
      xml_list = findXML()
      xml_file = chooseXML()
      xml_file=validXMLname(xml_file, xml_list)
      values, dom = parseXML(xml_file)
      changeXML(values)
      dom, xml_name = saveXML(dom)
      return dom
dom = main()
print dom.toxml()
