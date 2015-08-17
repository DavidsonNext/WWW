# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Vector Drawing with paper.js
# http://paperjs.org/

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

            canvas {  
                border:1px solid black;
                /*background:url("/static/1280px_Protractor_Rapporteur_Degrees_V3.jpg");*/
                background:url("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Protractor_Rapporteur_Degrees_V3.jpg/1920px-Protractor_Rapporteur_Degrees_V3.jpg");
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
            }

        </style>

    </head>


    <body>
        <canvas id="myCanvas" style="border:1px solid #000000;" width = 500px height = 300px ></canvas>
        <!-- <img src="/static/1280px-Protractor_Rapporteur_Degrees_V3.jpg"/> -->

        <!-- Load the Paper.js library -->
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.9.18/paper-full.min.js"></script>

        <script type="text/paperscript" canvas="myCanvas">

            var values = {
                fixLength: false,
                fixAngle: false,
                showCircle: false,
                showAngleLength: true,
                showCoordinates: false
            };

            ////////////////////////////////////////////////////////////////////////////////
            // Vector

            var vectorStart, vector, vectorPrevious;
            var vectorItem, items, dashedItems;

            var state = {'xi':null, 
                         'yi':null,
                         'xf':null,
                         'yf':null, 
                         'magnitude':null, 
                         'angle':null
                    };

            function processVector(event, drag) {
                vector = event.point - vectorStart;
                if (vectorPrevious) {
                    if (values.fixLength && values.fixAngle) {
                        vector = vectorPrevious;
                    } else if (values.fixLength) {
                        vector.length = vectorPrevious.length;
                    } else if (values.fixAngle) {
                        vector = vector.project(vectorPrevious);
                    }
                }
                drawVector(drag);
            }

            function drawVector(drag) {
                if (items) {
                    for (var i = 0, l = items.length; i < l; i++) {
                        items[i].remove();
                    }
                }
                if (vectorItem)
                    vectorItem.remove();
                items = [];
                var arrowVector = vector.normalize(10);
                var end = vectorStart + vector;
                vectorItem = new Group(
                    new Path(vectorStart, end),
                    new Path(
                        end + arrowVector.rotate(135),
                        end,
                        end + arrowVector.rotate(-135)
                    )
                );
                vectorItem.strokeWidth = 3.0;
                vectorItem.strokeColor = '#e4141b';
                // Display:
                dashedItems = [];
                // Draw Circle
                if (values.showCircle) {
                    dashedItems.push(new Path.Circle(vectorStart, vector.length));
                }
                // Draw Labels
                if (values.showAngleLength) {
                    //DS//drawAngle(vectorStart, vector, !drag);
                    if (!drag)
                        drawLength(vectorStart, end, vector.angle < 0 ? -1 : 1, true);
                }
                var quadrant = vector.quadrant;
                if (values.showCoordinates && !drag) {
                    drawLength(vectorStart, vectorStart + [vector.x, 0],
                            [1, 3].indexOf(quadrant) != -1 ? -1 : 1, true, vector.x, 'x: ');
                    drawLength(vectorStart, vectorStart + [0, vector.y],
                            [1, 3].indexOf(quadrant) != -1 ? 1 : -1, true, vector.y, 'y: ');
                }
                for (var i = 0, l = dashedItems.length; i < l; i++) {
                    var item = dashedItems[i];
                    item.strokeColor = 'black';
                    item.dashArray = [1, 2];
                    items.push(item);
                }
                // Update palette
                values.x = vector.x;
                values.y = vector.y;
                values.length = vector.length;
                values.angle = vector.angle;
            }

            function drawAngle(center, vector, label) {
                var radius = 25, threshold = 10;
                if (vector.length < radius + threshold || Math.abs(vector.angle) < 15)
                    return;
                var from = new Point(radius, 0);
                var through = from.rotate(vector.angle / 2);
                var to = from.rotate(vector.angle);
                var end = center + to;
                dashedItems.push(new Path.Line(center,
                        center + new Point(radius + threshold, 0)));
                dashedItems.push(new Path.Arc(center + from, center + through, end));
                var arrowVector = to.normalize(7.5).rotate(vector.angle < 0 ? -90 : 90);
                dashedItems.push(new Path([
                        end + arrowVector.rotate(135),
                        end,
                        end + arrowVector.rotate(-135)
                ]));
                if (label) {
                    // Angle Label
                    var text = new PointText(center + through.normalize(radius + 10) + new Point(0, 3));
                    text.content = Math.floor(vector.angle * 100) / 100 + '\xb0';
                    items.push(text);
                }
            }

            function drawLength(from, to, sign, label, value, prefix) {
                var lengthSize = 5;
                if ((to - from).length < lengthSize * 4)
                    return;
                var vector = to - from;
                var awayVector = vector.normalize(lengthSize).rotate(90 * sign);
                var upVector = vector.normalize(lengthSize).rotate(45 * sign);
                var downVector = upVector.rotate(-90 * sign);
                var lengthVector = vector.normalize(
                        vector.length / 2 - lengthSize * Math.sqrt(2));
                var line = new Path();
                line.add(from + awayVector);
                line.lineBy(upVector);
                line.lineBy(lengthVector);
                line.lineBy(upVector);
                var middle = line.lastSegment.point;
                line.lineBy(downVector);
                line.lineBy(lengthVector);
                line.lineBy(downVector);
                dashedItems.push(line);
                if (label) {
                    // Length Label
                    var textAngle = Math.abs(vector.angle) > 90
                            ? textAngle = 180 + vector.angle : vector.angle;
                    // Label needs to move away by different amounts based on the
                    // vector's quadrant:
                    var away = (sign >= 0 ? [1, 4] : [2, 3]).indexOf(vector.quadrant) != -1
                            ? 8 : 0;
                    var text = new PointText(middle + awayVector.normalize(away + lengthSize));
                    text.rotate(textAngle);
                    text.justification = 'center';
                    value = value || vector.length;
                    text.content = (prefix || '') + Math.floor(value * 1000) / 1000;
                    items.push(text);
                }
            }

            ////////////////////////////////////////////////////////////////////////////////
            // Mouse Handling

            var dashItem;

            function onMouseDown(event) {
                var end = vectorStart + vector;
                var create = false;
                if (event.modifiers.shift && vectorItem) {
                    vectorStart = end;
                    create = true;
                } else if (vector && (event.modifiers.option
                        || end && end.getDistance(event.point) < 10)) {
                    create = false;
                } else {
                    vectorStart = event.point;
                }
                if (create) {
                    dashItem = vectorItem;
                    vectorItem = null;
                }
                processVector(event, true);
            }

            function onMouseDrag(event) {
                if (!event.modifiers.shift && values.fixLength && values.fixAngle)
                    vectorStart = event.point;
                processVector(event, event.modifiers.shift);
            }

            function onMouseUp(event) {
                processVector(event, false);
                if (dashItem) {
                    dashItem.dashArray = [1, 2];
                    dashItem = null;
                }
                
                //DS
                state = {'xi':vectorStart.x, 
                         'yi':vectorStart.y,
                         'xf':vector.x,
                         'yf':vector.y, 
                         'magnitude':vector.length, 
                         'angle':vector.angle
                    };
                console.log(state);
                //DS

                vectorPrevious = vector;
            }

            function initializeVector(initState) {
                if (initState.magnitude && initState.angle) {
                    // var tmp = {'xi':0.5*myCanvas.width, 
                    //          'yi':270,
                    //          'xf':150,
                    //          'yf':150, 
                    //          'magnitude':0.0, 
                    //          'angle':0.0
                    //     };
                    var point1 = new Point(initState.xi,initState.yi);
                    var point2 = new Point(initState.xf,initState.yf);
                    var vector = point2 - point1;

                    var end = point1 + vector;
                    vectorItem = new Group(
                        new Path(point1, end)
                    );
                    vectorItem.strokeWidth = 3.0;
                    vectorItem.strokeColor = '#e4141b';
                }

            }

            getInput = function(){
                input = state;
                console.log(JSON.stringify(input))
                return JSON.stringify(input);
            }

            getState = function(){
                //state = {input: JSON.parse(getinput()), y:xfield.position};
                statestr = JSON.stringify(state);
                // $('#msg').html('getstate ' + statestr);
                return statestr
            }

            setState = function(statestr){
                console.log(statestr);
                // alert(statestr);
                initializeVector(statestr);
                $('#msg').html('setstate ' + statestr);
                state = JSON.parse(statestr);
                console.log(state);
                initializeVector(state);
                console.debug('State updated successfully from saved.');
            }

        </script>
    </body>
</html>

# <codecell>

### To be written

# <codecell>


