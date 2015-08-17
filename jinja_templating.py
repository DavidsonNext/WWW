
# coding: utf-8

# In[1]:

#!/usr/bin/env python
import os
import re
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath("__file__"))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


# ### Rendering Navbar Pages

# In[45]:

#------------------------------------------------------
fname = "index.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_main.html', context)
    f.write(html)
    

#------------------------------------------------------
fname = "topics.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_topics.html', context)
    f.write(html)
    
#------------------------------------------------------
fname = "drawing.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_drawing.html', context)
    f.write(html)    
    
    
#------------------------------------------------------
fname = "graphing.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_graphing.html', context)
    f.write(html)    


#------------------------------------------------------
fname = "data_entry.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_data_entry.html', context)
    f.write(html)
    

#------------------------------------------------------
fname = "contact.html"
# iList, actList = new_crawl_directory_for_html('../')
context = {
}

with open(fname, 'w') as f:
    html = render_template('page_contact.html', context)
    f.write(html)


# ###Rendering Interactive Links by Topic

# ###Macroeconomics

# In[52]:

PATH = os.path.dirname(os.path.abspath("__file__"))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

ignorePaths = set(['../.ipynb_checkpoints','../OldStructure','../Python','../SASS','../WWW'])

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
def crawl_directory_for_html(directory, base_url):
    iList=[]
    actList=[]
    for dirpath, subdirs, files in os.walk(directory):
        for file in files:
            relURL = os.path.join(dirpath, file)  #e.g., ../11_Loanable_Funds/LC1/(file.html)
#             relURL = relURL.split(base_url)[0]
            relURL = re.sub(directory,'', relURL)
            unit = relURL.split('/')[0]  #e.g., 11_Loanable_Funds
#             base_url = 'https://dnextinteractives.s3.amazonaws.com/Macroeconomics/'
            
            #Create S3 Link
            link = base_url + relURL#.lstrip('../')
#             print relURL
#             print link
            if file.endswith('.html'):
                if "OldStructure" in link or "WWW" in link: 
                    a = True
#                     print "Ignore folder: %s" % dirpath
                else:
                    iList.append(link)
    
            if "ActTable" in file:
#                 print link
                actList.append(link)
    

# def new_crawl_directory_for_html(directory):
#     iList=[]
#     actList=[]
#     units={}
#     for dirpath, subdirs, files in os.walk(directory):
#         r = dirpath.split('/')
#         if len(r)>2:
#             if any(x not in dirpath for x in ignorePaths): 
#                 name = r[1]
#                 LC = r[2]
#                 print name,LC

#                 for file in files:
#                     if file.endswith('.html'):
#                         relURL = os.path.join(dirpath, file)  #e.g., ../11_Loanable_Funds/LC1/(file.html)
#                         unit = relURL.split('/')[0]  #e.g., 11_Loanable_Funds
#                         baseURL = 'https://dnextinteractives.s3.amazonaws.com/Macroeconomics/'



#                         #Create S3 Link
#                         link = baseURL + relURL.lstrip('../')
#                         print "Folder: %s" % dirpath
#                         iList.append(link)

#                         if "ActTable" in file:
#                 #                 print link
#                             actList.append(link)
    
            
    return iList, actList 

def create_index_html(dir_to_crawl,f_output,base_url):
#     f_output = "MacroInteractives.html"
    iList, actList = crawl_directory_for_html(dir_to_crawl,base_url)
    context = {
        'TotalInteractives': len(iList) + len(actList),
        'JSXlist': iList,
        'actList': actList
    }
    
    with open(f_output, 'w') as f:
        html = render_template('interactives.html', context)
        f.write(html)
 
 
def main():
    base_url = "https://dnextinteractives.s3.amazonaws.com/calculus/"
    create_index_html('../DNextInteractives/calculus/','test.html',base_url)
 
########################################
 
if __name__ == "__main__":
    main()


# In[55]:

### Calculus
base_url = "https://dnextinteractives.s3.amazonaws.com/calculus"
create_index_html('../DNextInteractives/calculus','CaluclusInteractives.html',base_url)

### Macroeconomics
base_url = "https://dnextinteractives.s3.amazonaws.com/Macroeconomics"
create_index_html('../DNextInteractives/Macroeconomics','MacroInteractives.html',base_url)


# In[12]:




# In[2]:




# In[ ]:



