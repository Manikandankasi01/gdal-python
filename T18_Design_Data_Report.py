from osgeo import ogr
import checkCount

def readMapInfoFilesLayer(boundary,tableFile) :
    input_file1=boundary
    input_file2=tableFile
    driver = ogr.GetDriverByName("MapInfo File")
    #open boundary table
    boundary_Table=driver.Open(input_file1,0)
    boundary_Layer=boundary_Table.GetLayer()
    #open table
    table = driver.Open(input_file2, 0)
    layer = table.GetLayer()
    row_Count=layer.GetFeatureCount()
    networkEntities={}
    #store assets into Dictionary
    for tableLayer in layer:
        tId = tableLayer.GetField("id")
	rowObject=tableLayer.GetGeometryRef()
	objLine=str(rowObject)
	networkEntities[tId]=objLine
    #looping Boundary Layer
    for boundaryLayer in boundary_Layer:
        boundary_Type=boundaryLayer.GetField("Type")
        boundary_Id=str(boundaryLayer.GetField("id"))
        
        #Get Asset count within SAM level
        if boundary_Type=="ESA": 
            samObject=boundaryLayer.GetGeometryRef()
            asset_CountWithinLayer=checkCount.assetCountWithinLayer(samObject,row_Count,networkEntities)
            checkCount.generateReport(asset_CountWithinLayer,boundary_Type,tableFile,boundary_Id)
            continue
        
        #Get Asset count within ESA level
        elif boundary_Type=="FSA":
            samObject=boundaryLayer.GetGeometryRef()
            asset_CountWithinLayer=checkCount.assetCountWithinLayer(samObject,row_Count,networkEntities)
            checkCount.generateReport(asset_CountWithinLayer,boundary_Type,tableFile,boundary_Id)
            continue
        #Get Asset count within NAT level  
        elif boundary_Type=="NAT":
            samObject=boundaryLayer.GetGeometryRef()
            asset_CountWithinLayer=checkCount.assetCountWithinLayer(samObject,row_Count,networkEntities)
            checkCount.generateReport(asset_CountWithinLayer,boundary_Type,tableFile,boundary_Id)
            
            continue
        #Get Asset count within FSA level
        elif boundary_Type=="SAM":
            samObject=boundaryLayer.GetGeometryRef()
            asset_CountWithinLayer=checkCount.assetCountWithinLayer(samObject,row_Count,networkEntities)
            checkCount.generateReport(asset_CountWithinLayer,boundary_Type,tableFile,boundary_Id)
            
            continue
        #Get Asset count within ADA level
        elif boundary_Type=="ADA":
            samObject=boundaryLayer.GetGeometryRef()
            asset_CountWithinLayer=checkCount.assetCountWithinLayer(samObject,row_Count,networkEntities)
            checkCount.generateReport(asset_CountWithinLayer,boundary_Type,tableFile,boundary_Id)
            
            continue
        
def openMapinfoFiles():
    print " "
    mapInfofilePath=r"C:\Python Assessment\03.Original T18 _Trimmed (DDMMYYY)"
    boundaryPath=mapInfofilePath+r"\boundary.TAB"
    structurepointPath=mapInfofilePath+r"\structurepoint.TAB"
    routePath=mapInfofilePath+r"\route.TAB"
    ductPath=mapInfofilePath+r"\duct.TAB"
    equipmentPath=mapInfofilePath+r"\equipment.TAB"
    equipmentHfcPath=mapInfofilePath+r"\equipment_hfc.TAB"
    cablePath=mapInfofilePath+r"\cable.TAB"
    tableList=[structurepointPath,routePath,ductPath,equipmentPath,equipmentHfcPath,cablePath]
    for tableName in tableList:
        readMapInfoFilesLayer(boundaryPath,tableName)
        
if __name__ == "__main__":
    openMapinfoFiles()
            
