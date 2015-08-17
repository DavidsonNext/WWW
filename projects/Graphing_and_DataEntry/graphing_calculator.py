# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import HTML

# <markdowncell>

# #Graphing Calculator - inspired by AP Calculus
# Graphing calculators are permitted for use during "calculator active" problems on AP exams. Here we attempt to provide open access to those functionalities required for the AP exam.
# 
# https://apstudent.collegeboard.org/apcourse/ap-calculus-ab/calculator-policy
# 
# * Plot the graph of a function within an arbitrary viewing window
# * Find the zeros of functions (solve equations numerically)
# * Numerically calculate the derivative of a function
# * Numerically calculate the value of a definite integral

# <codecell>

%%HTML

<!DOCTYPE html>
<html>
    <head>
        <style> 
            
        </style>
    </head>


    <body>
            <div id="menu" style="width: 270px; float: left;">
                <ul>
                    <input class="txtbox" type="text" id="inputF" placeholder="Type a function f(x)" value="x^3+x^2-6*x" font-size: "10px">
                    <input class="btn" type="button" value="Plot" onClick="plotter()">
                    <!--
                    <input class="btn" type="button" value="add tangent" onClick="addTangent()">
                    -->
                    <input class="btn" type="button" value="Add Derivative" onClick="plotDerivative()">
                    <input class="btn" type="button" value="Clear All" onClick="clearAll()">
                </ul>
                <br></br>
                <ul>
                    <input class="txtbox" type="text" id="inputZstart" placeholder="Start value for zero search" font-size: "6">
                    <input class="btn" type="button" value="find Zero" onClick="findZeroes()">

                </ul>
            </div>
            <div id='jxgbox' class='jxgbox' style='width:450px; height:350px; margin-left: 180px; border: solid #1f628d 1px;'></div>        

        <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>
        <script type='text/javascript'>
            var initBoundingBox = [-11,11,11,-11];
            var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox:initBoundingBox, axis:true, showCopyright:false});
            var f, curve; // global objects
             
            function plotter() {
                var txtraw = document.getElementById('inputF').value;
                f = board.jc.snippet(txtraw, true, 'x', true);
                curve = board.create('functiongraph',[f,
                            function(){ 
                              var c = new JXG.Coords(JXG.COORDS_BY_SCREEN,[0,0],board);
                              return c.usrCoords[1];
                            },
                            function(){ 
                              var c = new JXG.Coords(JXG.COORDS_BY_SCREEN,[board.canvasWidth,0],board);
                              return c.usrCoords[1];
                            }
                          ],
                          {name:txtraw, withLabel:false});
                var q = board.create('glider', [2, 3, curve], {withLabel:false});
                var t = board.create('text', [
                      function(){ return q.X()+0.2; },
                      function(){ return q.Y()+0.1; },
                      //function(){ return "The slope of the function f(x)=" + txtraw + "<br>at x=" + q.X().toFixed(2) + " is equal to " + (JXG.Math.Numerics.D(f))(q.X()).toFixed(2); }
                      //function(){ return "f(x)=" + txtraw + "<br>f(x=" + q.X().toFixed(2) + ") = " + f(q.X()).toFixed(2)}
                      function(){ return "f(x=" + q.X().toFixed(2) + ") = " + f(q.X()).toFixed(2)}
                  ], 
                  {fontSize:15});
            }
             
            function clearAll() {
                JXG.JSXGraph.freeBoard(board);
                board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox:initBoundingBox, axis:true, showCopyright:false});
                f = null;
                curve = null;
            }
             
            function addTangent() {
                if (JXG.isFunction(f)) {
                    board.suspendUpdate();
                    var p = board.create('glider',[1,0,curve], {name:'drag me'});
                    board.create('tangent',[p], {name:'drag me'});
                    board.unsuspendUpdate();
                }
            }
             
            function plotDerivative() {
                if (JXG.isFunction(f)) {
                    board.create('functiongraph',[JXG.Math.Numerics.D(f),
                            function(){ 
                              var c = new JXG.Coords(JXG.COORDS_BY_SCREEN,[0,0],board);
                              return c.usrCoords[1];
                            },
                            function(){ 
                              var c = new JXG.Coords(JXG.COORDS_BY_SCREEN,[board.canvasWidth,0],board);
                              return c.usrCoords[1];
                            }], {dash:2});
                }
            }

            function isNumeric(num){
                return !isNaN(num)
            }

            function findZeroes() {
                var zeroraw = document.getElementById('inputZstart').value;
                if (JXG.isFunction(f) && isNumeric(zeroraw)) {
                    board.suspendUpdate();
                    var zero = JXG.Math.Numerics.fzero(f,parseFloat(zeroraw));
                    var f_zero = f(zero);
                    var p = board.create('point',[zero,f_zero], {name:'f(x='+zero.toFixed(2)+')=0.0',
                      strokeColor:'gray', face:'<>',fixed:true});
                    //board.create('tangent',[p], {name:'drag me'});
                    board.unsuspendUpdate();
                }

            }


            function findNumDerivative() {
                var zeroraw = document.getElementById('inputNumDerivative').value;
                if (JXG.isFunction(f) && isNumeric(zeroraw)) {
                    board.suspendUpdate();
                    var zero = JXG.Math.Numerics.fzero(f,parseFloat(zeroraw));
                    var f_zero = f(zero);
                    var p = board.create('point',[zero,f_zero], {name:'a zero of the function',
                      strokeColor:'gray', face:'<>'});
                    //board.create('tangent',[p], {name:'drag me'});
                    board.unsuspendUpdate();
                }

            }



        </script>
    </body>
</html>


# <markdowncell>

# ### No Grading setup at this time.

# <codecell>


# <codecell>


