# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Free-Body Diagram Example: Box on incline

# <codecell>

%%HTML
<!DOCTYPE html>
<html>
    <head>
        <style> 
            body {
                margin: 10px;
            }
            #jxgbox1 {  
                border:1px solid black; background-size: contain; background-repeat: no-repeat;
                background-position: center; background-size: 80% auto;
            }
            
        </style>

    </head>


    <body>       
        <!-- Jxg Box -->
        <div id='jxgbox1' class='jxgbox' style='width:450px; height:350px; float:left; border: solid #1f628d 2px;'></div>        
        
        <!-- Menu -->
        <div id="menu" style="width: 170px; float: left;">
              <ul>
                  Add Forces
                  <input class="btn" type="button" value="Normal" onClick="var vN = addNormal()">
                  <input class="btn" type="button" value="Gravitational" onClick="addGravitational()">
                  <input class="btn" type="button" value="Friction" onClick="addFriction()">
                  <br></br>

                  <input class="btn" type="button" value="Clear" onClick="clearAll()">
              </ul>
          </div>

        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>
            
            board = initBoard();

            function initBoard() {
                bboxlimits = [-10, 10, 10, -10];
                var board = JXG.JSXGraph.initBoard('jxgbox1', {boundingbox: bboxlimits, axis:false, showCopyright: false});
                state = {};

                N = undefined;
                vg = undefined;
                vf = undefined;

                var im = board.create('image',["https://studio.edge.edx.org/c4x/DavidsonNext/Ann101/asset/box_on_incline.png", 
                                      [bboxlimits[0]+0.8,bboxlimits[3]], [(bboxlimits[1]-bboxlimits[0]),1.0*(bboxlimits[3]-bboxlimits[2])] ],
                                      {fixed:true});
            
                cm = board.create('point',[0,1.5],{size:1,fixed:true,name:'cm',withLabel:false,strokeColor:'pink',fillColor:'pink'})

                return board;
            }

            // Create a vector providing two points.
            addNormal = function() {
                vN = createVector('N',[3,1],[5,5]); 
                // console.log(vN); 
                // console.log(board.elementsByName.N.point1.X(),board.elementsByName.N.point1.Y())
            }

            addFriction = function() {
                vf = createVector('f',[5,1],[7,5]);  
            }

            addGravitational = function() {
                vg = createVector('g',[4,1],[6,5]);
                // console.log(vg)
            }

            // Create a vector providing two points.
            createVector = function(vName,v1,v2) {
                if (!board.elementsByName[vName]) {
                    var tail = board.create('point', v1,{size:1,withLabel:false});
                    var tip = board.create('point', v2,{size:2,name:vName});
                    var l1 = board.create('arrow', [tail, tip],{name:vName}); 
                    return l1;
                }
            }

            clearAll = function() {
                board = initBoard();
            }

            grabVectorProp = function(vObject) {
                if (vObject) {
                    var x1 = board.elementsByName[vObject.name].point1.X();
                    var y1 = board.elementsByName[vObject.name].point1.Y();
                    var x2 = board.elementsByName[vObject.name].point2.X();
                    var y2 = board.elementsByName[vObject.name].point2.Y();
                    var angle = board.elementsByName[vObject.name].getAngle();
                    angle = 180.0*angle/Math.PI;
                    if (angle < 0) {
                        angle = 360.0 + angle;
                    }
                    var length = board.elementsByName[vObject.name].L();

                    return {'name':vObject.name,'tail':[x1,y1],'tip':[x2,y2],'length':length,'angle':angle}
                }
                else {
                    return undefined;
                }
            }

            fetchState = function() {
                input = {};
                input['cm'] = {'p1':[cm.X(),cm.Y()]};
                input['N'] = grabVectorProp(vN);
                input['g'] = grabVectorProp(vg);
                input['f'] = grabVectorProp(vf);
                console.log(input);
                
                return input;
            }

            getInput = function(){
                return JSON.stringify(fetchState());
            }

            getState = function(){
                //state = {input: JSON.parse(getinput()), y:xfield.position};
                state = {input: JSON.parse(getInput())}
                statestr = JSON.stringify(state);
                // $('#msg').html('getstate ' + statestr);
                return statestr
            }

            setState = function(statestr){
                state = JSON.parse(statestr);
                console.log(state); 
                input = state.input
                //addNormal();
                if (input['N']) {
                    vN = createVector('N',input['N']['tail'],input['N']['tip']);
                }
                if (input['g']) {
                    vg = createVector('g',input['g']['tail'],input['g']['tip']);
                }
                if (input['f']) {
                    vf = createVector('f',input['f']['tail'],input['f']['tip']);
                }
                board.update()
                
                //alert(statestr);
                console.debug('State updated successfully from saved.');
            }

        </script>
    </body>
</html>


# <codecell>

def vglcfn(e, ans):
  '''
  Grading a force diagram.
  '''
  class Vector(object):
      def __init__(self,name,length,angle,tail):
          self.name = name
          self.length = length
          self.angle = angle
          self.tail = tail
          return None

  class gradeVector:
      def __init__(self):
          return None

      def compareLengths(self,v1,v2):
          if abs(v1.length-v2.length) < 1.00:
              return True
          else:
              return False

      def checkAngle(self,v1,GIVEN,**kwargs):
          tol = kwargs.get('tol', 1.0)
          if abs(v1.angle - GIVEN) < tol:
              return True
          else:
              return False
      
      def checkCenterMass(self, cm, vectors, **kwargs):
          tol = kwargs.get('tol', 0.25)
          numFalse = []
          for v in vectors:
              dist = math.hypot(cm[0] - v.tail[0], cm[1] - v.tail[1])
              if dist > tol:
                  numFalse.append([v.name,dist])
        
          if len(numFalse) == 0:
              return True
          else:
              return False

### Old Grader for car traveling to the right.
#   answer = json.loads(json.loads(ans)['answer'])
#   cm = answer['cm']['p1']
#   if 'N' in answer and 'g' in answer and 'f' in answer:
#       vN = Vector(answer['N']['name'],answer['N']['length'],answer['N']['angle'],answer['N']['tail'])
#       vg = Vector(answer['g']['name'],answer['g']['length'],answer['g']['angle'],answer['g']['tail'])
#       vf = Vector(answer['f']['name'],answer['f']['length'],answer['f']['angle'],answer['f']['tail'])
#   else:  
#       return {'ok': False, 'msg': 'You need to use all three vectors.'}

#   if gradeVector().compareLengths(vN, vg) == False:
#       return {'ok': False, 'msg': 'Normal Force and Gravitational Force should be similar lengths.'}

#   if gradeVector().checkAngle(vN, 90.0, tol=2.0) == False:
#       return {'ok': False, 'msg': 'The angle of the Normal Force is incorrect. Your angle: %.1f' % vN.angle}

#   if gradeVector().checkAngle(vg, 270.0, tol=2.0) == False:
#       return {'ok': False, 'msg': 'The angle of the Gravitational Force is incorrect. Your angle: %.1f' % vg.angle}

#   if gradeVector().checkAngle(vf, 180.0, tol=2.0) == False:
#       return {'ok': False, 'msg': 'The angle of the Frictional Force is incorrect. Your angle: %.1f' % vf.angle}

#   if gradeVector().checkCenterMass(cm,[vN,vg],tol=0.25) == False:
#       return {'ok': False, 'msg': 'One or more of your vectors do not start from the center of mass.'}

#   return {'ok': True, 'msg': 'Good job!'}

# <codecell>


