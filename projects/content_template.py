# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import jinja2 as jj

# <codecell>

T = jj.Template(
    '''
    <a href="{{URL}}">
        <img class="img-responsive" src="projects/Graphing/curve_select_Macro.png" alt="">
    </a>
    <h3>
        <a href="{{URL}}">Curve Selection</a>
    </h3>
    <!-- Button trigger modal -->

    <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
      Demo
    </button>

    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">Curve Selection</h4>
          </div>
          <div class="modal-body">
            <iframe frameBorder="0" width={{iWidth}} height={{iHeight}} src="{{URL}}"></iframe>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
            
    <p>{{Description}}</p>
    <h4>Instructions:</h4> <p>{{Instructions}}</p>
    '''
    )
print T.render(URL='html',iWidth=500,iHeight=400,
               Description='''Example of selecting curves within figure, 
               i.e., an interactive multiple choice. Inspired by Macroeconomics 
               problems where students may have trouble visualizing relationships 
               between various economic variables.''',
               Instructions='''Select one of the two gray curves.''',
               )

# <codecell>


