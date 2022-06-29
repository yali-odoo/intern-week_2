# -*- coding:utf-8 -*-
{
    'name':"Greenville Product: Unique product lists per customer on website",
    'summary':""" """,
    'description':"""
    """,
    'author':'Odoo Inc',
    'category':'Custom Development',
    'license':'OPL-1',
    'depends':['base','sale','product','stock'],
    
    'data':[
        'security/product_security.xml',
        'security/ir.model.access.csv',
        'views/product_lists_view.xml',
        'views/res_partner_inherit_view.xml'
        
    ],
    
    'demo':[
        
    ]      
}
