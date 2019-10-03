import pcbnew
import os


# the internal coorinate space of pcbnew is 10E-6 mm. (a millionth of a mm)
# the coordinate 121550000 corresponds to 121.550000 

SCALE = 1000000.0


print("pcbnew python plugin path:" + pcbnew.__file__);

#Load board file

filename = "./light-tone-pedal.kicad_pcb";
print("Loading board" + filename);

pcb_board = pcbnew.LoadBoard(filename);

pcb_board.BuildListOfNets(); # required so 'pcb' contains valid netclass data

#################
#Generate Layers#
#################

layertable = {}

numlayers = pcbnew.PCB_LAYER_ID_COUNT
for i in range(numlayers):
	layertable[i] = pcb_board.GetLayerName(i)
	print("{} {}".format(i, pcb_board.GetLayerName(i)));
	
############################
#####Create a Track#########
############################

track = pcbnew.TRACK(pcb_board)
track.SetStart(pcbnew.wxPoint(136144000, 95504000))
track.SetEnd(pcbnew.wxPoint(176144000, 95504000))
track.SetWidth(1614400)
track.SetLayer(pcbnew.F_Cu)

track.SetNetCode(pcb_board.GetNetcodeFromNetname("GND"))
pcb_board.Add(track)


###########################################
#Create a new via and add it to the board##
###########################################

newvia = pcbnew.VIA(pcb_board)
# need to add before SetNet will work, 
# so just doing it first
pcb_board.Add(newvia)

toplayer=-1
bottomlayer=pcbnew.PCB_LAYER_ID_COUNT
for l in range(pcbnew.PCB_LAYER_ID_COUNT):
   if not track.IsOnLayer(l):
      continue
   toplayer = max(toplayer, l)
   bottomlayer = min(bottomlayer, l)

# now that I have the top and bottom layers, I tell the new
# via
newvia.SetLayerPair(toplayer, bottomlayer)

position = pcbnew.wxPoint(track.GetPosition().x+SCALE,track.GetPosition().y+2*SCALE)
newvia.SetPosition(position);
newvia.SetViaType(pcbnew.VIA_THROUGH)
newvia.SetWidth(1014400)
#newvia.SetNet(tonet)

pcb_board.Add(newvia);

pcbnew.Refresh();
pcbnew.SaveBoard(filename,pcb_board);
