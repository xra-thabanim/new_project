from odoo import models, fields, api

class School(models.Model):
    _name = 'school.student'

    #My decleration
    name = fields.Char(string="Name", required=True)
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    attachment = fields.Binary(string="Attachment", attachment=True)
    attachment_filename = fields.Char(string="Attachment Filename")
    status = fields.Selection([('promoted', 'Promoted'), ('not_promoted', 'Not Promoted')], string="Status")
    profile_picture = fields.Binary(string="Profile Picture")
    math_marks = fields.Float(string='Mathematics Marks')
    physical_science_marks = fields.Float(string='Physical Science Marks')
    life_orientation_marks = fields.Float(string='Life Orientation Marks')
    english_fal_marks = fields.Float(string='English FAL Marks')
    isizulu_hl_marks = fields.Float(string='Isizulu HL Marks')
    eng_graphics_design_marks = fields.Float(string='Engineering Graphics and Design Marks')
    electrical_technology_marks = fields.Float(string='Electrical Technology Marks')
    average_marks = fields.Float(string='Average Marks', compute='_compute_average_marks')
    
    #Method for calculating the average marks
    @api.depends('math_marks', 'physical_science_marks', 'life_orientation_marks', 'english_fal_marks', 'isizulu_hl_marks', 'eng_graphics_design_marks', 'electrical_technology_marks')
    def _compute_average_marks(self):
        for student in self:
            marks = [
                student.math_marks,
                student.physical_science_marks,
                student.life_orientation_marks,
                student.english_fal_marks,
                student.isizulu_hl_marks,
                student.eng_graphics_design_marks,
                student.electrical_technology_marks
            ]
            total_subjects = len(marks)
            total_marks = sum(marks)
            student.average_marks = total_marks / total_subjects if total_subjects > 0 else 0.0
            
            #Auto computing status
            student._compute_status()
    
    def _compute_status(self):
        for student in self:
            if student.average_marks > 50:
                student.status = 'promoted'
            else:
                student.status = 'not_promoted'
                
    #Getting promoted student into the report list
    @api.model
    def get_promoted_students_report_data(self):
        promoted_students = self.search([('status', '=', 'promoted'), ('average_marks', '>', 50)])
        return promoted_students

    @api.model
    def render_promoted_students_report(self, docids, data=None):
        report_data = self.get_promoted_students_report_data()
        return {
            'doc_ids': docids,
            'doc_model': 'school.student',  
            'docs': report_data,
        }

    @api.model
    def _action_report_promoted_students(self):
        action = {
            'name': 'Promoted Students',
            'type': 'ir.actions.act_window',
            'res_model': 'school.student',
            'view_mode': 'tree,form',  
        }
        return action
