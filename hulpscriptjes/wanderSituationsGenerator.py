import textwrap
import string

#situationDimensions= (20,20)
situationDimensions= (10,10)

situationXML= textwrap.dedent("""<situation>
                        <id>${id}</id>
                        <petriNetFile>petrinets/rotterdam/fastWanderSituation.xml</petriNetFile>

                        <situationArea>
                                <x1>${x1}</x1>
                                <y1>${y1}</y1>
                                <x2>${x2}</x2>
                                <y2>${y2}</y2>
                        </situationArea>

                        <situationType>exclusive</situationType>
                        <estimatedTime>5</estimatedTime>
                </situation> """)

situationIdBase = "slowWander"
                
situationTemplate = string.Template(situationXML)


                
                
def createSituation(newId, lowerBound, higherBound):
    return situationTemplate.substitute(id=newId, x1=lowerBound[0], y1=lowerBound[1], x2=higherBound[0], y2=higherBound[1])


# TODO: Create situation xml to make situations the size of areaSize, which is, like areaStart and areaEnd, a tuple containing the x and y coordinates/dimensions. The appropriate xml will be generated to fill the area from areaStart until areaEnd with these situations.
def createSituations(situationName, areaStart, areaEnd, areaSize):
    startLocation = areaStart
    xml = ""
    
    while startLocation[0] < areaEnd[0]:
        while startLocation[1] < areaEnd[1]:
            situationId = situationName + str(startLocation)
            endLocation = (startLocation[0] + areaSize[0], startLocation[1] + areaSize[1])
            newSituation = createSituation(situationId, startLocation, endLocation)
            #print newSituation
            xml += newSituation + "\n"
            startLocation = (startLocation[0], startLocation[1] + areaSize[1])
        startLocation = (startLocation[0] + areaSize[0], areaStart[1])
            

    return xml
            
            
def main():
    xml = createSituations(situationIdBase, (0,0), (500,500), situationDimensions)
    print xml
    
if __name__ == "__main__":
    main()