# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Drawing Points - Understanding Mouse Events for JSX elements.
# http://jsxgraph.uni-bayreuth.de/wiki/index.php/Browser_event_and_coordinates

# <codecell>

%%HTML

<!DOCTYPE html>
<html>
    <head>
        <style> 
            body {
                margin: 10px;
                /*padding-top: 40px;*/
            }
        </style>
    </head>

    <body>
        <!-- COMMENT: Define the jxgbox - aka, where all the interactive graphing will go. -->
        <div style="width: 100%; overflow: hidden;">
            <div id='jxgbox1' class='jxgbox' style='width:450px; height:350px; float:left; border: solid #1f628d 2px;'></div>
        </div>
        
        <!-- COMMENT: Buttons below are used to add debugging features to an interactive. Conole logging allows you to see
            output within a browser's console. Try reading about Chrome's console. -->
        
        <input class="btn" type="button" value="Pass State for Grading" onClick="passState()">
        <div id="spaceBelow">State:</div>

        
        <!-- COMMENT: Where our Javascript begins. -->
        <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>

            bboxlimits = [-1.1, 12, 12, -1.1];
            var board = JXG.JSXGraph.initBoard('jxgbox1', {axis:false, 
                                                    showCopyright: false,
                                                    showNavigation: false,
                                                    zoom: false,
                                                    pan: false,
                                                    boundingbox:bboxlimits,
                                                    grid: false,
                                                    hasMouseUp: true, 
            });
            
            xaxis = board.create('axis', [[0, 0], [12, 0]], {withLabel: true, name: "Real GDP", label: {offset: [320,-20]}});
            yaxis = board.create('axis', [[0, 0], [0, 12]], {withLabel: true, name: "Price Level", label: {offset: [-60,260]}});

            //Axes
            xaxis.removeAllTicks();
            yaxis.removeAllTicks();
            var xlabel = board.create('text',[-1,10,"Price<br>Level"],{fixed:true});
            var ylabel = board.create('text',[9,-0.5,"Real GDP"],{fixed:true});
            
            //Define Functions
            var p1 = board.create('point',[-1.0,1.5],{withLabel:false,visible:false});
            var p2 = board.create('point',[12.0,10.0],{withLabel:false,visible:false});
            var staticLine = board.create('line',[p1,p2],{name:'best-fit line',strokeColor:'gray',strokeWidth:'3',dash:'1',fixed:true});            
            
            
            var getMouseCoords = function(e, i) {
                var cPos = board.getCoordsTopLeftCorner(e, i),
                    absPos = JXG.getPosition(e, i),
                    dx = absPos[0]-cPos[0],
                    dy = absPos[1]-cPos[1];

                return new JXG.Coords(JXG.COORDS_BY_SCREEN, [dx, dy], board);
            }
        
            down = function(e) {
                var canCreate = true, i, coords, el;

                if (e[JXG.touchProperty]) {
                    // index of the finger that is used to extract the coordinates
                    i = 0;
                }
                coords = getMouseCoords(e, i);

                for (el in board.objects) {
                    if(JXG.isPoint(board.objects[el]) && board.objects[el].hasPoint(coords.scrCoords[1], coords.scrCoords[2])) {
                        canCreate = false;
                        break;
                    }
                }

                if (canCreate) {
                    board.create('point', [coords.usrCoords[1], coords.usrCoords[2]]);
                }
            }
            
            board.on('down', down);
            
            var kernel = IPython.notebook.kernel;
            
            passState = function(){
                console.log(f1);
                //var state = {'line1':{'p1':[line1.point1.X(),line1.point1.Y()],'p2':[line1.point2.X(),line1.point2.Y()]},
                //             'line2':{'p1':[line2.point1.X(),line2.point1.Y()],'p2':[line2.point2.X(),line2.point2.Y()]}
                //             };
                //statestr = JSON.stringify(state);
                //document.getElementById('spaceBelow').innerHTML += '<br>'+statestr;
                //var command = "state = '" + statestr + "'";
                //console.log(command);

                //var kernel = IPython.notebook.kernel;
                //kernel.execute(command);

                //return statestr
            }
            
            function set_value(){
                var var_value = state;
                console.log(var_value);
                var command = "state = '" + var_value + "'";
                console.log("Executing Command: " + command);

                var kernel = IPython.notebook.kernel;
                kernel.execute(command);
            }
            
        </script>
    </body>
</html>

# <codecell>

### To be written

# <codecell>


