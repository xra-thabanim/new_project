{
'name': "School Management",
'summary':"""School Management""",

'description' : """
   Treating Schools
   
   """,

   'author' : "Thabani",
   'website' : "",

   'category' : "Tools",
   'version' : "16.0.1.0.0",
   
   'depends' : ['base','contacts','hr','account'],

   'data' : ['security/ir.model.access.csv',
             'views/school.xml',
             'views/report_promoted_students.xml',
             'views/school_management_menu.xml',
             'views/report_menu.xml',
             'reports/school_card.xml',
             'reports/report.xml',

             ],


   'demo' : [],

   
   'installable' : True,
   'application' : True,
   'auto_install' : False,


}