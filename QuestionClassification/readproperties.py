#run this command from terminal : easy_install configobj

from configobj import ConfigObj
import os

proj_dir = os.path.abspath(os.path.join('.'))
query_proc_dir = os.path.abspath(os.path.join(proj_dir,'QuestionClassification'))

#return value for a given key from conf file
def read_property(key):
    #print os.path.abspath(os.path.join(query_proc_dir,'properties.conf'))
    
    config = ConfigObj(os.path.abspath(os.path.join(query_proc_dir,'properties.conf')))
    #print config
    value = config[key]
    return value

#value=read_property('word_features_train_coarse_path')
#print (value)
