import elist.elist as elel
import tlist.tlist as tltl
import edict.edict as eded
import estring.estring as eses
import re
from xdict.jprint import pobj
from xdict.jprint import pdir
from nvhead.consts import *

#################
def is_sarr(one):
    if(isinstance(one,list)):
        if(one.__len__()==0):
            return(True)
        else:
            if(isinstance(one[0],str)):
                return(True)
            else:
                return(False)
    else:
        return(False)

def is_darr(one):
    if(isinstance(one,list)):
        if(one.__len__()==0):
            return(True)
        else:
            if(isinstance(one[0],dict)):
                return(True)
            else:
                return(False)
    else:
        return(False)

#################
def fmt_one(s):
    s = eses.replace(s,re.compile("[\x20]+"),'\x20')
    s = s.replace(':\x20',':')
    s = s.replace(',\x20',',')
    s = s.replace(':',':\x20')
    s = s.replace(',',',\x20')
    return(s)

def one_s2t(s,**kwargs):
    '''
        single http head string to tuple
    '''
    s = fmt_one(s)
    regex = re.compile('(.*?):\x20(.*)')
    m = regex.search(s)
    if(m):
        name = m.group(1)
        body = m.group(2)
    else:
        name = ''
        body = s
    return((name,body))

def one_t2s(t,**kwargs):
    name = t[0]
    body = t[1]
    body = fmt_one(body)
    if(name == ""):
        s = body
    else:
        s = name +":\x20"+body
    return(s)

#################
# s = '''Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'''
# s = '''text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'''
# RFC 7231,Page 38,If no "q" parameter is present,the default weight is 1.

def type_subtype_q_fmt(s):
    s = s.replace(";\x20",";")
    s = s.replace("\x20;",";")
    s = s.replace("\x20;\x20",";")
    return(s)

def type_subtype_q_s2sarr(s,**kwargs):
    s = type_subtype_q_fmt(s)
    name,body = one_s2t(s)
    sarr = body.split(",\x20")
    return(sarr)

def type_subtype_q_ele_s2d(ele,**kwargs):
    arr = ele.split("/")
    type = arr[0]
    tmp = arr[1]
    if(";q=" in tmp):
        arr2 = tmp.split(";q=")
        subtype = arr2[0]
        q = arr2[1]
    else:
        subtype = tmp
        q = None
    d = {
        'type':type,
        'subtype':subtype,
        'q':q
    }
    return(d)

def type_subtype_q_ele_d2s(d,**kwargs):
    if(d["q"] == None):
        s = d['type'] + '/' + d['subtype']
    else:
        s = d['type'] + '/' + d['subtype'] + ';q=' + str(d['q'])
    return(s)

def type_subtype_q_sarr2darr(sarr,**kwargs):
    darr = elel.array_map(sarr,type_subtype_q_ele_s2d)
    return(darr)

def type_subtype_q_darr2sarr(darr,**kwargs):
    sarr = elel.array_map(darr,type_subtype_q_ele_d2s)
    return(sarr)

###########################
def type_subtype_q_cond_slct(sarr,key,match_value):
    darr = type_subtype_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]==match_value))
    sarr = type_subtype_q_darr2sarr(darr)
    return(sarr)

def type_subtype_q_cond_slct_not(sarr,key,match_value):
    darr = type_subtype_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]!=match_value))
    sarr = type_subtype_q_darr2sarr(darr)
    return(sarr)


def type_subtype_q_sort_by_q(darr):
    darr1 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']==None))
    darr2 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']!=None))
    ndarr1 = elel.sortDictList(darr1,cond_keys=['q','type','subtype'],reverse=True)
    def map_func(dele):
        if(dele['q'] == None):
            dele['q'] = 1.0
        else:
            dele['q'] = float(dele['q'])
        return(dele)
    idarr2 = elel.array_map(darr2,map_func)
    ndarr2 = elel.sortDictList(darr2,cond_keys=['q','type','subtype'],reverse=True)
    ndarr = elel.concat(ndarr1,ndarr2)
    return(ndarr)

#slct_via_type
#rm_via_type
#slct_via_subtype
#rm_via_subtype
#slct_via_q  
#rm_via_q 

class TypeSubtypeQ():
    def __init__(self,one,**kwargs):
        if(isinstance(one,str)):
            self.sarr = type_subtype_q_s2sarr(one)
            self.darr = type_subtype_q_sarr2darr(self.sarr)
        elif(is_sarr(one)):
            self.sarr = one
            self.darr = type_subtype_q_sarr2darr(self.sarr)
        else:
            self.sarr = type_subtype_q_darr2sarr(one)
            self.darr = one
    def __repr__(self):
        pobj(self.sarr)
        return("")
    def str(self):
        s = elel.join(self.sarr,",\x20")
        print(s)
        return(s)
    def qsort(self):
        self.darr = type_subtype_q_sort_by_q(self.darr)
        self.sarr = type_subtype_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def modify(self,func,*func_args,**func_kwargs):
        self.sarr = func(self.sarr,*func_args,**func_kwargs)

##########################

